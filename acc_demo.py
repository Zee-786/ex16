from account_class import Account

barclays007 = Account(6500.00)
barclays007.deposit(550.23)
barclays007.deposit(100)
barclays007.withdraw(50)

print('barclays balance', barclays007.getbalance())

hsbc008 = Account(0)
hsbc008.deposit(10)

secret_acc = Account(50000)
secret_acc.deposit(770000)

print('hsbc balance', hsbc008.getbalance())
print('savings balance', secret_acc.getbalance())
print('savings account number', Account.numCreated)

print("hsbc008 is class", hsbc008.__class__.__name__)
print('my main acc is class', secret_acc.__class__.__name__)
print('my main', secret_acc)
print('hsbc',hsbc008)

if secret_acc > hsbc008:
    print(f"{secret_acc} has more money than {hsbc008}!")
if hsbc008 < barclays007:
    print(f"{hsbc008} has less money than {barclays007}!")

print(Account.get_total_balance())
