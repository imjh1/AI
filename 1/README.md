# CSE4185 Assignment01: Maze Game

## Implement:
BFS와 A * Algorithm을 활용한 최단 경로 찾기 

## Requirements:
```
pygame library (pip install pygame) 
```
## How to run the code:
The main file to run the maze game is maze_game.py:

```
usage: maze_game.py [-h] [--method {bfs,astar,astar_four_circles,astar_many_circles}] [--scale SCALE]
              [--speed speed] [--keyboard] [--save SAVE]
              filename
```

Examples of how to run maze_game.py:
```
python maze_game.py category/stage1/small.txt --method bfs
```
```
python maze_game.py category/stage1/small.txt --scale 30 --speed 10 --keyboard
```

For help run:
```
python maze_game.py -h
```
Help Output:
```
CSE4185 Assignment01: Maze Game

positional arguments:
  filename              path to maze file [REQUIRED]

optional arguments:
  -h, --help            show this help message and exit
  --method {bfs,astar,astar_four_circles,astar_many_circles}
                        search method - default bfs
  --scale SCALE         scale - default: 20
  --speed SPEED         speed for the display - default 15
  --keyboard            you can play the game - default False
  --save SAVE           save output to image file - default not saved
```

## Result
```
python maze_game.py --method bfs category/stage1/small.txt
```
<img width="247" alt="stage1_small_bfs" src="https://user-images.githubusercontent.com/91405382/197309591-fada0cdc-3468-4115-b9d8-c4b0090e7e1d.png">

```
python maze_game.py --method astar category/stage1/small.txt
```
<img width="232" alt="stage1_small_astar" src="https://user-images.githubusercontent.com/91405382/197309602-e911da6d-ee8b-4191-9ab0-6e5c11eff802.png">

```
python maze_game.py --method astar_four_circles category/stage2/small.txt
```
<img width="233" alt="stage2_small_astar_four_circles" src="https://user-images.githubusercontent.com/91405382/197309612-20e29e09-d684-4ec5-82d5-1c30e498cd45.png">

```
python maze_game.py --method astar_many_circles category/stage3/small.txt
```
<img width="232" alt="stage3_small_astar_many_circles" src="https://user-images.githubusercontent.com/91405382/197309616-e200cf15-fdb5-4267-92b9-c2c9d8bd8fd5.png">