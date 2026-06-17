import pandas as pd

df = pd.read_csv("data/transactions.csv")
print(df)

#print number of transactions
#print the total income
#print total expenses


print("\n Total Transactions:" , len(df))

income = df[df["Amount"] > 0]["Amount"].sum()
expenses = abs(df[df["Amount"] < 0] ["Amount"].sum())

print(f" Total Income: ${income:.2f}")
print(f" Total Expenses:  ${expenses:.2f}")