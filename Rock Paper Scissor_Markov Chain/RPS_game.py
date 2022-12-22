# DO NOT MODIFY THIS FILE

import random


def play(player1, player2, num_games, verbose=False):
    p1_prev_play = ""
    p2_prev_play = ""
    results = {"p1": 0, "p2": 0, "tie": 0}

    for _ in range(num_games):
        p1_play = player1(p2_prev_play)
        p2_play = player2(p1_prev_play)

        if p1_play == p2_play:
            results["tie"] += 1
            winner = "Tie."
        elif (p1_play == "P" and p2_play == "R") or (
                p1_play == "R" and p2_play == "S") or (p1_play == "S"
                                                       and p2_play == "P"):
            results["p1"] += 1
            winner = "Player 1 wins."
        elif p2_play == "P" and p1_play == "R" or p2_play == "R" and p1_play == "S" or p2_play == "S" and p1_play == "P":
            results["p2"] += 1
            winner = "Player 2 wins."

        if verbose:
            print("Player 1:", p1_play, "| Player 2:", p2_play)
            print(winner)
            print()

        p1_prev_play = p1_play
        p2_prev_play = p2_play

    games_won = results['p2'] + results['p1']

    if games_won == 0:
        win_rate = 0
    else:
        win_rate = results['p1'] / games_won * 100

    print("Final results:", results)
    print(f"Player 1 win rate: {win_rate}%")

    return (win_rate)


def quincy(prev_play, counter=[0]):

    counter[0] += 1
    choices = ["R", "R", "P", "P", "S"]
    print(counter[0])
    return choices[counter[0] % len(choices)]


def mrugesh(prev_opponent_play, opponent_history=[]):
    opponent_history.append(prev_opponent_play)
    last_ten = opponent_history[-10:]
    most_frequent = max(set(last_ten), key=last_ten.count)

    if most_frequent == '':
        most_frequent = "S"

    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    return ideal_response[most_frequent]


def kris(prev_opponent_play):
    if prev_opponent_play == '':
        prev_opponent_play = "R"
    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    return ideal_response[prev_opponent_play]


def abbey(prev_opponent_play,
          opponent_history=[],
          play_order=[{
              "RRR": 0,
              "RRP": 0,
              "RRS": 0,
              "RPR": 0,
              "RPP": 0,
              "RPS": 0,
              "RSR": 0,
              "RSP": 0,
              "RSS": 0,
              "PRR": 0,
              "PRP": 0,
              "PRS": 0,
              "PPR": 0,
              "PPP": 0,
              "PPS": 0,
              "PSR": 0,
              "PSP": 0,
              "PSS": 0,
              "SRR": 0,
              "SRP": 0,
              "SRS": 0,
              "SPR": 0,
              "SPP": 0,
              "SPS": 0,
              "SSR": 0,
              "SSP": 0,
              "SSS": 0,
          }]):

    if not prev_opponent_play:
        prev_opponent_play = 'R'
    opponent_history.append(prev_opponent_play)

    last_three = "".join(opponent_history[-3:])
    if len(last_three) ==3:
        play_order[0][last_three] += 1


    tmp="".join(opponent_history[-2:0])
    potential_plays = [
        "".join(opponent_history[-2:]) + "R",
        "".join(opponent_history[-2:]) + "P",
        "".join(opponent_history[-2:]) + "S",
    ]
    ##print(potential_plays)
    sub_order = {
        k: play_order[0][k]
        for k in potential_plays if k in play_order[0]
    }
  
    if len(potential_plays[0]) >2:
      prediction = max(sub_order, key=sub_order.get)[-1:]
    
    else: prediction = 'P'
    #    print(potential_plays)
    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    return ideal_response[prediction]


def human(prev_opponent_play):
    play = ""
    while play not in ['R', 'P', 'S']:
        play = input("[R]ock, [P]aper, [S]cissors? ")
        print(play)
    return play


def random_player(prev_opponent_play):
    return random.choice(['R', 'P', 'S'])
