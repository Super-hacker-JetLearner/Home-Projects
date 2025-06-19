import pgzrun

HEIGHT = 200
WIDTH = 800
start_speed = 3  # Speed of the cactus
gravity = 0.4
jump_height = 9  # Height of the jump
acceleration = 0.01  # Acceleration of the cactus speed

dino = Actor("dino.png")
dino.x = 100
dino.y = 151
yv = 0  # Vertical velocity for jumping
ground = 150  # Ground level for the dino


cactus = Actor("cactus.png")
cactus.x = WIDTH
cactus.y = 150

stop = False  # Flag to stop the game

def on_key_down(key):
    global yv
    if stop:
        return
    if key == keys.SPACE or key == keys.UP:  # Jump when space or up arrow is pressed
        if abs(dino.y - ground) < 5:  # Only jump if on the ground
            yv = -jump_height  # Set a negative velocity to move up

def update():
    global yv, stop, start_speed
    if stop:
        return
    dino.y += yv
    yv += gravity  # Apply gravity
    if dino.y > ground:
        dino.y = ground
        yv = 0

    start_speed += acceleration  # Increase the speed of the cactus

    cactus.x -= start_speed  # Move the cactus to the left
    if cactus.x < 0:  # If the cactus goes off screen
        cactus.x = WIDTH  # Reset its position to the right side

    # Check for collision between dino and cactus
    if dino.colliderect(cactus):
        stop = True  # Stop the game if a collision occurs

def draw():
    if stop:
        screen.draw.text("Game Over", (WIDTH // 2 - 50, HEIGHT // 2), color="red", fontsize=40)
        return
    screen.fill((255, 255, 255))  # Fill the screen with white
    dino.draw()  # Draw the dino actor
    cactus.draw()
    
    
pgzrun.go()  # Start the game loop