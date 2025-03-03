print("\nPython Dictionaries")

myDict = {'name': 'Hannah', 'age': 18, 'city': 'Massena' }

print("My name is", myDict['name'])


print("\nAdding/Updating items in a dictionary\n")

myDict['country'] = 'USA' # Adding a key value pair 


print(myDict)


myDict['age'] = 24

print(myDict)

print('\nRemove Items from a dictionary') 

del myDict['country']

print(myDict)

print("\nDelete an item from the Dictionary, and its value")

rem_value = myDict.pop('age')

print(rem_value)


print("\nA New Dictionary\n")

dictionary2 = {'fruits': [ 'apple', 'banana', 'orange'], 'vegetables': ['broccoli', 'brussel sprouts', 'carrots']} 


# add another fruit:

dictionary2['fruits'].append('cherry')

# Print the dictionary 

print(dictionary2)

print(dictionary2['fruits'])
