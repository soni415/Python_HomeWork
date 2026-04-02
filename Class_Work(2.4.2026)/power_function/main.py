
def power_function(a,b):
 if b==0:
     return 1
 else:
     result=a*power_function(a,b-1)
 return result


result=power_function(2,3)
print(result)