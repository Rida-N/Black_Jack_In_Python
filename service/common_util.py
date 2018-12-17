def check_int(input_item):
  try:
    int(input_item)
  except:
    print('Oops, it seems not a number, please try again!')
    return False
  else:
    return True
