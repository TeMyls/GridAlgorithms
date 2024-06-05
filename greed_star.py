import time
import math
#import console
import os

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
	


def dist_form(x1,y1,x2,y2):
	Xs = math.pow((x2 - x1),2)
	Ys = math.pow((y2 - y1),2)
	return int((Xs + Ys))
	#return int(round(math.sqrt(Xs + Ys),0))
	
def AstarR(arr,cx,cy,gx,gy,og_cost,visited,all_gcost,pathdict):
	#the bad part about this implementation is that infinite loops happen if no path is found
	#[N,NE,E,SE,S,SW,W]
	#possible directions
	#x_vectors = [0,1,-1,1,0,-1,1,-1]
	#y_vectors = [-1,-1,0,1,1,1,0,-1]
	#[N,E,S,W]
	
	x_vectors = [0,-1,0,1]
	y_vectors = [-1,0,1,0]
	
	
	og_x = cx
	og_y = cy
	
	w = len(arr[0])
	h = len(arr)
	
	xy_ls = []
	f_cost_ls = []
	g_cost_ls = []
	
	
	
		
	if og_x == gx and og_y == gy:
		
		#os.system('cls')
		arr[og_y][og_x] = 8
		symbol_display(arr)
		curcoord = str(og_y) + str(og_x)
		while pathdict[curcoord]:
			coords = pathdict[curcoord]
			curcoord = str(coords[1]) + str(coords[0])
			arr[coords[1]][coords[0]] = 5
			
			time.sleep(.1)
			#console.clear()
			symbol_display(arr)
			#os.system('cls')
			
		#print(pathdict)
		
		
		#symbol_display(arr)
		
		
		return
		
	for i in range(len(x_vectors)):
		
		y = og_y + y_vectors[i]
		x = og_x + x_vectors[i]
		if x >= w or x < 0 or y >= h or y < 0 or arr[y][x] == 1 or [x,y] in visited:
			continue
		else: 
			
			h_cost = dist_form(x,y,gx,gy)
			#if using 4 vectors
			g_cost = 10
			#using 8 vectors
			
			#if i % 2 == 0:
				#g_cost = 10
			#else:
				#g_cost = 14
				
			g_cost += og_cost
			f_cost = h_cost + g_cost
			
			xy_ls.append([x,y])
			g_cost_ls.append(g_cost)
			f_cost_ls.append(f_cost)
			
	
	
	
	# if fcost list is empty non of the surrounding cells are viable, as there either walls or cells already visited
	if f_cost_ls:
	#no dead end
		lil = min(f_cost_ls)
	
		#many = f_cost_ls.count(min)
		ind = f_cost_ls.index(lil)
		visited.append([xy_ls[ind][0],xy_ls[ind][1]])
		all_gcost.append(g_cost_ls[ind])
		
		eks = xy_ls[ind][0]
		why = xy_ls[ind][1]
	
		arr[why][eks] = 6
		
		time.sleep(.1)
		#os.system('cls')
		#console.clear()
		symbol_display(arr)
		after = str(why) + str(eks)
	
		#the next cell in the grid points towrds the previous one in the form of a dictionary that key is the cell after the current one and value is 
		#once the goal is reached a traceback will begin
		
		if pathdict.get(after) == None:
			current = [cx,cy]
			pathdict.update({after:current})
			
		
		AstarR(arr,eks,why,gx,gy,g_cost_ls[ind],visited,all_gcost,pathdict)
	else:
	#reached dead end?
		xy_arr = visited.pop(1)
		eks = xy_arr[0]
		why = xy_arr[1]
		arr[why][eks] = 7
		new_g = all_gcost.pop(1)
		
		
		#print(pathdict)
		AstarR(arr,eks,why,gx,gy,new_g,visited,all_gcost,pathdict)
	
