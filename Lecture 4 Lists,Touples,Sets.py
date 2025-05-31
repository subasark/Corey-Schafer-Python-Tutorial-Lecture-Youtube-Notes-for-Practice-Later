# List = [1,2,3]
# Touple = (1,2,3)
# Set = {1,2,3}


## Lists
# Lists and Touples allows use to work with Sequential data
# Lists are mutable but touples are imutable

courses = ['History','Math','Physics','CompSci']
courses_2 = ['Art','Education']

#print(courses)

#Length of the list
#print(len(courses))

#Access individual items of the list
#print(courses[2])
#It's useful to use -1 to check the last item of our list if we do not know the length of our list

#Access range of items from a list
#print(courses[2:])

## List Methods

# Add a item in our list

# Apeends at the end of the list
#courses.append('Art') 
#it takes only one parameter

# Insert at a particular place of the list
# it takes two parameters first is the postion and the second one is the value
#courses.insert(0,'Art')

# Extend method : use to add multiple values from a list 
#courses.extend(courses_2)
#print(courses)

# Remove items from list 
# remove method
#courses.remove('Math')

# pop method : to remove the last element from the list
#popped = courses.pop()
#print(popped)
#print(courses)

# Reverse Lists
#courses.reverse()
#print(courses)

# Sort Lists
#courses.sort()
#print(courses)

#nums = [1,5,2,4,3]
#nums.sort()
#print(nums)
#sort method will alter the orignial list

#If you do not want to alter the orignal list you can use sort function 
#sorted_courses = sorted(courses)
#print(courses)
#print(sorted_courses)  

#Sort in reverse order
#nums = [1,5,2,4,3]
#nums.sort(reverse=True)
#print(nums)

# Min,Max,Sum

#nums = [1,5,2,4,3]
#print(min(nums))
#print(max(nums))
#print(sum(nums))

# Finding Values

#print(courses.index('CompSci'))
#print(courses.index('Art'))

#print('Math' in courses)
#print('Art' in courses)

#Print all the values of the list
#for course in courses:
#	print(course)

#Print all the values and index : Enumerate
#for index, course in enumerate(courses):
#	print(index, course)

#Convert Lists into strings
#courses_str = ', '.join(courses)
#print(courses_str)

#Convert Strings into Lists

#new_list = courses_str.split(', ')
#print(new_list)

## Touples

# Mutable

# list_1 = ['History', 'Math', 'Physics', 'CompSci']
# list_2 = list_1

# print(list_1)
# print(list_2)

# list_1[0] = 'Art'

# print(list_1)
# print(list_2)


# Immutable

# tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
# tuple_2 = tuple_1

# print(tuple_1)
# print(tuple_2)

# tuple_1[0] = 'Art'

# print(tuple_1)
# print(tuple_2)


# Sets
# Sets are Unordered collections of values with no duplicates
# Sets don't care about order
# Sets avoid duplicates

# cs_courses = {'History', 'Math', 'Physics', 'CompSci','Math'}
# art_courses = {'History', 'Math', 'Art', 'Design'}

#print('Math' in cs_courses)

#Compare two sets and check what are common in them , different in them and union them ?

# print(cs_courses.intersection(art_courses))
# print(cs_courses.difference(art_courses))
# print(cs_courses.union(art_courses))

# Empty Lists
empty_list = []
empty_list = list()

# Empty Tuples
empty_tuple = ()
empty_tuple = tuple()

# Empty Sets
empty_set = {} # This isn't right! It's a dict
empty_set = set()




