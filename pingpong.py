import pgzrun
import random




HEIGHT = 300
WIDTH = 300
TITLE = "Ping Pong 2 player 0-0"
left_y = 0
right_y = 0

score1 = 0
score2 = 0
cheat1 = False
cheat2 = False




l_go = 0
r_go = 0

xv = random.uniform(0.5,1) * random.choice([-1,1])
yv = random.uniform(0.5,1) * random.choice([-1,1])
ballx = 150
bally = 150


def moveorbounce():
    global bally, ballx, xv, yv, right_y, left_y
    if bally+yv < 10 or bally+yv > screen.height-10:
        yv *= -1
    # if ballx+xv < 0 or ballx+xv > screen.width:
    #     xv *= -1
    if left_y+45 > bally+yv > left_y-45 and ballx > 42.5 and ballx+xv < 42.5:
        xv *= -1
    if right_y+45 > bally+yv > right_y-45 and ballx < 257.5 and ballx+xv > 257.5:
        xv *= -1
    
    bally += yv
    ballx += xv

def draw_circle(x,y):
    screen.draw.filled_circle((x,y), 10, (0,0,255))
    
    


def draw_rectangle(x,y):
        rectangle = Rect((x,y), (5, 70))
        rectangle.center = x,y
        screen.draw.filled_rect(rectangle, (255,255,255))

# line1 = Actor("line")
# line2 = Actor("line")




def on_key_down(key):
    global left_y, right_y, r_go, l_go, cheat1, cheat2
    # print(key)
    if key == ord("s"):
        # print("up")
        # left_y += 10
        l_go = 1
    elif key == ord("w"):
        # print("down")
        # right_y -= 10
        l_go = -1
    elif key == ord("l"):
        r_go = 1
    
    elif key == ord("o"):
        r_go = -1
        
    elif key == ord("0"):
        if cheat2:
            cheat2 = False
        else:
            cheat2 = True
            
    elif key == ord("1"):
        if cheat1:
            cheat1 = False
        else:
            cheat1 = True
        
def on_key_up(key):
    global left_y, right_y, r_go, l_go
    # print(key)
    if key == ord("s"):
        # print("up")
        # left_y += 10
        if l_go == 1:
            l_go = 0
    elif key == ord("w"):
        # print("down")
        # right_y -= 10
        if l_go == -1:
            l_go = 0
    elif key == ord("l"):
        if r_go == 1:
            r_go = 0
    
    elif key == ord("o"):
        if r_go == -1:
            r_go = 0    

def update():
    global left_y, right_y, r_go, l_go, xv, yv, score1, score2, TITLE
    right_y += r_go*7
    left_y += l_go*7
    
    if left_y > 300:
        left_y = 300
    elif left_y < 0:
        left_y = 0
        
    if right_y > 300:
        right_y = 300
    elif right_y < 0:
        right_y = 0
        
        
    if xv > 0:   
        xv += 0.0015
    else:
        xv -= 0.0015
    
    if yv > 0:
        yv += 0.0015
    else:
        yv -= 0.0015
    if TITLE != f"{round(xv, 3)}     {round(yv, 3)}":
        TITLE = f"{round(xv, 3)}     {round(yv, 3)}" 

def draw():
    global left_y, right_y, ballx, bally, xv, yv, score1, score2, TITLE, cheat1, cheat2
    screen.clear()
    
    if cheat1:
        left_y = bally
    
    if cheat2:
        right_y = bally
    
    draw_rectangle(30,left_y)
    draw_rectangle(270,right_y)
    draw_circle(ballx,bally)
    moveorbounce()
    

    
    if ballx > 300:
        print(f"{xv}   {yv}")
        xv = 0
        yv = 0
        print("left player gains one point!")
        score1 += 1
        print(f"the current score is {score1} - {score2}")
        TITLE = f"Ping Pong 2 player {score1} - {score2}"
        ballx = 150
        bally = 150
        xv = random.uniform(0.5,1) * random.choice([-1,1])
        yv = random.uniform(0.5,1) * random.choice([-1,1])
        
    elif ballx < 0:
        print(f"{xv}   {yv}")
        xv = 0
        yv = 0
        print("right player gains one point!")
        score2 += 1
        print(f"the current score is {score1} - {score2}")
        TITLE = f"Ping Pong 2 player {score1} - {score2}"

        ballx = 150
        bally = 150
        xv = random.uniform(0.5,1) * random.choice([-1,1])
        yv = random.uniform(0.5,1) * random.choice([-1,1])
    
    # line1._surf = pygame.transform.scale(line1._surf, (5, 10))
    # line1._update_pos()

    # line1.x = 30
    # line1.y = left_y
    # line1.angle = 90
    # line1.draw()
    
    # line2.scale = 0.1
    # line2.x = 270
    # line2.y = right_y
    # line2.angle = 90
    # line2.draw()


pgzrun.go()