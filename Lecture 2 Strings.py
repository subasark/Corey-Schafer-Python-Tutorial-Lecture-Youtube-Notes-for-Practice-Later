
message = "Hello World"

#to solve single quote problem we can use escape character \ or we can use "" for the string

#multiple line string

message_2 = """Subam is a good boy
he is intelligent too"""

#length of a string len()
#print(len(message))

#individual charactre of a string variablename[index_number]
#print(message[2])

#range of charactre of a string variablename[start_index_number:end_index_number]
#print(message[0:5]) or print(message[:5])
#print(message[6:10]) or print(message[6:])

#string methods

#make lower case
#print(message.lower())

#make upper case
#print(message.upper())

#count words or characters
#print(message.count('l'))

#find index of word or characters
#print(message.find('World'))

#replace method
#message = 'Hello World'
#message = message.replace('World','Universe')
#print(new_message)

#concat Strings
greeting = 'Hello'
name = 'Subam'

#message = greeting + ', ' + name + '. Welcome'
#formateed string
message = '{}, {}. Welcome'.format(greeting, name)

print(message)






