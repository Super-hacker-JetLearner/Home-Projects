import pygame
import pgzrun
import math



image_height = 512
image_width = 512
window = pygame.display.set_mode( (image_width,image_height) )

clock = pygame.time.Clock()

# these are the coordinates of the corners of the cube
corners = [ [ 1, -1, -5],
            [ 1, -1, -3],
            [ 1,  1, -5],
            [ 1,  1, -3],
            [-1, -1, -5],
            [-1, -1, -3],
            [-1,  1, -5],
            [-1,  1, -3]]
                


camera_position = [1.2, -1.2, -5.2]


# z_angle = 0
# x_angle = 0
# y_angle = 0
angles = [0,0,0]
rotate_speed = 0.01
move_speed = 0.01
# angle_pairs = [[0,1], [0,2], [1,2]]

while True:
    
    clock.tick(60)
    window.fill((0,0,0))
   
    
    screen_positions = []
    difference_corners = []

    
    
    for i in range (8):
        
        
        # find the difference between camera and point positions to account for moving
        difference_corners.append([corners[i][0] - camera_position[0],  corners[i][1] - camera_position[1],  corners[i][2] - camera_position[2]])
        
        # -----------------------------------------------------------------------------------------------
        # change the angle of viewing
        # change the coordinates to polar and change the angle
        polar = []
        polar.append(math.sqrt(difference_corners[i][0]*difference_corners[i][0] + difference_corners[i][1]*difference_corners[i][1]))
        polar.append(math.atan2(difference_corners[i][0], difference_corners[i][1]))
        polar[1] += angles[0]
            
        # and then put it back into cartesian
        difference_corners[i][0] = polar[0] * math.cos(polar[1])
        difference_corners[i][1] = polar[0] * math.sin(polar[1])
        
        
        # ------------------------------------------------------------------------------------------------
        # change the angle of viewing
        # change the coordinates to polar and change the angle
        polar = []
        polar.append(math.sqrt(difference_corners[i][0]*difference_corners[i][0] + difference_corners[i][2]*difference_corners[i][2]))
        polar.append(math.atan2(difference_corners[i][0], difference_corners[i][2]))
        polar[1] += angles[1]
        

        # and then put it back into cartesian
        difference_corners[i][0] = polar[0] * math.cos(polar[1])
        difference_corners[i][2] = polar[0] * math.sin(polar[1])
        
        # ------------------------------------------------------------------------------------------------
        # change the angle of viewing
        # change the coordinates to polar and change the angle
        polar = []
        polar.append(math.sqrt(difference_corners[i][1]*difference_corners[i][1] + difference_corners[i][2]*difference_corners[i][2]))
        polar.append(math.atan2(difference_corners[i][1], difference_corners[i][2]))
        polar[1] += angles[2]
            
        # and then put it back into cartesian
        difference_corners[i][1] = polar[0] * math.cos(polar[1])
        difference_corners[i][2] = polar[0] * math.sin(polar[1])

        # -----------------------------------------------------------------------------------------------

        # divide by the z to make it 3d
        x_angle_proj = difference_corners[i][0] / -difference_corners[i][2]
        y_angle_proj = difference_corners[i][1] / -difference_corners[i][2]
        
        # scale and display it
        x_proj_remap = (1 + x_angle_proj) / 2
        y_proj_remap = (1 + y_angle_proj) / 2
        x_proj_pix = x_proj_remap * image_width
        y_proj_pix = y_proj_remap * image_height
        screen_positions.append([x_proj_pix, y_proj_pix])
        print(f"Corner: {i} x:{x_proj_pix} y:{y_proj_pix}\n")
        pygame.draw.circle(window, (255, 255, 255), (x_proj_pix, y_proj_pix), 5)


    # check for key events
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            
            # if keys[pygame.K_r]:
            #     angle_y = angle_x = angle_z = 0
            
            # if keys[pygame.K_a]:
            #     angle_y += rotate_speed
            # if keys[pygame.K_d]:
            #     angle_y -= rotate_speed
            
        # rotate the camera
        if keys[pygame.K_i]:
            angles[0] += rotate_speed
        if keys[pygame.K_k]:
            angles[0] -= rotate_speed
        if keys[pygame.K_j]:
            angles[1] += rotate_speed
        if keys[pygame.K_l]:
            angles[1] -= rotate_speed
        if keys[pygame.K_u]:
            angles[2] += rotate_speed
        if keys[pygame.K_o]:
            angles[2] -= rotate_speed
            # if keys[pygame.K_q]:
            #     angle_z += rotate_speed
            # if keys[pygame.K_e]:
            #     angle_z -= rotate_speed
        
        # move the camera
        if keys[pygame.K_a]:
            camera_position[0] += move_speed
        if keys[pygame.K_d]:
            camera_position[0] -= move_speed
        if keys[pygame.K_w]:
            camera_position[1] += move_speed
        if keys[pygame.K_s]:
            camera_position[1] -= move_speed
        if keys[pygame.K_q]:
            camera_position[2] += move_speed
        if keys[pygame.K_e]:
            camera_position[2] -= move_speed

    
    
    # update the display
    pygame.display.update()
