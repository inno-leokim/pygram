# Test Fixture
# setUp() : 테스트 사전 준비 작업
# tearDown() : 테스트 사후 작업(clean up 처리)

import unittest
import os
import myUtil

class MyUtilTest (unittest.TestCase):
    testfile = 'text.txt'
    
    # Fixture : 사전작업. 자동으로 실행됨
    def setUp(self):
        f = open(MyUtilTest.testfile, 'w')
        f.write('1234567890')
        f.close()
    
    # Fixture : 사후작업
    def tearDown(self):
        try:
            os.remove(MyUtilTest.testfile)
        except:
            pass
    
    def test_filelen(self):
        leng = myUtil.filelen(MyUtilTest.testfile)
        self.assertEqual(leng, 10)
    
    def test_count_in_file(self):
        cnt = myUtil.count_in_file(MyUtilTest.testfile, '0')
        self.assertEqual(cnt, 1)
        
if __name__ == '__main__':
    unittest.main()
    
        