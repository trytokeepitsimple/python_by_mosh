command = ""

while command != 'quit':
  command = input(" > ")
  if(command == 'start'):
        print("Car Started")
  elif(command=='stop'):
        print("car stopped")
  elif(command=='help'):
      print('''
       start - to start the car
       stop - to stop the car
       quit - tp exit
       ''')
  elif(command=='quit'):
      print("Exit")
  else:
    print("I don't understand given command")