#  Write a Python program to iterate over a list using a for loop.
#  Write a Python program to sort a list using both sort() and sorted().
'''
List1=['rishu','bikash','sanjet','sajan','bikky']
for value in List1:
    print(value)


List2=[4,2,5,3,9,6,7,10]
# List2.sort()
# print(List2)

List2=sorted(List2,reverse=True)
print(List2)
'''
# Practical Examples:

# 5) Write a Python program to iterate through a list and print each
# element. 
# 6) Write a Python program to insert elements into an empty list using a for loop and
# append().


List3=[]

while True:
    print('-'*40)
    choice=input('Enter your choice \n 1.print elements \n 2.insert elements \n ')
    print('-'*40)
    if choice=='1':
        for val in List3:
            print(val)
    elif choice=='2':
        value=input('Enter the value to insert: ')
        List3.append(value)
    else:
        break
        

