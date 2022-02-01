
rm(list = ls(all.names = TRUE))
# install.packages("stringr")
library("stringr")
library(tidyverse)

setwd('/home/stepski/Desktop')
data = read_csv('jacques.csv')

wine_id <- seq(1, length(data$Name))
data[,1] <- wine_id
names(data)[1] <- "wine_id"

data$`Preis in euro` <- gsub("€*", "", data$`Preis in euro`)
data$`Preis in euro` <- gsub("\n", "", data$`Preis in euro`)
data$Beschreibung <- gsub("Notiz:", "", data$Beschreibung)
data$Alkoholgehalt <- gsub('<div class="colC">' , '', data$Alkoholgehalt)
data$Alkoholgehalt <- gsub("% Vol.</div>" , '', data$Alkoholgehalt)
data$Weinstil <- gsub('<div class="colC" itemprop="color">' , '', data$Weinstil)
data$Weinstil <- gsub('</div>' , '', data$Weinstil)
data$Weinstil <- gsub('&amp;' , '&', data$Weinstil)

write_csv(data, 'jacques_de.csv')
