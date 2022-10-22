# CSE4185 Assignment03: Logic

## Problems
1. Change sentences to Proposition Logic Formula
   - "If it's summer and we're in California, then it doesn't rain."
   - "It's wet if and only if it is raining or the sprinklers are on."
   - "Either it's day or night (but not both)."

2. Change, Create First-Order Logic Formula
   - "Every person has a mother."
   - "At least one person has no children."
   - Female(x)와 Child(x,y) 함수를 활용하여, Daughter를 정의한 formula를 생성
   - Female(x)와 Parent(x,y) 함수를 활용하여, Grandmother를 정의한 formula를 생성

3. Change sentences to First-Order Logic Formula to find criminal
   - John: "It wasn’t me!"
   - Susan: "It was Nicole!"
   - Mark: "No,it was Susan!"
   - Nicole: "Susan’s a liar."
   - Exactly one person is telling the truth
   - Exactly one person crashed the server.

4. Change Theorems to First_Order Logic Formula
   - 각각의 숫자 x에는 하나의 successor가 있으며, 이는 x와 같지 않다. 
   - 각각의 숫자는 홀수 혹은 짝수이며, 둘다인 경우는 없다.
   - 짝수의 successor는 홀수이다.
   - 홀수의 successor는 짝수이다.
   - 모든 숫자 x에 대해서, x의 successor는 x보다 크다.
   - x가 y보다 크고, y가 z보다 크면, x는 z보다 크다.


## Result
```
python formulas.py
```
<img width="890" alt="result" src="https://user-images.githubusercontent.com/91405382/197311458-9eb66cad-37a1-4a43-9ba7-338c6560aa00.png">