

# from https://medium.com/swlh/fun-with-python-1-maze-generator-931639b4fb7e
# Maze generator -- Randomized Prim Algorithm

## Imports
import random
import time
from colorama import init
from colorama import Fore, Back, Style
import numpy as np
import random
import matplotlib.pyplot as plt

## Functions
def printMaze(maze):
	for i in range(0, height):
		for j in range(0, width):
			if (maze[i][j] == 'u'):
				print(Fore.WHITE + str(maze[i][j]), end=" ")
			elif (maze[i][j] == 'c'):
				print(Fore.GREEN + str(maze[i][j]), end=" ")
			else:
				print(Fore.RED + str(maze[i][j]), end=" ")
			
		print('\n')

# Find number of surrounding cells
def surroundingCells(rand_wall):
	s_cells = 0
	if (maze[rand_wall[0]-1][rand_wall[1]] == 'c'):
		s_cells += 1
	if (maze[rand_wall[0]+1][rand_wall[1]] == 'c'):
		s_cells += 1
	if (maze[rand_wall[0]][rand_wall[1]-1] == 'c'):
		s_cells +=1
	if (maze[rand_wall[0]][rand_wall[1]+1] == 'c'):
		s_cells += 1

	return s_cells


## Main code
# Init variables
wall = 'w'
cell = 'c'
unvisited = 'u'
height = 11*2
width = 27*2
maze = []

# Initialize colorama
init()

# Denote all cells as unvisited
for i in range(0, height):
	line = []
	for j in range(0, width):
		line.append(unvisited)
	maze.append(line)

# Randomize starting point and set it a cell
starting_height = int(random.random()*height)
starting_width = int(random.random()*width)
if (starting_height == 0):
	starting_height += 1
if (starting_height == height-1):
	starting_height -= 1
if (starting_width == 0):
	starting_width += 1
if (starting_width == width-1):
	starting_width -= 1

# Mark it as cell and add surrounding walls to the list
maze[starting_height][starting_width] = cell
walls = []
walls.append([starting_height - 1, starting_width])
walls.append([starting_height, starting_width - 1])
walls.append([starting_height, starting_width + 1])
walls.append([starting_height + 1, starting_width])

# Denote walls in maze
maze[starting_height-1][starting_width] = 'w'
maze[starting_height][starting_width - 1] = 'w'
maze[starting_height][starting_width + 1] = 'w'
maze[starting_height + 1][starting_width] = 'w'

