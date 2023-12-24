price = 1000000
buyer_has_good_credit = False
if buyer_has_good_credit:
    down_payment = (0.1*price)
else:
    down_payment = (0.2*price)
print(f"Down Payment: ${down_payment}")