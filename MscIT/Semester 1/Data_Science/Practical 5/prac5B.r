# R language
# R studio
print('5B. Data Pattern')
library(readr)
library(data.table)
FileName=paste0('c:/VKHCG/01-Vermeulen/00-RawData/IP_DATA_ALL.csv')
IP_DATA_ALL <- read_csv(FileName)
hist_country=data.table(Country=unique(IP_DATA_ALL$Country))
pattern_country=data.table(Country=hist_country$Country,
PatternCountry=hist_country$Country)
oldchar=c(letters,LETTERS)
newchar=replicate(length(oldchar),"A")
for (r in seq(nrow(pattern_country))){
    s=pattern_country[r,]$PatternCountry;
    for (c in seq(length(oldchar))){
        s=chartr(oldchar[c],newchar[c],s)
    };
    for (n in seq(0,9,1)){
        s=chartr(as.character(n),"N",s)
    };
    s=chartr(" ","b",s)
    s=chartr(".","u",s)
    pattern_country[r,]$PatternCountry=s;
};
View(pattern_country)