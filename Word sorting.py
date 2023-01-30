# program to sort hyphen-separated text in words alphabetically.
txt = input('Hyphen delimited text: ')
delimiter = '-'

def sortspecial(txt, sep):
    return sep.join(sorted(list(txt.split(sep))))

print(sortspecial(txt, delimiter))  #print sorted hyphen delimited txt 