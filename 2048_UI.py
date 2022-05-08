import pygame
import random
pygame.init()
BLACK=(0, 0, 0)
WHITE=(255, 255, 255)
BLUE=(0, 0, 255)
GREEN=(0, 255, 0)
RED=(255, 0, 0)
size=[600, 600]
BOARDN=4
BLOCKLEN=70

screen=pygame.display.set_mode(size)
pygame.display.set_caption("2048!")
font = pygame.font.SysFont('arial', 20)
done=False
clock=pygame.time.Clock()
class blockthingy:
  def __init__(self, blocknum, row, col):
    self.blocknum=blocknum
    self.row=row
    self.col=col
  def updirection(self): # 블럭이 위로 움직이거나 합쳐지는 경우
    pass
  def rightdirection(self): # 블럭이 오른쪽으로 움직이거나 합쳐지는 경우
    pass
  def downdirection(self): # 블럭이 아래로 움직이거나 합쳐지는 경우
    pass
  def leftdirection(self): # 블럭이 왼쪽으로 움직이거나 합쳐지는 경우
    pass
  def showblockthingy(self): # 블럭의 위치를 표시
    pygame.draw.rect(screen, RED, [(size[0]/2) + (BLOCKLEN*(self.col-(BOARDN/2))), (size[1]/2) + (BLOCKLEN*(self.row-(BOARDN/2))), BLOCKLEN, BLOCKLEN])
    text = font.render(str(self.blocknum), True, WHITE)
    textrect=text.get_rect()
    textrect.center=((size[0]/2) + (BLOCKLEN*(self.col-(BOARDN-1)/2)), (size[1]/2) + (BLOCKLEN*(self.row-(BOARDN-1)/2)))
    screen.blit(text, textrect)
  def __del__(self):
    pass

def runGame():
  global done
  global blocklist
  screen.fill(WHITE)
  blocklist=[[blockthingy(0, i, j) for j in range(0, BOARDN)] for i in range(0, BOARDN)]
  for i in range(BOARDN):
    for j in range(BOARDN):
      pygame.draw.rect(screen, BLACK, [(size[0]/2) + (BLOCKLEN*(i-(BOARDN/2))), (size[1]/2) + (BLOCKLEN*(j-(BOARDN/2))), BLOCKLEN, BLOCKLEN], 2)
  # 첫 블럭 생성
  newposition=random.randint(0, BOARDN*BOARDN)
  blocklist[newposition//BOARDN][newposition%BOARDN]=blockthingy(2, newposition//BOARDN, newposition%BOARDN)
  # blocklist[newposition//BOARDN][newposition%BOARDN].showblockthingy()
  while not done:
    clock.tick(10)
    for event in pygame.event.get():
      if event.type==pygame.QUIT:
        done=True
      elif event.type==pygame.KEYDOWN:
        if event.key==pygame.K_UP:
          pass
        elif event.key==pygame.K_RIGHT:
          pass
        elif event.key==pygame.K_DOWN:
          pass
        elif event.key==pygame.K_LEFT:
          pass
        else:
          continue
        # 블럭이 차지 않은 구역 확인 & 블럭이 모두 차있을 경우 게임 오버 & 해당 구역에서 랜덤하게 하나를 뽑아 블럭 생성
        checklist=[]
        for i in range(0, BOARDN*BOARDN):
          if blocklist[i//BOARDN][i%BOARDN].blocknum==0:
            checklist.append(i)
        if len(checklist)==0:
          done=True
        else:
          newposition=random.choice(checklist)
          blocklist[newposition//BOARDN][newposition%BOARDN]=blockthingy(2, newposition//BOARDN, newposition%BOARDN)
          # blocklist[newposition//BOARDN][newposition%BOARDN].showblockthingy()
    pygame.display.update() #update UI
if __name__=="__main__":
  runGame()
  pygame.quit()

