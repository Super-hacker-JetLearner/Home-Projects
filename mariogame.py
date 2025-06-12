import pgzrun


WIDTH = 900
HEIGHT = 500

mario = Actor("better mario")


yv = 0
xp = 150
yp = 0
go_x = 0
jump_height = 5
ground_jump = 7
side_speed = 6




walls = []
for i in range (5):
    
    wall = Actor("mario wall")
    wall.midbottom = 25 + i*130, 400
    walls.append(wall)


def gravity():
    global yv
    yv += 0.07

def on_key_down(key):
    global go_x, yv, yp, jump_height, ground_jump
    if key == 1073741906:
        if yp+ground_jump > HEIGHT:
            yv = -jump_height
        else:
            for i in walls:
                mario.y += ground_jump
                if mario.colliderect(i):
                    yv =- jump_height
                    break
                else:
                    mario.y -= ground_jump
        



    elif key == 1073741904:
        go_x = -1

    elif key == 1073741903:
        go_x = 1



def on_key_up(key):
    global go_x
    if key == 1073741904 and go_x == -1:
        go_x = 0
    elif key == 1073741903 and go_x == 1:
        go_x = 0

def check_walls():
    global yv,yp, go_x, side_speed
    if yp < HEIGHT and yp+yv > HEIGHT:
        yv = 0
        yp = HEIGHT-1
    
    for i in walls:
        
        
        
        if not mario.colliderect(i):
            mario.y += yv

            if mario.colliderect(i):
                print("collision")
                yv = 0
                mario.y -= yv
            else:
                mario.y -= yv
                
        if not mario.colliderect(i):
            mario.x += go_x*side_speed
            
            if mario.colliderect(i):
                go_x = 0
                mario.x -= go_x*side_speed
            else:
                mario.x -= go_x*side_speed


def update():
    global yv,yp, xp, go_x
    gravity()
    check_walls()

    yp += yv

    xp += go_x*6

def draw():
    global xp,yp, walls
    screen.fill("dark green")
    mario.midbottom = xp,yp
    mario.draw()
    # for i in walls:
    #     i.midbottom = 150,150
    #     i.draw()
    for i in walls:
        i.draw()
        

    
pgzrun.go()