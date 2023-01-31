import random
import string

print('Password generator')  #name of programm
len = int(input('Insert password length')) #input length
u_case=string.ascii_uppercase #upper case letter
l_case=string.ascii_lowercase #lower case letter
char=string.punctuation # character
numb=string.digits #numbers 0-9
rand_list=l_case+u_case+char+numb #all together
password=''.join(random.sample(rand_list,len))# generate the random password
print('Password -',password)


       