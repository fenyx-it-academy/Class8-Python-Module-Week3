str=input("Enter Words with hyphen-separated:")
str=str.split('-')
str.sort()
print('-'.join(str))