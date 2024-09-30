class Report:
    def __init__(self):
        self.total_income = 0

    def add_income(self, amount):
        self.total_income += amount

    def generate_report(self):
        return f"Total income for the club is Kshs. {self.total_income}"
