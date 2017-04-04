import pygame
import time
import random

pygame.init()

display_width = 800
display_height =600
black = (0,0,0)
white = (255,255,255)
red = (255,0,0)


gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Race Car')
clock = pygame.time.Clock()
carImg = pygame.image.load('car.png')

def things_dodged(count):
    font = pygame.font.SysFont(None,25)
    text = font.render("Dodged :"+str(count),True,black)
    gameDisplay.blit(text,(0 ,0))
def collision(ob1x, ob1y , ob1w , ob1h, ob2x , ob2y , ob2w , ob2h):
       if ob1y <= ob2y + ob2h + 1 and ob1y >= ob2y + 20:
               if ob1x > ob2x and ob1x+ob1w < ob2x+ob2w:
                        print('Collision case 1')
                        print(ob1x,ob1y,ob2x,ob2y)
                        return True
       elif ob1x+ob1w <= ob2x and ob1x+ob1w >= ob2x + 10:
               if ob1y > ob2y + 10 and ob1y+ob1h < ob2y + ob2h + 10:
                        print('Collision case 2')
                        print(ob1x,ob1y,ob2x,ob2y)
                        return True
       elif ob1x >= (ob2x+ob2w):
               if ob1y+ob1h > ob1y and ob1y > ob1y and ob1y+ob1h < ob1h+ob1w and ob1y < ob1y+ob1h :
                        print('Collision case 3')
                        crash()
                        return True
                

def car(x,y):
    gameDisplay.blit(carImg,(x,y))
def text_objects(text , font):
    textSurface = font.render(text ,True , black)
    return textSurface ,textSurface.get_rect()
def message_display(text):
    largeText = pygame.font.Font('28 Days Later.ttf',115)
    TextSurf,TextRect = text_objects(text ,largeText)
    TextRect.center= (display_width/2),(display_height/2)
    gameDisplay.blit(TextSurf,TextRect)
    pygame.display.update()
    time.sleep(2)
    game_loop()
    
    

def crash():
    message_display("You Crashed")
    

def things(thingx , thingy , thingw , thingh , color):
    pygame.draw.rect(gameDisplay , color , [thingx , thingy , thingw ,thingh])
    
    


def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.6)
    dodged = 0
    x_change = 0

    thing_startx = random.randrange(0, display_width)
    thing_starty = -600
    thing_speed = 7
    thing_width= 100
    thing_height = 100
        
    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            gameExit=True
                            pygame.quit()
                            quit()

                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_LEFT:
                                x_change = -20
                            elif event.key == pygame.K_RIGHT:
                                x_change = 20

                        if event.type == pygame.KEYUP:
                            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                                x_change =0

                        if x > (display_width - 50) or x < 0:
                            crash()
                        if thing_starty > display_height:
                                 thing_starty = 0 -thing_height
                                 thing_startx = random.randrange(0,display_width)
                                 dodged = dodged+1
                                 thing_speed+=0.5
                                 thing_width += (dodged * 10)
                        if collision(x,y,50,50,thing_startx,thing_starty,thing_width,thing_height):
                                 crash()
                       
                    #collision(ob1x, ob1y , ob1w , ob1h, ob2x , ob2y , ob2w , ob2h) 
                    
                     #       print(x,y,thing_startx,thing_starty)
                      #      crash()

                
        if thing_starty > display_height:
                             thing_starty = 0 -thing_height
                             thing_startx = random.randrange(0,display_width)
                             dodged = dodged+1
                             thing_speed+=1
                             thing_width += (dodged * 10)
        gameDisplay.fill(white)
        #things(thigx , thingy , thingw , thingh , color)
        things(thing_startx , thing_starty ,thing_width,thing_height , red)
        thing_starty +=thing_speed
        x += x_change
        car(x,y)
        things_dodged(dodged)
        if collision(x,y,50,50,thing_startx,thing_starty,thing_width,thing_height):
            crash()
        pygame.display.update()
        clock.tick(60);


game_loop()
pygame.quit()
quit()

        
        
