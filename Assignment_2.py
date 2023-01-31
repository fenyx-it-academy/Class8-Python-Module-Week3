## Assignment 2

counter1 = 0
counter2 = 0
counter3 = 0
list1 = []
list2 = []

while True :
    
    str_input = str(input("please write the words "))
    list1.append(str_input) 
    counter1 += 1
    continue_enter = input("do you want to enter another word ? (yes/no)")
  
    if continue_enter != "yes" :
        break 

length_of_list1 = len(list1) 


print("the word that you chose it ", list1)
while counter3 < length_of_list1:
    list2.append(min(list1))
    counter2 = list1.index(min(list1))
    del list1[counter2]

    counter3 += 1 
    
print("the result " , list2)
     
  
  

  
