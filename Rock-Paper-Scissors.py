import random
import shutil
from sys import exit
columns, rows = shutil.get_terminal_size()
print('Welcome to'. center(columns))
print('Stone Paper Scissors Game'.upper().center(columns))
print('''
RULES:-
   Rock wins over Scissors
   Scissors win over Paper
   Paper wins over Rock
  ''')
x = True 
try:
	t = int(input('Enter Number of Turns:- '))
	
except ValueError:
	print('Wrong Input. :-(\n PLEASE RESTART')
	exit()
countc=0 #computer score
countp=0 #player score
for i in range(0,t):
	print('''
 CHOICES:-
  A for Stone
  B for Paper
  C for Scissors
  ''')
	a = random.randrange(1,3)
	u = str(input('\nEnter Your Choice:- ')).upper()
	p=0
	c=0
	if u in 'ABC':
		if a==1:
			comp='Rock'
			if u=='B':
				countp+=1
				p+=1
			if u=='C':
				countc+=1
				c+=1
		if a==2:
			comp='Paper'
			if u=='A':
				countc+=1
				c+=1
			if u=='C':
				countp+=1
				p+=1
		if a==3:
			comp='Scissors'
			if u=='A':
				countp+=1
				p+=1
			if u=='B':
				countc+=1
				c+=1

		print("Computer's Choice: ", comp,'\n')
		print('Your Score: ', countp)
		print("Computer's Score: ", countc,'\n')
		if c>p:
			print('ROUND WINNER:- Computer'.center(columns))
			print('\n')
		elif p>c:
			print('ROUND WINNER:- Player'.center(columns))
			print('\n')
		else:
			print('ROUND Tie'.center(columns))
			print('\n')
	
	else:
		x = False
		print('Wrong Choice. :-(\n GAME TERMINATED\n PLEASE RESTART')
		break

if t!=0:	
	if x==True:
		if countp<countc:
			print('COMPUTER WINS THE GAME!!'.center(columns))
		elif countp>countc:
			print('PLAYER WINS THE GAME!!'.center(columns))
		else:
			print('GAME TIE'.center(columns))
