numbers= { "1":"one",
           "2":"two",
           "3" : "three",
           "4" : "four",
           "5" : "five",
           "6" : "six",
           "7" : "seven",
           "8" : "Eight",
           "9" : "Nine"
           }
output = ""
inp = input("Enter the numbers:")
for i in inp:
    output = output+numbers.get(i)+" "
print(output)