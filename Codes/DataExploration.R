###### Data analysis and exploration - Vinted ######################
#-------------------------------------------------------------------#
# The idea is to study the collected data in order to evaluate the relationship 
# between the number of interested people and the other factors 
# The metric that we seek to maximize is the following ratio :
# Ratio = Interested / Vues
# Because then we maximize the number of people that are truly interested into 
# buying the product (they put it on favorite articles)
#-------------------------------------------------------------------#

#-------------------------------------------------------------------#
#                   I - Import libraries and files 
#-------------------------------------------------------------------#
setwd("C:\\Users\\Sébastien CARARO\\Desktop\\Vinted\\Data\\Scraped")

library(ggplot2)
library(corrplot)
library(dplyr)
library(MASS)
library(glue)

table <- read.csv('./Air-force-one.csv', sep = ";", encoding = 'utf-8') %>%
  filter(Taille != "" & Taille != 'Na')
summary(table)
table$Taille <- as.numeric(as.character(table$Taille))
table$Prix <- as.numeric(gsub(",", ".", as.character(table$Prix)))
dim(table)
summary(table)
table$Ratio <- table$Interesses / table$Vues

table <- table %>%
  filter(!is.na(Prix))%>% 
  filter(Taille > 35 ) # Remove baby 

dim(table)
summary(table)

#-------------------------------------------------------------------#
#                           II - Overview
#-------------------------------------------------------------------#
ggplot()+
  geom_point(aes(x = table$Vues, y = table$Interesses, col = table$Prix))+
  labs(title = 'Relationship between interested and views')+
  xlab("Vues")+
  ylab("Interesses")

ggplot()+
  geom_point(aes(x = table$Prix, y = table$Ratio, col = table$Etat))+
  labs(title = 'Relationship between Ratio and price')+
  xlab("Price")+
  ylab("Ratio = Interested/Views")

ggplot()+
  geom_point(aes(y=table$Prix, x = 1, col = table$Etat))+
  ylab("Prix")

ggplot()+
  geom_histogram(aes(x = table$Ratio))

ggplot(data = table, aes(y = Prix)) +
  geom_boxplot() +
  facet_grid(. ~ Etat)+
  labs(x = "Ratio = Interested/Views", 
       y = "Price")


for(condition in levels(table$Etat)){
  print(condition)
  t <- table %>% filter(Etat == condition)
  p <- ggplot()+
    geom_histogram(aes(x = t$Prix), col = 'blue', binwidth = 5)+
    geom_vline(xintercept = median(t$Prix), col = 'dark green')+
    labs(title = condition, subtitle = glue("Median price = ", median(t$Prix), " euros"))+
    xlab("Prix")+
    ylab('Occurences')
  print(p)
}
#-------------------------------------------------------------------#
#                       III - Correlation matrix 
#-------------------------------------------------------------------#

mydata.cor <- cor(table %>% dplyr::select(Prix, Taille, Vues, Interesses, Ratio), method = c("pearson"))
rownames(mydata.cor) <- colnames(mydata.cor) # hack
corrplot(mydata.cor, method = "color")
print(mydata.cor)



#-------------------------------------------------------------------#
# IV - Try to determine relation between interested/minute and other variables
#-------------------------------------------------------------------#

trainDATA <- table[1:7610,] %>% dplyr::select(Prix, Taille, Etat, Vues, Ratio)
testDATA <- table[161:170,] %>% dplyr::select(Prix, Taille, Etat, Vues, Ratio)

model <- lm(Ratio ~ ., data = trainDATA)
print(model)

model <- lm(Prix ~ Etat + Taille, data = trainDATA)
print(model)
