import pygame,time,os
import random
pygame.init()
os.getcwd()
fpsclock=pygame.time.Clock()
displaysurf=pygame.display.set_mode((800,600))
pygame.display.set_caption('car_race')

white=(255,255,255)
red=(255,0,0)
black=(0,0,0)

redcarImg=pygame.image.load('redcar.png')
bluecarImg=pygame.image.load('bluecar.jpg')
roadImg=pygame.image.load('road.jpg')
boomImg=pygame.image.load('boom.png')
crashSound=pygame.mixer.Sound('crash.wav')
x=350
y=400
m=170
n=200
def redcar(x,y):
    displaysurf.blit(pygame.transform.scale(redcarImg,(80,100)),(x,y))
def road():
    displaysurf.blit(pygame.transform.rotate(pygame.transform.scale(roadImg,(800,600)),90
                                            ),(0,0))
def bluecar(m,n):
    displaysurf.blit(pygame.transform.rotate(pygame.transform.scale(redcarImg,(80,100)),180),(m,n))
def boom(i,j):
    displaysurf.blit(pygame.transform.scale(boomImg,(150,150)),(i,j))
change_n=0
change_x=0
crashed=False
while not crashed:
    displaysurf.fill(white)
    road()
    redcar(x,y)
    
    bluecar(m,n)
    
    n+=20
    if n>700:
            n=-100
            a=random.randint(0,1)
            if a==1:
                m=170
            else:
                m=350
    if ((m==x) and (n==y+40 or n==y-40)):
           crashSound.play()
           boom(x,y)
           crashed=True            
    for event in pygame.event.get():

         
        
            
        if event.type==pygame.QUIT:
            crashed=True
                        
        
        
        if event.type==pygame.KEYDOWN:

            if event.key==pygame.K_LEFT:
                if x==350:
                  change_x=-180

            elif event.key==pygame.K_RIGHT:
                if x==170: 
                  change_x=180
            else:
                change_x=0
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                change_x=0
    
        
        
        x=x+change_x   
    pygame.display.update()
                
    fpsclock.tick(30)
pygame.quit()
