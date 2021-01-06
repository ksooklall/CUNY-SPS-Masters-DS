require(ggplot2)

#1. Load the diamonds dataset, which is included with the ggplot2 package. Identify which variables in the
#diamond set are numeric, and which are categorical (factors).
df <- diamonds
summary(df)

numeric_cols <- unlist(lapply(df, is.numeric))
categorical_cols <- unlist(lapply(df, is.factor))

#2. Generate summary level descriptive statistics: Show the mean, median, 25th and 75th quartiles, min, and
#max for each of the applicable variables in diamonds.
summary(df[, numeric_cols])

#3. Determine the frequency for each of the diamond colors.
table(df$color)

#4. Determine the frequency for each of the diamond cuts, by color
table(df$color, df$cut)

#5. Create a graph for a single numeric variable.
qplot(df$price)

#6. Create a scatterplot of two numeric variables.
qplot(x=df$carat, y=df$price)