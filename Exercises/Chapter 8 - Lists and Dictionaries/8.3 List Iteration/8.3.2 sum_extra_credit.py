test_grades = [101, 83, 107, 90]
sum_extra = -999 # Initialize 0 before your loop

sum_extra = 0

for score in test_grades:
    if score > 100:
        sum_extra += (score-100)

print('Sum extra:', sum_extra)