#  Write a Python program to add elements to a list using insert() and append().
#  Write a Python program to remove elements from a list using pop() and remove().
'''
List1=['rishu','biaksh','bikky','sajan']
print(List1)
print("-"*20)
List1.insert(1,'megha')
print(List1)
print("-"*20)

List1.append('puja')
print(List1)
print("-"*20)

List1.pop()
print(List1)
print("-"*20)

List1.remove('biaksh')
print(List1)

'''

# Practical Examples: 
# 3) Write a Python program to update a list using insert() and
# append(). 
# 4) Write a Python program to remove elements from a list using pop() and
# remove().

List2=[]

def update_el(index,value):
    List2[index]=value

def add_el(value,index=None):
    if index is None:
        List2.append(value)
    else:
        List2.insert(index,value)

def delete_el(value=None):
    if value is None:
        List2.pop()
    else:
        List2.remove(value)

while True:
    
    if List2==[]:
        user=input('Enter some elements in the List: ')
        add_el(user)
    else:
        cho=input('Enter your choice :\n1.Update\n2.Add\n3.Delete: ')
        if cho=='1':
            index=int(input('Enter the index to update: '))
            value=input('Enter the value to update: ')
            update_el(index,value)
            print(List2)
        elif cho=='2':
            value=input('Enter the value to add: ')
            n=int(input('Do you want add a value with index 1.yes/2.no: '))
            if n==1:
                index=int(input('Enter the index to add: '))
                add_el(value,index)
            else:
                add_el(value)
        elif cho=='3':
            value=input('Enter the value to delete: ')
            delete_el(value)
        else:
            print(List2)
            break