while (walls):
	# Pick a random wall
	rand_wall = walls[int(random.random()*len(walls))-1]

	# Check if it is a left wall
	if (rand_wall[1] != 0):
		if (maze[rand_wall[0]][rand_wall[1]-1] == 'u' and maze[rand_wall[0]][rand_wall[1]+1] == 'c'):
			# Find the number of surrounding cells
			s_cells = surroundingCells(rand_wall)

			if (s_cells < 2):
				# Denote the new path
				maze[rand_wall[0]][rand_wall[1]] = 'c'

				# Mark the new walls
				# Upper cell
				if (rand_wall[0] != 0):
					if (maze[rand_wall[0]-1][rand_wall[1]] != 'c'):
						maze[rand_wall[0]-1][rand_wall[1]] = 'w'
					if ([rand_wall[0]-1, rand_wall[1]] not in walls):
						walls.append([rand_wall[0]-1, rand_wall[1]])


				# Bottom cell
				if (rand_wall[0] != height-1):
					if (maze[rand_wall[0]+1][rand_wall[1]] != 'c'):
						maze[rand_wall[0]+1][rand_wall[1]] = 'w'
					if ([rand_wall[0]+1, rand_wall[1]] not in walls):
						walls.append([rand_wall[0]+1, rand_wall[1]])

				# Leftmost cell
				if (rand_wall[1] != 0):	
					if (maze[rand_wall[0]][rand_wall[1]-1] != 'c'):
						maze[rand_wall[0]][rand_wall[1]-1] = 'w'
					if ([rand_wall[0], rand_wall[1]-1] not in walls):
						walls.append([rand_wall[0], rand_wall[1]-1])
			

			# Delete wall
			for wall in walls:
				if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
					walls.remove(wall)

			continue

	# Check if it is an upper wall
	if (rand_wall[0] != 0):
		if (maze[rand_wall[0]-1][rand_wall[1]] == 'u' and maze[rand_wall[0]+1][rand_wall[1]] == 'c'):

			s_cells = surroundingCells(rand_wall)
			if (s_cells < 2):
				# Denote the new path
				maze[rand_wall[0]][rand_wall[1]] = 'c'

				# Mark the new walls
				# Upper cell
				if (rand_wall[0] != 0):
					if (maze[rand_wall[0]-1][rand_wall[1]] != 'c'):
						maze[rand_wall[0]-1][rand_wall[1]] = 'w'
					if ([rand_wall[0]-1, rand_wall[1]] not in walls):
						walls.append([rand_wall[0]-1, rand_wall[1]])

				# Leftmost cell
				if (rand_wall[1] != 0):
					if (maze[rand_wall[0]][rand_wall[1]-1] != 'c'):
						maze[rand_wall[0]][rand_wall[1]-1] = 'w'
					if ([rand_wall[0], rand_wall[1]-1] not in walls):
						walls.append([rand_wall[0], rand_wall[1]-1])

				# Rightmost cell
				if (rand_wall[1] != width-1):
					if (maze[rand_wall[0]][rand_wall[1]+1] != 'c'):
						maze[rand_wall[0]][rand_wall[1]+1] = 'w'
					if ([rand_wall[0], rand_wall[1]+1] not in walls):
						walls.append([rand_wall[0], rand_wall[1]+1])

			# Delete wall
			for wall in walls:
				if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
					walls.remove(wall)

			continue

	# Check the bottom wall
	if (rand_wall[0] != height-1):
		if (maze[rand_wall[0]+1][rand_wall[1]] == 'u' and maze[rand_wall[0]-1][rand_wall[1]] == 'c'):

			s_cells = surroundingCells(rand_wall)
			if (s_cells < 2):
				# Denote the new path
				maze[rand_wall[0]][rand_wall[1]] = 'c'

				# Mark the new walls
				if (rand_wall[0] != height-1):
					if (maze[rand_wall[0]+1][rand_wall[1]] != 'c'):
						maze[rand_wall[0]+1][rand_wall[1]] = 'w'
					if ([rand_wall[0]+1, rand_wall[1]] not in walls):
						walls.append([rand_wall[0]+1, rand_wall[1]])
				if (rand_wall[1] != 0):
					if (maze[rand_wall[0]][rand_wall[1]-1] != 'c'):
						maze[rand_wall[0]][rand_wall[1]-1] = 'w'
					if ([rand_wall[0], rand_wall[1]-1] not in walls):
						walls.append([rand_wall[0], rand_wall[1]-1])
				if (rand_wall[1] != width-1):
					if (maze[rand_wall[0]][rand_wall[1]+1] != 'c'):
						maze[rand_wall[0]][rand_wall[1]+1] = 'w'
					if ([rand_wall[0], rand_wall[1]+1] not in walls):
						walls.append([rand_wall[0], rand_wall[1]+1])

			# Delete wall
			for wall in walls:
				if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
					walls.remove(wall)


			continue

	# Check the right wall
	if (rand_wall[1] != width-1):
		if (maze[rand_wall[0]][rand_wall[1]+1] == 'u' and maze[rand_wall[0]][rand_wall[1]-1] == 'c'):

			s_cells = surroundingCells(rand_wall)
			if (s_cells < 2):
				# Denote the new path
				maze[rand_wall[0]][rand_wall[1]] = 'c'

				# Mark the new walls
				if (rand_wall[1] != width-1):
					if (maze[rand_wall[0]][rand_wall[1]+1] != 'c'):
						maze[rand_wall[0]][rand_wall[1]+1] = 'w'
					if ([rand_wall[0], rand_wall[1]+1] not in walls):
						walls.append([rand_wall[0], rand_wall[1]+1])
				if (rand_wall[0] != height-1):
					if (maze[rand_wall[0]+1][rand_wall[1]] != 'c'):
						maze[rand_wall[0]+1][rand_wall[1]] = 'w'
					if ([rand_wall[0]+1, rand_wall[1]] not in walls):
						walls.append([rand_wall[0]+1, rand_wall[1]])
				if (rand_wall[0] != 0):	
					if (maze[rand_wall[0]-1][rand_wall[1]] != 'c'):
						maze[rand_wall[0]-1][rand_wall[1]] = 'w'
					if ([rand_wall[0]-1, rand_wall[1]] not in walls):
						walls.append([rand_wall[0]-1, rand_wall[1]])

			# Delete wall
			for wall in walls:
				if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
					walls.remove(wall)

			continue

	# Delete the wall from the list anyway
	for wall in walls:
		if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
			walls.remove(wall)
	


