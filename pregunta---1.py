import random

Lista = []

for i in range(10):
   Lista.append(random.randrange(1, 20))

resultaList = []

for num in Lista:
   if num not in resultaList:
       resultaList.append(num)

print("item 2 sin duplicados es:", resultaList)

"""lista ordenada de mayor a menor"""

resultaList.sort()

for numero in resultaList:
   print(numero, " ", end="")


