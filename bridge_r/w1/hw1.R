"
Please create the following exercises in .rmd format, publish to rpub and submit both the .rmd file and
the rpub link.
"

# 1. Write a loop that calculates 12-factorial

fact <- 1
for (i in c(1:12)) {
  fact <- fact * i
}
print(factorial(12) == fact)
sprintf('12 factorial = %i', fact)
  
# 2. Show how to create a numeric vector that contains the sequence from 20 to 50 by 5.

vect1 <- c(20:50)
vect1 <- as.numeric(vect1)
vect1 <- vect1[vect1 %% 5 == 0]

vect2 <- c(20:50)[c(20:50) %% 5 == 0]
print(all(vect1 == vect2) == 1)

# 3. Create the function “quadratic” that takes a trio of input numbers a, b, and c and solve the quadratic equation. 
# The function should print as output the two solutions.

quadratic <- function(a, b, c) {
  numeratorp <- -b + sqrt(b^2 - 4 * a * c)
  numeratorn <- -b - sqrt(b^2 - 4 * a * c)
  denominator <- 2 * a
  ans <- c(numeratorp /denominator, numeratorn / denominator)
  
  return (ans)
}

printf(quadratic(2, -5, -3))