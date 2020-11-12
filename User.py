class User:
    username = ""
    phone = ""
    password = ""
    city = ""
    birth_date = ""
    email = ""

    def is_not_fake(self):
        return len(self.username) > 0

    def to_dict(self):
        return {"username": self.username, "phone": self.phone, "password": self.password,
                "city": self.city, "birthDate": self.birth_date, "email": self.email}
