# CSE4185 Assignment02: Pacman

## Implement:
Minimax, Alpha-beta Pruning, Expectimax를 활용한 Multi-Agent 구현하기 

![upload img](https://i.esdrop.com/d/koodoeiok4nv/1qNP1c9liu.png)

## How to run the code:
The main file to run the pacman is pacman.py:

```
python pacman.py
```

Examples of how to run pacman.py:
```
python pacman.py -p ReflexAgent -m bigmap -n 1 -g DirectionalGhost -z 0.8 -k 1
```
```
python pacman.py -p MinimaxAgent -m minimaxmap -a depth=4
```

```
python pacman.py -p AlphaBetaAgent -m 4185map -a depth=2
```

```
python pacman.py -p ExpectimaxAgent -m mediummap -a depth=2
```

For help run:
```
python pacman.py -h
```
Help Output:
```
CSE4185 Assignment02: Pacman

Usage:
  USAGE:      python pacman.py <options>
  EXAMPLES:   (1) python pacman.py
                  - starts an interactive game
              (2) python pacman.py --map smallmap --zoom 2
              OR  python pacman.py -m smallmap -z 2
                  - starts an interactive game on a smaller board, zoomed in


Options:
  -h, --help            show this help message and exit
  -n GAMES, --numGames=GAMES
                        the number of GAMES to play [Default: 1]
  -m MAP_FILE, --map=MAP_FILE
                        the MAP_FILE from which to load the map layout
                        [Default: mediummap]
  -p TYPE, --pacman=TYPE
                        the agent TYPE in the pacmanAgents module to use
                        [Default: HumanAgent]
  -t, --textGraphics    Display output as text only
  -q, --quietTextGraphics
                        Generate minimal output and no graphics
  -g TYPE, --ghosts=TYPE
                        the ghost agent TYPE in the ghostAgents module to use
                        [Default: RandomGhost]
  -k NUMGHOSTS, --numghosts=NUMGHOSTS
                        The maximum number of ghosts to use [Default: 4]
  -z ZOOM, --zoom=ZOOM  Zoom the size of the graphics window [Default: 1.0]
  -f, --fixRandomSeed   Fixes the random seed to always play the same game
  -r, --recordActions   Writes game histories to a file (named by the time
                        they were played)
  --replay=GAMETOREPLAY
                        A recorded game file (pickle) to replay
  -a AGENTARGS, --agentArgs=AGENTARGS
                        Comma separated values sent to agent. e.g.
                        "opt1=val1,opt2,opt3=val3"
  -x NUMTRAINING, --numTraining=NUMTRAINING
                        How many episodes are training (suppresses output)
                        [Default: 0]
  --frameTime=FRAMETIME
                        Time to delay between frames; <0 means keyboard
                        [Default: 0.1]
  -c, --catchExceptions
                        Turns on exception handling and timeouts during games
  --timeout=TIMEOUT     Maximum length of time an agent can spend computing in
                        a single game [Default: 30]



```

## [Pᗣᗧ•••MᗣN Game Rule]
```
1. 팩맨이 흰색 작은 원을 먹을 경우, 10 point를 획득
2. 팩맨이 한 step을 갈때마다 1 point씩 감소
3. 팩맨이 모든 작은 원을 다먹을 시 승리, 유령이 팩맨을 잡을 시 패배. 
4. 팩맨의 목숨은 한 번뿐이다. 
5. 모서리에 존재하는 흰색 캡슐을 먹을 경우, 유령은 흰색 모드로 변하며, 유령의 속도가 반으로 
감소하고, 팩맨을 쫓지 않는다. 
6. 팩맨이 흰색 유령을 잡을 시 200 point 획득
7. 게임 승리 시, 500 point 획득
8. 게임 패배 시, 500 point 감소
```

## Result
### 1. MinMax Agent
```
python pacman.py -p MinimaxAgent -m minimaxmap -a depth=4 -n 1000 -q
```
<img width="232" alt="1" src="https://user-images.githubusercontent.com/91405382/197310385-f283d419-523b-4e36-9c00-d67a31390061.png">

### 2. Alpha-Beta Pruning Agent
```
python pacman.py -p AlphaBetaAgent -m minimaxmap -a depth=4 -n 1000 -q
```
<img width="232" alt="2" src="https://user-images.githubusercontent.com/91405382/197310424-a8c9c56c-c038-4e5b-86bf-878480d0fbcd.png">
Alpha-Beta Pruning Agent는 Minmax 알고리즘과 매우 유사하지만, lower bound와 upper bound를 이용하여 검색을 일찍 중단하는 차이가 있다. 같은 결과를 도출하면서 더 효율적인 탐색을 함

### 3. Expectimax Agent
Minimax Agent에서는 모든 유령이 optimal하게 움직인다는 가정하에서 점수가 최대가 되는 이동 경로를 선택했다. 
Expectimax Agent에서는 유령이 optimal하게 움직일 수도, 아닐 수도 있다는 가정하에서 유령의 경로 선택의 확률에 따른 점수의 기대값을 계산하여 이 값이 최대가 되는 이동 경로를 선택한다.

<img width="197" alt="Expecti" src="https://user-images.githubusercontent.com/91405382/197310555-3be34aaf-bc6c-4ee4-8b97-9ce6a04f4076.png">
위와 같은 state에서, depth가 2 이상인 minmax algorithm을 이용하면 pacman은 game을 이길 수 없다고 판단하여, 가장 적게 이동하고 패배하는 선택(오른쪽으로 이동)을 한다. 
<img width="411" alt="3" src="https://user-images.githubusercontent.com/91405382/197310631-5609bce8-cdfe-4a4b-a78d-ab3ed1c3ff8a.png">

Expectimax Agent는 ghost와 pacman의 이동에 따른 점수의 기댓값을 계산한다. 
팩맨이 오른쪽으로 이동하면 빨간색 유령에게 잡혀 무조건 게임에서 지게 된다.
하지만 왼쪽으로 이동하면 파란색 유령이 아래로 움직일 경우 게임에서 승리할 수 있다. 
따라서 팩맨은 위와 같은 상태에서 파란색 유령이 아래로 움직일 수도 있다는 기대를 가지고 왼쪽의 이동을 선택하게 된다.

```
python pacman.py -p ExpectimaxAgent -m stuckmap -a depth=3 -n 100 -q
```
<img width="450" alt="4" src="https://user-images.githubusercontent.com/91405382/197310748-a2df9bb9-f4a8-431a-9ccc-96ea9607270e.png">
