from util import manhattanDistance
from game import Directions
import random, util

from game import Agent
import math

## Example Agent
class ReflexAgent(Agent):

  def Action(self, gameState):

    move_candidate = gameState.getLegalActions()

    scores = [self.reflex_agent_evaluationFunc(gameState, action) for action in move_candidate]
    bestScore = max(scores)
    Index = [index for index in range(len(scores)) if scores[index] == bestScore]
    get_index = random.choice(Index)

    return move_candidate[get_index]

  def reflex_agent_evaluationFunc(self, currentGameState, action):

    successorGameState = currentGameState.generatePacmanSuccessor(action)
    newPos = successorGameState.getPacmanPosition()
    oldFood = currentGameState.getFood()
    newGhostStates = successorGameState.getGhostStates()
    newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

    return successorGameState.getScore()



def scoreEvalFunc(currentGameState):

  return currentGameState.getScore()

class AdversialSearchAgent(Agent):

  def __init__(self, getFunc ='scoreEvalFunc', depth ='2'):
    self.index = 0
    self.evaluationFunction = util.lookup(getFunc, globals())

    self.depth = int(depth)

######################################################################################

class MinimaxAgent(AdversialSearchAgent):
  """
    [문제 01] MiniMax의 Action을 구현하시오. (20점)
    (depth와 evaluation function은 위에서 정의한 self.depth and self.evaluationFunction을 사용할 것.)
  """
  def Action(self, gameState):
    ####################### Write Your Code Here ################################
    def minmax(self, gameState):
        action_pac = None
        action_ghost = None
        score, move = Max_Score(self, gameState, action_pac, action_ghost, 0, 0)
        
        return move
    
    
    def Max_Score(self, gameState, action_pac, action_ghost, index, depth):
        if depth == self.depth: #지정한 depth만큼 움직였다면 평가함수 return      
            return self.evaluationFunction(gameState), action_pac           
        if gameState.isWin() or gameState.isLose(): #게임의 승,패가 결정되었다면 평가함수 return
            return self.evaluationFunction(gameState), action_pac   
        
        score = -math.inf
        move_candidate = gameState.getLegalActions() #pacman의 이동가능 경로(act)
        for act in move_candidate:
            successorGameState = gameState.generatePacmanSuccessor(act) # pacman이 이동한 상태의 gameState
      
            s2, a2 = Min_Score(self, successorGameState, act, action_ghost, index + 1, depth) # s2: 1번 ghost의 이동에 따른 최소 score
            if s2 > score: # score: s2의 최대값
                arr = []
                score = s2
                move = act
                arr.append([s2, act])
            elif s2 == score: 
                arr.append([s2, act])
        if len(arr) > 1: # 최대값이 2개 이상일 경우 random하게 선택
            rand_choice = random.choice(arr)
            score = rand_choice[0]
            move = rand_choice[1]
        return score, move # 점수가 최대가 되는 이동경로 return
    
    
    def Min_Score(self, gameState, action_pac, action_ghost, index, depth):
        if gameState.isWin() or gameState.isLose():
            return self.evaluationFunction(gameState), action_pac            

        score = math.inf
        move_candidate = gameState.getLegalActions(index) #ghost의 이동가능 경로(act)
        for act in move_candidate:
            successorGameState = gameState.generateSuccessor(index, act) # ghost가 이동한 상태의 gameState

            if index == gameState.getNumAgents() - 1: 
                #모든 agent가 움직이면 depth 1 증가시키고 그 때의 gameState에서 Max_Score 함수 다시 실행
                s2, a2 = Max_Score(self, successorGameState, action_pac, act, 0, depth+1)
            else: # s2: 다음 ghost의 이동에 따른 최소 score
                s2, a2 = Min_Score(self, successorGameState, action_pac, act, index+1, depth)

            if s2 < score: # score: s2의 최소값
                score = s2
                move = act   
        
        return score, action_pac #점수의 최소값 return
    
    return minmax(self, gameState)
    raise Exception("Not implemented yet")

    ############################################################################




