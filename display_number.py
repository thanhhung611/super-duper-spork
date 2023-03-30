#this function to display number that is modulo to 5, if number is greater than 500 stop
def display_numbers():
  numbers = [12, 75, 150, 180, 145, 525, 50]
  for item in numbers:
    if item > 500:
      print('Debug2')
      break
    elif item > 150:
      print('Debug1')
      continue
    elif item%5 == 0:
      print(item)
