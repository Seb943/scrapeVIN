###### Data analysis and exploration - Vinted ######################
#-------------------------------------------------------------------#
# The idea is to study the collected data in order to evaluate the relationship 
# between the number of interested people and the other factors 
# The metric that we seek to maximize is the following ratio :
# Ratio = Interested / Views
# Because then we maximize the number of people that are truly interested into 
# buying the product (they put it on favorite articles)
#-------------------------------------------------------------------#

#-------------------------------------------------------------------#
#                   I - Import libraries and files 
#-------------------------------------------------------------------#
#setwd("C:\\Users\\Sébastien CARARO\\Desktop\\Vinted\\Data\\Scraped")

library(ggplot2)
library(corrplot)
library(dplyr)
library(MASS)
library(glue)

table <- read.csv('Air-force-one.csv', sep = ";", encoding = 'utf-8') %>%
  filter(Size != "" & Size != 'Na')
summary(table)
table$Size <- as.numeric(as.character(table$Size))
table$Price <- as.numeric(gsub(",", ".", as.character(table$Price)))
dim(table)
summary(table)
table$Ratio <- table$Interested / table$Views

table <- table %>%
  filter(!is.na(Price))%>% 
  filter(Size > 35 ) # Remove baby 

dim(table)
summary(table)

table$Condition <- as.character(table$Condition)
# for french version...
table$Condition[table$Condition == "BON Ã‰TAT"] <- 'GOOD CONDITION'
table$Condition[table$Condition == "NEUF"] <- 'NEW WITHOUT TAGS'
table$Condition[table$Condition == "NEUF, AVEC Ã‰TIQUETTE"] <- 'NEW WITH TAGS'
table$Condition[table$Condition == "SATISFAISANT"] <- 'SATISFACTORY'
table$Condition[table$Condition == "TRÃˆS BON Ã‰TAT"] <- 'VERY GOOD CONDITION'
levels(as.factor(table$Condition))

#-------------------------------------------------------------------#
#                           II - Overview
#-------------------------------------------------------------------#
ggplot()+
  geom_point(aes(x = table$Views, y = table$Interested, col = table$Price))+
  labs(title = 'Relationship between interested and views')+
  xlab("Views")+
  ylab("Interested")

ggplot()+
  geom_point(aes(x = table$Price, y = table$Ratio, col = table$Condition))+
  labs(title = 'Relationship between Ratio and price')+
  xlab("Price")+
  ylab("Ratio = Interested/Views")

ggplot()+
  geom_point(aes(y=table$Price, x = 1, col = table$Condition))+
  ylab("Price")

ggplot()+
  geom_histogram(aes(x = table$Ratio))

ggplot(data = table, aes(y = Price)) +
  geom_boxplot() +
  facet_grid(. ~ Condition)+
  labs(x = "Ratio = Interested/Views", 
       y = "Price")


for(condition in levels(table$Condition)){
  print(condition)
  t <- table %>% filter(Condition == condition)
  p <- ggplot()+
    geom_histogram(aes(x = t$Price), col = 'blue', binwidth = 5)+
    geom_vline(xintercept = median(t$Price), col = 'dark green')+
    labs(title = condition, subtitle = glue("Median price = ", median(t$Price), " euros"))+
    xlab("Price")+
    ylab('Occurences')
  print(p)
}
#-------------------------------------------------------------------#
#                       III - Correlation matrix 
#-------------------------------------------------------------------#

mydata.cor <- cor(table %>% dplyr::select(Price, Size, Views, Interested, Ratio), method = c("pearson"))
rownames(mydata.cor) <- colnames(mydata.cor) # hack
corrplot(mydata.cor, method = "color")
print(mydata.cor)



#-------------------------------------------------------------------#
# IV - Try to determine relation between interested/minute and other variables
#-------------------------------------------------------------------#

model <- lm(Ratio ~ ., data = table)
print(model)

model <- lm(Price ~ Condition + Size, data = table)
print(model)
