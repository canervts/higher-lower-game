from game_data import data
import random
from art import logo, vs
from replit import clear

def get_random_account():
  """Get data from random account"""
  return random.choice(data)

def format_text(text):
  name = text["name"]
  description = text["description"]
  country = text["country"]
  return f"{name}, a {description}, from {country}"

def answer_check(answer,text_a,text_b):
#  print(f"{answer}")
  follower_a = int(text_a["follower_count"])
#  print(f"{follower_a}")
  follower_b = int(text_b["follower_count"])
#  print(f"{follower_b}")
  if follower_a > follower_b and answer =="a":
    return True
  elif follower_b > follower_a and answer =="b":
    return True
  else :
    return False




print(logo)

score=0
game_should_continue = True
account_a = get_random_account()
account_b = get_random_account()

while game_should_continue:
  account_a = account_b
  account_b = get_random_account()

  while account_a == account_b:
    account_b = get_random_account()
  
  print(f"Compare A: {format_text(account_a)}")
  print(vs)
  print(f"Against B: {format_text(account_b)}")

  answer = input("Who has more followers? Type 'A' or 'B': ").lower()
  is_correct = answer_check(answer,account_a,account_b)
  #print(is_correct)
  clear()
  print(logo)
  if is_correct:
    score += 1
    print(f"You're right! Current score: {score}.")
  else:
    game_should_continue = False
    print(f"Sorry, that's wrong. Final score: {score}")