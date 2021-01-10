#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Read Instructions carefully before attemption this assignment

# 1) don't rename any function name
# 2) don't rename any variable name
# 3) don't remove any #comment 
# 4) don't remove """ under triple quate values """
# 5) you have to write code where you found "wrtie your code here"
# 6) after download rename this file with this format "PIAICCompletRollNumber_AssignmentNo.py"
#   Example piaic17896_Assignment1.py
# 7) After complete this assignment please push on your own github repository.
# 8) you can submit this assignment through google form
# 9) copy your this file absolute url then paste in google form
#  Example above: https://github.com/EnggQasim/Batch04_to_35/blob/main/Sunday/1_30%20to%203_30/Assignments/assignment1.txt

# * Because all assignment we will be cheked through software if you missed any above points 
# * then we can't assign your scores in our database.


# In[9]:


import numpy as np

# Task no 1
def function1():
    # create 2d array from 1,12 range 
    # dimension should be 6row 2 columns  
    # and assign this array values in x values in x variable
    # Hint: you can use arange and reshape numpy methods  
    x =  np.arange(1,13).reshape((6,2)) 

    return x
    """
    expected output:
    [[ 1  2]
    [ 3  4]
    [ 5  6]
    [ 7  8]
    [ 9 10]
    [11 12]]
    """
function1()


# In[18]:


# Task2
def function2():
    #create 3D array (3,3,3)
    #must data type should have float64
    #array value should be satart from 10 and end with 36 (both included)
    # Hint: dtype, reshape 
    
    #x = np.arange(1,28,dtype=np.float64).reshape((3,3,3))     wrtie your code here  
    x = np.arange(10,37,dtype=np.float64).reshape((3,3,3))
     
    

    return x
    """
    Expected: out put
array([[[10., 11., 12.],
        [13., 14., 15.],
        [16., 17., 18.]],

       [[19., 20., 21.],
        [22., 23., 24.],
        [25., 26., 27.]],

       [[28., 29., 30.],
        [31., 32., 33.],
        [34., 35., 36.]]])    
    """
function2()


# In[826]:


#task3
def function3():
    #extract those numbers from given array. those are must exist in 5,7 Table
    #example [35,70,105,..]
    a = np.arange(1, 100*10+1).reshape((100,10))
    x = a[np.logical_and(a%5==0,a%7==0)] #wrtie your code here
    return x
    """
    Expected Output:
     [35,  70, 105, 140, 175, 210, 245, 280, 315, 350, 385, 420, 455,
       490, 525, 560, 595, 630, 665, 700, 735, 770, 805, 840, 875, 910,
       945, 980] 
    """ 
function3()


# In[43]:



#task4
def function4():
#Swap columns 1 and 2 in the array arr.
   
arr = np.arange(9).reshape(3,3)
  
return arr[:,[1,0,2]] #wrtie your code here
"""
Expected Output:
      array([[1, 0, 2],
            [4, 3, 5],
            [7, 6, 8]])
""" 
function4() 


# In[878]:



#task5
def function5():
#Create a null vector of size 20 with 4 rows and 5 columns with numpy function
   
z =np.zeros((4,5)).astype('int') #wrtie your code here

return z
"""
Expected Output:
      array([[0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]])
""" 
function5()


# In[59]:


#task6
def function6():
    # Create a null vector of size 10 but the fifth and eighth value which is 10,20 respectively
   
    arr = np.zeros(10)  #wrtie your code here\
    arr[5]=10
    arr[8]=20
    return arr
function6()


# In[825]:



  
#task7
def function7():
  #  Create an array of zeros with the same shape and type as X. Dont use reshape method
  x = np.arange(4, dtype=np.int64)
    
  return  x*0
  """
  Expected Output:
        array([0, 0, 0, 0], dtype=int64)
  """
function7()


# In[879]:


#task8
def function8():
    # Create a new array of 2x5 uints, filled with 6.
     x = np.arange(10,dtype=np.uint32).reshape(2,5)           #write your code here
     x[0]=6 
     x[1]=6
     return x

     """
     Expected Output:
              array([[6, 6, 6, 6, 6],
                     [6, 6, 6, 6, 6]], dtype=uint32)
     """
function8()   


# In[690]:



#task9
def function9():
# Create an array of 2, 4, 6, 8, ..., 100.
a =np.arange(51).reshape((1,51))*2 # write your code here
a=np.delete(a,0)
return a

"""
 Expected Output:
          array([  2,   4,   6,   8,  10,  12,  14,  16,  18,  20,  22,  24,  26,
                28,  30,  32,  34,  36,  38,  40,  42,  44,  46,  48,  50,  52,
                54,  56,  58,  60,  62,  64,  66,  68,  70,  72,  74,  76,  78,
                80,  82,  84,  86,  88,  90,  92,  94,  96,  98, 100])
 """ 
function9()


# In[719]:



#task10
def function10():
 # Subtract the 1d array brr from the 2d array arr, such that each item of brr subtracts from respective row of arr.
 
 arr = np.array([[3,3,3],[4,4,4],[5,5,5]])
 brr = np.array([1,2,3])
 subt =np.subtract(arr,(np.vstack(brr)))      # write your code here 
  
 return subt

 """
  Expected Output:
            array([[2 2 2]
                   [2 2 2]
                   [2 2 2]])
 """ 
