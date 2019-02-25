class Address:
    def __init__(self,street,city,state):
        self.steet = street
        self.city = city
        self.state = state

class User:
    def __init__(self,first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        # list of addresses
        self.addresses = []

user = User('John','Doe')

address1 = Address('Richmond Ave','Houston','TX')
address2 = Address('Holman St','Houston','TX')

user.addresses.append(address1)
user.addresses.append(address2)

print(user.addresses)