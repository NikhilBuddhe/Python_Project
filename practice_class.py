class new_class(object):
    "doing arithmatic operations"
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2
        
    def addition(self, send):
        print("addition of two numbers", self.var1+ self.var2)
        print("message is", send)
        
output = new_class(2, 3)
print(output.addition("hello"))
print(getattr(output, "var1"))
