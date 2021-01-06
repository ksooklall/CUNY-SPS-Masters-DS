path <- '/home/kenan/Documents/learning/masters/bridge_r/w2/'
library(RCurl)
"
region
A factor with levels: Africa; Asia, Asia and Pacific; Latin.Amer, Latin America and Caribbean; Near.East, Near East and North Africa.

tfr
Total fertility rate (children per woman).

contraceptors
Percent of contraceptors among married women of childbearing age.
"
df <- read.csv(paste(path, 'Robey.csv', sep=''))

# 1. Use the summary function to gain an overview of the data set. Then display the mean and median for at least two attributes.
summary(df)
print(mean(df$tfr))
print(median(df$contraceptors))

# 2. Create a new data frame with a subset of the columns and rows. Make sure to rename it.
sdf <- subset(df, region == 'Latin.Amer')

#3. Create new column names for the new data frame.
colnames(sdf) <- c('country', 'region', 'tfr', 'contra')

#4. Use the summary function to create an overview of your new data frame. The print the mean and median for the same two attributes. Please compare.
summary(sdf)
print(mean(sdf$tfr))
print(median(sdf$contra))

#5. For at least 3 values in a column please rename so that every value in that column is renamed.
#For example, suppose I have 20 values of the letter “e” in one column. Rename those values so that all 20 would show as “excellent”.
df$region <- as.character(df$region)
df$region[df$region == 'Latin.Amer'] <- "LatinAmerica"

#6. Display enough rows to see examples of all of steps 1-5 above.
print(sdf)
print(df)

#7. BONUS – place the original .csv in a github file and have R read from the link. This will be a very useful skill as you progress in your data science education and career.
text_data <- getURI('https://vincentarelbundock.github.io/Rdatasets/csv/carData/Robey.csv')
github_df <- read.csv(text=text_data)
head(github_df)
