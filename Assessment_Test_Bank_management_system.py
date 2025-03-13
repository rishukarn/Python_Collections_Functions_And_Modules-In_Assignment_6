import datetime

dt=datetime.datetime.now()
# print(str(dt))
bank_Date={}
print('\t\tWELCOME TO PYTHON BANK MANAGEMENT SYSTEM\n')

def banker():

    print("Welcome to Banker's App\n \n\t\t Operation Menu\n")
    oper=int(input('\t\t1) Add Customer\n\t\t2) View Customer\n\t\t3) Search Customer\n\t\t4) View All Customer\n\t\t5) Total Amounts in Bank\n Enter operation which you want to perform : '))
    if oper==1:
        account_no=int(input('Enter account no : '))
        if account_no not in bank_Date:
            cust_name=input('Enter customer name : ')
            opening_blnc=int(input('Enter opening balance : '))
            bank_Date[account_no]={'name':cust_name,
                                    'balance':opening_blnc,
                                    'opening Date':str(dt)
                                }
        else:
            print('This account number already in your database')
    elif oper==2:
        account_no=int(input('Enter account no : '))
        print(bank_Date)
    elif oper==3:
        account_no=int(input('Enter account no : '))
        print(bank_Date[account_no])
    elif oper ==4:
        account_no=int(input('Enter account no : '))
        print(bank_Date)

    elif oper==5:
        totle_blnc=0
        for key in bank_Date:
            totle_blnc+=bank_Date[key]['balance']
        print(totle_blnc)

def customer():
    print("Welcome to Customer's App\n \n\t\t Operation Menu\n")
    oper=int(input('\t\t1) Withdraw Amount\n\t\t2) Deposite Amount\n\t\t3) View Balance\n\n Enter operation which you want to perform : '))

    if oper==1:
        ac_no=int(input('Enter your account no : '))
        if ac_no in bank_Date:
            withdraw_am=int(input('Enter a withdraw amount : '))
            bank_Date[ac_no]['balance']-=withdraw_am
            print(f'Your withdraw is successfully completed\n Current balance is {bank_Date[ac_no]['balance']}')
    elif oper==2:
        ac_no=int(input('Enter your account no : '))
        if ac_no in bank_Date:
            deposite_am=int(input('Enter a deposite amount : '))
            bank_Date[ac_no]['balance']+=deposite_am
            print(f'Your deposite is successfully completed\n Current balance is {bank_Date[ac_no]['balance']}')
    elif oper==3:
        ac_no=int(input('Enter your account no : '))
        if ac_no in bank_Date:
            print(f'Your balance is : {bank_Date[ac_no]['balance']}')


while True:
    print('\t\tSelect your role\n\n\t\t1) Banker\n\t\t2) Customer\n\t\t3) Exit\n')
    chose=int(input('choose your role : '))
    if chose==1:
        banker()
    elif chose==2:
        customer()
    elif chose==3:
        exit()
    else:
        print('Your inpute is invalid!')