#1913949
#Nguyễn Thái Linh

import unittest
from TestUtils import TestParser


class ParserSuite(unittest.TestCase):
   def test1(self):
        input = """
                Class Shape {
                    Val $numOfShape: Int = 0;
    
                }
                """
        expect = "successful"
        self.assertTrue(TestParser.test(input,expect,1))