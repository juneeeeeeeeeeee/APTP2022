import main
import pygame

pygame.init()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
size = [600, 600]

screen = pygame.display.set_mode(size)
pygame.display.set_caption("2048!")
namefont = pygame.font.SysFont('arial', 70, True, False)
font=pygame.font.SysFont('arial', 20)
done = False
clock = pygame.time.Clock()
MAX_SCORE=0
SCORE=0

if __name__=="__main__":
  
  
  while not done:
    screen.fill(WHITE)
    clock.tick(10)
    nametext = namefont.render("2048!", True, BLACK)
    nametextrect = nametext.get_rect()
    nametextrect.center = (round(size[0]/2),round(size[1]/7))
    screen.blit(nametext, nametextrect)
    pygame.draw.rect(screen, RED, [round(size[0]/4),round(size[1]*1/3),round(size[0]/2),round(size[1]/6)])
    pygame.draw.rect(screen, BLUE, [round(size[0]/4),round(size[1]*2/3),round(size[0]/2),round(size[1]/6)])
    gametext1 = font.render("PLAY GAME", True, WHITE)
    gametextrect1 = gametext1.get_rect()
    gametextrect1.center = (round(size[0]/2),round(size[1]*5/12))
    screen.blit(gametext1, gametextrect1)
    gametext2 = font.render("AI MODE", True, WHITE)
    gametextrect2 = gametext2.get_rect()
    gametextrect2.center = (round(size[0]/2),round(size[1]*9/12))
    screen.blit(gametext2, gametextrect2)
    maxscoretext = font.render("max score:{0}".format(MAX_SCORE), True, BLACK)
    maxscoretextrect = maxscoretext.get_rect()
    maxscoretextrect.center = (round(size[0]/2),round(size[1]*3/12))
    screen.blit(maxscoretext, maxscoretextrect)
    pygame.draw.rect(screen, BLACK, [round(size[0]/3),round(size[1]*21/24),round(size[0]/3),round(size[1]*2/24)], 4)
    resetmaxscoretext = font.render("reset max score", True, BLACK)
    resetmaxscoretextrect = resetmaxscoretext.get_rect()
    resetmaxscoretextrect.center = (round(size[0]/2),round(size[1]*11/12))
    screen.blit(resetmaxscoretext, resetmaxscoretextrect)
    for event in pygame.event.get():
    
      if event.type==pygame.QUIT:
        done=True
      elif event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
        pygame.mouse.get_rel()
        mouse_pos=pygame.mouse.get_pos()
        if mouse_pos[0]>round(size[0]/4) and mouse_pos[0]<round(size[0]/4)+round(size[0]/2) and mouse_pos[1]>round(size[1]*1/3) and mouse_pos[1]<round(size[1]*1/3)+round(size[1]/6):
          SCORE=main.runGame()
          if SCORE>MAX_SCORE:
            MAX_SCORE=SCORE
        elif mouse_pos[0]>round(size[0]/3) and mouse_pos[0]<round(size[0]*2/3) and mouse_pos[1]>round(size[1]*21/24) and mouse_pos[1]<round(size[1]*23/24):
          MAX_SCORE=0
    pygame.display.update()
  pygame.quit()