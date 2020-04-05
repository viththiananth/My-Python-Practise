#Time for some fake graphics! Let’s say we want to draw game boards that look like this:
board_size=int(input("What is the size game board?"))

def horiz_line():
    print(" --- "*int(board_size))
def vert_line():
    print("|   "*(int(board_size)+1))

for i in range(board_size):
    horiz_line()
    vert_line()