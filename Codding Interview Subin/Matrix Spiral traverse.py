import numpy as np
# def spiral_traverse(matrix):
#     direction = 0
#     left = 0
#     right = len(matrix[1])
#     top = 0
#     bottom = len(matrix)
#     linear = []
#     while  True:
#         if direction ==0: #Traverse from left to right
#             print(matrix[top][left:right])
#             linear.extend(matrix[top][left:right])
#             top = top+1
#         if direction ==1: # Traverse from top to bottom
#             print(matrix[top:bottom][right-1])
#             linear.extend(matrix[top:bottom][right-1])
#             right = right -1
#         if direction ==2: #Right to left
#             print(matrix[bottom][right:left:-1])
#             linear.extend(matrix[bottom-1][right:left:-1])
#             bottom = bottom -1
#         if direction ==3:
#             print(matrix[bottom:top:-1][left])
#             linear.extend(matrix[bottom:top:-1][left])
#             left = left +1
#
#         direction =(direction +1 ) %4

def spiral_traverse(matrix): #Burn in hell Python indexing and for loop in range
    direction = 0
    left = 0
    right = len(matrix[1])-1
    top = 0
    bottom = len(matrix)-1
    linear = []
    print((right +1)*(bottom +1))
    while top<=bottom and left <=right: # *** Breaking condition is very important in this scenerio
        if direction == 0:
            for i in range(left,right+1):
                linear.append(matrix[top][i])
            top = top +1
        if direction == 1:
            for i in range(top,bottom+1):
                linear.append(matrix[i][right])
            right = right - 1

        if direction == 2:
            for i in range(right,left-1,-1):
                linear.append(matrix[bottom][i])
            bottom = bottom -1
        if direction == 3:
            for i in range(bottom,top-1,-1):
                linear.append(matrix[i][left])
            left = left +1
        direction =(direction +1 ) %4
    print(linear)




matrix = np.random.randint(low=1,high=100,size=(40,50))
print(matrix)
print("output :")
spiral_traverse(matrix)