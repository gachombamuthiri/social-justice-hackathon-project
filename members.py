import datetime

class Member:
    def __init__(self, full_name, gender, next_of_kin, dob, contact_details, sub_county, school, games_of_interest, weight, height, special_needs, group=False):
        self.full_name = full_name
        self.gender = gender
        self.next_of_kin = next_of_kin
        self.dob = dob
        self.contact_details = contact_details
        self.sub_county = sub_county
        self.school = school
        self.games_of_interest = games_of_interest
        self.weight = weight
        self.height = height
        self.special_needs = special_needs
        self.group = group
        self.age_group = self.get_age_group()

    def get_age(self):
        today = datetime.date.today()
        age = today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))
        return age
    
    def get_age_group(self):
        age = self.get_age()
        if 12 <= age <= 17:
            return 'Minor'
        elif 18 <= age <= 25:
            return 'Middle'
        elif 26 <= age <= 35:
            return 'Senior'
        else:
            return 'Out of Range'

class MembershipFee:
    INDIVIDUAL_FEE = 1000
    GROUP_FEE = 500

    @staticmethod
    def calculate_total_fee(individuals, groups):
        total = (individuals * MembershipFee.INDIVIDUAL_FEE) + (groups * MembershipFee.GROUP_FEE)
        return total
