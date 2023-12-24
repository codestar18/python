course = "Python for Beginners"

'''Difference between Functions and Methods
.upper and others only belong to strings so they are 
called (methods)
but len,print not only belongs to strings so they are called
fuctions'''
print(len(course))
print(course.upper())
print(course.lower())
print(course.isalnum())
print(course.islower())
print(course.isupper())
print(course.find('P'))#returns the position of first occurance of the letter
#it is case sensitive
#it returns negative value if the letter doesn't exist

print(course.find('Q'))#find
print(course.replace('Beginners','Vitians'))#find and replace
#replcae replaces it temporarily
print("Beginners" in course)