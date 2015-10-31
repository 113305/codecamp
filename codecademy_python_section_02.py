#2.1
meal = 44.50

#2.2
meal = 44.50
tax = 0.0675

#2.3
meal = 44.50
tax = 0.0675
tip = 0.15

#2.4
meal = 44.50
tax = 0.0675
tip = 0.15
meal = meal + meal*tax

#2.5
meal = 44.50
tax = 0.0675
tip = 0.15

meal = meal + meal * tax
total = meal + meal * tip

print("%.2f" % total)
