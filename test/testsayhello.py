import inspect
import os
import sys
import unittest

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
sys.path.insert(0,currentdir) # this instruction is necessary for successful importation of utilityfortest module when
                              # the test is executed standalone
from sayhello import SayHello

class TestSayHello(unittest.TestCase):

    def testGreet(self):
        name = 'Philippe Brolly'
        s = SayHello(name)

        self.assertEqual('Hello ' + name + ' !', s.greet())
