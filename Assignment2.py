string=input("plese enter string: ")   
# string="green-red-yellow-black-white"

listStr=string.split(sep="-")

listStr=sorted(listStr)

for item in listStr:
    if item==listStr[len(listStr)-1]:
        print(item, end=(""))
    else:
        print(item, end=("-"))