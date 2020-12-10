import pygame
pygame.init()

win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Paint!")

x = 50
y = 50
width = 10
height = 10
vel = 10
color = (255, 255, 255)
isJump = False
jumpCount = 10

run = True

while run:
    pygame.time.delay(111)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_u]:
        color = (0, 0, 0)
    if keys[pygame.K_d]:
        color = (255, 0, 0)
    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
    if keys[pygame.K_RIGHT] and x < 500 - vel - width:
        x += vel
    if keys[pygame.K_p]:
        color = (255, 0, 255)
    if keys[pygame.K_w]:
        color = (255, 255, 255)
    if keys[pygame.K_y]:
        color = (255, 255, 0)
    if keys[pygame.K_g]:
        color = (0, 255, 0)
    if keys[pygame.K_b]:
        color = (0, 0, 255)
    if keys[pygame.K_r]:
        color = (255, 0, 0)
    if not (isJump):
        if keys[pygame.K_UP] and y > vel:
            y -= vel
        if keys[pygame.K_DOWN] and y < 500 - height - vel:
            y += vel
        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        if jumpCount >= -10:
            y -= (jumpCount * abs(jumpCount)) * 0.5
            jumpCount -= 1
        else:
            jumpCount = 10
            isJump = False

    pygame.draw.rect(win, (color), (x, y, width, height))
    pygame.display.update()

pygame.quit()
