import numpy as np

# ---------------------------------------
# CSCI 127, Joy and Beauty of Data
# Program 5: Eight Puzzle
# Justin Guerrero
# DUE DECEMBER 4TH.....
# ---------------------------------------
# A brief overview of the program.
# ---------------------------------------

class EightPuzzle:          ## Defining our puzzle class

    def __init__(self):
        self.solution = np.array([1,2,3,4,5,6,7,8," "])
        self.solution = self.solution.reshape(3,3)
        print(self.solution)

    def __str__(self):
        separator = "+-+-+-+\n"
        answer = separator
        for row in range(3):
            for col in range(3):
                answer += "|" + str(self.puzzle[row][col])
            answer += "|\n"
            answer += separator
        return answer

    def puzzle_1(self):
        self.puzzle = np.array([1,2,3,4,5,6,7,8," "])
        self.puzzle = self.puzzle.reshape(3,3)
        self.blank_x = 2
        self.blank_y = 2
        

    def puzzle_2(self):
        self.puzzle = np.array([4,1,3,7,2,5,8," ", 6])
        self.puzzle = self.puzzle.reshape(3,3)
        self.blank_x = 2
        self.blank_y = 1

    def puzzle_3(self):
        self.puzzle = np.array([5,4," ",7,1,8,3,6,2])
        self.puzzle = self.puzzle.reshape(3,3)
        self.blank_x = 0
        self.blank_y = 2

        
    def swap(self, x1, y1, x2, y2):
        self.puzzle[x1][y1], self.puzzle[x2][y2] = \
                             self.puzzle[x2][y2], self.puzzle[x1][y1]

# ---------------------------------------
# Do not change anything above this line
# ---------------------------------------

    def is_puzzle_solved(self):
        return np.array_equal(self.puzzle, self.solution)
       
##        

    def move_blank(self):
        repuesta = input("Where would you like to move? Left / Right / Up / Down: ") #--Create a question for location--#
        if repuesta.lower() == "quit" or repuesta.lower() == "Q":
            quit()
        if repuesta.lower() == "left" or repuesta.lower() == "l":
            if self.blank_y != 0:
                self.swap(self.blank_x, self.blank_y, self.blank_x, self.blank_y - 1) ##-- the (x1, y1) are the entries that will be swapped with (x2,y2)
                self.blank_y = self.blank_y - 1
            else:
                print("That move isn't cool, try again")
            
        if repuesta.lower() == "right" or repuesta.lower() == "r":
            if self.blank_y != 2:
                self.swap(self.blank_x, self.blank_y, self.blank_x, self.blank_y + 1)
                self.blank_y = self.blank_y +1
            else:
                print("That move isn't cool, try again")
            
        if repuesta.lower() == "up" or repuesta.lower() == "u":
            if self.blank_x != 0:
                self.swap(self.blank_x, self.blank_y, self.blank_x - 1, self.blank_y)
                self.blank_x = self.blank_x - 1
            else:
                print("That move isn't cool, try again")

        if repuesta.lower() == "down" or repuesta.lower() == "d":
            if self.blank_x  != 2:
                self.swap(self.blank_x, self.blank_y, self.blank_x + 1, self.blank_y)
                self.blank_x = self.blank_x +1
            else:
                print("What you thinking!? You can't do that!")
       

            
        
# ---------------------------------------
# Do not change anything below this line
# ---------------------------------------

def solve(puzzle):
    steps = 0
    print("Puzzle:\n")
    print(puzzle)
    while not puzzle.is_puzzle_solved():
        puzzle.move_blank()
        print(puzzle)
        steps += 1
    print("Congratulations - you solved the puzzle in", steps, "steps!\n")
        

def main():
    puzzle = EightPuzzle()
    puzzle.puzzle_1()
    solve(puzzle)
    puzzle.puzzle_2()
    solve(puzzle)
    puzzle.puzzle_3()
    solve(puzzle)
    
# ---------------------------------------

main()
