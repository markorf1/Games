
import random

money = 100

#Write your game of chance functions here
def coin(guess, bet):
  result = random.randint(1, 2)

  if bet > money:
    print("""
    not enough money.
    bet less or go to sleep.""")
    return False
  elif bet <= 0:
    print("""
    bet positive""")
    return False
  else:
    if guess == "heads":
      print("""
    played coin:
you placed $""" + str(bet) + " on heads.")
    elif guess == "tails":
      print("""
    played coin:
you placed $""" + str(bet) + " on tails.")
    else:
      print("your guess is not valid. type 'heads' or 'tails'")
      return False

  if result == 1:
    print("the coin lands on heads!")
  else:
    print("the coin lands on tails!")

  if guess == "heads" and result == 1:
    print("win $" + str(bet) + """!
have $""" + str(money+bet) + "!")
    return bet
  elif guess == "heads" and not result == 1:
    print("lose $" + str(bet) + """.
have $""" + str(money-bet) + ".")
    return -bet
  elif guess == "tails" and result == 1:
    print("lose $" + str(bet) + """.
have $""" + str(money-bet) + ".")
    return -bet
  elif guess == "tails" and not result == 1:
    print("win $" + str(bet) + """!
have $""" + str(money+bet) + "!")
    return bet
  else:
    print("something's wrong")




def cho_han(guess, bet):
  dice1 = random.randint(1, 6)
  dice2 = random.randint(1, 6)

  if bet > money:
    print("""
    not enough money.
    bet less or go to sleep.""")
    return False
  elif bet <= 0:
    print("""
    bet positive""")
    return False
  else:
    if guess == "even":
      print("""
  played cho han:
you placed $""" + str(bet) + " on " + str(guess) + """.
the dice rolled """ + str(dice1) + " and " + str(dice2) + ", which sum up to " + str(dice1 + dice2) + ".")
    elif guess == "odd":
      print("""
  played cho han:
you placed $""" + str(bet) + " on " + str(guess) + """.
the dice rolled """ + str(dice1) + " and " + str(dice2) + ", which sum up to " + str(dice1 + dice2) + ".")
    else:
      print("your guess is not valid. type 'even' or 'odd'")
      return False

  if guess == "even" and (dice1 + dice2) % 2 == 0:
    print("win $" + str(bet) + """!
have $""" + str(money + bet) + "!")
    return bet
  elif guess == "even" and not (dice1 + dice2) % 2 == 0:
    print("lose $" + str(bet) + """.
have $""" + str(money - bet) + ".")
    return -bet
  elif guess == "odd" and (dice1 + dice2) % 2 == 0:
    print("lose $" + str(bet) + """.
have $""" + str(money - bet) + ".")
    return -bet
  elif guess == "odd" and not (dice1 + dice2) % 2 == 0:
    print("win $" + str(bet) + """!
have $""" + str(money + bet) + "!")
    return bet
  else:
    print("something's wrong")




def cards(bet):
  your_card = random.randint(1, 13)
  opponents_card = random.randint(1, 13)

  if bet > money:
    print("""
    not enough money.
    bet less or go to sleep.""")
    return False
  elif bet <= 0:
    print("""
    bet positive""")
    return False
  else:
    print("""
  played cards:
your bet is $""" + str(bet) + """.
your card's value is """ + str(your_card) + """.
the opponent's card's value is """ + str(opponents_card) + ".")
  if your_card > opponents_card:
    print("""your card is higher!
win $""" + str(bet) + """!
have $""" + str(money + bet) + "!")
    return bet
  elif your_card < opponents_card:
    print("""the opponent's card is higher...
lose $""" + str(bet) + """.
have $""" + str(money - bet) + ".")
    return -bet
  else:
    print("""it's a tie!
get none, lose none, have $""" + str(money) + " still...")
    return 0




def roulette(guess, bet):
  ball = random.randint(0,36)

  if bet > money:
    print("""
    not enough money.
    bet less or go to sleep.""")
    return False
  elif bet <= 0:
    print("""
    bet positive""")
    return False
  elif guess != "odd" or "even" or int:
    print("""
    your guess is not valid.
    type 'even', 'odd', or a number between 0 and 36""")
    return False
  else:
    print("""
  played roulette:
you placed $""" + str(bet) + " on " + str(guess) + """.
the ball lands on """ + str(ball) + ".")

  if guess == ball:
    print("""you win big time!
win $""" + str(bet * 34) + """!!!
have $""" + str(money + bet * 34) + "!!!")
    return bet * 34
  elif guess == "even" and ball % 2 == 0:
    print("win $" + str(bet) + """!
have $""" + str(money + bet) + "!")
    return bet
  elif guess == "even" and not ball % 2 == 0:
    print("lose $" + str(bet) + """.
have $""" + str(money - bet) + ".")
    return -bet
  elif guess == "odd" and ball % 2 == 0:
    print("lose $" + str(bet) + """.
have $""" + str(money - bet) + ".")
    return -bet
  elif guess == "odd" and not ball % 2 == 0:
    print("win $" + str(bet) + """!
have $""" + str(money + bet) + "!")
    return bet
  elif guess != ball:
    print("lose $" + str(bet) + """.
have $""" + str(money - bet) + ".")
    return -bet



#Call your game of chance functions here
money += coin("Heads", 20)
money += coin("tails", 35)
money += cho_han("even", 46)
money += cards(31)
money += roulette(0, -40)
money += roulette("Odd", 13)
