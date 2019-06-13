class Generic_Major:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        self.major = "Generic Major"
        self.major_troubles = False
        self.math_troubles = False
        self.major_advising = "If you are having trouble with your major please seek advisor"
        self.math_advising = ["If you are having trouble with math please seek the help in wilson 1-112", "also"]

    def set_major_troubles(self, mtroub):
        self.major_troubles = mtroub

    def set_math_troubles(self, mtroub):
        self.math_troubles = mtroub

    def get_first_name(self):
        return self.first

    def get_last_name(self):
        return self.last

    def get_major(self):
        return self.major

    def get_major_advising(self):
        return self.major_advising
    
    def get_math_advising(self):
        return self.math_advising

    def get_math_troubles(self):
        if self.math_troubles:
            print(self.math_advising)

    def get_major_troubles(self):
        if self.major_troubles:
            print(self.major_advising)

class CLS_Major(Generic_Major):
    def __init__(self, first, last):
        Generic_Major.__init__(self, first, last)
        self.major = "College of Lit Studies"

class COE_Major(Generic_Major):
    def __init(self, first, last):
        Generic_Major.__init__(self, first, last)
        self.major = "College of Engineering"
        self.major_advising.insert(0, "Please visit the engineering success center for your troubles")

class Computer_Engineering_Major(COE_Major):
    def __init__(self, first, last):
        COE_Major.__init__(self,first,last)
        self.major = "Computer Engineering"
        self.major_troubles.insert(0, "Please visit the student success center in B259")

class Computer_Science_Major(COE_Major):
    def __init__(self, first, last):
        COE_Major.__init__(self, first, last)
        self.major = "Computer Science"
        
        
    
    






# -------------------------------------------------
# Do not change anything below this line
# -------------------------------------------------


def advise(student):
    print("Student:", student.get_first_name(), student.get_last_name())
    print("Major: " + student.get_major() + ", Major Troubles: " +
          str(student.get_major_troubles()) + ", Math Troubles: " +
          str(student.get_major_troubles()))
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
