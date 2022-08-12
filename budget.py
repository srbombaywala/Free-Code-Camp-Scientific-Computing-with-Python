class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
    
    def deposit(self, amount, description = ''):
        self.ledger.append({"amount":amount, "description":description})

    def withdraw(self, amount, description = ''):
        if self.check_funds(amount):
            self.ledger.append({"amount":-amount, "description":description})
            return True
        else:
            return False
    
    def get_balance(self):
        bal = 0
        for i in range(len(self.ledger)):
            bal = bal + self.ledger[i]['amount']
        return bal
    
    def transfer(self, amount, transfer_to):
        if self.check_funds(amount):
            self.ledger.append({"amount":-amount, "description":'Transfer to ' + transfer_to.name})
            transfer_to.ledger.append({"amount":amount, "description":'Transfer from ' + self.name})
            return True
        else:
            return False

    def check_funds(self,amount):
        if amount > self.get_balance():
            return False
        else:
            return True

    
    def __str__(self):
        larray = []
        for i in range(len(self.ledger)):
            first = self.ledger[i]["description"][:23] # first 23 letters of description
            second = str("{0:.2f}".format(self.ledger[i]["amount"])).rjust(30-len(first)) # amount to two decimal points and right justified
            larray.append(first + second+"\n")
        total = 0
        for i in range(len(self.ledger)):
            total = total + self.ledger[i]['amount']
        # return((''.join(larray)))
        return "*"*int((30-len(self.name))/2) + self.name + '*'*int((30-len(self.name))/2) + "\n" + ((''.join(larray))) + "Total: " + str(total)

def create_spend_chart(categories):
    names_of_categories = []
    spent_by_catogories = []
    total_spent = 0
    for cat in categories:
        total_spent = total_spent + cat.ledger[1]['amount']
        spent_by_catogories.append(cat.ledger[1]['amount'])
        names_of_categories.append(cat.name)
    spent_in_percent = [int((((i/total_spent)*10)//1)*10) for i in spent_by_catogories]

    # CHART
    title = "Percentage spent by category"+"\n"
    graph = ''
    for i in reversed(range (0,101,10)):
        graph += str(i).rjust(3) + "| "
        for value in spent_in_percent:
            if value <i :
                graph += "   "
            else:
                graph += "o  "
        graph += '\n'

    separator_line = "    -" + "---"*len(spent_by_catogories)+'\n'
    label = ''
    for i in range (len(max(names_of_categories,key=len))):
        label += "     "
        for lab in names_of_categories:
            lab += ' '* (len(max(names_of_categories,key=len))-len(lab))
            label += lab[i]+'  '
        if i < len(max(names_of_categories,key=len))-1:
            label += '\n'
    # print(len(max(names_of_categories,key=len))) # length of maximum length string in a list
    return ((title+graph+separator_line+label).rstrip('\n'))