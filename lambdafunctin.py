# lambda functon
#lambda arguments:expression


x = lambda a : a + 10
print(x(5))

# lambda fuction in string 
#slicing

slicing= (lambda a:a[2:5])("hello world")
print(slicing)

#zfill

zfill=(lambda a:a.zfill(10))("hello")
print(zfill)

#swapcase

swapcase=(lambda a:a.swapcase())("Hello My Name Is PETER")
print(swapcase)


#returen 

rjust = (lambda a: a.rjust(80,'*'))("python is a programming language")
print(rjust)

#partition

partition=(lambda a:a.partition("python"))("python is a programming language")
print(partition)

#startwith

startwith=(lambda a:a.startswith("programmig"))("python is a programming language")
print(startwith)

#endwith

endtwith=(lambda a:a.endswith("programmig"))("python is a programming language")
print(endtwith)

#find

find=(lambda a:a.find("p"))("python is a programming language")
print(find)

# center

center= (lambda a: a.center(80,'*'))("python is a programming language")
print(center)

#ljust

ljust= (lambda a: a.ljust(80,'*'))("python is a programming language")
print(ljust)

#rjust

rjust= (lambda a: a.rjust(80,'*'))("python is a programming language")
print(rjust)

#rfind

rfind= (lambda a: a.rfind('o'))("python is a programming language")
print(rfind)

#count

count= (lambda a: a.count('o'))("python is a programming language")
print(count)

#lower

lower= (lambda a: a.lower())("python is a programming language")
print(lower)

#islower

islower= (lambda a: a.islower())("python is a programming language")
print(islower)

#upper

upper= (lambda a: a.upper())("python is a programming language")
print(upper)

#isupper

isupper= (lambda a: a.isupper())("python is a programming language")
print(isupper)

#capitalize

capitalize= (lambda a: a.capitalize())("python is a programming language")
print(capitalize)

#join

join= (lambda list:" ".join(list))(["string","method","in","tuple"])
print(join)

#re.sub

import re
resub=(lambda a:re.sub("","-","a"))("my names is twinkle")
print(resub)

