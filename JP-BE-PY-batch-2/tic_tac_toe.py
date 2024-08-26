import os

board = {
    "0": {},
    "1": {},
    "2": {}
}

def display_tic(x, y):
    x = str(x)
    y = str(y)

    if board.get(x) is None:
        return " "
    
    if board.get(x).get(y) is None:
        return " "
    
    return board[x][y]

def print_tic_tac_toe():
    # os.system('cls||clear')
    
    board_str = f"""
    {display_tic(0, 0)} | {display_tic(0, 1)} | {display_tic(0, 2)} 
    ---------
    {display_tic(1, 0)} | {display_tic(1, 1)} | {display_tic(1, 2)} 
    ---------
    {display_tic(2, 0)} | {display_tic(2, 1)} | {display_tic(2, 2)} 
    """
    
    print(board_str)

def is_win():
  if board["0"].get("0") == board["0"].get("1") == board["0"].get("2") != None:
    print(board["0"]["0"], "won")
    os.abort()
  
  elif board["1"].get("0") == board["1"].get("1") == board["1"].get("2") != None:
    print(board["1"]["0"], "won")
    os.abort()
    
  elif board["2"].get("0") == board["2"].get("1") == board["2"].get("2") != None:
    print(board["2"]["0"], "won")
    os.abort()
    
  elif board["0"].get("0") == board["1"].get("0") == board["2"].get("0") != None:
    print(board["0"]["0"], "won")  
    os.abort()
    
  elif board["0"].get("1") == board["1"].get("1") == board["2"].get("1") != None:
    print(board["0"]["1"], "won")  
    os.abort()
    
  elif board["0"].get("2") == board["1"].get("2") == board["2"].get("2") != None:
    print(board["0"]["2"], "won")
    os.abort()
    
  elif board["0"].get("0") == board["1"].get("1") == board["2"].get("2") != None:
    print(board["0"]["0"], "won")  
    os.abort()
    
  elif board["0"].get("2") == board["1"].get("1") == board["2"].get("0") != None:
    print(board["0"]["2"], "won")  
    os.abort()
    
    
def is_valid_choice(choice):
  if choice in available_choices:
    return True
  
  return False

def remove_choice(choice):
  available_choices.remove(choice)
    
print_tic_tac_toe()

available_choices = [1, 2, 3, 4, 5, 6, 7, 8, 9]


turn = ""
while True:
    if turn == "":
        turn = "x"
    choice = int(input(f"make your choice: {available_choices}:\n"))

    if not is_valid_choice(choice):
      print("please make a valid choice")
      continue
    
    remove_choice(choice)

    if choice == 1:
        board["0"]["0"] = turn
    elif choice == 2:
        board["0"]["1"] = turn
    elif choice == 3:
        board["0"]["2"] = turn
    elif choice == 4:
        board["1"]["0"] = turn
    elif choice == 5:
        board["1"]["1"] = turn
    elif choice == 6:
        board["1"]["2"] = turn
    elif choice == 7:
        board["2"]["0"] = turn
    elif choice == 8:
        board["2"]["1"] = turn
    elif choice == 9:
        board["2"]["2"] = turn
    else:
        print("please make proper choice")
        break

    print_tic_tac_toe()
    is_win()

    if turn == "x":
        turn = "o"
    else:
        turn = "x"