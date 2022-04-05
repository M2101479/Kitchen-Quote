def items(x):
  global price
  Base_cupboard=200
  Wall_cupboard=350
  Oven=450
  Microwave=250
  Metal_Sink= 200
  Pot_sink = 500
  Hob=600
  Tap=200
  Dishwasher=500
  Fitting=1200
  if x.upper() == 'BASE CUPBOARD':
    price=price+Base_cupboard
  elif x.upper() == 'WALL CUPBOARD':
    price=price+Wall_cupboard
  elif x.upper() == 'OVEN':
    price=price+Oven
  elif x.upper() == 'MICROWAVE':
    price=price+Microwave
  elif x.upper() == 'METAL SINK':
    price=price+Metal_Sink
  elif x.upper() == 'POT SINK':
    price=price+Pot_sink
  elif x.upper() == 'HOB':
    price=price+Hob
  elif x.upper() == 'HOT WATER TAP':
    price=price+Tap
  elif x.upper() == 'DISHWASHER':
    price=price+Dishwasher
  elif x.upper() == 'FITTING':
    price=price+Fitting
  else:
    print('Not a valid item ')

  if x.upper() == 'OVEN' or x.upper() == 'MICROWAVE' or x.upper() == 'METAL SINK' or x.upper() == 'POT SINK' or x.upper() == 'HOB' or x.upper() == 'HOT WATER TAP' or x.upper() == 'DISHWASHER':
    price=price+100
  elif x.upper()== 'BASE CUPBOARD' or x.upper() == 'WALL CUPBOARD':
    price=price+50
  return('')
    




  
def login(x,y):
  for z in range(0,4):
    User=input('Enter your username ')
    Code=input('Enter your password ')
    if x != User and y != Code:
      if z == 0:
        print('Incorrect login. 3 attempts left ')
      elif z == 1:
        print('Incorrect login. 2 attempts left ')
      elif z == 2:
        print('Incorrect login. 1 attempts left ')
      else:
        continue
        return('')
    else:
      return('')


  
    
    






price=0
Username='KitchenStaff'
Password='kitquote'
print(login(Username,Password))
loop=True
while loop == True:
  loop2=True
  loop3=True
  while loop2 == True:
    print('Price List')
    print('Base cupboard per unit: £200')
    print('Wall cupboard per unit: £350')
    print('Oven: £450')
    print('Microwave: £250')
    print('Metal sink: £200')
    print('Pot sink: £500')
    print('Hob: £600')
    print('Hot water tap: £200')
    print('Dishwasher: £500')
    print('Fitting: £1,200 and £50 extra per unit and £100 extra per appliance.')
    item=input('Select your item ')
    print(items(item))
    exit=input('Do you wish to add more items ')
    if exit.upper() == 'NO':
      loop2=False
      print('')
  while loop3 == True:
    print('£',price)
    accept=input('Do  you wish to accept your quote? ')
    if accept.upper() == 'YES' :
      print('Quote has been booked')
      loop3=False
      loop=False
      continue
      print('')
    confirm=input('Quote will be lost. Do you still wish to reject the quote ')
    if confirm.upper() == 'YES':
      loop3=False