def AstarI(arr,start_x,start_y,goal_x,goal_y):
	#the bad part about this implementation is that infinite loops happen if no path is found
	#[N,NE,E,SE,S,SW,W]
	#possible directions
	#x_vectors = [0,1,-1,1,0,-1,1,-1]
	#y_vectors = [-1,-1,0,1,1,1,0,-1]
	#[N,E,S,W]
	
	x_vectors = [0,-1,0,1]
	y_vectors = [-1,0,1,0]
	
	
	cur_x = start_x
	cur_y = start_y
	
	w = len(arr[0])
	h = len(arr)
	
	og_cost = 0
	
	#this dictionary documents child:parent pairs
	#in the form of strings representing the literal coordinates within the 2d array
	#this is done in order to traceback the shortest possible path from the goal node to the start node
	dir_dict = {}
	root = str(start_x) + str(start_y)
	
	dir_dict.update({root:None})
	#goal node
	target_child = str(goal_x) + str(goal_y)
	#keeps track pf all visited nodes
	visited = [[start_x,start_y]]
	all_gcost = [0]
	
	visited_color = 6
	traceback_color = 5
	goal_color = 8
	start_color = 7
	wall_color = 1
	
	#if the 
	while dir_dict.get(target_child) == None:
		#arrays that keep track of each cells variables 
		#change each iteration 
		xy_ls = []
		f_cost_ls = []
		g_cost_ls = []
		if cur_x == goal_x and cur_y == goal_y:
			
			break
			
			
		for i in range(len(x_vectors)):
		
			y = cur_y + y_vectors[i]
			x = cur_x + x_vectors[i]
			if x >= w or x < 0 or y >= h or y < 0 or arr[y][x] == wall_color or [x,y] in visited:
				continue
			else: 
				
				h_cost = dist_form(x,y,goal_x,goal_y)
				#if using 4 vectors
				g_cost = 10
				#using 8 vectors
				
				#if i % 2 == 0:
					#g_cost = 10
				#else:
					#g_cost = 14
					
				g_cost += og_cost
				f_cost = h_cost + g_cost
				
				xy_ls.append([x,y])
				g_cost_ls.append(g_cost)
				f_cost_ls.append(f_cost)
	
		#print(xy_ls)
		#if the fcost list is empty non of the surrounding cells are viable, as there either walls or cells already visited
		if f_cost_ls:
		#no dead end
			lil = min(f_cost_ls)
		
			#many = f_cost_ls.count(min)
			ind = f_cost_ls.index(lil)
			visited.append([xy_ls[ind][0],xy_ls[ind][1]])
			all_gcost.append(g_cost_ls[ind])
			
			
			new_x = xy_ls[ind][0]
			new_y = xy_ls[ind][1]
		
			arr[new_y][new_x] = visited_color
			
			#animation
			time.sleep(.1)
			os.system('cls')
			#console.clear()
			symbol_display(arr)
			
			#linking nodes
			child = str(new_x) + str(new_y)
		
			#the next cell in the grid points towrds the previous one
			#once the goal is reached a traceback will begin
			
			if dir_dict.get(child) == None:
				parent = [cur_x,cur_y]
				dir_dict.update({child:parent})
				
			cur_x = new_x
			cur_y = new_y
			
			
		else:
		#reached dead end?
		#just grabbing a cell we've visited until we find a cell with a neighbor that isn't in visited
		#why pop 1 instead of 0?
		#the pointer is at the start would be deleted. 
		#which is essential to termination
		#instead of startcoords:None it would be startcoord:some random coordinate
			xy_arr = visited.pop(1)
			new_x = xy_arr[0]
			new_y = xy_arr[1]
			arr[new_y][new_x] = start_color
			og_cost = all_gcost.pop(1)
			
			cur_x = new_x
			cur_y = new_y

	#if the first wasn't an infinite loop current x and current y should be goal x and goal y'
	#and the root shoyld point to none
	curcoord = str(cur_x) + str(cur_y)
	while dir_dict[curcoord]:
		coords = dir_dict[curcoord]
		arr[coords[1]][coords[0]] = traceback_color
		
		#animation
		time.sleep(.1)
		os.system('cls')
		#console.clear()
		symbol_display(arr)
		curcoord = str(coords[0]) + str(coords[1])
		
		#print(dir_dict)
		
		
	#os.system('cls')
	#console.clear()
	arr[start_y][start_x] = start_color
	arr[goal_y][goal_y] = goal_color
	#print(visited)
	#print(target_child)
	#print(dir_dict)
	symbol_display(arr)
	
grid = [
	[0,0,0,0,0,0,0,0,0],
	[1,1,1,0,1,1,1,0,1],
	[0,0,0,0,1,0,0,0,0],
	[0,1,0,1,1,1,0,1,1],
	[0,1,0,0,0,1,0,0,0],
	[0,1,1,1,0,1,1,1,1],
	[0,1,0,0,0,0,0,0,0],
	[0,1,1,1,1,1,1,1,1],
	[0,0,0,0,0,0,0,0,0],
	]

	
grids = [
	[0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0,0,0]
	
	]
	
grid1 = [
	[0,0,0,0,0],
	[0,0,0,0,0],
	[0,0,0,0,0],
	[0,0,0,0,0],
	[0,0,0,0,0]
	]
	
open = []
closed = []
#[up,right,down,left]
#x_vectors = [0,-1,0,1]
#y_vectors = [-1,0,1,0]
#[up,right,down,left]
start_x = 0
start_y = 0
end_x = len(grid[0]) - 1
end_y = len(grid) - 1

grid[start_y][start_x] = 7
grid[end_y][end_x] = 8
visited = []
first = str(start_x) + str(start_y)
symbol_display(grid)
#AstarR(grid,start_x,start_y,end_x,end_y,0,visited,[0],{first:None})
AstarI(grid,start_x,start_y,end_x,end_y)
