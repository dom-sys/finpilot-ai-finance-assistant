from flask import Flask, render_template
import pandas as pd
app = Flask(__name__)

def load_transactions(): 
    return pd.read_csv("data/transactions.csv")

def calculate_summary(df): 
    income = df[df["Amount"] > 0]["Amount"].sum()
    expenses = abs(df[df["Amount"] < 0]["Amount"].sum())
    net_savings = income - expenses
    total_transactions = len(df)
    
    return income, expenses, net_savings, total_transactions



@app.route("/")
def home():
    df = load_transactions()
    income, expenses, net_savings, total_transactions = calculate_summary(df)


    return render_template( 
        "index.html",
    total_transactions=total_transactions,
    income= f"{income:.2f}",
    expenses= f"{expenses:.2f}",
    net_savings= f"{net_savings:.2f}"
    )

if __name__ == "__main__":
    app.run(debug =True)

