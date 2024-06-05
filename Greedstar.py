import time
import math
#import console
import random
import os

def empty_map(rows,columns,empty_arr):
	for i in range(rows):
		empty_arr.append([0]*columns)
			
	return  empty_arr

def symbol_display(arr):
	h=''
	for i in arr:
		for j in i:
			
			if j == 0:
				h = h + '⬜️'
			if j == 1:
				h = h +  '🟫'
			if j == 5:
				h = h +  '🟧'
			if j == 6:
				h = h +  '🟦'
			if j == 7:
				h = h +  '🟩'
			if j == 8:
				h = h +  '🟥'
		h = h + '\n'
	print(h)

def random_direction(arr,y,x,visited):
	w = len(arr[0])
	h = len(arr)
	#direction vectors in array
	#[up,right,down,left]
	x_vectors = [0,-1,0,1]
	y_vectors = [-1,0,1,0]
	
	#possible future values of X and Y depening on position
	possible_Xs = []
	possible_Ys = []
	#original X and Y
	og_x = x
	og_y = y
	for i in range(len(x_vectors)):
		y = og_y + y_vectors[i]
		x = og_x + x_vectors[i]
		if x >= w or x < 0 or y >= h or y < 0:
			continue
		else:
			#0 is the blank tile
			#Adding it to the Possble Array means it will be filled
			if arr[y][x] == 0:
				
				possible_Xs.append(x)
				possible_Ys.append(y)
	#by making the choice zero or the array lenght its possible to make the walker stick to walls
	choice = 0
	if len(possible_Xs) > 0:
		choice = random.randint(0,len(possible_Xs) - 1)
		#choice = 0
	else:
		if len(visited) != 0:
			coords = visited.pop(0)
			return random_direction(arr,coords[0],coords[1],visited)
		
		
		 
	return possible_Ys[choice],possible_Xs[choice]
	
def random_walk(arr,y,x,steps):
	visited = []
	arr[y][x] = 1
	symbol_display(arr)
	while steps != 0:
		
		y,x = random_direction(arr,y,x,visited)
		visited.append([y,x])
		steps = steps - 1
		arr[y][x] = 1
		
		#console.clear()
		os.system('cls')
		symbol_display(arr)
		time.sleep(.07)
		#symbol_display(arr)

def dist_form(x1,y1,x2,y2):
	Xs = math.pow((x2 - x1),2)
	Ys = math.pow((y2 - y1),2)
	return int((Xs + Ys))

