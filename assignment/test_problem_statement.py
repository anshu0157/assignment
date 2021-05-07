import unittest
from problem_statement import *

class Testcode(unittest.TestCase):
    def test_greater(self):
        l=[34,31,53,76,-21,21j,'anshu']
        l1=[]
        for i in range(len(l)):
            object=problem_statement(l[i])
            greater=object.getStudentsWithMarksMoreThan()
            self.assertAlmostEqual(greater,'need to provide json data' )

