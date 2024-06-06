import turtle
import random

mbappe = turtle.Turtle()
mbappe.shape("turtle")
mbappe.color("red")
mbappe_jr = turtle.Turtle()
mbappe_jr.color("green")
mbappe_jr.shape("turtle")

mbappe.penup()
mbappe.goto(-300, 100)
mbappe_jr.penup()
mbappe_jr.goto(-300, -100)
mbappe.goto(250, 100)
mbappe.pendown()
mbappe.pencolor("red")
mbappe.circle(60)
mbappe.penup()
mbappe.goto(-300, 100)



mbappe_jr.goto (250, -100)
mbappe_jr.pendown()
mbappe_jr.pencolor("green")
mbappe_jr.circle(60)
mbappe_jr.penup()
mbappe_jr.goto(-300, -100)



dice = [1, 2, 3, 4, 5, 6]

while mbappe.pos() < (300,100) and mbappe_jr.pos() < (300,-100):
    diceOutcome1 = random.choice(dice)
    print("result of dice role: ", diceOutcome1)
    print("Numbers of steps")
    print(10*diceOutcome1)
    mbappe.fd(10*diceOutcome1)
    diceOutcome2 = random.choice(dice)
    print("result of dice role: ", diceOutcome2)
    print("Numbers of steps")
    print(10 * diceOutcome2)
    mbappe_jr.fd(10 * diceOutcome2)

    if mbappe.pos() >= (250,100):
        print("MBAPEEEE WINS")
        break


    elif mbappe_jr.pos() >= (250, -100):
        print("MBAPEEEE(JR) WINS")
        break





turtle.exitonclick()
