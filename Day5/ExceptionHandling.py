'''
try - test the block of code with errors/may contains error
except - handle errors
finally - irrespective of results, finally will b e executed. cleanup codes
else - no errors in try


'''
import traceback
try:
    print(10%0)
except NameError:
    print("variable is not defined")
except:
    print("Other Exception occured")
    traceback.print_exc()
finally:
    print("Finally Block")

print("Hello Team")



try:
    print("hello")
except NameError:
    print("variable is not defined")
except:
    print("Other Exception occured")
    traceback.print_exc()
else:
    print("Else Block")

age = 10
if age < 18:
    raise Exception("Sorry, Not eligible")

print("Hello")