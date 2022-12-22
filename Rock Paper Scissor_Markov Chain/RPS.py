# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.
myList= {}

def player(prev_play, opponent_history=[]):
    if prev_play in ['R','S','P']:
        opponent_history.append(prev_play)
    
    guess = "P"
    depth = 9
    if len(opponent_history)>depth:
      tmp = ''.join(opponent_history[-depth:])
      if ''.join(opponent_history[-(depth+1):]) in myList.keys():
        myList[''.join(opponent_history[-(depth+1):])]+=1
      else:
        myList[''.join(opponent_history[-(depth+1):])] = 1

      doable = [tmp+'P', tmp+'S', tmp+'R']
      for i in doable:
        if not i in myList.keys():
          myList[i]=0
      predictions = max(doable, key=lambda key:myList[key])

      if predictions[-1] == 'R':
        guess = 'P'
      elif predictions[-1] == 'P':
        guess = 'S'
      elif predictions[-1] == 'S':
        guess = 'R'

    return guess




















"""

myList = {}

def player(prev_play, opponent_history=[]):
    if prev_play in ['R','P','S']:
      opponent_history.append(prev_play)

    guess = "R"

    depth=8
    if len(opponent_history)>depth:
      tem=''.join(opponent_history[-depth:])
      if ''.join(opponent_history[-(depth+1):]) in myList.keys():
        myList[''.join(opponent_history[-(depth+1):])] +=1
      else: 
        myList[''.join(opponent_history[-(depth+1):])]=1

      doable=[tem + 'R', tem + 'P', tem + 'S']

      for i in doable:
        if not i in myList.keys():
          myList[i]=0
      predictions = max(doable, key=lambda key: myList[key])

      if predictions[-1] == 'P':
        guess = 'S'
      elif predictions[-1] == 'R':
        guess = 'P'
      elif predictions[-1] == 'S':
        guess= 'R'


    return guess

"""
