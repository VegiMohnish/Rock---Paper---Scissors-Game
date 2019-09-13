import math
import random

stone = "stone"
paper = "paper"
scissor = "scissor"

def print_choice():
	print("enter 1 to select stone: ")
	print("enter 2 to select paper: ")
	print("enter 3 to select scissor: ")

computer_count = 0
user_count = 0

choice = True
while(choice):
	#input1 = input("Press enter to play: ")
	print_choice()
	ch = int(input())
	c = random.choice([stone,paper,scissor])
	if ch==1:
		print("Computer choose ",c)
		if c == stone:
			print("tie")
			print("----Scores----")
			print("computer: ",computer_count)
			print("user: ",user_count)
		elif c == paper:
			print("computer wins")
			print("----Scores----")
			computer_count += 1
			print("computer: ",computer_count)
			print("user: ",user_count)
		elif c == scissor:
			print("user wins")
			print("----Scores----")
			user_count += 1
			print("computer: ",computer_count)
			print("user: ",user_count)
	elif ch==2:
		# c = random.choice([stone,paper,scissor])
		print("Computer choose ",c)
		if c == paper:
			print("tie")
			print("----Scores----")
			print("computer: ",computer_count)
			print("user: ",user_count)
		elif c == scissor:
			print("computer wins")
			print("----Scores----")
			computer_count += 1
			print("computer: ",computer_count)
			print("user: ",user_count)
		elif c == stone:
			print("user wins")
			print("----Scores----")
			user_count += 1
			print("computer: ",computer_count)
			print("user: ",user_count)
	elif ch==3:
		# c = random.choice([stone,paper,scissor])
		print("Computer choose ",c)
		if c == scissor:
			print("tie")
			print("----Scores----")
			print("computer: ",computer_count)
			print("user: ",user_count)
		elif c == stone:
			print("computer wins")
			print("----Scores----")
			computer_count += 1
			print("computer: ",computer_count)
			print("user: ",user_count)
		elif c == paper:
			print("user wins")
			print("----Scores----")
			user_count += 1
			print("computer: ",computer_count)
			print("user: ",user_count)
	else:
		print("please enter the valid input ")
	if (computer_count == 5 or user_count == 5):
		choice = False
		if (computer_count > user_count):
			print("---------------------------")
			print("Game Over!!")
			print("Final Scores")
			print("computer: ",computer_count)
			print("user: ",user_count)
			print("Computer wins the game!!")
		else:
			print("---------------------------")
			print("Game Over!!")
			print("Final Scores")
			print("computer: ",computer_count)
			print("user: ",user_count)
			print("User wins the game!!")
