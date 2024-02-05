# for n in [1,2,3,4,5]:
#     print(n)

# for c in "Hello World":
#     print(c)

class MyCollection:
    def __init__(self):
        self.size = 10
        self.data = list(range(self.size))
        
    def __iter__(self):
        self.index = 0
        return self
    
    def __next__(self):
        if self.index >= self.size:
            raise StopIteration
        
        n = self.data[self.index]
        self.index += 1
        return n
    
coll = MyCollection()

for x in coll:
    print(x)