#dictonaries have key value pairs
'''each key should be unique in a
 dictionary key = 'name,age,gender'
values = 'Jayasree,22,female'
keys are casesensitive'''
customer = {
    "name" : "Jayasree",
    "age" : 22,
    "gender" : "female"
}
print(customer)
print(customer["gender"])
'''using get doesn't give an error it just
 gives none as output
if given a wrong key value'''
print(customer.get(("Age")))
#updating key value
customer["name"] = "Jayasree Tummala"
print(customer["name"])
print(customer.get("Birthday" ,"18 December 2001"))

#additing new key
customer["Birthday"] = "18 December 2001"
print(customer)