# Mark the remaining unvisited cells as walls
for i in range(0, height):
	for j in range(0, width):
		if (maze[i][j] == 'u'):
			maze[i][j] = 'w'

# Set entrance and exit
for i in range(0, width):
	if (maze[1][i] == 'c'):
		maze[0][i] = 'c'
		break

for i in range(width-1, 0, -1):
	if (maze[height-2][i] == 'c'):
		maze[height-1][i] = 'c'
		break

# Print final maze
printMaze(maze)

##########################################

global droite
droite=0
global haut
haut=1
global gauche
gauche=2
global bas
bas=3

def QLearning(Q,alpha,state,chosen_action,lambda_):
	
	target = lambda_*max(Q[deplacement(state,chosen_action)])-Q[state][chosen_action]
	#print(Q[deplacement(state,chosen_action)])
	Q[state][chosen_action] = Q[state][chosen_action] + alpha * target
	#print(Q[state][chosen_action])
	return Q

	
def epsilon_greedy_policy(Q,epsilon,choixpossible,state):
	randomAction= np.random.choice((0,1),p=[epsilon,(1-epsilon)])
	choix=-1
	if (randomAction== 0):
		if(len(choixpossible)>1):
			choix=choixpossible[random.randint(0,len(choixpossible)-1)]
		else : 
			choix = choixpossible[0]
		#print("random action")
		#print(choix)
		
	else :
		valmax=0
		indice=0
		listechoix=[]
		
		for i in Q[state]:
		
			if (i>=valmax and (indice in choixpossible)):
				valmax=i
				listechoix.append(indice)
			indice+=1
		
		if (len(listechoix)>1):
			choix = listechoix[random.randint(0,len(listechoix)-1)]
		else :
			choix = listechoix[0]
		
	return choix
	
def choixPossible(position,maze):
	choix_possible=[]
	
	#print(position)
	
	if(position[0]>0 and position[0]<height-1 and maze[position[0]][position[1]+1]=='c'):
		choix_possible.append(droite)
		#print(maze[position[0]][position[1]+1])
		#print("droite possible")
	
	if(position[1]>0 and position[1]<width-1 and maze[position[0]-1][position[1]]=='c'):
		choix_possible.append(haut)
		#print(maze[position[0]-1][position[1]])
		#print("haut possible")
		
	if(position[0]>0 and position[0]<height-1 and maze[position[0]][position[1]-1]=='c'):
		choix_possible.append(gauche)
		#print(maze[position[0]][position[1]-1])
		#print("gauche possible")
		
	if(position[1]>0 and position[1]<width-1 and maze[position[0]+1][position[1]]=='c'):
		choix_possible.append(bas)
		#print(maze[position[0]+1][position[1]])
		#print("bas possible")
		
	if (len(choix_possible)==0):
		print("erreur choix possible")
		
	return choix_possible
	


