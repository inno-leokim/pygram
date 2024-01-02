import sys

def openurl(url):
    print(url)
    
## 이 파일이 module로써 다른 파일에서 import된다면 __name__은 모듈 이름이된다.
## 이 파일이 스크립트로써 실행된다면 __name__은 __main__이된다.
## python module_03.py naver.com을 실행한다면 naver.com이 출력된다. 
if __name__ == '__main__':
    openurl(sys.argv[1])