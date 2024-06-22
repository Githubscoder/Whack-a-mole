
import turtle
import random
import time

# Initialize the screen
world = turtle.Screen()
world.title("Whack-a-Mole Game")
world.register_shape('pixilart-drawing.gif')
world.register_shape('Hammer.gif')
# Define positions for the mole to appear
positions = [(50, 50), (150, 50), (250, 50),
             (50, 150), (150, 150), (250, 150),
             (50, 250), (150, 250), (250, 250)]

# Initialize score
score = 0

# Create the scorekeeper turtle
keeper = turtle.Turtle()
keeper.hideturtle()
keeper.penup()
keeper.goto(400, 0)
keeper.write(f"Score: {score}", font=("Arial", 16, "normal"))

# Create the mole turtle
mole = turtle.Turtle()
mole.color('red')
mole.shape('pixilart-drawing.gif')
mole.penup()
mole.hideturtle()

# Function to move the mole to a random position
def mole_move():
    mole.hideturtle()
    new_position = random.choice(positions)
    mole.goto(new_position)
    mole.showturtle()
    # Schedule the next move
    world.ontimer(mole_move, 1000)  # Move the mole every 1 second

# Function to track the score
def score_track(x, y):
    global score
    score += 1
    keeper.clear()
    keeper.write(f"Score: {score}", font=("Arial", 16, "normal"))

# Bind the score_track function to mouse clicks on the mole
mole.onclick(score_track)

# Draw the board
board = turtle.Turtle()
board.hideturtle()
board.speed(0)
board.width(2)
board.color("Black")

def draw_board():
    # Draw outer lines
    for _ in range(4):
        board.forward(300)
        board.left(90)
 
        
    # Draw inner lines
    for position in [100, 200]:
        board.penup()
        board.goto(position, 0)
        board.pendown()
        board.left(90)
        board.forward(300)
        board.right(90)
    for position in [100, 200]:
        board.penup()
        board.goto(0, position)
        board.pendown()
        board.forward(300)
def hammerit(x,y):
    hammer.goto(x,y)
    hammer.showturtle()
    time.sleep(0.5)
    hammer.hideturtle()
    
    

    
draw_board()

hammer=turtle.Turtle()
hammer.hideturtle()
hammer.penup()
hammer.shape('Hammer.gif')

# Start the mole movement and the game loop
mole_move()
world.onclick(hammerit)

world.mainloop()







