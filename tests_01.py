import unittest
import myCalc


class MyCalcTest(unittest.TestCase):
    
    def test_add(self):
        c = myCalc.add(20, 10)
        self.assertEqual(c, 30)
        
    def test_substract(self):
        c = myCalc.substract(20, 10)
        self.assertEqual(c, 10)
        
if __name__ == '__main__':
    unittest.main() # MyClacTest가 unittest를 상속받았고 main()가 실행되면 MyCalcTest 안에 메서드들이 실행된다.
    