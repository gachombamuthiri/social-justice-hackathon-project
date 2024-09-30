class FacilitationFee:
    FEE_PER_MEMBER = 500

    def __init__(self):
        self.total_facilitation_fees = 0

    def collect_facilitation_fee(self, num_members):
        total_fee = num_members * FacilitationFee.FEE_PER_MEMBER
        self.total_facilitation_fees += total_fee
        return total_fee

    def calculate_patron_commission(self, total_fee):
        commission = total_fee * 0.20
        return commission
