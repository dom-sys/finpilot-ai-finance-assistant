import pandas as pd
import plotly.express as px 

#Functions

def load_transactions():
    return pd.read_csv("data/transactions.csv")
def calculate_summary(df):
 income = df[df["Amount"] > 0]["Amount"].sum()
 expenses = abs(df[df["Amount"] < 0] ["Amount"].sum())
 net_savings = income - expenses

 return income, expenses, net_savings, len(df) 

def calculate_category_totals(df):
    category_totals = (df[df["Amount"]< 0]
.groupby("Category")["Amount"].sum()
)
    return (abs(category_totals))

def find_largest_expense(df):
    return df.loc[df["Amount"].idxmin()]


df = load_transactions()
income, expenses, net_savings, total_transactions = calculate_summary(df)
print(f" Total Transactions:", total_transactions)

print(f" Total Income: ${income:.2f}")
print(f" Total Expenses:  ${expenses:.2f}")
print(f" Net Savings: ${net_savings:.2f}")

#check spending by category

category_totals = calculate_category_totals(df)
print("\n Spending by Category: ", category_totals)


#find the biggest expense
largest_expense = find_largest_expense(df)
print("\nLargest Expense: ")
print(f'{largest_expense["Description"]} - $ {abs(largest_expense["Amount"]):.2f}')


category_chart = abs(category_totals)
fig = px.bar(
    x = category_chart.index,
    y = category_chart.values, 
    labels = {"x": "Category", "y": "Amount($)"},
    title = "Spending by Category"
)
fig.show()
print(type(category_chart))