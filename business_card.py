from faker import Faker

fake = Faker()

class BaseContact:
    def __init__(self, full_name, phone, email):
        self.full_name = full_name
        self.phone = phone
        self.email = email

    def display(self):
        return (
            f"Full Name: {self.full_name}\n"
            f"Phone: {self.phone}\n"
            f"Email: {self.email}\n"
        )
    
    def contact(self):
        return f"{self.full_name} can be reached at mobile phone {self.phone} ."
    
    @property
    def label_length(self):
        parts = self.full_name.split()
        if len(parts) >= 2:
            first_name = parts[0]
            surname = parts[-1]
            return len(first_name) + len(surname) + 1  
        else:
            return len(self.full_name)


class BusinessContact(BaseContact):
    def __init__(self, full_name, mobile_phone, business_phone, email, title, company):
        super().__init__(full_name, mobile_phone, email)
        self.business_phone = business_phone
        self.title = title
        self.company = company

    def display(self):
        base_info = super().display()
        return (
            f"{base_info}"
            f"Mobile Phone: {self.phone}\n"
            f"Business Phone: {self.business_phone}\n"
            f"Title: {self.title}\n"
            f"Company: {self.company}\n"
        )
    def contact1(self):
        return f"{self.full_name} can be reached at business phone {self.business_phone} ."

def create_random_contacts(n):
    contacts = []

    for i in range(n):
        full_name = fake.name()
        mobile_phone = fake.phone_number()
        business_phone = fake.phone_number()
        email = fake.email()
        title = fake.job()
        company = fake.company()
        contact = BusinessContact(full_name, mobile_phone, business_phone, email, title, company)
        contacts.append(contact)

    return contacts

random_contacts = create_random_contacts(5)
for contact in random_contacts:
    print(contact.display())
    print(contact.contact())
    print(contact.contact1())
    print(f"Full name length (including space): {contact.label_length}")
    print()