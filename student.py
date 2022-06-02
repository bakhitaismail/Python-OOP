class Student:
    school = "AkiraChix"
    def __init__(self,names,year_of_birth):
        self.names = names
        self.year_of_birth = year_of_birth
    def full_name(self):
        return f"Hello {self.names}, your welcome to {self.school}"
    def message(self):
        age = 2022 - self.year_of_birth
        return f"Hello {self.names} your were born in {self.year_of_birth} and your age is {age}"
    def get_initials(self):
        initials = "BI"
        full_name = self.names.split()
        for names in full_name:
         return initials