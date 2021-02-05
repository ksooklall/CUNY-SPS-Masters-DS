"""
EXAMPLE 3.54
Two books are assigned for a statistics class: a textbook and its corresponding study guide. The
university bookstore determined 20% of enrolled students do not buy either book, 55% buy the
textbook only, and 25% buy both books, and these percentages are relatively constant from one
term to another. If there are 100 students enrolled, how many books should the bookstore expect
to sell to this class?
"""

pnb = 0.2
pt = 0.55
pb = 0.25
n = 100

E = 1 * pt * n + 2 * pb * n
print(E)

"""
EXAMPLE 3.56
The textbook costs $137 and the study guide $33. How much revenue should the bookstore expect
from this class of 100 students?
"""

t = 137
sg = 33

R = pt * n * t + (t + sg) * pb * n
print(R)

"""
EXAMPLE 3.57
What is the average revenue per student for this course?
"""

Avg = pt * t + pb * (sg + t)
print('{} or {}'.format(Avg, R*1.0/n))


