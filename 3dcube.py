import pygame
# import math
import numpy as np
from math import *

screen_size = 800
window = pygame.display.set_mode( (screen_size,screen_size) )

clock = pygame.time.Clock()


projection_matrix = [[1,0,0],
                     [0,1,0],
                     [0,0,0]]

# np.dot(projection_matrix, point)

cube_points = [n for n in range (8)]
for i in range (2):
    for j in range (2):
        for k in range (2):
            cube_points[k+(j*2)+(i*4)] = [[i*2-1], [j*2-1], [k*2-1]]
# print(cube_points)


def connect_points(i, j, points):
    pygame.draw.line(window, (255,255,255), (points[i][0], points[i][1]), (points[j][0], points[j][1]))







rotate_speed = 0.01
angle_x = angle_y = angle_z = 0
scale = 100
while True:
    clock.tick(60)
    window.fill((0,0,0))
    
    rotation_x = [[1, 0, 0],
                  [0, cos(angle_x), -sin(angle_x)],
                  [0, sin(angle_x), cos(angle_x)]]
    
    rotation_y = [[cos(angle_y), 0, sin(angle_y)],
                  [0, 1, 0],
                  [-sin(angle_y), 0, cos(angle_y)]]
    
    rotation_z = [[cos(angle_z), -sin(angle_z), 0],
                  [sin(angle_z), cos(angle_z), 0],
                  [0, 0, 1]]
    
    
    # angle_x += 0.01
    # angle_y += 0.01
    # angle_z += 0.01
    
    
    points = [0 for _ in range (len(cube_points))]
    i = 0
    for point in cube_points:
        rotate_x = np.dot(rotation_x, point)
        rotate_y = np.dot(rotation_y, rotate_x)
        rotate_z = np.dot(rotation_z, rotate_y)
        
        point_2d = np.dot(projection_matrix, rotate_z)
        x = (point_2d[0][0]*scale) + screen_size/2
        y = (point_2d[1][0]*scale) + screen_size/2
        
        points[i] = x,y
        i += 1
        pygame.draw.circle(window, (255, 0, 0), (x,y), 5)
    
    
    connect_points(0, 1, points)
    connect_points(0, 2, points)
    connect_points(0, 4, points)
    connect_points(1, 3, points)
    connect_points(1, 5, points)
    connect_points(2, 6, points)
    connect_points(2, 3, points)
    connect_points(3, 7, points)
    connect_points(4, 5, points)
    connect_points(4, 6, points)
    connect_points(5, 7, points)
    connect_points(6, 7, points)

    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
        if keys[pygame.K_r]:
            angle_y = angle_x = angle_z = 0
            
        if keys[pygame.K_a]:
            angle_y += rotate_speed
        if keys[pygame.K_d]:
            angle_y -= rotate_speed
        if keys[pygame.K_w]:
            angle_x += rotate_speed
        if keys[pygame.K_s]:
            angle_x -= rotate_speed
        if keys[pygame.K_q]:
            angle_z += rotate_speed
        if keys[pygame.K_e]:
            angle_z -= rotate_speed

    pygame.display.update()
    
    
