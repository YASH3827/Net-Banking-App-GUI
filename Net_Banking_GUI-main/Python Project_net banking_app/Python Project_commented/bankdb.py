import json  # Importing the json module to handle reading and writing of JSON files.

class Database:  # Define the Database class to manage user data and transactions.
    
    def __init__(self):  # Constructor method for initializing the Database object.
        """Initializes the database by setting the file name and loading data."""
        self.file = "bankdb.json"  # Specifies the filename for the JSON database.
        self.load_data()  # Loads the existing data from the file.

    def load_data(self):  # Method to load data from the JSON file.
        """Attempts to load the data from the file. Creates a new file if not found."""
        try:
            # Tries to open the file in read mode and load the JSON data.
            with open(self.file, "r") as f:
                self.data = json.load(f)  # Reads and parses the JSON content into a Python dictionary.
        except FileNotFoundError:
            # If the file doesn't exist, it creates an empty dictionary.
            self.data = {}  # Initializes an empty dictionary if the file is not found.
            with open(self.file, "w") as f:
                json.dump(self.data, f)  # Writes the empty dictionary to the file.

    def save_data(self):  # Method to save the data to the JSON file.
        """Saves the current data dictionary to the JSON file."""
        with open(self.file, "w") as f:
            json.dump(self.data, f)  # Dumps the current data as JSON to the file.

    def add_user(self, name, email, password):  # Method to add a new user to the database.
        """Adds a new user to the database with a name, email, and password."""
        if email in self.data:  # Checks if the email already exists in the database.
            return False  # Returns False if the email is already registered.
        # Adds the new user with initial balance of 0.
        self.data[email] = {"name": name, "password": password, "balance": 0}
        self.save_data()  # Saves the updated data to the file.
        return True  # Returns True if the user was successfully added.

    def authenticate_user(self, email, password):  # Method to authenticate a user.
        """Validates if the email and password match any user in the database."""
        # Checks if the email exists and if the password matches the stored password.
        return email in self.data and self.data[email]["password"] == password

    def get_balance(self, email):  # Method to get the balance of a specific user.
        """Returns the balance of the user associated with the provided email."""
        return self.data[email]["balance"]  # Returns the balance from the user's data.

    def update_balance(self, email, amount):  # Method to update the balance of a user.
        """Updates the user's balance, ensuring it does not go negative."""
        # Checks if the updated balance would be negative.
        if self.data[email]["balance"] + amount < 0:
            return False  # Returns False if the balance would go negative.
        # Updates the balance by adding the specified amount.
        self.data[email]["balance"] += amount
        self.save_data()  # Saves the updated data to the file.
        return True  # Returns True if the balance was successfully updated.
