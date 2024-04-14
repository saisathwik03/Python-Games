def initializeWallet():
    wallet={'balance':10000, 'credit_history':[], 'debit_history':[], 'mini_statement':[], 'total_history':[]}
    return wallet

def displaybalance(wallet):
    current_balance=wallet['balance']
    return current_balance

def addfunds(wallet,amount):
    m=0
    if amount<=0:
        print("amount should not be zero(0) or negative")
    elif amount > 0:
        wallet['balance']=wallet['balance']+amount
        wallet['credit_history'].append('credited_amount: ' + str(amount))
        wallet['mini_statement'].append(str(amount))
        m=wallet['mini_statement'][-1:-6:-1]
        m=m[::-1]
        print("current balance: ", wallet['balance'])
        print("credited amount", wallet['credit_history'])
        print("history of first five transactions:",m)

def makepayment(wallet,amount):
    m=0
    if amount <= 0:
        print("enter valid input")
    elif amount > wallet['balance']:
        print("in sufficient funds")
    else:
        wallet['balance']=wallet['balance']-amount
        wallet['debit_history'].append('debited amount:' + str(amount))
        wallet['mini_statement'].append(str(amount))
        m=wallet['mini_statement'][-1:-6:-1]
        m=m[::-1]
        print("current balance: ", wallet['balance'])
        print("debited amount", wallet['debit_history'])
        print("history of first five transactions:",m)

def transaction_history(wallet):
    total = wallet['credit_history'] + wallet['debit_history']
    wallet['total_history'].append(total)
    print(wallet['total_history'])

def usewallet():
    print("Wlecome to mywallet", initializeWallet())
    wallet=initializeWallet()

    while True:
        print( """
          Menu Loop:
          a: view balance
          b: add Funds
          c: make payment
          d: view transaction history
          e: Exit
          """)
        print()
        choice=input("enter choice a/b/c/d/e: ")
        print()
        if choice=='a':
            print(displaybalance(wallet))
            print()
        elif choice=='b':
            amount=float(input("enter amount to add: "))
            addfunds(wallet,amount)
            print()
        elif choice=='c':
            amount=float(input("enter amount to make payment: "))
            makepayment(wallet,amount)
            print()
        elif choice=='d':
            transaction_history(wallet)
            print()
        elif choice=='e':
            return

usewallet()