import random
import time 
#for pythonista
import console
#outside of pythonista
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
				h = h +  '🟥'
			
		h = h + '\n'
	print(h)


def paver(arr,rect):
	#paves individual rooms
	#x0,y1,w2,h3
	x = rect[0]
	y = rect[1]
	w = rect[2]
	h = rect[3]
	#print(x,y,w,h,sep='_')
	grid_w = len(arr[0]) - 1
	grid_h = len(arr) - 1
	for row in range(y,y+h):
		for col in range(x,x+w):
			#if col < grid_w and row < grid_h:
			arr[row][col] = 1
			'''
			if col == x or col == x + w - 1:
				arr[row][col] = 1
			elif row == y or row == y + h - 1:
				arr[row][col] = 1
			else:
				arr[row][col] = 0
			'''
			

def pathways(x,y,arr,sx,sy,ex,ey):
  #actual tunnels
	grid_w = len(arr[0]) - 1
	grid_h = len(arr) - 1
	for row in range(sy,ey + 1):
		for col in range(sx,ex + 1):
			
			#if col < grid_w and row < grid_h:
			if col == x:
				arr[row][col] = 1
		
			if row == y:
				arr[row][col] = 1
			
		
			
def tunnel_maker(arr,rooms):

	#x0,y1,w2,h3
	tunnels = []
	#these exist to limit the area searched in the array to build tunnels
	sx,ex,sy,ey = 0,0,0,0
	for i in range(len(rooms)-1):
		
		
		#centers of two rooms
		cx1 = (rooms[i][0] + rooms[i][0] + rooms[i][2])//2
		cy1 = (rooms[i][1] + rooms[i][1] + rooms[i][3])//2
		
		cx2 = (rooms[i+1][0] + rooms[i+1][0] + rooms[i+1][2])//2
		cy2 = (rooms[i+1][1] + rooms[i+1][1] + rooms[i+1][3])//2
		#decides whether the tunnel between two room will be top right or bottom left compared to the center of the rooms
		choice1 = random.random()
		#decides whether a third path will be added
		choice2 = random.random()
		#print(choice2)
		if choice1 > .5:
			#arr[cy2][cx1] = 2
			if cy2 <= cy1:
				sy = cy2
				ey = cy1
			if cy2 >= cy1:
				sy = cy1
				ey = cy2
			if cx2 <= cx1:
				sx = cx2
				ex = cx1
				
			if cx2 >= cx1:
				sx = cx1
				ex = cx2
			
			tunnels.append((cx1,cy2,sx,sy,ex,ey))
			#print('a')
		else:
			#arr[cy1][cx2] = 2
			if cy2 <= cy1:
				sy = cy2 
				ey = cy1 
			if cy2 >= cy1:
				sy = cy1 
				ey = cy2 
			if cx2 <= cx1:
				sx = cx2 
				ex = cx1 
				
			if cx2 >= cx1:
				sx = cx1 
				ex = cx2 
			#print('b')
			tunnels.append((cx2,cy1,sx,sy,ex,ey))
		
		if choice2 > .6:
			#temp exists so the same room isn't selected
			temp = rooms.copy()
			temp.pop(i + 1)
			temp.pop(i)
			rand = random.randint(0,len(temp) - 1 )
			cx1 = (temp[rand][0] + temp[rand][0] + temp[rand][2])//2
			cy1 = (temp[rand][1] + temp[rand][1] + temp[rand][3])//2
			
			cx2 = (rooms[i][0] + rooms[i][0] + rooms[i][2])//2
			cy2 = (rooms[i][1] + rooms[i][1] + rooms[i][3])//2
			if cy2 <= cy1:
				sy = cy2 
				ey = cy1 
			if cy2 >= cy1:
				sy = cy1 
				ey = cy2 
			if cx2 <= cx1:
				sx = cx2 
				ex = cx1 
				
			if cx2 >= cx1:
				sx = cx1 
				ex = cx2 
			#print('b')
			tunnels.append((cx2,cy1,sx,sy,ex,ey))
		
			
	
	for i in tunnels:
		pathways(i[0],i[1],arr,i[2],i[3],i[4],i[5])
		
				
		

	

def random_walk(arr,y,x,steps):
	w = len(arr[0])
	h = len(arr)
	#queue
	
	visited = []
	#[up,right,down,left]
	arr[y][x] = 1
	x_vector = [0,1,0,-1]
	y_vector = [-1,0,1,0]
	rand_dir = random.randint(0,len(x_vector) - 1)
	while steps != 0:
		y = y + y_vector[rand_dir]
		x = x + x_vector[rand_dir]
		
		
		if x >= w or x < 0 or y >= h or y < 0:
			y = y - y_vector[rand_dir]
			x = x - x_vector[rand_dir]
			
			x_vector.pop(rand_dir)
			y_vector.pop(rand_dir)
			
			new_rand_dir = random.randint(0,len(x_vector) - 1)
			
			y = y + y_vector[new_rand_dir]
			x = x + x_vector[new_rand_dir]
			
			
			
			arr[y][x] = 1
			steps = steps - 1
			
			x_vector = [0,1,0,-1]
			y_vector = [-1,0,1,0]
		else:
			arr[y][x] = 1
			steps = steps - 1
		rand_dir = random.randint(0,len(x_vector) - 1)
		console.clear()
		symbol_display(arr)
		time.sleep(.2)
		
		
		
	#symbol_display(arr)
	
			
			
			
arr = empty_map(16,19,[])	
random_walk(arr,15,18,20)
