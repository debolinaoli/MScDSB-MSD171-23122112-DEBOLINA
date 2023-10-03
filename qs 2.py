# define a class expense tracker that stores the expenses and income in a dictionary implement the method to store the transaction ,view transaction, calculate the  total expense/income............
class expenseTracker:
    def _init_(self):
        self.expenseDict = {
              "income" : [],
              "expense" : []
        }
    def store_transactions(self, type,amt,category,date,details):
        trans = {
            "amount": amt,
            "category": category,
            "date": date,
            "details": details,
        }
        if type == "income":
            self.expenseDict['income'].append(trans)
        else:
            self.expenseDict['expense'].append(trans)
    def view_transactions(self):
        print("your income : ")
        for item in self.expenseDict["income"]:
            print(item)
        print("your expenses: ")
        for item in self.expenseDict["expense"]:
            print(item)
    def calculate_transactions(self):
        total_income = 0
        for item in self.expenseDict['income']:
            total_income += item["amount"]
        print("total income \t:\t", total_income)
        total_expense = 0
        for item in self.expenseDict["INCOME"]:
            total_expense += item["AMOUNT"]
        print("TOTAL EXPENSE\t:\t", total_expense)