import greedy_approach
my_var = 10
def func():
    global my_var
    print(my_var)

func() 
def ne_func():
    var1 = 10
    var2 = 20
    return var1, var2

result = ne_func()
for os in result: 
    print(os)
print(type(result))