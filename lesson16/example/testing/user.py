class User:
    def __init__(self, fname, lname, age):
        self.fname = fname
        self.lname = lname
        self.age = age

    def full_name(self):
        return f"{self.fname} {self.lname}"

    def is_adult(self):
        return self.age >= 18
