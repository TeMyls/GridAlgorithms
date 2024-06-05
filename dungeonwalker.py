import random
import time 
#for pythonista
#import console
#outside of pythonista
import os


class walker:
	def __init__(self,arr,x,y,steps,x_vect,y_vect):
		self.arr = arr
		self.visited = []
		self.xv = x_vect
		self.yv = y_vect
		self.steps = steps
		self.x = x
		self.y = y
		self.last_dir = []

	
	def __str__(self):
		return str(self.x) + str(self.y)
		
	def terminate(self,arr,area,x,y):
		w = len(arr[0])
		h = len(arr)
		
		
		#[up,right,down,left]
		x_vectors = [0,-1,0,1]
		y_vectors = [-1,0,1,0]
		og_x = x
		og_y = y
		steps = 9
		total = 0
		arr[y][x] = 1
		spaces = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,11,11,12,12,13,13,14,14,15,15]
		for i in range(len(spaces)):
			j = 0
			curl = spaces[i]
			#this exist to make the area perfectly square or rectangle
			if i == steps - 1:
				curl -= 1
			
			if total < area:
				while j < curl:
					j += 1
					
					if i < len(x_vectors):
						y = y + y_vectors[i]
						x = x + x_vectors[i]
					else:
						y = y + y_vectors[i%len(x_vectors)]
						x = x + x_vectors[i%len(x_vectors)]
					if x >= w or x < 0 or y >= h or y < 0:
						continue
					else:
						arr[y][x] = 1
					
							
							
					#console.clear()
					#os.system('cls')
					#symbol_display(arr)
					#time.sleep(.1)
					#print(y,x,sep = ' ')
					
			else:
				continue
			total += spaces[i]	

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
			self.last_dir = [og_y - possible_Ys[choice],og_x - possible_Xs[choice]]
			#choice = 0
		else:
			if len(self.visited) != 0:
				coords = self.visited.pop(0)
				return self.random_direction(arr,coords[0],coords[1],visited)
			
		
		return possible_Ys[choice],possible_Xs[choice]
	def random_step(self):
		
		self.arr[self.y][self.x] = 1
		if self.steps > 0:
			self.y,self.x = self.random_direction(self.arr,self.y,self.x,self.visited)
			self.visited.append([self.y,self.x])
			self.steps = self.steps - 1
			self.arr[self.y][self.x] = 1
			#print(self.steps)
		if self.steps == 1:
			print('terminating')
			self.terminate(self.arr,9,self.x,self.y)
		
	
 
	def update_arr(self,arr):
		self.arr = arr
		
	
	def tick(self):
		self.random_step()
		
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
			if j == 4:
    				h = h +  '🟩'
			
		h = h + '\n'
	print(h)

def any_cells_left(arr,target):
    	
	tally = 0
	for i in arr:
		tally += i.count(target)
		
	
	#The goal os to get rid of all the empty spaces, or zeros
	print(tally)
	return tally > 0
	
def floodFill(image, sr, sc, color):
	w = len(image)
	h = len(image[0])
	replacing = image[sr][sc]
	print(replacing,color)
	kyu = []
	kyu.append((sr,sc))
	while kyu:
		
		cur = kyu.pop(0)
		
		if cur[0] >= w or cur[0] < 0 or cur[1] >= h or cur[1] < 0:
			continue
		else:
			if image[cur[0]][cur[1]] == color:
				continue
			elif image[cur[0]][cur[1]] == replacing:
				image[cur[0]][cur[1]] = color
				#print('y')
				if cur[0] + 1 < w and cur[0] + 1 >= 0:
					if image[cur[0] + 1][cur[1]] == replacing:
						#print('s')
						kyu.append((cur[0] + 1, cur[1]))
				if cur[0] - 1 < w and cur[0] - 1 >= 0:
					if image[cur[0] - 1][cur[1]] == replacing:
						#print('n')
						kyu.append((cur[0] - 1, cur[1]))
				if cur[1] + 1 < h and cur[1] + 1 >= 0:
					if image[cur[0]][cur[1] + 1] == replacing:
						#print('w')
						kyu.append((cur[0], cur[1] + 1))
				if cur[1] - 1 < h and cur[1] - 1>= 0:
					if image[cur[0]][cur[1] - 1] == replacing:
						#print('e')
						kyu.append((cur[0], cur[1] - 1))
	return image
		
