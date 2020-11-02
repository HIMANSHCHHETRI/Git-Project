import random
def game():
    randno=random.randint(1,3)
    return randno

def result(p,c):
    if p == c:
        return "none"
    elif p == 1 and c == 2:
        return "true"
    elif p == 2 and c == 1:
        return "false"
    elif c == 2 and p == 3:
        return "true"
    elif c == 3 and p == 2:
        return "false"
    elif p == 3 and c == 1:
        return "true"
    elif p == 1 and c == 3:
        return "false"

snake = {"s":1, "w":2, "g":3 }
print("Snake(s) , Water(w) , Gun(G) :-")
p=input("Your turn:-")
c=game()

keys = list(snake.keys())
vals = list(snake.values())
a=snake[p]
print("Computer Turn:-" + keys[vals.index(c)])
r=result(a,c)

if r=="none":
    print("Tie!")
elif r=="true":
    print("You Win:")
elif r=="false":
    print("Comp Win:")
else:
    print("Wrong input")