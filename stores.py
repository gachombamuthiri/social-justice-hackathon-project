class StoreItem:
    def __init__(self, name, price, stock, max_stock):
        self.name = name
        self.price = price
        self.stock = stock
        self.max_stock = max_stock

    def purchase(self, quantity):
        if self.stock >= quantity:
            self.stock -= quantity
            return self.price * quantity
        else:
            raise ValueError(f"Not enough stock for {self.name}")

    def check_stock(self):
        if self.stock <= 0.2 * self.max_stock:
            return f"Low stock alert for {self.name}. Please reorder!"
        return f"{self.name} stock level is sufficient."

class Purchase:
    DISCOUNT_THRESHOLD = 10000
    DISCOUNT_RATE = 0.05

    def __init__(self, total_amount):
        self.total_amount = total_amount

    def apply_discount(self):
        if self.total_amount > Purchase.DISCOUNT_THRESHOLD:
            discount = self.total_amount * Purchase.DISCOUNT_RATE
            discounted_amount = self.total_amount - discount
            return discounted_amount, discount
        return self.total_amount, 0
