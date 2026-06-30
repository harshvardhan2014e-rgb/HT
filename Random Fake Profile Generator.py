import random

first_names = [
    'John', 'Jane', 'Corey', 'Travis', 'Dave', 'Kurt', 'Neil', 'Sam',
    'Steve', 'Tom', 'James', 'Robert', 'Michael', 'Charles', 'Joe',
    'Mary', 'Maggie', 'Nicole', 'Patricia', 'Linda', 'Barbara',
    'Elizabeth', 'Laura', 'Jennifer', 'Maria', 'Adam', 'Sturt',
    'Nikolson', 'Tom', 'Harry', 'Ruskin', 'Thor', 'Rocky', 'Ravid',
    'David', 'Harris', 'Eion', 'Elon', 'Mark', 'Will', 'Chris'
]

last_names = [
    'Smith', 'Doe', 'Jenkins', 'Robinson', 'Davis', 'Stuart',
    'Jefferson', 'Jacobs', 'Wright', 'Patterson', 'Wilks',
    'Arnold', 'Johnson', 'Williams', 'Jones', 'Brown',
    'Davis', 'Miller', 'Wilson', 'Moore', 'Taylor',
    'Anderson', 'Thomas', 'Jackson', 'White', 'Harris',
    'Martin', 'Potter', 'Jukerberg', 'Smith', 'Nebula',
    'Downy', 'Downy Jr'
]

street_names = [
    'Main', 'High', 'Pearl', 'Maple', 'Park', 'Oak',
    'Pine', 'Cedar', 'Elm', 'Washington', 'Lake', 'Hill'
]

fake_cities = [
    'Metropolis', 'Eerie', "King's Landing", 'Sunnydale',
    'Bedrock', 'South Park', 'Atlantis', 'Mordor',
    'Olympus', 'Dawnstar', 'Balmora', 'Gotham',
    'Springfield', 'Quahog', 'Smalltown', 'Epicburg',
    'Pythonville', 'Faketown', 'Westworld', 'Thundera',
    'Vice City', 'Blackwater', 'Oldtown', 'Valyria',
    'Winterfell', 'Braavos', 'Lakeview'
]

states = [
    'AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DC', 'DE',
    'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY',
    'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT',
    'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH',
    'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT',
    'VT', 'VA', 'WA', 'WV', 'WI', 'WY'
]


class Name:

    def __init__(self, num=1):
        self.num = num

    def fname(self):
        for _ in range(self.num):
            print(random.choice(first_names))

    def lname(self):
        for _ in range(self.num):
            print(random.choice(last_names))

    def full_name(self):
        for _ in range(self.num):
            first = random.choice(first_names)
            last = random.choice(last_names)
            print(first + " " + last)

    def full_profile(self):
        for _ in range(self.num):
            first = random.choice(first_names)
            last = random.choice(last_names)

            phone = random.randint(1000000000, 9999999999)

            street_number = random.randint(1, 9999)
            street_name = random.choice(street_names)
            city = random.choice(fake_cities)
            state = random.choice(states)
            zip_code = random.randint(10000, 99999)

            address = f"{street_number} {street_name} St, {city}, {state} {zip_code}"
            email = f"{first.lower()}.{last.lower().replace(' ', '')}@example.com"

            print(f"Name    : {first} {last}")
            print(f"Phone   : {phone}")
            print(f"Address : {address}")
            print(f"Email   : {email}")
            print("-" * 40)


num = int(input("Enter the number of profiles you want to generate: "))

obj = Name(num)

print("\nGenerating First Names")
obj.fname()

print("\nGenerating Last Names")
obj.lname()

print("\nGenerating Full Names")
obj.full_name()

print("\nGenerating Full Profiles")
obj.full_profile()