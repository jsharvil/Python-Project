import tkinter as tk
from tkinter import messagebox

Menu = {
    "Latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 150
    },
    "Espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 20,
        },
        "cost": 100,
    },
    "Cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 200,
    }
}

profit = 0
resources = {
    "water": 500,
    "milk": 200,
    "coffee": 100,
}

def check_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            messagebox.showwarning("Coffee Machine", f"Sorry, not enough {item}.")
            return False
    return True

def process_coins():
    total = int(input("Please insert your money 💸.\nEnter your amount: Rs"))
    return total

def is_payment_successful(money_received, coffee_cost):
    global profit
    if money_received >= coffee_cost:
        profit += coffee_cost
        change = money_received - coffee_cost
        messagebox.showinfo("Coffee Machine", f"Here is your Rs{change} in change.")
        return True
    else:
        messagebox.showwarning("Coffee Machine", "Sorry, not enough money. Money refunded!")
        return False

def make_coffee(coffee_name, coffee_ingredients):
    for item in coffee_ingredients:
        resources[item] -= coffee_ingredients[item]
    messagebox.showinfo("Coffee Machine", f"Here is your {coffee_name}. Enjoyyyy!!!!!!!😊")

def withdraw_money():
    global profit
    withdrawal_amount = int(input("Enter the amount to withdraw from the machine's profit: Rs"))
    if withdrawal_amount <= profit:
        profit -= withdrawal_amount
        messagebox.showinfo("Coffee Machine", f"You have successfully withdrawn Rs{withdrawal_amount} from the machine's profit.")
    else:
        messagebox.showwarning("Coffee Machine", "Sorry, insufficient funds in the machine's profit.")

password = "xyz@1234"
password1 = "abc@1234"

def order_coffee(choice):
    if choice.lower() == "off":
        window.destroy()
    elif choice.lower() == "report":
        enter_password = input("Enter the password to access the report: ")
        if enter_password == password:
            print(f"water={resources['water']}ml")
            print(f"milk={resources['milk']}ml")
            print(f"coffee={resources['coffee']}gm")
            print(f"Money=Rs{profit}")
        else:
            messagebox.showwarning("Coffee Machine", "Incorrect password. Access denied ❌.")
    elif choice.lower() == "withdraw":
        enter_pass = input("Enter password to withdraw money 💸💸💸💸 :")
        if enter_pass == password1:
            withdraw_money()
        else:
            messagebox.showwarning("Coffee Machine", "Incorrect password ❌")
    else:
        coffee_type = Menu.get(choice)
        if coffee_type:
            if check_resources(coffee_type['ingredients']):
                payment = process_coins()
                if is_payment_successful(payment, coffee_type['cost']):
                    make_coffee(choice, coffee_type['ingredients'])
            else:
                messagebox.showwarning("Coffee Machine", "Not enough resources. Please choose another option.")
        else:
            messagebox.showwarning("Coffee Machine", "Invalid choice. Please select a valid coffee option.")

# Create Tkinter GUI
window = tk.Tk()
window.title("Coffee Machine")

label = tk.Label(window, text="☕ COFFEE MACHINE ☕", font=("Helvetica", 16))
label.grid(row=0, column=0, columnspan=3, pady=10)

choices = ["Latte", "Espresso", "Cappuccino", "Report", "Withdraw", "Off"]
for i, choice in enumerate(choices):
    btn = tk.Button(window, text=choice, width=30,height=2, command=lambda ch=choice: order_coffee(ch))
    btn.grid(row=i // 3 + 1, column=i % 3, padx=5, pady=5)

window.mainloop()
