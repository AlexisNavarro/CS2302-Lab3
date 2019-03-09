# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 07:44:41 2019

@author: Alexis Navarro
CS 2302 
Lab #3
Purpose:The purpose of this code is to allow me to learn the different way Binary search trees can be used by either making one from a list, taking the values from the tree and transfering them to  list
        , Obtaining the values at a certain depth, and searching for a value in my Binary Search Tree.
"""
import numpy as np
import matplotlib.pyplot as plt


class BST(object):
    # Constructor
    def __init__(self, item, left=None, right=None):  
        self.item = item
        self.left = left 
        self.right = right  

def IsEmpty(L):  
    return L.head == None   

def Append(L,x): 
    # Inserts x at end of list L
    if IsEmpty(L):
        L.head = Node(x)
        L.tail = L.head
    else:
        L.tail.next = Node(x)
        L.tail = L.tail.next
        
def Insert(T,newItem):
    if T == None:
        T =  BST(newItem)
    elif T.item > newItem:
        T.left = Insert(T.left,newItem)
    else:
        T.right = Insert(T.right,newItem)
    return T


        
def Smallest(T):
    t= T
    while t.left is not None:
        t=t.left
    return t

def SmallestREC(T):
    if T.left is None:
        return T
    return SmallestREC(T.left)

def LargestREC(T):
    if T.right is None:
        return T
    else:
        return LargestREC(T.right)
    
def Find(T,k):
    if T is None or T.item == k:
        return T
    
    if T.item < k:
        return Find(T.right,k)
    
    return Find(T.left, k)

            
#------------------------------------------------------------------------------
#Method to draw my Binary Search Tree
#Requires the Use of draw Triangle to function properly

    
def draw_Triangle(ax,n,p,w):# this method makes a triangle shape that is used by the tree method; also this method is modified by the squares method from lab 1
    if n>0:
        i1 = [1,0]#modified this to create the shape of a triangle
        q = p*w + p[i1]*(1-w)
        ax.plot(p[:,0],p[:,1],color='k')
        draw_Triangle(ax,n-1,q,w)
        
plt.close("all") 
orig_size = 1000
fig, ax = plt.subplots()
ax.set_aspect(1.0)
ax.axis('on')
plt.show()
fig.savefig('Triangle.png')

#The method to create trees was modified from lab 1 , beacause I was having issues creating the circles in my trees and transfering the values from a sorted tree to the drawing.
def drawTrees(Tree, x,y, xMove,yMove):
    if Tree is not None:
        plt.text(x-.4,y+yMove,Tree.item, bbox={"boxstyle":"circle","facecolor":"white"}) # this lets me create the circles, place them in a correct position on my BST, and allows me to input the values of my tree in its designated parts.
        
        if Tree.left is not None: # here we traverse through our Tree and we insert the values that go to the left while drawing the left side of the tree
            q=np.array([[x-xMove , y], [x, y +yMove]])#split both sides of the tree which saves a lot of time
            
            draw_Triangle(ax,1,q,.9)# call this method to draw our triangles
            
            drawTrees(Tree.left, x-xMove, y-yMove,xMove/2,yMove)# Recursive call the method to finish creating the figure by going down the tree and dividing how much in the X Axis the figures should move
            
        if Tree.right is not None:# here we traverse through our Tree and we insert the values that go to the right while drawing the right side of the tree
            q1=np.array([[x , y+yMove], [x + xMove, y]])
        
            draw_Triangle(ax,1,q1,.9)
                
            drawTrees(Tree.right,  x+xMove, y-yMove,xMove/2,yMove)
    
        



#------------------------------------------------------------------------------
# Methods that were used to draw a BST tree that was used until I was able to draw the figure for a BST           
def InOrder(T):
    if T is not None:
        InOrder(T.left)
        print(T.item, end = ' ' )
        InOrder(T.right)
        
def InOrderD(T,space):
    if T is not None:
        InOrderD(T.right, space+'  ')
        print(space, T.item)
        InOrderD(T.left,space+'  ')
        

    
    
#------------------------------------------------------------------------------   
#Iterative Search method 
def Search(T,k):
    temp = T
    while True:
        #print (temp.item)
        if temp.item == k :
            print('found the value', temp.item)
            return temp
        elif temp.item<k:
            temp = temp.right
        elif temp.item>k:
            temp=temp.left
        
#------------------------------------------------------------------------------    
#Method to create a sorted tree , BUT NOT TO DRAW THE FIGURE
def build_SortedTree(L):
    
    if len(L)<0:
        return None
    
    elif len(L)>0:
        middle = len(L)//2
        
        root = BST(L[middle]) # the root is declared to the middle value of our list 
        
        root.left = build_SortedTree(L[:middle]) # we are able to make root.left by calling the method recursively and storing the variables from the starting position of the list to the middle
        root.right = build_SortedTree(L[middle+1:])# root.right is the same as root.left however it stores all the variables beginning at the value after the middle till it reaches the end of the list 
    
        return root
#------------------------------------------------------------------------------ 
#method to convert the Binary Search Tree to a List
def BST_ToList(Tree, L):
    if Tree is None:
        return None
    else:
        BST_ToList(Tree.left,L)
        E.append(Tree.item)# uses the append method to insert the values of the tree to the end of the empty list
        BST_ToList(Tree.right, L)
    return E
 
    
#------------------------------------------------------------------------------ 
#method to find the elements at a specific depth and when found it prints the items in that depth
def Elem_AtDepth(Tree,k):
    if Tree is None:
        return None
    if k==0:
        print(Tree.item)
    else:
        Elem_AtDepth(Tree.left,k-1)
        Elem_AtDepth(Tree.right,k-1)
    

#------------------------------------------------------------------------------    
#MAIN
        
T = None
A = [10,4,2,8,1,3,5,9,7,15,12,18]
for a in A:
    T = Insert(T,a)
    
    
plt.close("all")         
fig, ax = plt.subplots()
#drawTrees(T,10,10,10,10) # uncomment or comment to see one Binary tree, since only one can be seen at a time
ax.set_aspect(1.0)
ax.axis('on')
plt.show()
fig.savefig('Trees.png')



#InOrderD(T,'')
Search(T, 8) # calls the method to find a value in the Binary Search Tree


#------------------------------------------

L = [1,2,3,4,5,6,7]
E=[]                    #Empty list that will be used to transfer the BST values to a list

Binary_Tree = build_SortedTree(L)
#InOrderD(Binary_Tree,'')
#drawTrees(Binary_Tree,10,10,10,10)  # uncomment or comment to see one Binary tree, since only one can be seen at a time

print(BST_ToList(Binary_Tree, E))# calls the method to convert the Binary search tree to a list

Elem_AtDepth(Binary_Tree,1)#calls the method to print the elements at a depth in the binary tree that was previously made

