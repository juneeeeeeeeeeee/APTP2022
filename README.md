# APTP 2022
Asterisk Python Team Project 2022

# 2019-2 객체지향 프로그래밍 프로젝트 - **{4096}**
구성원: 2-5 김예건 | 2-5 이영채 | 2-6 김덕용

## 1. 주제
{2048게임을 구현하고자 한다. 2048게임이란 퍼즐게임으로 규칙에 맞게 2048이라는 숫자를 만들게 되면 클리어하게 되는 게임이다. 기존의 2048과 달리 칸을 추가함으로써 더욱 다양한 게임 구성이 가능할 것으로 보이며 학습 또한 더욱 잘 될 것으로 예상된다. 이를 통해 게임을 즐기는 사람들의 선택의 폭을 넓힌다.}

## 2. 동기
{평소 유아 및 청소년을 대상을 한 게임에 관심이 많아 2048이나 Atomus같은 게임에 관심을 두고 살펴보고 있었다. 그중에서도 2048은 학생의 계산 능력 및 공간적 사고 능력을 키울 수 있는 게임으로 GUI또한 구현방법이 비교적 명확해 보이고 Class 구현이 체계적으로 구성될 수 있을 것 같아 정하였다.}

## 3. 프로그램 사용 대상
{게임의 룰이 단순하고 쉽게 접근할 수 있어 전 연령의 사람들이 즐길 수 있다. 주로 미취학 아동, 청소년들이 이용할 것으로 기대된다.}

## 4. 목적
{https://play2048.co/
보통은 위 링크와 같이 4*4 사이즈의 보드판에서 진행한다. 허나, 우리는 사용자가 원하는 판 사이즈를 입력하면, 이에 맞게 판을 만들어 게임을 진행할 수 있도록 하려한다. 또한 친구들과 함께 경쟁하며 시간을 단축하여 참여할 수 있도록 게임 클리어까지 걸린 시간을 측정한 후, 측정된 시간을 서버에 보내 서버에서 랭크를 확인할 수 있도록 제작할 것이다.}

## 5. 주요기능
1. 숫자가 적혀있는 상자들이 상하좌우로 움직일 수 있다.
2. 상자끼리 만날 때 같은 숫자로 이루어진 상자이면 두 상자가 하나로 합쳐지고 숫자가 두 배가 된다. 
3. 다른 숫자의 상자이면 색이 다르다. 
4. 상자가 벽을 만나면 움직이지 않는다. 
5. 다른 숫자의 상자가 만나면 벽처럼 작용해 서로 합쳐지지 않고 막는다.
6. 16칸이 상자로 다 차고 더 합칠 수 있는 상자가 없을 때 게임이 종료된다.
7. 칸의 개수를 4x4~8x8개까지 설정할 수 있다.
8. 점수를 저장하고 최고 점수를 표시할 수 있다.
9. 서버를 통해 최고 점수를 비교해 랭크를 만들 수 있다.

## 6. 프로젝트 핵심
1. 각 상자를 객체로 구현하는 것이 중요하다. 이를 통해 상자의 숫자, 움직임 등 겹치는 것이 많은 기능이 class를 통해 구현이 가능할 것으로 보인다
2. 서버를 통해 점수를 저장하고 랭크를 표시하는 기능이 필요하다. 또한 사용자에 따라 최고점수가 갱신되면 서버에서도 갱신된 점수를 사용자 점수에 넣어야 하기 때문에 이를 바꾸는 것도 필요할 것으로 보인다.
3. GUI를 구현할 때 판의 크기에 따라 상자의 크기 등이 달라져야 하므로 이 부분 또한 생각이 필요하다고 생각한다.

## 7. 구현에 필요한 라이브러리나 기술
{pygame, sys, socket, time, random, threading}

## 8. **분업 계획**
김덕용: GUI 구현, board 구현
이영채: 상자 Class 구현
김예건: 서버 및 클라이언트 구현

## 9. 기타


1. 서버에 점수를 올리고 싶다면 server.py를 먼저 실행시킨 후 board.py를 실행시키세요. 서버를 사용하기 전에 client.py의 IP와 server.py의 IP를 같게 수정하세요. 기본값은 127.0.0.1입니다. IP는 HOST변수에 들어있습니다. ip_check.py를 통해 IP를 알아낼 수 있습니다.
2. 만약 오프라인으로 즐기고 싶다면 board.py를 실행시키세요

<hr>

#### readme 작성관련 참고하기 [바로가기](https://heropy.blog/2017/09/30/markdown/)

#### 예시 계획서 [[예시 1]](https://docs.google.com/document/d/1hcuGhTtmiTUxuBtr3O6ffrSMahKNhEj33woE02V-84U/edit?usp=sharing) | [[예시 2]](https://docs.google.com/document/d/1FmxTZvmrroOW4uZ34Xfyyk9ejrQNx6gtsB6k7zOvHYE/edit?usp=sharing) | [[예시 3]](https://github.com/goldmango328/2018-OOP-Python-Light) | [[예시4]](https://github.com/ssy05468/2018-OOP-Python-lightbulb) | [[모두보기]](https://github.com/kadragon/oop_project_ex/network/members)



