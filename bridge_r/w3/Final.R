library("ggplot2")
library('dplyr')
library("wordcloud")
"
Dataset Storm tracks data

Description
This data is a subset of the NOAA Atlantic hurricane database best track data, https://www.nhc.noaa.gov/data/#hurdat. The data includes the positions and attributes of 198 tropical storms, measured every six hours during the lifetime of a storm.

Format
A tibble with 10,010 observations and 13 variables:

name
Storm Name

year,month,day
Date of report

hour
Hour of report (in UTC)

lat,long
Location of storm center

status
Storm classification (Tropical Depression, Tropical Storm, or Hurricane)

category
Saffir-Simpson storm category (estimated from wind speed. -1 = Tropical Depression, 0 = Tropical Storm)

wind
storm's maximum sustained wind speed (in knots)

pressure
Air pressure at the storm's center (in millibars)

ts_diameter
Diameter of the area experiencing tropical storm strength winds (34 knots or above)

hu_diameter
Diameter of the area experiencing hurricane strength winds (64 knots or above)
"

df <- read.csv('https://vincentarelbundock.github.io/Rdatasets/csv/dplyr/storms.csv')
df$date <- paste(df$year, df$month, df$day, sep='-')
df <- df[ , !(names(df) %in% c('month', 'day', 'hour', 'X'))]

global_stats <- summary(df)

# Number of storms per year
# Are storms getting stronger
ydf <- as.data.frame(table(df$year))
colnames(ydf) <- c('Year', 'Frequency')
#barplot(storm_counts, main=' Number of storms by year', xlab='Year', ylab='Count', col=c('darkblue', 'red')) + geom_text(stat='count', aes(label=..count..), vjust=-1)
ydf <- as.data.frame(table(df$year))
colnames(ydf) <- c('Year', 'Frequency')
#ggplot(ydf, aes(x = Year, y = Frequency, fill=Frequency)) + geom_bar(stat = "identity") + geom_text(aes(label = Frequency), nudge_y=1, check_overlap=TRUE)+ scale_x_discrete(guide = guide_axis(angle = 90))
ggplot(ydf, aes(x = Year, y = Frequency)) + geom_col(aes(fill = Frequency)) + geom_text(aes(label = Frequency), angle = 90)
# Number of storms per year with category, stacked bar plot
# df.groupby(['year', 'status'])['status'].count().unstack().plot(kind='bar', stacked=True); plt.show()
tb1 <- table(df$status, df$year)
barplot(tb1, xlab='Year', ylab='Status Counts', col=c('red','green','blue'))
legend(x=1, y=575, legend=unique(df$status), fill=c('red','green','blue'))

# Pressue and wind relation
qplot(df$pressure, df$wind, main='Pressure vs Wind', xlab='Pressure (millibars)', ylab='Wind (knots)', col=df$status) + theme(plot.title = element_text(hjust = 0.5))

# Location map
#geoplot(lat=df$lat, lon=df$long)

# Most popular storm
edf <- subset(df, name =='Emily')

# Hurricane that did the most damage
#df.groupby('name').agg('hu_diameter': 'sum', 'ts_dismeter': 'sum')
hdf <- df %>% group_by(name) %>% summarise(Hurricane = sum(hu_diameter), Tropical_Storm = sum(ts_diameter))
hdf <- filter(hdf, Tropical_Storm > 0)
hdf <- melt(hdf, id.vars ="name", measure.vars = c("Hurricane","Tropical_Storm"))
colnames(hdf) <- c('name', 'Storm_Type', 'value')

ggplot(hdf, aes(value, name, colour = Storm_Type)) + labs(title="Storm Damage", x ="Name", y = "Area (miles^2)") + theme(plot.title = element_text(hjust = 0.5)) + scale_x_discrete(guide = guide_axis(angle = 90)) + geom_point()
ggplot(hdf, aes(name, value, colour = Storm_Type)) + labs(title="Storm Damage", x ="Name", y = "Area (miles^2)") + theme(plot.title = element_text(hjust = 0.5)) + scale_x_discrete(guide = guide_axis(angle = 90)) + geom_point()


# Where are storms in most recent years
edf <- filter(df, name == 'Emily')


# Number of hurricanes between 1975-2015: 198
length(unique(df$name))

# Word cloud of names
cdf <- count(df, name)
wordcloud(words = cdf$name, freq = cdf$n, color = 'blue', size = 1, shape = "circle", backgroundColor = "white") 