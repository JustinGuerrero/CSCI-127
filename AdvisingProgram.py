# -------------------------------------------------
# CSCI 127, Joy and Beauty of Data
# Program 4: Advising System
# Justin Guerrero
# Last Modified: 11/1/2018
# -------------------------------------------------
# A brief overview of the program.
# -------------------------------------------------

    

class Generic_Major:   #This is the Superclass that all the subclasses draw from
    
    def __init__(self, first, last):
        self.first = first.capitalize()  ## Don't forget to capitalize the first and last names
        self.last = last.capitalize()
        self.MathTroubles = False
        self.MajorTroubles = False  ## We want to set the majors = to false as a parameter for the major troubles
        self.major = "Generic Major"
        self.math_troubles = "--->Please visit the math learning center in Wilson 1-112 if you are having troubles with math"
        
        self.major_resources = ["Visit your professor during office hours", "Visit your advisor"]

    def set_math_troubles(self, values):
        self.MathTroubles = values #values are what are returned and grabbed by the boolean function

    def set_major_troubles(self, values):
        self.MajorTroubles = values
        
    def get_first_name(self):
        return self.first

    def get_last_name(self):
        return self.last

    def major(self, major):
        self.major = major

    def get_major(self):
        return self.major

    def get_math_troubles(self):
        if self.MathTroubles: ## Here this says if math troubles = not false
            print("--->Because you are having troubles with math, ")
            print(self.math_troubles)

    def get_major_troubles(self):
        if self.MajorTroubles:
            print("--->Because you are having troubles with your major: ")
            for i in self.major_resources:
                print("--->", i)
        
    def getMathBool(self):
        return self.MathTroubles #This is where the boolean is returned false or true 

    def getMajBool(self):
        return self.MajorTroubles

class CLS_Major(Generic_Major):
    
    def __init__(self, first, last):
        Generic_Major.__init__(self, first, last)
        self.major = "College of Letters and Sciences"
        
        

class COE_Major(Generic_Major):

    def __init__(self, first, last):
        Generic_Major.__init__(self, first, last)
        self.major = "College of Engineering"
        self.major_resources.insert(0, "Visit the EMPower Student Center in Roberts 313")
        
        

class Computer_Engineering_Major(COE_Major):

    def __init__(self, first, last):
        COE_Major.__init__(self, first, last)
        self.major = "Computer Engineering"
        self.major_resources.insert(0, "---> Visit the CS Student Success Center in Barnard Hall 259")
        self.major_resources.insert(1, "--->Visit a CS professional advisor in Barnard 357")
        

class Physics_Major(CLS_Major):

    def __init__(self, first, last):
        CLS_Major.__init__(self, first, last)
        self.major = "Physics"
        self.major_resources.insert(0, "--->Visit the Physics learning center in barnard 230")


class Computer_Science_Major(COE_Major):

    def __init__(self, first, last):
        COE_Major.__init__(self, first, last)



# -------------------------------------------------
# Do not change anything below this line
# -------------------------------------------------


def advise(student):
    print("Student:", student.get_first_name(), student.get_last_name())
    print("Major: " + student.get_major() + ", Major Troubles: " +
          str(student.getMajBool()) + ", Math Troubles: " +
          str(student.getMathBool()))
    print()
    if not student.get_math_troubles() and not student.get_major_troubles():
        print("No advising is necessary.  Keep up the good work!")
    else:
        student.major_advising()
        student.math_advising()
    print("------------------------------")

# -------------------------------------------------

def process(student):
    advise(student)
    student.set_major_troubles(True)
    student.set_math_troubles(True)
    advise(student)

# -------------------------------------------------

def main():

    # Every student has a major, even if it is "undeclared"
    msu_student = Generic_Major("jalen", "nelson")
    process(msu_student)

    msu_student.set_math_troubles(False)
    advise(msu_student)

    msu_student.set_math_troubles(True)
    msu_student.set_major_troubles(False)
    advise(msu_student)

    # A CLS (College of Letters and Science) major is a subclass of a Generic major
    msu_student = CLS_Major("emma", "phillips")
    process(msu_student)

    # A COE (College of Engineering) major is a subclass of a Generic major
    msu_student = COE_Major("camden", "miller")
    process(msu_student)

    # A Computer Engineering major is a subclass of a COE major
    msu_student = Computer_Engineering_Major("gabriel", "smith")
    process(msu_student)

    # A Physics major is a subclass of a CLS major
    msu_student = Physics_Major("lena", "hamilton")
    process(msu_student)

    # A Computer Science major is a subclass of a COE major
    msu_student = Computer_Science_Major("halley", "jones")
    process(msu_student)

    msu_student.set_math_troubles(False)
    advise(msu_student)

    msu_student.set_math_troubles(True)
    msu_student.set_major_troubles(False)
    advise(msu_student)

# -------------------------------------------------

main()
