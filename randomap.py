import random
import time 
#for pythonista
#import console
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
			if j == 2:
    				h = h +  '🟦'
			if j == 3:
    				h = h +  '⬛'
			
		h = h + '\n'
	print(h)

class walker:
	def __init__(self,arr,x,y,steps,x_vect,y_vect):
		self.arr = arr
		self.visited = []
		self.xv = x_vect
		self.yv = y_vect
		self.steps = steps
		self.x = x
		self.y = y
		
	
	def __str__(self):
		return str(self.x) + str(self.y)
		
	
	def random_direction(self,arr,y,x,visited):
		w = len(arr[0])
		h = len(arr)
		#direction vectors in array
		#[up,right,down,left]
		x_vectors = self.xv
		y_vectors = self.yv
		
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
			if len(self.visited) != 0:
				coords = self.visited.pop(0)
				return self.random_direction(arr,coords[0],coords[1],visited)
			
			
		#print(possible_Xs,possible_Ys)
		return possible_Ys[choice],possible_Xs[choice]
	def random_step(self):
		
		self.arr[self.y][self.x] = 1
		if self.steps > 0:
			self.y,self.x = self.random_direction(self.arr,self.y,self.x,self.visited)
			self.visited.append([self.y,self.x])
			self.steps = self.steps - 1
			self.arr[self.y][self.x] = 1
	
 
	def update_arr(self,arr):
		self.arr = arr
	
    
	
	def tick(self):
		self.random_step()
		
			

def place_entrance_exit(arr):
    occupied = []
    w = len(arr[0])
    h = len(arr)
    #[up,right,down,left]
    xv = [0,-1,0,1]
    yv = [-1,0,1,0]
    for y in range(1,len(arr) - 2):
        for x in range(1,len(arr[0]) - 2):
            cur = arr[y][x]
            north = arr[y + yv[0]][x+ xv[0]]
            northwest = arr[y + yv[0]][x+ xv[3]]
            northeast =  arr[y + yv[1]][x+ xv[0]]
            south =  arr[y + yv[2]][x + xv[2]]
            southwest = arr[y + yv[2]][x + xv[3]]
            southeast =  arr[y + yv[1]][x + xv[2]]
            west = arr[y + yv[3]][x + xv[3]]
            east = arr[y + yv[1]][x + xv[1]]
            if cur == 1 and north == 1 and northeast == 1 and northwest == 1 and south == 1 and southeast == 1 and southwest == 1 and west == 1 and east == 1:
                occupied.append([y,x])
    #print(occupied)
    start = random.choice(occupied)
    occupied.remove(start)
    arr[start[0]][start[1]] = 2
    end = random.choice(occupied)
    arr[end[0]][end[1]] = 3

def marathon():
	arr = empty_map(40,50,[])	
	
	runners = []
	#[up,right,down,left]
	x_vectors = [0,-1,0,1]
	y_vectors = [-1,0,1,0]
	up_bias_x = [0,0,0,-1,-1,0,1,1]
	up_bias_y = [-1,-1,-1,0,0,1,0,0]
	
	runner_num = 1
	steps = 6
	ry = random.randint(len(arr)//4,len(arr) - 1 - len(arr)//4)
	rx = random.randint(len(arr)//4,len(arr[0]) - 1 - len(arr[0])//4)
	#ry = random.randint(runner_num,len(arr) - 1 - runner_num)
	#rx = random.randint(runner_num,len(arr[0]) - 1 - runner_num)
	for i in range(runner_num):
		
		dot = walker(arr,rx + 1,ry,steps,x_vectors,y_vectors)
		runners.append(dot)
	for i in range(steps):
		for j in runners:
			
			j.tick()
			j.update_arr(arr)
		#console.clear()
		#os.system('cls')
		#symbol_display(arr)
		#time.sleep(.1)
  
	#for i in arr:
	#	print(i)
	print('done')
	#place_entrance_exit(arr)
	symbol_display(arr)