function10()    


# In[691]:




#task11
def function11():
# Replace all odd numbers in arr with -1 without changing arr.

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
ans = np.where(arr%2==1,-1,arr)
    #write your code here 
  
return ans

"""
 Expected Output:
          array([ 0, -1,  2, -1,  4, -1,  6, -1,  8, -1])
""" 
function11()


# In[622]:



#task12
def function12():
# Create the following pattern without hardcoding. Use only numpy functions and the below input array arr.
# HINT: use stacking concept

arr = np.array([1,2,3])
arr0=np.array([1,1,1,2,2,2,3,3,3,1,2,3,1,2,3])
ans =np.append(arr0,arr)                    #write your code here 
  
return ans

"""
 Expected Output:
          array([1, 1, 1, 2, 2, 2, 3, 3, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3])
 """
function12()    


# In[656]:


#task13
def function13():
    # Set a condition which gets all items between 5 and 10 from arr.
    
    
    arr = np.array([2, 6, 1, 9, 10, 3, 27])
    ans =arr[(arr < 10) & (arr  > 5)]  #write your code here 
  
    return ans

    """
     Expected Output:
              array([6, 9])
     """ 
function13()


# In[571]:


#task14
import numpy as np
def function14():
    # Create an 8X3 integer array from a range between 10 to 34 such that the difference between each element is 1 and then Split the array into four equal-sized sub-arrays.
    # Hint use split method
    
    
    arr = np.arange(10, 34, 1).reshape(8,3) #write reshape code
    ans = np.split(arr,4)                                                #write your code here 
  
    return ans

    """
     Expected Output:
       [array([[10, 11, 12],[13, 14, 15]]), 
        array([[16, 17, 18],[19, 20, 21]]), 
        array([[22, 23, 24],[25, 26, 27]]), 
        array([[28, 29, 30],[31, 32, 33]])]
     """
function14()


# In[599]:



#task15
def function15():
#Sort following NumPy array by the second column


arr = np.array([[ 8,  2, -2],[-4,  1,  7],[ 6,  3,  9]])
ans = arr[np.argsort(arr[:,1])]               #write your code here 
  
return ans

"""
 Expected Output:
       array([[-4,  1,  7],
               [ 8,  2, -2],
               [ 6,  3,  9]])
 """ 
function15()


# In[615]:



#task16
def function16():
#Write a NumPy program to join a sequence of arrays along depth.


x = np.array([[1], [2], [3]])
y = np.array([[2], [3], [4]])
ans = np.dstack((x,y)) #write your code here 
  
return ans

"""
 Expected Output:
            [[[1 2]]

             [[2 3]]

             [[3 4]]]
 """
function16()


# In[662]:




#Task17
def function17():
# replace numbers with "YES" if it divided by 3 and 5
# otherwise it will be replaced with "NO"
# Hint: np.where
arr = np.arange(1,10*10+1).reshape((10,10))
return   np.where(arr%15==0,'YES','NO')        # Write Your Code HERE

#Excpected Out
"""
array([['NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO'],
   ['NO', 'NO', 'NO', 'NO', 'YES', 'NO', 'NO', 'NO', 'NO', 'NO'],
   ['NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'YES'],
   ['NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO'],
   ['NO', 'NO', 'NO', 'NO', 'YES', 'NO', 'NO', 'NO', 'NO', 'NO'],
   ['NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'YES'],
   ['NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO'],
   ['NO', 'NO', 'NO', 'NO', 'YES', 'NO', 'NO', 'NO', 'NO', 'NO'],
   ['NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'YES'],
   ['NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO', 'NO']],
  dtype='<U3')
"""
function17()


# In[829]:


#Task18
def function18():
    # count values of "students" are exist in "piaic"
    piaic = np.arange(100)
    students = np.array([5,20,50,200,301,7001])
    x = np.intersect1d(piaic,students).size                                       # Write you code Here
    return x

    #Expected output: 3
function18()


# In[841]:


# Task19
def function19():
    #Create variable "X" from 1,25 (both are included) range values
    #Convert "X" variable dimension into 5 rows and 5 columns
    #Create one more variable "W" copy of "X" 
    #Swap "W" row and column axis (like transpose)
    # then create variable "b" with value equal to 5
    # Now return output as "(X*W)+b:

    X =np.arange(1,26).reshape(5,5)   # Write your code here
    W =np.asarray(X).T   # Write your code here 
    b =5   # Write your code here
    output =(X*W)+b    # Write your code here
    return output
    #expected output
    """
    array([[  6,  17,  38,  69, 110],
       [ 17,  54, 101, 158, 225],
       [ 38, 101, 174, 257, 350],
       [ 69, 158, 257, 366, 485],
       [110, 225, 350, 485, 630]])
    """
function19()


# In[842]:


#Task20
def fucntion20():
    #apply fuction "abc" on each value of Array "X"
    x = np.arange(1,11)
    def abc(x):
        return x*2+3-2

    return abc(np.arange(1,11)) #Write your Code here
#Expected Output: array([ 3,  5,  7,  9, 11, 13, 15, 17, 19, 21])
#--------------------------X-----------------------------X-----------------------------X----------------------------X---------------------
fucntion20()

