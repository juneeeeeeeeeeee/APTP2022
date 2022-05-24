import pygame
import random
import copy
import math
import time

pygame.init()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
size = [600, 600]
BOARDN = 3
BLOCKLEN = 70
checkmoved = 0
score = 0

screen = pygame.display.set_mode(size)
pygame.display.set_caption("2048!")
font = pygame.font.SysFont('arial', 20)
bigfont=pygame.font.SysFont('arial', 40, True, True)
done = False
clock = pygame.time.Clock()


class blockthingy:
    def __init__(self, blocknum, row, col):
        self.blocknum = blocknum
        self.row = row
        self.col = col

    """
    상하로 이동 시 열끼리 시행 (line 209에 j)
    좌우로 이동 시 행끼리 시행 (line 217에 i)
    
    direction 함수에서 블럭 이동과 합체를 따로 진행하면 알고리즘이 너무 복잡해져 list 정렬로 동시에 진행
    updirection 에서 up 기준으로만 설명
    
    up과 left 입력 시에는 왼쪽위에서 오른아래로 스캔
    down과 right 입력 시에는 오른아래서 왼쪽위로 스캔
    (2, 2, 0, 2) 일때
    left 입력 시 (4, 2, 0, 0)
    right 입력 시 (0, 0, 2, 4) 가 되기 때문
    """

    

    def showblockthingy(self):  # 블럭의 위치를 표시
        colorR = 367 - math.log(self.blocknum) * 20
        colorG = 216 - math.log(self.blocknum) * 15
        colorB = 193 - math.log(self.blocknum) * 26
        if colorR > 255:
            colorR = 255
        if colorR < 0:
            colorR = 0
        if colorG > 255:
            colorG = 255
        if colorG < 0:
            colorG = 0
        if colorB > 255:
            colorB = 255
        if colorB < 0:
            colorB = 0
        # 숫자 커질수록 색깔 진해짐
        # rect 범위를 +2 -4 로 조정해줌으로써 숫자타일이 검은색 구분선 가리던 문제 해결
        pygame.draw.rect(screen, (colorR, colorG, colorB), [(size[0] / 2) + (BLOCKLEN * (self.col - (BOARDN / 2)))+2,
                                                            (size[1] / 2) + (BLOCKLEN * (self.row - (BOARDN / 2)))+2, BLOCKLEN-4, BLOCKLEN-4])
        text = font.render(str(self.blocknum), True, WHITE)
        textrect = text.get_rect()
        textrect.center = ((size[0] / 2) + (BLOCKLEN * (self.col - (BOARDN - 1) / 2)),
                           (size[1] / 2) + (BLOCKLEN * (self.row - (BOARDN - 1) / 2)))
        screen.blit(text, textrect)

    def __del__(self):
        pass


blocklist = [[blockthingy(0, i, j) for j in range(0, BOARDN)] for i in range(0, BOARDN)]


