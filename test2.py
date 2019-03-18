'''

import unittest

class simpleTest2(unittest.TestCase):
   def setUp(self):
      self.a = 10
      self.b = 20
      name = self.shortDescription()
      if name == "Add":
         self.a = 10
         self.b = 20
         print name, self.a, self.b
      if name == "sub":
         self.a = 50
         self.b = 60
         print name, self.a, self.b
   def tearDown(self):
      print '\nend of test',self.shortDescription()

   def testadd(self):
      """Add"""
      result = self.a+self.b
      self.assertTrue(result == 100)
   def testsub(self):
      """sub"""
      result = self.a-self.b
      self.assertTrue(result == -10)
      
if __name__ == '__main__':
   unittest.main()
   
'''

import unittest
class simpleTest3(unittest.TestCase):
   def setUp(self):
      self.a = 10
      self.b = 20
      
   def testadd(self):
      """Add"""
      result = self.a+self.b
      self.assertTrue(result == 100)
   def testsub(self):
      """sub"""
      result = self.a-self.b
      self.assertTrue(result == -10)
      
def suite():
   suite = unittest.TestSuite()
   #suite.addTest (simpleTest3("testadd"))
   suite.addTest (simpleTest3("testsub"))
   #suite.addTest(unittest.makeSuite(simpleTest3))
   return suite
   
if __name__ == '__main__':
   runner = unittest.TextTestRunner()
   test_suite = suite()
   runner.run (test_suite)


