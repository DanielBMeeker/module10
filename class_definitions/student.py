class Student:
    """Student class"""
    def __init__(self, lname, fname, major, gpa=0.0):
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        majors = ('BIS-OOP', 'CIS', 'Web Development', 'Network Security')
        if not (name_characters.issuperset(lname) and name_characters.issuperset(fname)):
            raise ValueError
        if major not in majors:
            raise ValueError
        if not isinstance(gpa, float) or not 0.0 <= gpa <= 4.0:
            raise ValueError
        self.last_name = lname
        self.first_name = fname
        self.major = major
        self.gpa = gpa

    def __str__(self):
        return self.last_name + ", " + self.first_name + " has major " + self.major + " with gpa: " + str(self.gpa)
