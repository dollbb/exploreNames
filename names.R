library(RSQLite)
library(ggplot2)

db <- dbConnect(dbDriver("SQLite"), "database.sqlite")

namePlt <- function(babyName) {

   babyName = paste0(toupper(substr(babyName, 1, 1)), tolower(substr(babyName, 2, nchar(babyName))))
    bName = paste0("'", babyName, "'")

    ndat <- data.frame(dbGetQuery(db, paste0("SELECT *
                  FROM NationalNames
                  WHERE name = " , bName) 
                 ))
    
    if (length(unique(ndat$Gender)) > 1) {
        
        ff <- data.frame(Name = babyName, Gender="F", Year = 1880:2014)
        fdat <- subset(ndat, Gender == "F")
        fdat <- merge(fdat, ff, by=c("Name","Gender","Year"), all.y=T)
        
        mf <- ff
        mf$Gender <- "M"
        mdat <- subset(ndat, Gender == "M")
        mdat <- merge(mdat, mf, by=c("Name","Gender","Year"), all.y=T)
        
        ndat <- rbind(fdat, mdat)
        ndat[is.na(ndat)] <- 0
        
        p <- ggplot(ndat, aes(x=Year, y=Count, colour=Gender)) + geom_line(size=.75) + scale_colour_manual(values = c("pink", "powderblue"))+ ggtitle(babyName) + theme_bw()        
            
    } else {
            
        if (unique(ndat$Gender) == "F") {
            lcol = "pink"
        } else {
            lcol = "powderblue"
        }
        
        p <- ggplot(ndat, aes(x=Year, y=Count)) + geom_line(size=.75, colour=lcol) + ggtitle(babyName)+theme_bw()            
        
    }               
    
    print(p)
    return(ndat)
}


