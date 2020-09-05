"""Quick lines of code to solve the hanoi tower problem."""

n = int(input("How big do you want the tower to be?"))
moves = 0


def move(source, destination, auxiliary, n):
    """ Recursive Python function to solve the tower of hanoi.
            Args_1:
                source (string): the pole of the tower at the beginning.
            Args_2:
                destination (string): where one wants to move the tower.
            Args_3:
                auxiliary (string): the other pole, used as an aid to accomplish the task.
            Args_4:
                n (int): height of the tower
    """
    global moves
    if n == 1:
        moves += 1
        print("Move number", moves, ": move disk 1 from", source, "to", destination)
        return

    move(source, auxiliary, destination, n - 1)
    moves += 1
    print("Move number", moves, ": move disk", n, "from", source, "to", destination)

    move(auxiliary, destination, source, n - 1)


move("A", "C", "B", n)
