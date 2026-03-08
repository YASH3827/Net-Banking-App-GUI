from tkinter import *  # Importing all Tkinter widgets for GUI creation.
from tkinter import messagebox  # Importing messagebox for displaying alerts.
from bankdb import Database  # Importing the Database class for handling user data.
from bankapi import BankAPI  # Importing the BankAPI class for performing transactions.


class BankingApp:
    """A class to represent the banking application with a GUI using Tkinter."""

    def __init__(self):
        """Initializes the banking app, setting up the database, API, and GUI."""
        # Create database and API objects
        self.dbo = Database()  # Creating an instance of the Database class to interact with the user data.
        self.api = BankAPI()  # Creating an instance of the BankAPI class for financial transactions.

        # Initialize the GUI
        self.root = Tk()  # Initializing the Tkinter root window for the application.
        self.root.title("Internet Banking")  # Setting the window title.
        self.root.geometry("350x600")  # Setting the window size.
        self.root.configure(bg="#34495E")  # Setting the background color of the window.

        # Load the login GUI
        self.login_gui()  # Displaying the login GUI initially.

        self.root.mainloop()  # Running the Tkinter event loop to keep the app running.

    def login_gui(self):
        """Displays the login form in the GUI."""
        self.clear()  # Clears any existing widgets in the GUI.

        # Title for the login page
        Label(self.root, text="Internet Banking", bg="#34495E", fg="white", font=("Verdana", 20, "bold")).pack(pady=(30, 30))

        # Email input
        Label(self.root, text="Enter Email", bg="#34495E", fg="white").pack(pady=(10, 5))
        self.email_input = Entry(self.root, width=30)  # Entry widget for the email input.
        self.email_input.pack(ipady=5, pady=(0, 10))

        # Password input
        Label(self.root, text="Enter Password", bg="#34495E", fg="white").pack(pady=(10, 5))
        self.password_input = Entry(self.root, width=30, show="*")  # Entry widget for password input (with masking).
        self.password_input.pack(ipady=5, pady=(0, 10))

        # Login button
        Button(self.root, text="Login", width=20, command=self.perform_login).pack(pady=(20, 10))

        # Register button and message for non-members
        Label(self.root, text="Not a member?", bg="#34495E", fg="white").pack(pady=(10, 5))
        Button(self.root, text="Register Now", command=self.register_gui).pack(pady=(5, 10))

    def register_gui(self):
        """Displays the registration form in the GUI."""
        self.clear()  # Clears any existing widgets in the GUI.

        # Title for the registration page
        Label(self.root, text="Register", bg="#34495E", fg="white", font=("Verdana", 20, "bold")).pack(pady=(30, 30))

        # Name input
        Label(self.root, text="Enter Name", bg="#34495E", fg="white").pack(pady=(10, 5))
        self.name_input = Entry(self.root, width=30)  # Entry widget for name input.
        self.name_input.pack(ipady=5, pady=(0, 10))

        # Email input
        Label(self.root, text="Enter Email", bg="#34495E", fg="white").pack(pady=(10, 5))
        self.email_input = Entry(self.root, width=30)  # Entry widget for email input.
        self.email_input.pack(ipady=5, pady=(0, 10))

        # Password input
        Label(self.root, text="Enter Password", bg="#34495E", fg="white").pack(pady=(10, 5))
        self.password_input = Entry(self.root, width=30, show="*")  # Entry widget for password input (with masking).
        self.password_input.pack(ipady=5, pady=(0, 10))

        # Register button
        Button(self.root, text="Register", width=20, command=self.perform_registration).pack(pady=(20, 10))

        # Back to login button
        Button(self.root, text="Back to Login", command=self.login_gui).pack(pady=(10, 10))

    def clear(self):
        """Clears all widgets from the current GUI."""
        for widget in self.root.pack_slaves():  # Iterates through all widgets in the window.
            widget.destroy()  # Destroys each widget, effectively clearing the GUI.

    def perform_registration(self):
        """Handles the user registration logic."""
        name = self.name_input.get()  # Retrieves the name input.
        email = self.email_input.get()  # Retrieves the email input.
        password = self.password_input.get()  # Retrieves the password input.

        if self.dbo.add_user(name, email, password):  # Adds the user to the database.
            messagebox.showinfo("Success", "Registration Successful!")  # Shows a success message.
            self.login_gui()  # Navigates back to the login GUI.
        else:
            messagebox.showerror("Error", "Email already exists!")  # Shows an error message if email is already registered.

    def perform_login(self):
        """Handles the user login logic."""
        email = self.email_input.get()  # Retrieves the email input.
        password = self.password_input.get()  # Retrieves the password input.

        if self.dbo.authenticate_user(email, password):  # Verifies the user's credentials.
            messagebox.showinfo("Success", "Login Successful!")  # Shows a success message.
            self.dashboard_gui(email)  # Navigates to the user's dashboard.
        else:
            messagebox.showerror("Error", "Invalid Email/Password!")  # Shows an error message for invalid credentials.

    def dashboard_gui(self, email):
        """Displays the user's dashboard with account options."""
        self.clear()  # Clears the current GUI.

        # Title for the dashboard
        Label(self.root, text="Dashboard", bg="#34495E", fg="white", font=("Verdana", 20, "bold")).pack(pady=(30, 30))

        # Buttons for various actions in the dashboard
        Button(self.root, text="View Balance", width=20, command=lambda: self.view_balance(email)).pack(pady=(10, 10))
        Button(self.root, text="Deposit Money", width=20, command=lambda: self.transaction_gui(email, "deposit")).pack(pady=(10, 10))
        Button(self.root, text="Withdraw Money", width=20, command=lambda: self.transaction_gui(email, "withdraw")).pack(pady=(10, 10))
        Button(self.root, text="Transfer Funds", width=20, command=lambda: self.transaction_gui(email, "transfer")).pack(pady=(10, 10))
        Button(self.root, text="Logout", width=20, command=self.login_gui).pack(pady=(20, 10))

    def view_balance(self, email):
        """Displays the user's current balance in a message box."""
        balance = self.dbo.get_balance(email)  # Retrieves the user's balance from the database.
        messagebox.showinfo("Balance", f"Your current balance is: ${balance:.2f}")  # Displays the balance in a message box.

    def transaction_gui(self, email, transaction_type):
        """Displays the transaction form for deposit/withdraw/transfer."""
        self.clear()  # Clears the current GUI.

        # Title for the transaction form
        Label(self.root, text=transaction_type.capitalize(), bg="#34495E", fg="white", font=("Verdana", 20, "bold")).pack(pady=(30, 30))

        # Amount input for the transaction
        Label(self.root, text="Enter Amount", bg="#34495E", fg="white").pack(pady=(10, 5))
        self.amount_input = Entry(self.root, width=30)  # Entry widget for amount input.
        self.amount_input.pack(ipady=5, pady=(0, 10))

        if transaction_type == "transfer":  # If the transaction type is transfer, show recipient input.
            Label(self.root, text="Recipient Email", bg="#34495E", fg="white").pack(pady=(10, 5))
            self.recipient_input = Entry(self.root, width=30)  # Entry widget for recipient email input.
            self.recipient_input.pack(ipady=5, pady=(0, 10))

        # Submit button for the transaction
        Button(self.root, text="Submit", width=20, command=lambda: self.perform_transaction(email, transaction_type)).pack(pady=(20, 10))
        Button(self.root, text="Back to Dashboard", width=20, command=lambda: self.dashboard_gui(email)).pack(pady=(10, 10))

    def perform_transaction(self, email, transaction_type):
        """Performs the transaction (deposit, withdraw, or transfer)."""
        amount = float(self.amount_input.get())  # Retrieves the amount input and converts it to float.
        if transaction_type == "deposit":
            self.dbo.update_balance(email, amount)  # Updates the balance for deposit.
            messagebox.showinfo("Success", "Deposit Successful!")  # Shows success message.
        elif transaction_type == "withdraw":
            if self.dbo.update_balance(email, -amount):  # Attempts to update the balance for withdrawal.
                messagebox.showinfo("Success", "Withdrawal Successful!")  # Success message.
            else:
                messagebox.showerror("Error", "Insufficient Balance!")  # Error message for insufficient balance.
        elif transaction_type == "transfer":
            recipient_email = self.recipient_input.get()  # Retrieves the recipient email for transfer.
            if self.api.transfer_funds(email, recipient_email, amount):  # Performs the transfer.
                messagebox.showinfo("Success", "Transfer Successful!")  # Success message.
            else:
                messagebox.showerror("Error", "Transfer Failed!")  # Error message for failed transfer.
        self.dashboard_gui(email)  # Returns to the dashboard after the transaction.

# Instantiate the BankingApp class to start the application.
BankingApp()
