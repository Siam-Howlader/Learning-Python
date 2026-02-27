account_numbers = []
account_names = []
balances = []
flag = True
menu = f"""#{'='*30} MENU {'='*30}
#{' '*26}1. Create Account{' '*22}#
#{' '*26}2. Deposit{' '*29}#
#{' '*26}3. Withdraw{' '*28}#
#{' '*26}4. Transfer{' '*28}#
#{' '*26}5. Show All Accounts{' '*19}#
#{' '*26}6. Search Account{' '*22}#
#{' '*26}7. Richest Account{' '*21}#
#{' '*26}8. Total Bank Balance{' '*18}#
#{' '*26}9. Sort Accounts by Balance{' '*12}#
#{' '*26}10. Exit{' '*31}#
#{'='*65}#
"""
while (flag):
    print(menu)
    m = int(input("Eneter number(1-5) : "))
    if m==10:
        print(f"\n{"="*66}\n#{" "*28} EXITED {" "*28}#\n{"="*66}")
        flag = False
        break
    elif m == 1:
        while(True):
            acc_number = input("Enter account number(6-digit) : ")
            if len(acc_number) == 6 and acc_number.isnumeric():
                if acc_number not in account_numbers:
                    account_numbers.append(acc_number)
                    acc_name = input("Enter Name : ").strip()
                    account_names.append(acc_name)
                    while (True):
                        balance = int(input("Enter initial balance : "))
                        if balance >= 0:
                            break
                    balances.append(balance)
                else:
                    print("Already have an account.")
                break
            else:
                print("Account number must contain 6 digits and no character allowed.")
    elif m == 2:
        while True:
            acc_number = input("Enter account number(6-digits) : ")
            if len(acc_number)==6 and acc_number.isnumeric():
                if acc_number in account_numbers:
                    while True:
                        amount = int(input("Enter the amount : "))
                        if amount>=0:
                            break
                        else:
                            print("Amount must be greater than or equal to 0.")
                    idx = account_numbers.index(acc_number)
                    balances[idx]+=amount
                    print(f"{amount} tk deposited to account number {acc_number}")
                    break
                else:
                    print("Account not found!")
            else:
                print("Account number should contain 6 digits and no character allowed.")
    elif m == 3:
        while True:
            acc_number = input("Enter account number(6-digits) : ")
            if len(acc_number) == 6 and acc_number.isnumeric():
                if acc_number in account_numbers:
                    while True:
                        amount = int(input("Enter the amount : "))
                        if amount >= 0:
                            idx = account_numbers.index(acc_number)
                            if balances[idx]>=amount:
                                balances[idx] -= amount
                                print(f"{amount} tk withdrawed successfuly from account number {acc_number}")
                            else:
                                print("Not enough balance!")
                            break
                        else:
                            print("Amount must be greater than or equal to 0.")
                    break
                else:
                    print("Account not found!")
            else:
                print("Account number should contain 6 digits and no character allowed.")
    elif m == 4:
        while True:
            from_acc = input("From account number : ")
            to_acc = input("From account number : ")
            f1=False
            f2=False
            if len(from_acc)==6 and from_acc.isnumeric():
                f1=True
            if len(to_acc) == 6 and to_acc.isnumeric():
                f2 = True
            if (f1) and (f2):
                if from_acc in account_numbers and to_acc in account_numbers:
                    while True:
                        amount = int(input("Enter the amount : "))
                        if amount >= 0:
                            from_idx = account_numbers.index(from_acc)
                            to_idx  = account_numbers.index(to_acc)
                            if(balances[from_idx]>=amount):
                                balances[from_idx]-=amount
                                balances[to_idx]+=amount
                                print(f"{amount} tk transferred from {from_acc} to {to_acc} successfully!")
                                break
                            else:
                                print(f"Not enough balance in account {from_acc}")
                        else:
                            print("Amount must be greater than or equal to 0.")
                    break
                else:
                    print("Account number not found!")
    elif m == 5:
        for i in range(0,len(account_names)):
            print(f"Acc No: {account_numbers[i]} | Name: {account_names[i]} | Balance: {balances[i]}")
    elif m == 6:
        search_acc = input("Enter name or account number : ").strip()
        if search_acc.lower() in account_names or search_acc in account_numbers:
            if search_acc.isnumeric():
                idx=account_numbers.index(search_acc)
            else:
                idx = account_names.index(search_acc.lower())
            print(
                f"Acc No: {account_numbers[idx]} | Name: {account_names[idx]} | Balance: {balances[idx]}")
        else:
            print("Account not found!")
    elif m == 7:
        idx = balances.index(max(balances))
        print(
            f"Acc No: {account_numbers[idx]} | Name: {account_names[idx]} | Balance: {balances[idx]}")
    elif m == 8:
        sum=0
        for i in balances:
            sum+=i
        print(f"Total bank balance : {sum} tk")
    elif m == 9:
        for i in range(0,len(account_names)):
            for j in range(i+1,len(account_names)):
                if balances[i]<balances[j]:
                    balances[j], balances[i] = balances[i], balances[j]
                    account_names[j], account_names[i] = account_names[i], account_names[j]
                    account_numbers[j], account_numbers[i] = account_numbers[i], account_numbers[j]
        for i in range(0, len(account_names)):
            print(
                f"Acc No: {account_numbers[i]} | Name: {account_names[i]} | Balance: {balances[i]}")
    else:
        print("Enter correct number. Thank you.")