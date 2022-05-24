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
font = pygame.font.SysFont('arial', 20)
done = False
clock = pygame.time.Clock()

if __name__=="__main__":
  clock.tick(10)
  
  pygame.display.update()
