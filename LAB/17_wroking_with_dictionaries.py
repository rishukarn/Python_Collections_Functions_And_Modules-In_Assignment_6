#  Write a Python program to update a value in a dictionary.

dic={
    "name":"Rishu",
    "age":25,
    "city":"Birgunj",
    "country":"Nepal",
    "phone":9845012345,
    "email":"rishu@gmail.com"

}

dic['name']='bikash'
print(dic)

#  Write a Python program to merge two lists into one dictionary using a loop.

keys = ['name', 'age', 'city']
values = ['Alice', 25, 'New York']
dic1={}

for i in range(len(keys)):
    dic1[keys[i]]=values[i]

print(dic1)



# Practical Examples: 
# 15) Write a Python program to update a value at a particular key in a dictionary. 
# 16) Write a Python program to separate keys and values from a dictionary using keys() and values() methods. 
for key in dic.keys():
    print(key)
for value in dic.values():
    print(value)
for k ,v in dic.items():
    print(k,v)
# 17) Write a Python program to convert two lists into one dictionary using a for loop. 
# 18) Write a Python program to count how many times each character appears in a string.



text = "hello world"


char_count = {}


for char in text:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1
print(char_count)