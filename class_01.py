class Rectangle:
    count = 0 #클래스 변수
    
    def __init__(self, width, height):
        # self.* = 인스턴스 변수 
        self.width=width
        self.height=height
        
        self.__area = width * height # private
        Rectangle.count += 1
    
    # 인스턴스 메서드(self를 포함하고 있다)
    def calcArea(self):
        area = self.width * self.height
        return area
    
    # private 인스턴스 메서드 
    def __internalRun(self):
        pass
    
    # 정적 메서드: 
    # 인스턴스 생성 여부와 상관없이 독립적으로 사용되며 인스턴스 변수, 클래스 변수에 접근할 수 없다. 
    @staticmethod
    def isSquare(rectWidth, rectHeight):
        return rectWidth == rectHeight
    
    # 클래스 메서드: 
    # 인스턴스 생성 후 클래스 변수에만 접근할 수 있다. 인스턴스 변수에는 접근할 수 있다.
    @classmethod
    def printCount(cls):
        print(cls.count) 
        
    # 매직 메서드:
    # __del__(소멸자), __add__, __del__, __cmp__, __str__
    def __add__(self, other):
        obj = Rectangle(self.width + other.width, self.height + other.height)
        return obj 
        
        
square = Rectangle.isSquare(5,5)
print(square)

rect1 = Rectangle(5,5)
rect2 = Rectangle(2,5)
rect1.printCount()

rect3 = rect1 + rect2 #__add__가 호출됨. rect3이라는 새로운 인스턴스가 생성된다.
rect3.printCount()

# 인스턴스 생성
r = Rectangle(2,3)

# 메서드 호출
area = r.calcArea()
print("area = ", area)

# 인스턴스 변수 엑세스
r.width = 10 # 인스턴스 변수에 접근하여 값을 변경한다.
print("width = ", r.width)

# 클래스 변수 엑세스
print(Rectangle.count)
print(r.count) #인스턴스에서도 클래스 변수에 접근할 수 있다.

r1 = Rectangle(2,3)

Rectangle.count = 50 #클래스 변수의 값을 변경
r1.count = 10  # 클래스 변수 count와 이름이 같지만 값이 할당 되면서 새로운 count 인스턴스 변수가 새로 생김
