# Import csv
import csv

# Set the file name to a variable
FILENAME = "students.csv"

class Student:
    def __init__(self, id, firstName, lastName, gradYear, city):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.gradYear = gradYear
        self.city = city

    def getFullName(self):
        formString = self.firstName, self.lastName
        return(formString)

    def __str__(self):
        x = ""
        x += "ID: {}\n".format(self.id)
        x += "YOG: {}\n".format(self.gradYear)
        x += "City: {}".format(self.city)
        return(x)

    def getStudents():
        students = []
        with open(FILENAME, "r", newline="") as student_file:
            z = csv.reader(student_file)
            for a, b, c, d, e in z:
                y = Student.__init__(a, b, c ,d, e)
                y.strip()
                students.append(y)
        return students

    def findStudentById(students, student_id):
        for i in students:
            if i == student_id:
                return i
            else:
                return "None"

    def main():
        print()