def runGame():
    global done
    done=False
    global blocklist
    blocklist = [[blockthingy(0, i, j) for j in range(0, BOARDN)] for i in range(0, BOARDN)]
    global checkmoved
    checkmoved=0
    global score
    score=0
    screen.fill(WHITE)
    for i in range(BOARDN):
        for j in range(BOARDN):
            pygame.draw.rect(screen, BLACK, [(size[0] / 2) + (BLOCKLEN * (i - (BOARDN / 2))),
                                             (size[1] / 2) + (BLOCKLEN * (j - (BOARDN / 2))), BLOCKLEN, BLOCKLEN], 2)
    # 첫 블럭 생성
    newposition = random.randint(0, BOARDN * BOARDN)
    blocklist[newposition // BOARDN][newposition % BOARDN] = blockthingy(2, newposition // BOARDN, newposition % BOARDN)
    blocklist[newposition // BOARDN][newposition % BOARDN].showblockthingy()
    while not done:
        clock.tick(10)
        # 점수판
        pygame.draw.rect(screen, (180,255,180), [round(size[0]/3),round(size[1]*11/120),round(size[0]/3),round(size[1]/20)])

        scoretext1 = font.render("SCORE", True, BLACK)
        scoretextrect1 = scoretext1.get_rect()
        scoretextrect1.center = (round(size[0]/2),round(size[1]/15))
        screen.blit(scoretext1, scoretextrect1)

        scoretext2 = font.render(str(score), True, BLACK)
        scoretextrect2 = scoretext2.get_rect()
        scoretextrect2.center = (round(size[0]/2),round(size[1]*7/60))
        screen.blit(scoretext2, scoretextrect2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    for j in range (0, BOARDN):  
                        collist = []  # 정렬할 list
                        for k in range (0, BOARDN):  # 하나의 열에서 N개의 blocklist.blocknum을 차례로 list에 대입
                            collist.append(blocklist[k][j].blocknum)
                        rememberlist = copy.deepcopy(collist)  # 블럭 변화 감지를 위한 tmp list
                        while 0 in collist:  # blocknum들의 합체를 위해 하나의 열에서 white 배경에 해당하는 0 제거
                            collist.remove(0)
                        if len(collist) >= 2:  # blocknum 합체는 숫자가 2개 이상일 때만 필요
                            for k in range (0, len(collist)-1):  # 0을 제외하고 자신의 blocknum이 위의 blocknum과 같을 경우 합체
                                if collist[k] != 0 and collist[k] == collist[k+1]:
                                    collist[k] *= 2
                                    collist[k+1] = 0
                                    score += collist[k]  # 그냥 점수...
                        while 0 in collist:  # 합체한 후 남은 0 제거 ( (2,2,2,2)에서 (4,0,4,0)이 되면 (4,4,0,0)처럼 왼쪽으로 몰아줘야돼서 사이의 0 제거) )
                            collist.remove(0)
                        while len(collist) < BOARDN:  # list 길이 4로 복구
                            collist.append(0)
                        for k in range (0, BOARDN):  # blocklist.blocknum에 다시 대입
                            blocklist[k][j].blocknum = collist[k]
                        if rememberlist != collist:  # 블럭에 변화가 있다면 1
                            checkmoved = 1

                elif event.key == pygame.K_DOWN:
                    for j in range (0, BOARDN):
                        collist = []
                        for k in range (0, BOARDN):
                            collist.append(blocklist[k][j].blocknum)
                        rememberlist = copy.deepcopy(collist)
                        while 0 in collist:
                            collist.remove(0)
                        if len(collist) >= 2:
                            for k in range (len(collist)-1, 0, -1):
                                if collist[k] != 0 and collist[k] == collist[k-1]:
                                    collist[k] *= 2
                                    collist[k-1] = 0
                                    score += collist[k]
                        while 0 in collist:
                            collist.remove(0)
                        while len(collist) < BOARDN:
                            collist.insert(0, 0)
                        for k in range (0, BOARDN):
                            blocklist[k][j].blocknum = collist[k]
                        if rememberlist != collist:
                            checkmoved = 1

                elif event.key == pygame.K_LEFT:
                    for i in range (0, BOARDN):  # line 33에서 설명한 부분. [여기][]만 매개변수로서 의미있고 [][여기]는 비워두면 오류나서 그냥 똑같이 i로 채움...
                        collist = []
                        for k in range (0, BOARDN):
                            collist.append(blocklist[i][k].blocknum)
                        rememberlist = copy.deepcopy(collist)
                        while 0 in collist:
                            collist.remove(0)
                        if len(collist) >= 2:
                            for k in range (0, len(collist)-1):
                                if collist[k] != 0 and collist[k] == collist[k+1]:
                                    collist[k] *= 2
                                    collist[k+1] = 0
                                    score += collist[k]
                        while 0 in collist:
                            collist.remove(0)
                        while len(collist) < BOARDN:
                            collist.append(0)
                        for k in range (0, BOARDN):
                            blocklist[i][k].blocknum = collist[k]
                        if rememberlist != collist:
                            checkmoved = 1

                elif event.key == pygame.K_RIGHT:
                    for i in range (0, BOARDN):
                        collist = []
                        for k in range (0, BOARDN):
                            collist.append(blocklist[i][k].blocknum)
                        rememberlist = copy.deepcopy(collist)
                        while 0 in collist:
                            collist.remove(0)
                        if len(collist) >= 2:
                            for k in range (len(collist)-1, 0, -1):
                                if collist[k] != 0 and collist[k] == collist[k-1]:
                                    collist[k] *= 2
                                    collist[k-1] = 0
                                    score += collist[k]
                        while 0 in collist:
                            collist.remove(0)
                        while len(collist) < BOARDN:
                            collist.insert(0, 0)
                        for k in range (0, BOARDN):
                            blocklist[i][k].blocknum = collist[k]
                        if rememberlist != collist:
                            checkmoved = 1

                else:
                    continue
                # 블럭이 차지 않은 구역 확인 & 블럭이 모두 차있을 경우 게임 오버 & 해당 구역에서 랜덤하게 하나를 뽑아 블럭 생성
                checklist = []
                for i in range(0, BOARDN * BOARDN):
                    if blocklist[i // BOARDN][i % BOARDN].blocknum == 0:
                        checklist.append(i)
                        pygame.draw.rect(screen, WHITE, [(size[0] / 2) + (BLOCKLEN * (i%BOARDN - (BOARDN / 2)))+2,
                                                       (size[1] / 2) + (BLOCKLEN * (i//BOARDN - (BOARDN / 2)))+2,
                                                       BLOCKLEN-4, BLOCKLEN-4])
                    else:  # 블럭이 차있는 구역은 블럭 생성
                        blocklist[i // BOARDN][i % BOARDN].showblockthingy()
                if len(checklist) == 0:
                    done = True
                    gameovertext = bigfont.render("GAME OVER!", True, BLACK)
                    gameovertextrect = gameovertext.get_rect()
                    gameovertextrect.center = (size[0]/2,size[1]/2)
                    screen.blit(gameovertext, gameovertextrect)
                    pygame.display.update()
                    time.sleep(2)
                    
                elif checkmoved == 1:  # 전체 블럭에 변화가 있을 때만 newrect 생성
                    newposition = random.choice(checklist)
                    blocklist[newposition // BOARDN][newposition % BOARDN] = blockthingy(2, newposition // BOARDN,
                                                                                         newposition % BOARDN)
                    blocklist[newposition // BOARDN][newposition % BOARDN].showblockthingy()
        pygame.display.update()  # update UI
        checkmoved = 0
    return score



if __name__ == "__main__":
    runGame()
    pygame.quit()

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
                            mov+=1
                          k에 1을 더함

                        while (mov가 k보다 작거나 같은 경우)
                          mov번째 블럭을 오른쪽에서 mov번째 위치로 옮김 
                          // ex) mov가 0인 블럭은 숫자가 있는 맨 오른쪽 블럭이고, 이 블럭을 오른쪽에서 0번째 위치, 즉 맨 오른쪽으로 옮긴다        
                        """