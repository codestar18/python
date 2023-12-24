has_high_income = False
has_good_credit = True
has_criminal_record = True

if has_good_credit and has_high_income:
    print("Eligible for loan")
else:
    print("Not Eligible")

if has_good_credit or has_high_income:
    print("Eligible")
else:
    print("Not eligible")

if has_criminal_record and not has_high_income:
    print("True")