def adjecent_cells(arr,x,y):
    xv = [0,-1,0,1]
    yv = [-1,0,1,0]
    w = len(arr)
    h = len(arr[0])
    north = arr[y + yv[0]][x+ xv[0]]
    northwest = arr[y + yv[0]][x+ xv[3]]
    northeast =  arr[y + yv[1]][x+ xv[0]]
    south =  arr[y + yv[2]][x + xv[2]]
    southwest = arr[y + yv[2]][x + xv[3]]
    southeast =  arr[y + yv[1]][x + xv[2]]
    west = arr[y + yv[3]][x + xv[3]]
    east = arr[y + yv[1]][x + xv[1]]
    	

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
    occupied.remove(end)
    return occupied
def place_key(arr,occupied):
   
    w = len(arr[0])
    h = len(arr)
    #[up,right,down,left]
    
    #print(occupied)
    key = random.choice(occupied)
    occupied.remove(key)
    arr[key[0]][key[1]] = 4
    return key

def marathon(rows,cols,peeps):
    arr = empty_map(rows,cols,[])	
	#[up,right,down,left]
    runners = []
    x_vectors = [0,-1,0,1]
    y_vectors = [-1,0,1,0]
 
    runner_num = peeps
    steps = 10
    for i in range(runner_num):
        ry = random.randint(len(arr)//2.5,len(arr) - 1 - len(arr)//2.5)
        rx = random.randint(len(arr)//2.5,len(arr[0]) - 1 - len(arr)//2.5)
        dot = walker(arr,rx,ry,steps,x_vectors,y_vectors)
        runners.append(dot)
    for i in range(steps):
        for j in runners:
			
            j.tick()
		#console.clear() 
        os.system('cls')
        symbol_display(arr)
        time.sleep(.15)
	
    floodFill(arr,runners[0].y,runners[0].x,2)
    #symbol_display(arr)
	#console.clear()
	
    
    if any_cells_left(arr,1):
        marathon(rows,cols,peeps)
    floodFill(arr,runners[0].y,runners[0].x,1)
	
    occupied = place_entrance_exit(arr)
    place_key(arr,occupied)
    symbol_display(arr)
    print('done')
		


def spiral(x,y,arr,area):
    w = len(arr[0])
    h = len(arr)
	
	
	#[up,right,down,left]
    x_vectors = [0,-1,0,1]
    y_vectors = [-1,0,1,0]
    og_x = x
    og_y = y
    steps = 9
    total = 0
    arr[y][x] = 1
    spaces = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,11,11,12,12,13,13,14,14,15,15]
    for i in range(len(spaces)):
        j = 0
        curl = spaces[i]
		#this exist to make the area perfectly square or rectangle
        if i == steps - 1:
            curl -= 1
        
        if total < area:
            while j < curl:
				
				
                if i < len(x_vectors):
                    y = y + y_vectors[i]
                    x = x + x_vectors[i]
                else:
                    y = y + y_vectors[i%len(x_vectors)]
                    x = x + x_vectors[i%len(x_vectors)]
                if x >= w or x < 0 or y >= h or y < 0:
                    continue
                else:
                    arr[y][x] = 1
				
						
						
				#console.clear()
                os.system('cls')
                symbol_display(arr)
                time.sleep(.1)
                print(y,x,sep = ' ')
                j += 1
        else:
            continue
        total += spaces[i]
			
ROWS = 29
COLS = 29
#arr = empty_map(ROWS,COLS,[])	

#spiral(10,9,arr,10)
marathon(ROWS,COLS,4)
