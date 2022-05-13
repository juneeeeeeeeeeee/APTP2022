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
    # 1 합쳐지는 경우 : 인접한 위 바로 위의 블럭 값이 같은 경우 - 블럭이 하나만 남거나 위 아래 비교해서 다를 때
    # 2 합쳐지지 않는 경우 : #1을 반복할 수 없는 경우

    pass
  def rightdirection(self): # 블럭이 오른쪽으로 움직이거나 합쳐지는 경우
    # 1 합쳐지는 경우 : 인접한 위 바로 위의 블럭 값이 같은 경우 - 블럭이 하나만 남거나 왼쪽 오른쪽 비교해서 다를 때
    # 2 합쳐지지 않는 경우 : #1을 반복할 수 없는 경우

    pass
  def downdirection(self): # 블럭이 아래로 움직이거나 합쳐지는 경우
    # 1 합쳐지는 경우 : 인접한 위 바로 위의 블럭 값이 같은 경우 - 블럭이 하나만 남거나 위 아래 비교해서 다를 때
    # 2 합쳐지지 않는 경우 : #1을 반복할 수 없는 경우
    pass
  def leftdirection(self): # 블럭이 왼쪽으로 움직이거나 합쳐지는 경우
    # 1 합쳐지는 경우 : 인접한 위 바로 위의 블럭 값이 같은 경우 - 블럭이 하나만 남거나 왼쪽 오른쪽 비교해서 다를 때
    # 2 합쳐지지 않는 경우 : #1을 반복할 수 없는 경우
    pass
  def showblockthingy(self): # 블럭의 위치를 표시
    pygame.draw.rect(screen, RED, [(size[0]/2) + (BLOCKLEN*(self.col-(BOARDN/2))), (size[1]/2) + (BLOCKLEN*(self.row-(BOARDN/2))), BLOCKLEN, BLOCKLEN])
    text = font.render(str(self.blocknum), True, WHITE)
    textrect=text.get_rect()
    textrect.center=((size[0]/2) + (BLOCKLEN*(self.col-(BOARDN-1)/2)), (size[1]/2) + (BLOCKLEN*(self.row-(BOARDN-1)/2)))
    screen.blit(text, textrect)
  def __del__(self):
    pass
blocklist=[[blockthingy(0, i, j) for j in range(0, BOARDN)] for i in range(0, BOARDN)]
def runGame():
  global done
  global blocklist
  screen.fill(WHITE)
  for i in range(BOARDN):
    for j in range(BOARDN):
      pygame.draw.rect(screen, BLACK, [(size[0]/2) + (BLOCKLEN*(i-(BOARDN/2))), (size[1]/2) + (BLOCKLEN*(j-(BOARDN/2))), BLOCKLEN, BLOCKLEN], 2)
  # 첫 블럭 생성
  newposition=random.randint(0, BOARDN*BOARDN)
  blocklist[newposition//BOARDN][newposition%BOARDN]=blockthingy(2, newposition//BOARDN, newposition%BOARDN)
  blocklist[newposition//BOARDN][newposition%BOARDN].showblockthingy()
  while not done:
    clock.tick(10)
    for event in pygame.event.get():
      if event.type==pygame.QUIT:
        done=True
      elif event.type==pygame.KEYDOWN:
        if event.key==pygame.K_UP:
          pass # 홍상은 : 이거 위 방향키 눌렀을 때 함수인데 이거 알고리즘 대략 작성해주셈
        elif event.key==pygame.K_RIGHT:
          pass
          """
          총 행의 개수가 boardn이므로 1행부터 boardn행까지 각각 밑의 동작 반복
          
          // 각 행의 블럭들 중 숫자가 있는 블럭을 판별 //
          n = 0
          while (각 행의 모든 블럭을 판단하지 않은 경우)
            처음 블럭 위치 : 각 행의 맨 오른쪽 블럭의 위치
            
            if (현재 위치의 블럭에 숫자가 있다면)
              n에 1을 더함
              그 블럭을 n번 블럭으로 설정
                            
            블럭 위치를 한 칸 왼쪽으로 옮김
              
          // 숫자가 있는 블럭들을 합침 //
          m = 1
          while (m이 n보다 작다면)
            if (n이 2보다 크거나 같다면)
          
              if (m번 블럭과 m+1번 블럭에 저장된 값이 같다면)
                m번 블럭의 값을 2배 해준다
                m+1번 블럭의 값을 0으로 만든다
                m에 2를 더한다
                
              else
                m에 1을 더한다
              
              
          // 합친 블럭들을 한쪽으로 옮겨주는 과정 //
          mov = 0
          k = 1
          while (k가 n보다 작거나 같을 경우)
            if (k번 블럭에 숫자가 있다면)
              그 블럭을 mov번 블럭으로 설정
              k에 1을 더함
          
          while (mov가 k보다 작은 경우)
            mov번째 블럭을 오른쪽에서 mov번째 위치로 옮김 
            // ex) mov가 1인 블럭은 숫자가 있는 맨 오른쪽 블럭이고, 이 블럭을 오른쪽에서 1번째 위치, 즉 맨 오른쪽으로 옮긴다        
          """

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
          blocklist[newposition//BOARDN][newposition%BOARDN].showblockthingy()
    pygame.display.update() #update UI
if __name__=="__main__":
  runGame()
  pygame.quit()

