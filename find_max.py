numbers = [3, 6, 2, 8, 40, 10]
max_val = numbers[0]
for number in numbers:
  if number > max_val:
      max_val = number
print(f"Maximum value in the list is:{max_val}")