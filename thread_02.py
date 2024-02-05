# 예제(A)
import threading, requests, time
 
def getHtml(url):
    resp = requests.get(url)
    time.sleep(1)
    print(url, len(resp.text), ' chars')
 
t1 = threading.Thread(target=getHtml, args=('http://google.com',)) # args는 튜플로 전달되어야 한다. 따라서 ','를 붙여줬다. 그렇지 않으면 string 타입이 된다.
t1.start()
 
print("### End ###")