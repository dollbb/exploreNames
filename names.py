import sqlite3
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

from fuzzywuzzy import fuzz
from fuzzywuzzy import process

sns.set_style("whitegrid")

con = sqlite3.connect("database.sqlite")
cursor = con.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

df = pd.read_sql_query("SELECT * FROM NationalNames", con)


def namePlt(name=None):
    '''
    Plot name usage over time by gender
    name = name string
    '''
    if name == None:
        print "gotta enter a name"
        return
    if len(name) > 1:
        name = name[0].upper() + name[1:len(name)].lower()
        name = "'" + name + "'"
        query = "SELECT * from NationalNames WHERE name = " + name
        nameDF = pd.read_sql_query(query, con)
        nameDF = nameDF.drop(['Id','Name'], axis=1)
    else:
        print "the name needs some more letters"
        return
    if len(nameDF.Gender.unique()) > 1: 
        fdf = nameDF.loc[nameDF['Gender'] == "F"]
        mdf = nameDF.loc[nameDF['Gender'] == "M"]
                
        fdf.columns = ['Year','Gender', 'F']
        mdf.columns = ['Year','Gender', 'M']

        nameDF = pd.merge(fdf, mdf, on='Year', how='outer', sort=True)
        
        plt.figure()
        plt.plot(nameDF['Year'], nameDF['F'], color='pink', label="F")
        plt.plot(nameDF['Year'], nameDF['M'], color='powderblue', label="M")
        plt.xlabel('Year')
        plt.ylabel('Count')
        plt.title(name)
        plt.legend()
        plt.show()
        
        return nameDF
    else:        
        if nameDF.Gender.unique() == 'F':
            lin_col = 'pink'
        else:
            lin_col = 'powderblue'

        plt.figure()
        plt.plot(nameDF['Year'], nameDF['Count'], color= lin_col)
        plt.xlabel('Year')
        plt.ylabel('Count')
        plt.title(name)
        plt.show()
        
    return nameDF
    

    



def nameVars(dat, name=None, numMatch=25):
    '''
    Get variants on a name by Levenshtein distance.
    dat = name data set
    name = name string
    numMatch = number of variants to return
    '''
    name = name[0].upper() + name[1:len(name)].lower()
    nsum = dat.groupby(['Name','Gender'])['Count'].sum()
    
    nsum = pd.DataFrame(nsum)
    nsum.reset_index(inplace=True)

    names = dat.Name.unique()

    ndf = process.extract(name, names, limit = numMatch)
    ndf = pd.DataFrame(data = ndf, columns = ['Name', 'sim'])

    ndf = pd.merge(ndf, nsum, on = 'Name', how= 'inner')

    return ndf 

