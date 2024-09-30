class Equipment:
    def __init__(self, name, market_value):
        self.name = name
        self.market_value = market_value

    def calculate_surcharge(self):
        surcharge = self.market_value * 1.10  # 10% surcharge
        return surcharge
