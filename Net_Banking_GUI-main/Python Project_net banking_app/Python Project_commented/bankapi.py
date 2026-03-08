from bankdb import Database

class BankAPI:
    def __init__(self):
        self.dbo = Database()

    def transfer_funds(self, sender_email, recipient_email, amount):
        if recipient_email not in self.dbo.data or sender_email == recipient_email:
            return False
        if self.dbo.update_balance(sender_email, -amount):
            self.dbo.update_balance(recipient_email, amount)
            return True
        return False
