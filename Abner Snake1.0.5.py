class Point:
    row = 0
    col = 0
    def __init__(self,row,col):
        self.row=row
        self.col=col
    def copy(self):
        return Point(row=self.row,col=self.col)

import pygame
import random
import tkinter as tk
import random
from pygame import *
root = tk.Tk()

pygame.init()
#显示字体初始化
pygame.font.init()
#系统默认字体
myfont = pygame.font.SysFont('arial',30)


W = 800
H = 600
speed = 5

ROW=30
COL=40

size = (W,H)
window = pygame.display.set_mode(size)
pygame.display.set_caption('Abner Eat Snake')
head=Point(row = int(ROW/2),col = int(COL/2))
head_color=(62,120,168)
food = Point(row=random.randint(0,ROW-1),col=random.randint(0,COL-1))
food_color=(214,81,64)
snake_color =(128,128,128) 
snakes=[]
scoore = 0
direct = 'left'


def rect(point,color):
    cell_width=W/COL
    cell_height=H/ROW
    
    left=point.col*cell_width
    top=point.row*cell_height

    pygame.draw.rect(window,color,(left,top,cell_width,cell_height))
quit = True
clock = pygame.time.Clock()

while quit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit = False
        elif event.type==pygame.KEYDOWN:
            if event.key==273 or event.key==119:
                if direct=='left' or direct=='right':
                    direct='up'
            if event.key==274 or event.key==115:
                if direct=='left' or direct=='right':
                    direct='down'
            if event.key==276 or event.key==97:
                if direct=='up' or direct=='down':
                    direct='left'
            if event.key==275 or event.key==100:
                if direct=='up' or direct=='down':
                    direct='right'
    
    eat = head.row==food.row and head.col==food.col
    if eat:
        scoore += 1
        if scoore % 5 == 0:
            speed += 5
        food = Point(row=random.randint(0,ROW-1),col=random.randint(0,COL-1))
    snakes.insert(0,head.copy())

    
    if not eat:
        snakes.pop()
                
    if direct == 'left':
        head.col-=1
    elif direct == 'right':
        head.col+=1
    elif direct == 'up':
        head.row-=1
    elif direct == 'down':
        head.row+=1
    alive=False
    dead=False
    if head.col<0 or head.row<0 or head.col>=COL or head.row>=ROW:
        dead=True
    for snake in snakes:
        if head.col==snake.col and head.row==snake.row:
            dead = True
            break
    if dead:
        cad = tk.Label(root,text='you lose')
        cad.pack()
        
        quit=False
    if scoore == 100:
        alive=True
    if alive == 10000000000:
        cad = tk.Label(root,text='you win')
        cad.pack()
        
        quit=False
    pygame.draw.rect(window,(255,255,255),(0,0,W,H))
    for snake in snakes:
        rect(snake,snake_color)
    rect(head,head_color)
    rect(food,food_color)

    #显示文字
    textImage = myfont.render("score: " + str(scoore), True, (0, 0, 255))
    window.blit(textImage, (10, 10))
    textImage = myfont.render("speed: " + str(speed), True, (0, 0, 255))
    window.blit(textImage, (670, 10))

    pygame.display.flip()
    clock.tick(speed)
    
root.mainloop()
