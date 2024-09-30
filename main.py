from members import MembershipFee
from store import StoreItem, Purchase
from facilitation import FacilitationFee
from equipment import Equipment
from reports import Report

# Initialize the system components
club_report = Report()

# Add membership income
membership_fee = MembershipFee.calculate_total_fee(individuals=10, groups=3)
club_report.add_income(membership_fee)

# Add store sales income
football = StoreItem(name="Football", price=1000, stock=50, max_stock=100)
discounted_purchase = Purchase(total_amount=12000)
discounted_amount, discount = discounted_purchase.apply_discount()
club_report.add_income(discounted_amount)

# Add facilitation fees income
facilitation = FacilitationFee()
facilitation_fee = facilitation.collect_facilitation_fee(15)  # 15 members
club_report.add_income(facilitation_fee)

# Add surcharges for lost/damaged equipment
football_eq = Equipment(name="Football", market_value=1000)
surcharge = football_eq.calculate_surcharge()
club_report.add_income(surcharge)

# Generate and print the report
print(club_report.generate_report())