class AlphaBetaAgent(AdversialSearchAgent):
  """
    [문제 02] AlphaBeta의 Action을 구현하시오. (25점)
    (depth와 evaluation function은 위에서 정의한 self.depth and self.evaluationFunction을 사용할 것.)
  """
  def Action(self, gameState):
    ####################### Write Your Code Here ################################
    def minmax(self, gameState):
        action_pac = None
        action_ghost = None
        score, move = Max_Score(self, gameState, action_pac, action_ghost, 0, 0, -math.inf, math.inf)
        
        return move
    
    
    def Max_Score(self, gameState, action_pac, action_ghost, index, depth, alpha, beta):
        if depth == self.depth:            
            return self.evaluationFunction(gameState), action_pac   
                        
        if gameState.isWin() or gameState.isLose():
            return self.evaluationFunction(gameState), action_pac   
        
        score = -math.inf        
        move_candidate = gameState.getLegalActions()
        for act in move_candidate:
            successorGameState = gameState.generatePacmanSuccessor(act)

            s2, a2 = Min_Score(self, successorGameState, act, action_ghost, index + 1, depth, alpha, beta)
            if s2 > score:
                arr = []
                score = s2
                move = act
                if score > beta: # upper bound 범위를 벗어날 경우 검색 중단
                    break
                arr.append([s2, act])
                alpha = max(alpha, score) # 알파 값 갱신
            elif s2 == score:
                arr.append([s2, act])

        if len(arr) > 1:
            rand_choice = random.choice(arr)
            score = rand_choice[0]
            move = rand_choice[1]
        return score, move
    
    
    def Min_Score(self, gameState, action_pac, action_ghost, index, depth, alpha, beta):
        if gameState.isWin() or gameState.isLose():
            return self.evaluationFunction(gameState), action_pac            
        
        score = math.inf
        move_candidate = gameState.getLegalActions(index) 
        for act in move_candidate:
            successorGameState = gameState.generateSuccessor(index, act)

            if index == gameState.getNumAgents() - 1:
                s2, a2 = Max_Score(self, successorGameState, action_pac, act, 0, depth+1, alpha, beta)
            else:
                s2, a2 = Min_Score(self, successorGameState, action_pac, act, index+1, depth, alpha, beta)

            if s2 < score:
                score = s2
                move = act   
                if score < alpha: # lower bound 범위를 벗어날 경우 검색 중단
                    break
                beta = min(beta, score) #베타값 갱신
        return score, action_pac
    
    
    return minmax(self, gameState)
    raise Exception("Not implemented yet")

    ############################################################################



class ExpectimaxAgent(AdversialSearchAgent):
  """
    [문제 03] Expectimax의 Action을 구현하시오. (25점)
    (depth와 evaluation function은 위에서 정의한 self.depth and self.evaluationFunction을 사용할 것.)
  """
  def Action(self, gameState):
    ####################### Write Your Code Here ################################
    def expectimax(self, gameState):
        action_pac = None
        action_ghost = None
        score, move = Max_Score(self, gameState, action_pac, action_ghost, 0, 0)
        return move
    
    
    def Max_Score(self, gameState, action_pac, action_ghost, index, depth):
        if depth == self.depth:            
            return self.evaluationFunction(gameState), action_pac   
                        
        if gameState.isWin() or gameState.isLose():
            return self.evaluationFunction(gameState), action_pac   
    
        score = -math.inf
        
        move_candidate = gameState.getLegalActions()
        for act in move_candidate:    
            successorGameState = gameState.generatePacmanSuccessor(act)
            s2, a2 = Expect_Score(self, successorGameState, act, action_ghost, index + 1, depth)    
            
            if s2 > score:
                arr = []
                score = s2
                move = act
                arr.append([s2, act])
            elif s2 == score:
                arr.append([s2, act])
        if len(arr) > 1:
            rand_choice = random.choice(arr)
            score = rand_choice[0]
            move = rand_choice[1]
        return score, move            
            
        
    def Expect_Score(self, gameState, action_pac, action_ghost, index, depth):
        if gameState.isWin() or gameState.isLose():
            return self.evaluationFunction(gameState), action_pac            
        
        score = 0
        move_candidate = gameState.getLegalActions(index) 
        for act in move_candidate:
            successorGameState = gameState.generateSuccessor(index, act)

            if index == gameState.getNumAgents() - 1:
                s2, a2 = Max_Score(self, successorGameState, action_pac, act, 0, depth+1)
            else:
                s2, a2 = Expect_Score(self, successorGameState, action_pac, act, index+1, depth)           
            score += s2
        expectation = score / len(move_candidate) #각 이동경로를 선택할 확률은 같으므로 기대값은 평균이 됨
        return expectation, action_pac #기대값 return
    
    
    return expectimax(self, gameState)
    raise Exception("Not implemented yet")

    ############################################################################
