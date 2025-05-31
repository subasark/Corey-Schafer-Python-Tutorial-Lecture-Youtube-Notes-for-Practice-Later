# Dictionary
# Key , Value pair
# Key : Unqiue identifier , Value : Data
# Keys usually a int or a string

student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']} 



# print(student) #Prints the dictionary
# print(student['courses']) #Prints the data provided by the key 

# get method to get the value of key by passing the key
# print(student.get('courses'))

#get method with pre defined argument
#print(student.get('phone', 'Not Found'))

# Add a new entry to the dict
# student['phone'] = '99999-11111'

# similarly we can update any value same way
# student['name'] = 'Jane'

# Update multiple values in one shot using the update method , we can update exsting values as well as add new values
# student.update({'name': 'Jane', 'age': '26', 'phone': '55555-11111'})

# Delete key from dict
# del student['age']
# age = student.pop('age')

# print(len(student)) # length of the dict
# print(student.keys())
# print(student.values())
# print(student.items())

# Loop through all the keys and values in a dict

#for key, value in student.items():
#	print(key, value)



