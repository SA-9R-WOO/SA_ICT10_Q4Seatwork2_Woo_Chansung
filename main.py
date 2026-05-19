from pyscript import display, document


# Class definition
class Classmate:
    def __init__(self, name, section, favorite_subject):
        self.name = name
        self.section = section
        self.favorite_subject = favorite_subject

    def introduce(self):
        return f"Hello, my name is {self.name} and my section is from {self.section}. The subject I like the most is {self.favorite_subject}."


# Store classmates
classmates = [
    Classmate("Eaden", "Ruby", "Math"),
    Classmate("Arianne", "Ruby", "Science"),
    Classmate("Tristan", "Ruby", "PE"),
    Classmate("Dylan", "Ruby", "PE"),
    Classmate("Reever", "Ruby", "Social Studies")
]

# Function to add classmate
def add_classmate(e):
    name = document.getElementById("classmate1").value
    section = document.getElementById("section").value
    subject = document.getElementById("subject").value

    new_student = Classmate(name, section, subject)
    classmates.append(new_student)

    display(f"{name} added successfully!\n", append=True, target='output')


# Function to display classmates
def show_classmates(e):
    document.getElementById('output').innerHTML = " "

    for student in classmates:
        intro = student.introduce()
        display(intro + "\n", target='output')