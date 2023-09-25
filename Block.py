import hashlib
import datetime

class Block:
    
    def __init__(self, numero, previous_hash, operation, amount, account, comment):
        self.numero = numero
        self.previous_hash = previous_hash
        self.operation = operation
        self.amount = int(amount)
        self.account = account
        self.date = datetime.datetime.now()
        self.comment = comment
        self.hashe = self.get_hash()
        
    @staticmethod
    def genesis():
        return block(0,"0","Genesis","0","#TCHEETOS","Genesis block")
    
    def __str__(self):
        print ("Previous_hash: " + self.previous_hash +"\n" + "Amount: " + self.amount + "\n" + "Date" + str(self.date) +"\n" + self.comment)
        
    def to_json(self):
        return {
            "numero": self.numero,
            "previous_hash": self.previous_hash,
            "operation": self.operation,
            "amount": self.amount,
            "account": self.account,
            "date": self.date.strftime("%Y-%m-%d %H:%M:%S"),
            "comment": self.comment,
            "hash": self.hash
        }