class MyShape:
 def __init__(self,color,is_filled):
        self.color = color
        self.is_filled = is_filled

 def __str__(self,color,is_filled):
    print(f"{self.color}({self.is_filled})")
myshape = MyShape("red",False)
area=0
print(myshape.color)
print(myshape.is_filled)
print(area)
 
