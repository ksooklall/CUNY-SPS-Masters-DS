# 1. Create a vector that contains 20 numbers.
# (You may choose whatever numbers you like,
# but make sure there are some duplicates.)

x <- c(1:10, 2:9, 7:8)

# 2. Use R to convert the vector from question 1 into a character vector.
charVec <- as.character(x)

# 3. Use R to convert the vector from question 1 into a vector of factors
factVec <- as.factor(x)

# 4. Use R to show how many levels the vector in the previous question has.
fv_levels <- nlevels(factVec)

# 5 Use R to create a vector that takes the vector from
# question 1 and performs on it the formula 3x^2 - 4x + 1
nv <- 3 * x ^ 2 - 4 * x + 1

#6. Create a named list. That is, create a list with several elements
# that are each able to be referenced by name.
namelist <- list(val1=1, val2=2, val3=3)
namedlist <- list(rank = 1:5, players = c("Ada Lovelace", "Grace Hopper"))

# 7. Create a data frame with four columns - one each character,
# factor (with three levels), numeric, and date.
# Your data frame should have at least 10 observations (rows).
c1 <- c('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j')
c2 <- c(1:10)
c3 <- seq(as.Date("2020/12/01"), by = "day", length.out = 10)
c4 <- c(10:19)
my_df <- data.frame(c1, c2, c3, c4)

title <- as.character(c("Unforgiven","The Deer Hunter", "It Happened One Night",
                        "The Bridge on the River Kwai", "Lawrence of Arabia",
                        "The Silence of the Lambs", "The Godfather Part II", "Casablanca",
                        "The Godfather", "All about Eve"))
genre <- c("Western", "Drama", "Comedy",
           "Drama", "Drama", "Drama", "Drama", "Drama", "Drama", "Drama")
wins <- as.numeric(c(4, 8, 5, 7, 7, 5, 6, 3, 3, 6))
release <- as.Date(c("1992-1-1", "1978-1-1", "1934-1-1", "1957-1-1", "1962-1-1",
                     "1991-1-1", "1974-1-1", "1943-1-1", "1972-1-1", "1950-1-1"))
df <- data.frame(title, genre, wins, release)

# 8. Illustrate how to add a row with a value for the factor column that isn't already in the list of levels
# (Note: You do not need to accomplish this with a single line of code.)

#df[nrow(df)+1] = c("West Side Story", "Musical", 10, "1961-1-1")
df <- rbind(df, data.frame(title="West Side Story", genre="Musical", wins=10, release="1961-1-1"))

# 9. Show the code that would read in a CSV file called temperatures.csv
# from the current working directory.
tdf <- read.csv('temperature.csv')

# 10. Use a loop to calculate the final balance, rounded to the nearest cent,
# in an account that earns 3.24% interest compounded monthly after six years
# if the original balance is $1,500.

bal <- 1500
years <- 6
months <- c(0: (years * 12-1))
interest_rate <- 0.0324
# 1500 * ( 1 + 0.0324/12) ^ (12 * 6)
for (i in months) {
  interest <- interest_rate / 12
  bal <- bal + (bal * interest)
}
bal <- round(bal, 2)


# 11. Create a numeric vector of length 20 and
# then write code to calculate the sum of every third element of the vector you have created.

vect <- c(1:20)
vsum <- 0
for (i in c(1:length(vect))) {
  if (i %% 3 == 0) {
    vsum <- vsum + vect[i]
  }
}
# sum(vect[vect %% 3 == 0])

# 12 Use a for loop to calculate sum of i = 1 to 10 of x^i for the value x=2
fsum = 0
for (i in c(1:10)) {
  fsum <- fsum + 2^i
}

# 13. Use a while loop to accomplish the same task as in the previous exercise.
wsum <- 0
s <- 1
while (s <= 10) {
  wsum <- wsum + 2 ^ s
  s <- s + 1
  print(s)
}

# 14. Solve the problem from the previous two exercises without using a loop.
noloop <- sum(2^(c(1:10)))