def Star_A(arr,start_x,start_y,goal_x,goal_y):
	#[N,NE,E,SE,S,SW,W]
	#possible directions
	#8 direction
	#x_vectors = [0,1,-1,1,0,-1,1,-1]
	#y_vectors = [-1,-1,0,1,1,1,0,-1]
	#[N,E,S,W]
	#4 direction
	x_vectors = [0,-1,0,1]
	y_vectors = [-1,0,1,0]

	
	w = len(arr[0])
	h = len(arr)
	
	compound_g_cost = 0
	
	root = str(start_x) + str(start_y)
	near_dict = {root:[]}
	
	#keeps track pf all visited nodes
	
	open_list = [[start_x,start_y]]
	
	#set of nodes already evaluated
	closed_list = []
	
	initial_g_cost = 0
	initial_h_cost = dist_form(start_x,start_y,goal_x,goal_y)
	initial_f_cost = initial_g_cost + initial_h_cost
	
	
	all_g_cost = [initial_g_cost]
	all_f_cost = [initial_f_cost]
	
	
	
	
	
	
	
	#initial index of the arrays
	ind = 0
	
	
	
	
	
	
	visited_color = 6
	traceback_color = 5
	goal_color = 8
	start_color = 7
	wall_color = 1
	
	#if the 
	while open_list:
		#arrays that keep track of each cells variables 
		#change each iteration 
		
		temp_g_cost_ls = []
		lowest_f_cost = 100000000
		lowest_g_cost = 0
		
		#open to closed migration
		
		#print(all_g_cost)
		
				
		current = open_list.pop(ind)
		all_f_cost.pop(ind)
		all_g_cost.pop(ind)
		
		
		cur_x = current[0]
		cur_y = current[1]
		cur_name = str(cur_x) + str(cur_y)
		
		closed_list.append(current)
	
		#print(lowest_f_cost)
		for i in range(len(x_vectors)):
		
			y = cur_y + y_vectors[i]
			x = cur_x + x_vectors[i]
			
			h_cost = dist_form(x,y,goal_x,goal_y)
				
			#if using 4 vectors
			g_cost = 10
			
			#if using 8 vectors
			#if i % 2 == 0:
				#g_cost = 10
			#else:
				#g_cost = 14
				
			g_cost += compound_g_cost
		
			f_cost = h_cost + g_cost
			
			#with this it only points back towards it's parent which would be the visited color 
			#the root node would be []
			#it relies on visited color
			if x < w and x >= 0 and y < h and y >= 0 and arr[y][x] != wall_color and arr[y][x] == visited_color:
				
				if near_dict.get(cur_name) == None:
					near_dict.update({cur_name:[x,y]})
				else:
					near_dict.update({cur_name:[x,y]})
			
			if x >= w or x < 0 or y >= h or y < 0 or arr[y][x] == wall_color or [x,y] in closed_list:
				
				continue
				
			else: 
				
				
				
				if [x,y] not in open_list:
					open_list.append([x,y])
					all_f_cost.append(f_cost)
					all_g_cost.append(g_cost)
				
		if [goal_x,goal_y] == [cur_x,cur_y]:
			print('path found')
			break
		
					
		if not all_f_cost:
			print('no path')
			break
		#print(open_list)
		lowest_f_cost = min(all_f_cost)
		ind = all_f_cost.index(lowest_f_cost)
		arr[cur_y][cur_x] = visited_color
		#compound_g_cost += all_g_cost[ind]
		
		
		
		#animation
		
		
		time.sleep(.07)
		os.system('cls')
		#console.clear()
		symbol_display(arr)
		
		
		
	
			
		
		
	########################%
	if cur_x == goal_x and cur_y == goal_y:
	
		coord = str(cur_x) + str(cur_y)
		
		while near_dict[coord] != []:
		
			
			
			XYs = near_dict[coord]
		
			#break
		
			arr[XYs[1]][XYs[0]] = traceback_color
			
			#animation
			time.sleep(.07)
			os.system('cls')
			#console.clear()
			symbol_display(arr)
			
			cur_x = XYs[0]
			cur_y = XYs[1]
			coord = str(cur_x) + str(cur_y)
			#print(coord)
			
		
		
		
	
	#console.clear()
 
	os.system('cls')
	arr[start_y][start_x] = start_color
	#arr[goal_y][goal_x] = goal_color
	symbol_display(arr)	
			
		

			
		
		
	
grida = [
	[0,0,1,0,0,0,0,0,0],
	[1,0,1,1,0,1,1,0,1],
	[0,0,0,1,0,0,1,0,0],
	[0,1,0,1,0,1,1,0,1],
	[0,1,0,1,0,1,0,0,0],
	[0,1,1,1,0,1,1,1,1],
	[0,1,0,0,0,0,0,0,0],
	[0,1,0,1,1,1,1,1,1],
	[0,0,0,0,0,0,0,1,0],
	]

	
gridl = [
	[0,0,0,0,0,0,0,0,0,0,0],
	[1,1,1,1,1,0,1,1,1,1,1],
	[0,0,0,0,0,0,0,0,0,0,0],
	[1,1,1,1,1,1,1,1,1,0,1],
	[0,0,0,0,0,0,0,0,0,0,0],
	[1,0,1,1,1,1,1,1,1,1,1],
	[0,0,0,0,0,0,0,0,0,0,0],
	[0,0,1,0,0,0,0,0,0,0,0],
	[0,1,1,1,1,1,1,1,1,1,1],
	[0,0,0,0,0,0,0,0,0,0,0]
	
	]
	
gridi = [
	[0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0]
	]
	
gridm = [
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	[0,1,1,1,1,1,1,1,1,1,1,1,1,0,1],
	[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
	]
	
grid = empty_map(19,19,[])	
ry = random.randint(0,len(grid) - 1)
rx = random.randint(0,len(grid[0]) - 1)
random_walk(grid,ry,rx,60)
	

start_x = 0
start_y = 0
end_x = len(grid[0]) - 1
end_y = len(grid) - 1

grid[start_y][start_x] = 7
grid[end_y][end_x] = 8
symbol_display(grid)
Star_A(grid,start_x,start_y,end_x,end_y)
