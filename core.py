from copy import *
from numpy import *
from random import *
def main_loop(m):
    while still_alive(m)!="You Win!" and still_alive(m)!=False:
        for i in m:
            print i
        move = input('1=up,2=right,3=down,4=left, Enter your move:')
        m=next_map(m,move)[0]
    
#########################################################
# This function is used to flatten a complex list       #
#########################################################
def flatten(map):
	m=[]
	for i in map:
		if type(i)!=int:
			k=flatten(i)
			for j in k:
				m.append(j)
		else:
			m.append(i)
	return m
	
def init():
    m=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
    m=produce_block(m)
    m=produce_block(m)
    return m

def produce_block(game_map):
	m=deepcopy(game_map)
	m_flatten=array(flatten(m))
	m_zero_pos = where(m_flatten==0)[0]
	if size(m_zero_pos)>0:
		pos = m_zero_pos[int(random()*size(m_zero_pos))]
		pos_i = int(pos/4)
		pos_j = pos % 4
		temp=random()
		m[pos_i][pos_j]=2*(temp>0.1)+4*(temp<=0.1)
		return m
	else:
		return m
		
#########################################################
# This function is used to calculate what the 		#
# map will be like after moved to the i direction.	#
# Here i=1,2,3,4 means up, right, down, left 		#
# respectively.						#
#########################################################
def next_map(map,direction):
	moves=[]
	m=deepcopy(map)
	for i in m:
		i.append(100)
	m.append([100,100,100,100,100]) #m is 5*5
	if (1==direction): #up
		for i in range(1,4):
			for j in range(0,4):
				temp=i-1
				if (0!=m[i][j]):
					while (0==m[temp][j]) and (temp>-1):  ## find map[temp][j]>0 inside the map
						temp=temp-1
					if (-1==temp): #all the blocks on top are empty
						temp=0
						m[temp][j]=m[i][j]
						m[i][j]=0
					else: #map[temp][j]>0
						if (m[temp][j]==m[i][j]): #merge the two blocks
							m[temp][j]=m[temp][j]*2
							m[i][j]=0
						else:  ## can not merge
							if temp+1 != i: # move!						
								temp = temp+1
								m[temp][j]=m[i][j] #move the block
								m[i][j]=0
							else:
								temp = temp+1
					if (temp,j)!=(i,j):
						moves.append((i,j,temp,j))
	if (2==direction): #right
		for j in [2,1,0]:
			for i in range(0,4):
				temp=j+1
				if (0!=m[i][j]):
					while (0==m[i][temp]) and (temp<4):  ## find map[i][temp]>0 inside the map
						temp=temp+1
					if (4==temp): #all the blocks on the right are empty
						temp=3
						m[i][temp]=m[i][j]
						m[i][j]=0
					else: #map[i][temp]>0
						if (m[i][temp]==m[i][j]): #merge the two blocks
							m[i][temp]=m[i][temp]*2
							m[i][j]=0
						else:  ## can not merge
							if temp-1 != j: # move!						
								temp = temp-1
								m[i][temp]=m[i][j] #move the block
								m[i][j]=0
							else:
								temp = temp-1
					if (i,temp)!=(i,j):
						moves.append((i,j,i,temp))
	if (3==direction): #down
		for i in [2,1,0]:
			for j in range(0,4):
				temp=i+1
				if (0!=m[i][j]):
					while (0==m[temp][j]) and (temp<4):  ## find map[temp][j]>0 inside the map
						temp=temp+1
					if (4==temp): #all the blocks at downside are empty
						temp=3
						m[temp][j]=m[i][j]
						m[i][j]=0
					else: #map[temp][j]>0
						if (m[temp][j]==m[i][j]): #merge the two blocks
							m[temp][j]=m[temp][j]*2
							m[i][j]=0
						else:  ## can not merge
							if temp-1 != i: # move!						
								temp = temp-1
								m[temp][j]=m[i][j] #move the block
								m[i][j]=0
							else:
								temp = temp-1
					if (i,j)!=(temp,j):
						moves.append((i,j,temp,j))
	if (4==direction): #left
		for j in range(1,4):
			for i in range(0,4):
				temp=j-1
				if (0!=m[i][j]):
					while (0==m[i][temp]) and (temp>-1):  ## find map[i][temp]>0 inside the map
						temp=temp-1
					if (-1==temp): #all the blocks on the right are empty
						temp=0
						m[i][temp]=m[i][j]
						m[i][j]=0
					else: #map[i][temp]>0
						if (m[i][temp]==m[i][j]): #merge the two blocks
							m[i][temp]=m[i][temp]*2
							m[i][j]=0
						else:  ## can not merge
							if temp+1 != j: # move!						
								temp = temp+1
								m[i][temp]=m[i][j] #move the block
								m[i][j]=0
							else:
								temp=temp+1
					if (i,temp)!=(i,j):
						moves.append((i,j,i,temp))
	#All the moves are finished, now randomly produce a block
	m.remove([100,100,100,100,100])
	for i in m:
		i.remove(100)
	if m!=map:
		m=produce_block(m)
	return m,moves
	
def still_alive(map):
	m=flatten(map)
	if max(m)==2048:
		return "You Win!"
	elif next_map(map,1)[0]==next_map(map,2)[0]==next_map(map,3)[0]==next_map(map,4)[0]==map:
		return False
	else:
		return True

