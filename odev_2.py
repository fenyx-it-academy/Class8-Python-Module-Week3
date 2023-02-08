def hyphen_to_sorted():
    items=[]
    items=[n for n in input('enter an string : ').split('-')]
    items.sort()
    print('-'.join(items))
    

hyphen_to_sorted()

