import pgzrun
import time


WIDTH = 1000
HEIGHT = 800

tag_pos = [950, 500]
run_pos = [50, 500]


tagged = False
the_time = time.time()
length = 0
def update():
    global tag_pos, run_pos, tagged, length, the_time
    if tagged:
        return
    length = time.time() - the_time
    if keyboard.j:
        tag_pos = [tag_pos[0] - 5, tag_pos[1]]
    if keyboard.l:
        tag_pos = [tag_pos[0] + 5, tag_pos[1]]
    if keyboard.i:
        tag_pos = [tag_pos[0], tag_pos[1] - 5]
    if keyboard.k:
        tag_pos = [tag_pos[0], tag_pos[1] + 5]

    if keyboard.a:
        run_pos = [run_pos[0] - 5, run_pos[1]]
    if keyboard.d:
        run_pos = [run_pos[0] + 5, run_pos[1]]
    if keyboard.w:
        run_pos = [run_pos[0], run_pos[1] - 5]
    if keyboard.s:
        run_pos = [run_pos[0], run_pos[1] + 5]

    # make sure the positions are within the screen bounds
    if run_pos[0] < 0:
        run_pos[0] = 0
    if run_pos[0] > WIDTH:
        run_pos[0] = WIDTH
    if run_pos[1] < 0:
        run_pos[1] = 0
    if run_pos[1] > HEIGHT:
        run_pos[1] = HEIGHT
    if tag_pos[0] < 0:
        tag_pos[0] = 0
    if tag_pos[0] > WIDTH:
        tag_pos[0] = WIDTH
    if tag_pos[1] < 0:
        tag_pos[1] = 0
    if tag_pos[1] > HEIGHT:
        tag_pos[1] = HEIGHT

    if abs(run_pos[0] - tag_pos[0]) < 30 and abs(run_pos[1] - tag_pos[1]) < 30:
        print("You got tagged!")
        tagged = True
        
    

def draw():
    global tagged, length
    screen.fill("white")
    screen.draw.filled_circle(run_pos, 20, "blue")
    screen.draw.filled_circle(tag_pos, 20, "red")
    screen.draw.text(f"Time: {round(length, 2)} seconds", topleft=(10, 10), fontsize=30, color="black")
    if tagged:
        screen.draw.text("You got tagged!", center=(WIDTH/2, 50), fontsize=50, color="black")
    else:
        screen.draw.text("Tag the blue circle!", center=(WIDTH/2, 50), fontsize=30, color="black")


pgzrun.go()