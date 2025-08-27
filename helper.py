from faker import Faker

faker = Faker()

def generate_valid_registration_data():
    name = faker.first_name()
    email = faker.email()
    password = faker.password(length=6)
    return name, email, password

def generate_invalid_registration_data():
    name = faker.first_name()
    email = faker.email()
    bad_password = faker.password(length=5)
    return name, email, bad_password  
