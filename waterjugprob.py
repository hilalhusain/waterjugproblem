jug1 = int(input("Small Jug Capacity: "))
jug2 = int(input("Large Jug Capacity: "))

amt1 = int(input("water present in small jug, J1: "))
amt2 = int(input("water present in large jug, J2: "))

t = int(input("Final in Large Jug: " ))

#jug1 = 3
#jug2 = 5
#t = 1

def jugSolver(amt1, amt2):

    print(amt1, amt2)

    if (amt2 == t and amt1 == 0):
        return

    elif amt2 == jug2:
        jugSolver(amt1, 0)

    elif amt1 != 0:
        if amt1 <= jug2-amt2:
            jugSolver(0, amt1+amt2)
        elif amt1 > jug2-amt2:
            jugSolver(amt1-(jug2-amt2),amt2+(jug2-amt2))

    else:
        jugSolver(jug1, amt2)

print("\nJ1 J2")
#jugSolver(2,4)
jugSolver(amt1,amt2)