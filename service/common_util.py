def check_int(input_item):
    try:
        int(input_item)
    except:
        print("It's not a number!")
        return False
    else:
        return True
