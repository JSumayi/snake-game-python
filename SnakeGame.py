"""Snake, classic arcade game."""

from turtle import *
from random import randrange
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
score = 0
delay = 200    # Initial delay between snake movements
levels = [{'speed' : 200}, {'speed' : 150}, {'speed' : 100}] # Different levels with increasing speed
current_level = 0


# Obstacles (randomly generated)
obstacles = []


def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

# Place a new obstacle
def place_obstacle():
    global obstacles
    obstacle = vector(randrange(-15, 15) * 10, randrange(-15, 15) * 10)
    if obstacle not in obstacles and obstacle not in snake and obstacle != food:
        obstacles.append(obstacle)
        square(obstacle.x, obstacle.y, 9, 'red')

#Move the snake forward
def move():
    global score, delay, current_level

    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)       

    if head == food:
        score += 1
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'black')

    for obstacle in obstacles:
        square(obstacle.x, obstacle.y, 9, 'red')

    square(food.x, food.y, 9, 'green')
    update()

    # Check for level up
    if score >= 3 and current_level == 0:
        current_level = 1
        delay = levels[current_level]['speed']
        print("Level Up! Speed increased.")
    elif score >= 6 and current_level == 1:
        current_level = 2
        delay = levels[current_level]['speed']
        print("Level Up! Speed increased again.")

    ontimer(move, delay)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')

# Initialize obstacles
for _ in range(5):
    place_obstacle()

    
move()
done()
