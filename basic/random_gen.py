lightblue=(0,174,255)
import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
screen.fill(lightblue)
images=pygame.image.load('test.png')
noi=16
current_image=0

time = 0

while not done:
        time += 1
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                        pygame.quit()
                        quit()

        if time % 180 == 0:
            if(current_image>noi-1):
                current_image=0
            else:
               current_image+=1
        screen.blit(images,(50,100),(current_image*32,0,32,32))
        pygame.display.flip()