def deplacement(position,direction):
	if (direction == droite):
		#print("je me déplace vers la droite")
		return (position[0],position[1]+1)
	if (direction == haut):
		#print("je me déplace vers le haut")
		return (position[0]-1,position[1])	
	if (direction == gauche):
		#print("je me déplace vers la gauche")
		return (position[0],position[1]-1)	
	if (direction == bas):
		#print("je me déplace vers le bas")
		return (position[0]+1,position[1])
	else:
		print("error direction")
		return
		
def showShortRoute(memTraj,indice,depart):
	p1=[depart[0]+1,depart[1]]
	for i in range(0,height):
		for j in range(0,width):
			if maze[i][j]=='w':
				plt.plot(j,height - i,markerfacecolor="red",marker="s",markersize=8)

	x,y=[height -depart[0],height -p1[0]], [depart[1],p1[1]]
	plt.plot(y,x)
	for i in range (1,len(memTraj[indice])):
		p2 = deplacement(p1,memTraj[indice][i])
		x,y=[height -p1[0],height -p2[0]], [p1[1],p2[1]]
		plt.plot(y,x)
		p1=p2
	plt.show
			

prctMurSup=0.5
count=0
listeMur=[]

gradient={}

for i in range(1,height-2):
	for j in range(1,width-2):
		if maze[i][j]=='w':
			count+=1
			listeMur.append([i,j])
			
print(count)
for i in range(0,int(prctMurSup*count)):
	suppr=random.choice(listeMur)
	maze[suppr[0]][suppr[1]]='c'
	listeMur.remove(suppr)
printMaze(maze)

#initialisation du gradient
for i in range(0,height-1):
	for j in range(0,width-1):
		if maze[i][j]=='c':
			#[droite,haut,gauche,bas]
			gradient[(i,j)]=[0,0,0,0]
			

#recuperation des coord de départ et d'arrivee
for i in range(0, width):
	if (maze[0][i] == 'c'):
		depart=(0,i)
		gradient[depart]=[0,0,0,0]
		break

for i in range(width-1, 0, -1):
	if (maze[height-1][i] == 'c'):
		arrivee=(height-1,i)
		gradient[arrivee]=[1,1,1,1]
		break

lambda_=0.7 # poids de la reward de l'étape suivante
alpha=0.7 # poids de l'ajout à la reward actuel
pourcEpsilon = 0.75 # pourcentage de décroissance de epsilon
epsilon= 1
CompteurDepl=0
traceBackDepl=[]
tourActuel = 0
compteurTour = 200
position = depart
memTrajTemp=[]
memTraj=[]
#print(gradient)
while (tourActuel< compteurTour):
	
	choixpossible = choixPossible(position,maze)
	#print(choixpossible)
	
	chosen_action = epsilon_greedy_policy(gradient,epsilon,choixpossible,position)
	#print(chosen_action)
	memTrajTemp.append(chosen_action)
	gradient = QLearning(gradient,alpha,position,chosen_action,lambda_)
	position = deplacement(position,chosen_action)
	CompteurDepl+=1
	if(position == arrivee):
		memTraj.append(memTrajTemp)
		memTrajTemp=[]
		epsilon *= pourcEpsilon
		tourActuel +=1
		position = depart
		traceBackDepl.append(CompteurDepl)
		CompteurDepl=0
	
#print(gradient)
#print("il y a eu " + str(compteur) + " tours")
#print(traceBackDepl)
plt.plot([i for i in range(0,compteurTour)],traceBackDepl)
plt.title('Nombre de déplacements')
plt.figure()
indice = traceBackDepl.index(min(traceBackDepl))
#print(indice)
#print(memTraj[indice])
#print(depart)
print("trajet le plus court = "+ str(min(traceBackDepl)))
showShortRoute(memTraj,indice,depart)
plt.show()





