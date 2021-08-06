class Category:

    def __init__(self, category):
        self.category = category
        self.ledger = list()
        self.spent = 0

    def deposit(self, amount, description=""):
        d = {}
        d["amount"] = amount
        d["description"] = description
        self.ledger.append(d)

    def withdraw(self, amount, description=""):

        if self.check_funds(amount) is False:
            return False

        d = {}
        d["amount"] = float(-abs(amount))
        d["description"] = description
        self.ledger.append(d)
        ## collects values for the spend chart
        self.spent += round(amount, 1)

        return True

    def get_balance(self):
        return sum([self.ledger[k]["amount"] for k in range(len(self.ledger))])

    def transfer(self, amount, name):
        if self.check_funds(amount) is False:
            return False

        self.withdraw(amount, f"Transfer to {name.category}")
        name.deposit(amount, f"Transfer from {self.category}")

        return True

    def check_funds(self, amount):
        if self.get_balance() < amount:
            return False
        return True

    def __str__(self):
        t = []
        for i in (self.ledger):
            t.append(f'{i["description"][0:23]}'.ljust(23))
            t.append(f'{i["amount"]:.2f}\n'.rjust(8))
        return f'{self.category.center(30, "*")}\n' + "".join(t) + f'Total: {self.get_balance()}'


def create_spend_chart(list):

    values = []
    names = []
    chart = []

    for i in list:
        values.append(i.spent)
        names.append(i.category.title())

    chart.append("Percentage spent by category\n")

    # prints the % and markers
    for percent in range(100, -10, -10):

        chart.append(f"{str(percent).rjust(3)}|")
        for value in values:

            if round((value / sum(values)) * 100) >= percent:
                chart.append(" o ")
            else:
                chart.append("   ")
        chart.append(" \n")

    # prints the dashes
    chart.append("    ")
    for _ in range(len(names)):
        chart.append("---")
    chart.append("-\n")

    # prints the names
    for index in range(len(max(names, key=len))):
        chart.append("     ")
        for name in range(len(names)):
            if index + 1 <= len(names[name]):
                chart.append(f"{names[name][index]}  ")
            else:
                chart.append("   ")
        chart.append("\n")
    chart.pop(-1)

    return "".join(chart)
