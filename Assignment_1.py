from pascal_function import pascal_triangle as pas_tri
while True:
  number = (input('enter the number:\n'))
  try:
    number = int(number)
  except:
    print("Invalid input, please enter an integer")
    quit()
  pas_tri(number)
  continues= input("if you want to continue write yes, if not any key \n")
  if continues != 'yes':
    break