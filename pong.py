import turtle

wn = turtle.Screen()
wn.title("Pong by Devesh")
wn.bgcolor("black")
wn.setup(width = 800 , height=600)
wn.tracer(0)

# Score Tacker

score_a = 0
score_b = 0
# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

# Paddle B

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

# Ball 
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.25
ball.dy = -0.25

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0 Player B: 0", align="center", font=("Courier",24,"normal"))


# Function

def paddle_a_up():
    y = paddle_a.ycor() #ycor return the y corrdinate
    y += 20             #moving 20 pixil up in y
    paddle_a.sety(y)    #setting updated value in y

def paddle_a_down():
    y = paddle_a.ycor() #ycor return the y corrdinate
    y -= 20             #moving 20 pixil down in y
    paddle_a.sety(y)    #setting updated value in y

def paddle_b_up():
    y = paddle_b.ycor() #ycor return the y corrdinate
    y += 20             #moving 20 pixil up in y
    paddle_b.sety(y)    #setting updated value in y

def paddle_b_down():
    y = paddle_b.ycor() #ycor return the y corrdinate
    y -= 20             #moving 20 pixil down in y
    paddle_b.sety(y)    #setting updated value in y
# Keyboard Binding
wn.listen()
# For padel 1
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
# For padel 2
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

# Main Game Loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    # Border Checking for top and bottom
    # Total Height is 600, -300 to 300 
    # Ball size is 20 pixel, deducting 10 each from 300 i.e 290
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    # Checking Border for left and right border
    # Logic - Total width is 800, 400 each side
    # checking for 390 because it crosses the paddel
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        ## Score update
        score_a +=1
        pen.clear()
        pen.write(f"Player A: {score_a} Player B: {score_b}", align="center", font=("Courier",24,"normal"))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
         ## Score update
        score_b +=1
        pen.clear()
        pen.write(f"Player A: {score_a} Player B: {score_b}", align="center", font=("Courier",24,"normal"))
        
        
    
    # Bounce logic
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() < -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1