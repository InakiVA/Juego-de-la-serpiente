"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?-Edrick
2. How can you make the snake go around the edges?-Iñaki
3. How would you move the food?-Iñaki
4. Change the snake to respond to mouse clicks.
"""
import random
from random import randrange
from turtle import *

from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
colors=['black','green','blue','yellow','pink']#colores aleatorios
rSnake=random.randint(0,len(colors)-1)
cSnake=colors[rSnake]
del colors[rSnake]#para que sean colores diferentes
rFood=random.randint(0,len(colors)-1)
cFood=colors[rFood]

def change(x, y):
    """Change snake direction."""
    aim.x = x
    aim.y = y

def move():
    """Move snake forward one segment."""    
    head = snake[-1].copy()
    head.move(aim)
    if head in snake:            
        square(head.x, head.y, 9, 'red')
        update()
        return
    #puede ir en el contorno, y se traspasa al otro lado del mapa
    if head.x<-200:
        head.x=190
    elif head.x>190:
        head.x=-200
    if head.y<-200:
        head.y=190
    elif head.y>190:
        head.y=-200

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, cSnake)

    square(food.x, food.y, 9, cFood)
    pFood=[10,-10]#mover comida-------
    r1F=random.randint(0,1)#eje x y
    r2F=random.randint(0,1)#arriba/abajo, derecha/izquierda
    if r1F==0 and food.x>=-190 and food.x<=180:
        food.x+=pFood[r2F]
    elif r1F==0 and food.x<-190:
        food.x=-190
    elif r1F==0 and food.x>180:
        food.x=180
    if r1F==1 and food.y>=-190 and food.y<=180:
        food.y+=pFood[r2F]
    elif r1F==1 and food.y<-190:
        food.y=-190
    elif r1F==1 and food.y>180:
        food.y=180   
    #-------mover comida
    update()
    ontimer(move, 100)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
