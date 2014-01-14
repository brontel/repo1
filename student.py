"""
Design and implement a class named "Student" with three methods

__init__(self, courseName)

addCourseMark(self, course, mark)

average(self)

"""

class Student:
    studentName = ""
    courseMarks = {}

    def __init__(self, name):
        """
        Creates a new student with a name

        >>> myStudent = Student("bob")
        >>> myStudent.studentName == "bob"
        True

        """

        self.studentName = name

    def addCourseMark(self, course, mark):
        """
        Adds a course mark given a course and mark

        >>> myStudent = Student("bob")
        >>> myStudent.addCourseMark("c410", 75)
        >>> myStudent.courseMarks["c410"] == 75
        True

        """
        self.courseMarks[course] = mark

    def average(self):
        """
        Calculates the average of all the marks of all the courses

        >>> myStudent = Student("bob")
        >>> myStudent.addCourseMark("c410", 75)
        >>> myStudent.addCourseMark("c411", 70)
        >>> myStudent.addCourseMark("c414", 100)
        
        >>> myStudent.average() == (75 + 70 + 100) / 3
        True

        """
        sums = 0
        count = 0
        for mark in self.courseMarks.values():
            sums += mark
            count += 1
        return sums / count

if __name__ == "__main__":
    import doctest
    doctest.testmod()
