import turtle 

#wn
wn = turtle.Screen()
wn.title("Pong by Betsy Avila")
#background color
wn.bgcolor("black")
#pixels that is takes up
wn.setup(width = 800, height = 600) 
 #stops the window from refreshing
wn.tracer(0)

#paddle A

#paddle B
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white") 
paddle_a.penup()
paddle_a.goto(-350,0) 
 

#ball
paddle_b = turtle.Turtle()

#Main Game Loop 
while True: 
    wn.update() 

    