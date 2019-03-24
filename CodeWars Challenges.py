# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 15:56:31 2016

@author: dkatz44
"""

def get_sum(a,b):

    if a != b:  
        total = 0
        if a < b:
            for x in range(a, b + 1):
                total += x
        else:
            for x in range(b, a + 1):
                total += x      
        return total
    else:
        return a

# Finding Duplicates

def duplicate_count(text):

     uniqueList = []
    
     text = text.lower()    
    
     for x in text:
         if x not in uniqueList:
             uniqueList.append(x)
    
     print(uniqueList)
    
     duplicates = []
     
     for x in uniqueList:
         
        tempList = []
        
        for i in text:            
            if i == x:
                tempList.append(i)
                
        if len(tempList) > 1:
            duplicates.append(x)
     
     returnString = ""       
     if len(duplicates) == 0:
         returnString = 0
     elif len(duplicates) == 1:
         returnString = len(duplicates)
     elif len(duplicates) > 1:
         #for x in duplicates:
         returnString = ' and '.join(map(str, duplicates))
                
            
     return returnString

duplicate_count("11112223455BBBbbb6")
         
         
#%%
         
# Square each number
         
         
def square_digits(num):

    numStr = str(num)

    numList = []
    
    for i in numStr:
        numList.append(str(int(i)*int(i)))
        
    
    finalString = ''.join(map(str,numList))
    
    return int(finalString)
    
    pass


#%%


# first letter of each word in caps


def toJadenCase(string):
    # ...

    newString = string[0].upper()

    for x in range(len(string)):
        if x >= 1:
            if string[x - 1] == " ":
                newString += string[x].upper()
            else:
                newString += string[x]
                
    return newString
    
toJadenCase("ok ok ok okok")

            
            
#%% 
        
        
# Unique in order
        
def unique_in_order(iterable):
    
    newList = []
    
    if len(iterable) == 1:
        newList.append(iterable)
    
    if len(iterable) == 2:
        if iterable[0] == iterable[1]:
            newList.append(iterable[0])
        else:
            newList.append(iterable[0])
            newList.append(iterable[1])
    
    if len(iterable) > 2:    
    
       # newList.append(iterable[0])    
    
        for x in range(0, len(iterable) - 1):
            print(iterable[x], " ", iterable[x+1])
            if iterable[x] != iterable[x + 1]:
                print("appended:", iterable[x])
                newList.append(iterable[x])
        
        if iterable[-1] != newList[-1]:
            print("appended:",iterable[-1])
            newList.append(iterable[-1])
    
    return newList
    
    pass
            

          
unique_in_order('AAAABBBCCDAABBB')  


def unique_in_order(iterable):
    result = []
    prev = None
    for char in iterable[0:]:
        if char != prev:
            result.append(char)
            prev = char
    return result 


#%%
     
     
def DNA_strand(dna):
    # code here
         
    newString = ""
    
    for x in dna:
        if x == "A":
            newString += "T"
        elif x == "T":
            newString += "A"
        elif x == "G":
            newString += "C"
        elif x == "C":
            newString += "G"

    return newString
    
def DNA_strand(dna):
    return dna.translate(string.maketrans("ATCG","TAGC"))

#%%

def likes(names):
    #your code here

    finalString = ""

    if len(names) == 0:
        finalString = "no one likes this"
        
    if len(names) == 1:
        finalString = names[0] + " likes this"
    
    if len(names) == 2:
        finalString = names[0] + " and " + names[1] + " like this"
        
    if len(names) == 3:
        finalString = names[0] + ", " + names[1] + " and " + names[2] + " like this"
    
    if len(names) > 3:
        finalString = names[0] + ", " + names[1] + " and " + str(len(names) - 2) + " others like this"
        
        
    return finalString

def likes(names):
    n = len(names)
    return {
        0: 'no one likes this',
        1: '{} likes this', 
        2: '{} and {} like this', 
        3: '{}, {} and {} like this', 
        4: '{}, {} and {others} others like this'
    }[min(4, n)].format(*names[:3], others=n-2)


#%%

def namelist(names):
    #your code here
    print(names)
    nameString = ""

    if len(names) == 0:
        nameString = ""
        
    if len(names) == 1:
        nameString = names[0]['name']

    if len(names) == 2:
        nameString = names[0]['name'] + " & " + names[1]['name']
    
    if len(names) >= 3:
        for x in names[0:len(names)-1]:
            nameString += x['name'] + ", "

        nameString = nameString[:-2]
        
    if len(names) > 2:
        nameString += " & " + names[-1]['name']
    print(nameString)
    
    return nameString
    
def namelist(names):
    if len(names) > 1:
        return '{} & {}'.format(', '.join(name['name'] for name in names[:-1]), 
                                names[-1]['name'])
    elif names:
        return names[0]['name']
    else:
        return ''


namelist([ {'name': 'Bart'}, {'name': 'Lisa'}, {'name': 'Maggie'} ])
# returns 'Bart, Lisa & Maggie'

namelist([ {'name': 'Bart'}, {'name': 'Lisa'} ])
# returns 'Bart & Lisa'

namelist([ {'name': 'Bart'} ])
# returns 'Bart'

namelist([])
# returns ''
        
#%%

def countBits(n):   
    
    return sum([int(x) for x in str("{0:b}".format(n))])

"""    
def countBits(n):
    return bin(n).count("1")
"""
#%%

print(x for x in range(10))
#%%

def averages(arr):

    import statistics as s
    
    return [s.mean([arr[x], arr[x+1]]) for x in range(len(arr)-1)]

    pass

averages([2,3,4,5])

#%%
# move the zeros to the end while keeping the order of the other elements

def move_zeros(array):
    #your code here

    zeroIndices = [x for x, y in enumerate(array) if (type(array[x]) == int and str(array[x]) == '0') or str(array[x]) == '0.0']
    print(zeroIndices)
    
    newList = [array[x] for x, y in enumerate(array) if x not in zeroIndices]
    print(newList)    
    
    for x in zeroIndices:
        newList.append(array[x])
    
    return newList

    



move_zeros([1, 6, 10, 2, 0, False, 0, 2, 0, 5, 3, -7, 0, 6, -9, 0, 'b', 0, -1, 4, -6, '0'])

#%%           
           [1, 6, 10, 2, False, 2, 5, 3, -7, 6, -9, 'b', -1, 4, -6, 0, 0, 0, 0, 0, 0, 0]
           [1, 6, 10, 2, False, 2, 5, 3, -7, 6, -9, 'b', -1, 4, -6, '0', 0, 0, 0, 0, 0, 0]



def move_zeros(arr):
    l = [i for i in arr if isinstance(i, bool) or i!=0]
    return l+[0]*(len(arr)-len(l))
    
def move_zeros(array):
    return sorted(array, key=lambda x: x==0 and type(x) is not bool)
    
#%%

# remove values in array 2 from array 1
    
def array_diff(a, b):
    #your code here

    return [x for x in a if x not in b]
    


array_diff([1,2,2,3],[1,2,2])


#%%

# HH:MM:SS

def make_readable(seconds):
    # Do something   
    hours = 0
    minutes = 0    
    
    for x in range(1,seconds+1):
        if x % 60 == 0:
            minutes += 1
            s = 0
        if minutes == 60:
            hours += 1
            minutes = 0

    return '{:02d}:{:02d}:{:02d}'.format(hours,minutes,seconds % 60)
    
make_readable(5001)

#print(83*60+21)


def make_readable(s):
    return '{:02}:{:02}:{:02}'.format(s / 3600, s / 60 % 60, s % 60)

#%%

"""

In mathematics, a perfect power is a positive integer that can be expressed as an integer 
power of another positive integer. 

More formally, n is a perfect power if there exist natural numbers m > 1, and k > 1 such that mk = n.
Your task is to check wheter a given integer is a perfect power. 
If it is a perfect power, return a pair m and k with mk = n as a proof. 
Otherwise return Nothing, Nil, null, None or your language's equivalent.

Note: For a perfect power, there might be several pairs. 
For example 81 = 3^4 = 9^2, so (3,4) and (9,2) are valid solutions. 
However, the tests take care of this, so if a number is a perfect power, return any pair that proves it.

isPP(4) => [2,2]
isPP(9) => [3,2]
isPP(5) => None

"""


def isPPSlow(n):
    #your code here
    
    nums = []
    for x in range(2,n-1):
        if len(nums) != 0 or x*2 > n:
            break
        for y in range(2,n-1):
#            print(y,x,y**x)
            if y**x > n and x**y > n:
                break
            if y**x == n:
                nums = [y,x]
                break
            if x**y == n:
                nums = [x,y]
                break  

    if len(nums) == 0:
        nums = None
    
    return nums    


#%%

isPPSlow(125) 


#%%

def isPP(n):
    #your code here
    
    nums = []
    """
    for x in range(2,n-1):
        if len(nums) != 0 or x*2 > n:
            break
        for y in range(2,n-1):
#            print(y,x,y**x)
            if y**x > n and x**y > n:
                break
            if y**x == n:
                nums = [y,x]
                break
            if x**y == n:
                nums = [x,y]
                break  
    """
        
    for y in range(2,n-1):
        root = n**(1/y)
        if root < 2:
            break
        if round(root,5) % 1 == 0:
            nums = [int(round(root,5)), y]
            break
    
    if len(nums) == 0:
        nums = None
    print(nums)
    return nums    
    

#%%
        
isPP(441)


#%%

#clockwise path through array

def snail(array):
    
    
    arrayWidth = len(array[0])
    arrayHeight = len(array)    
    
    listCount = len(array)
    overallLength = sum([len(x) for x in array])
    snailList = []
    
#    print(listCount)
    
    if overallLength != 0:    
    
        coordList = []
    
        for x,y in enumerate(array):
            for z,q in enumerate(array[x]):
  #              print(x,z)
                coordList.append([x,z])
    
 #   print(coordList)    
    
        newCoordList = []    
        
        for i in coordList:
            x = i[0]
            y = i[1]
            print(array[x][y])
            print(i)
        
        x = 0
        y = 0
        
        newCoords = []
        
        newCoords.append([x,y])
        
        counter = len(array) - 1  
        
        i = counter
           
        for z in range(1,counter + 1):
            print("condition1: ", [x, y+z])
            newCoords.append([x, y + z])
    
        for z in range(1,counter + 1):
            print("condition2: ", [x+z, counter])
            newCoords.append([x + z, counter])
        
        for z in reversed(range(0,counter)):
            print("condition3: ", [counter, y+z])
            newCoords.append([counter, y + z])
        
        for z in reversed(range(1, counter)):
            print("condition4: ", [x+z, y])
            newCoords.append([x + z, y])
    
         
    
        for z in range(1,counter):
            print("condition1: ", [x + 1, y+z])
            newCoords.append([x + 1, y + z])
    
        for z in range(2,counter):
            print("condition2: ", [x+z, counter-1])
            newCoords.append([x + z, counter])
        
        for z in reversed(range(1,counter-1)):
            print("condition3: ", [counter-1, y+z])
            newCoords.append([counter-1, y + z])
        
        for z in reversed(range(1, counter-2)):
            print("condition4: ", [x+z, y])
            newCoords.append([x + z, y])
    
       
        for i in newCoords:
      #      print(x[0], x[1])
            x = i[0]
            y = i[1]
            snailList.append(array[x][y])
   
    return snailList


#%%

def snail(array):
    
    
    arrayWidth = len(array[0])
    arrayHeight = len(array)    
    
    listCount = len(array)
    overallLength = sum([len(x) for x in array])
    snailList = []
    
#    print(listCount)
    
    if overallLength != 0:    
    
        coordList = []
    
        for x,y in enumerate(array):
            for z,q in enumerate(array[x]):
  #              print(x,z)
                coordList.append([x,z])
    
        print(coordList)     
        
        for i in coordList:
            x = i[0]
            y = i[1]
        #    print(array[x][y])
        #    print(i)
        
        pathX = 0
        pathY = 0
        
        newCoords = []
        
        widthCount = arrayWidth - 1
        heightCount = arrayHeight - 1
        c34widthCount = arrayWidth - 1
        c34heightCount = arrayHeight - 1        
        
        newCoords.append([pathX, pathY])       

        while len(newCoords) < overallLength:
            for i in range(widthCount):
                pathY += 1
                if [pathX, pathY] not in newCoords \
                and len(newCoords) < overallLength \
                and [pathX, pathY] in coordList:
                    newCoords.append([pathX, pathY])
                    print("condition1: ",[pathX, pathY])       
            
            for i in range(heightCount):
                pathX += 1
                if [pathX, pathY] not in newCoords \
                and len(newCoords) < overallLength \
                and [pathX, pathY] in coordList:
                    newCoords.append([pathX, pathY])
                    print("condition2: ",[pathX, pathY])
                
            for i in range(widthCount):
                print("widthCount",widthCount)
                print([pathX,pathY])
                pathY -= 1
                if [pathX, pathY] not in newCoords \
                and len(newCoords) < overallLength \
                and [pathX, pathY] in coordList:
                    newCoords.append([pathX, pathY])
                    print("condition3: ",[pathX, pathY])
                
                
            for i in range(heightCount):
                print([pathX,pathY])
                pathX -= 1
                if [pathX, pathY] not in newCoords \
                and len(newCoords) < overallLength \
                and [pathX, pathY] in coordList:
                    newCoords.append([pathX, pathY])
                    print("condition4: ",[pathX, pathY])
                
               
            pathX += 1            
            widthCount -= 1
            heightCount -= 1
            
        for i in newCoords:
            x = i[0]
            y = i[1]
            snailList.append(array[x][y])

    return snailList

#%%        

array = [[1,2,3],
         [8,9,4],
         [7,6,5]]

snail(array)


#%%

array = [[1,2,3,4],
         [12,13,14,5],
         [11,16,15,6],
         [10,9,8,7]]


snail(array)

#%%

array = [[1, 2, 3, 4, 5],
         [16,17,18,19,6],
         [15,24,25,20,7],
         [14,23,22,21,8],
         [13,12,11,10,9]]


snail(array)

#%%

array = [[ 1,  2,  3,  4,  5, 6],
         [20, 21, 22, 23, 24, 7],
         [19, 32, 33, 34, 25, 8],
         [18, 31, 36, 35, 26, 9],
         [17, 30, 29, 28, 27, 10],
         [16, 15, 14, 13, 12, 11]]


snail(array)

#%%

snail([[2,2],[2,2]])

#%%
print(array[0])

#%%

def snail(array):
    
    
    arrayWidth = len(array[0])
    arrayHeight = len(array)    
    
    listCount = len(array)
    overallLength = sum([len(x) for x in array])
    snailList = []
    
    if overallLength != 0:    
    
        coordList = []
    
        for x,y in enumerate(array):
            for z,q in enumerate(array[x]):
                coordList.append([x,z])
         
        
        for i in coordList:
            x = i[0]
            y = i[1]
        
        newCoords = []
        
        widthCount = arrayWidth
        heightCount = arrayHeight

        start = 0
        end = arrayWidth -1
        colRowList = []
        colRowCount = arrayWidth + arrayHeight
    
        while len(colRowList) <= colRowCount:
            colRowList.append(start)
            colRowList.append(end)
            colRowList.append(end)
            colRowList.append(start)
            
            start +=1
            end -= 1
            
        i = 0    
        while len(newCoords) < overallLength:
            for y in range(widthCount):
                if [colRowList[i], y] not in newCoords \
                and len(newCoords) < overallLength \
                and [colRowList[i], y] in coordList:
                    newCoords.append([colRowList[i], y])
                
            i+=1
        
            for x in range(heightCount):
                if [x, colRowList[i]] not in newCoords \
                and len(newCoords) < overallLength \
                and [x, colRowList[i]] in coordList:
                    newCoords.append([x, colRowList[i]])
                
            i+=1
        
            for y in reversed(range(widthCount)):
                if [colRowList[i], y] not in newCoords \
                and len(newCoords) < overallLength \
                and [colRowList[i], y] in coordList:
                    newCoords.append([colRowList[i], y])
                
            i+=1
        
            for x in reversed(range(heightCount)):
                if [x, colRowList[i]] not in newCoords \
                and len(newCoords) < overallLength \
                and [x, colRowList[i]] in coordList:
                    newCoords.append([x, colRowList[i]])
                
            i+=1
        
        print(newCoords)        
        for i in newCoords:
            x = i[0]
            y = i[1]
            snailList.append(array[x][y])

    return snailList

#%%        

array = [[1,2,3],
         [8,9,4],
         [7,6,5]]

snail(array)


#%%

array = [[1,2,3,4],
         [12,13,14,5],
         [11,16,15,6],
         [10,9,8,7]]


snail(array)

#%%

array = [[1, 2, 3, 4, 5],
         [16,17,18,19,6],
         [15,24,25,20,7],
         [14,23,22,21,8],
         [13,12,11,10,9]]


snail(array)

#%%

array = [[ 1,  2,  3,  4,  5, 6],
         [20, 21, 22, 23, 24, 7],
         [19, 32, 33, 34, 25, 8],
         [18, 31, 36, 35, 26, 9],
         [17, 30, 29, 28, 27, 10],
         [16, 15, 14, 13, 12, 11]]


snail(array)

#%%
def snail(array):
    return list(array[0]) + snail(zip(*array[1:])[::-1]) if array else []
    
#%%
    
# roman numeral converter
  """complete the solution by transforming the roman numeral into an integer"""
  
  # MDCLXVI
  """
  I = 1
  V = 5
  X = 10
  L = 50
  C = 100
  D = 500
  M = 1000
  
  """   
def solution(roman):
    
    numList = []    
    
    for x in roman:
        if x == 'I':
            numList.append(1)
        elif x == 'V':
            numList.append(5)
        elif x == 'X':
            numList.append(10)
        elif x == 'L':
            numList.append(50)
        elif x == 'C':
            numList.append(100)
        elif x == 'D':
            numList.append(500)
        elif x == 'M':
            numList.append(1000)

    sumList = []    
    
    for x in range(len(numList)-1):
        if numList[x] >= numList[x+1]:
            sumList.append(numList[x])
        else:
            sumList.append(-(numList[x]))
            
    sumList.append(numList[-1])
    
    solution = sum(sumList) 
    
    return solution

#%%

roman = 'XIX'

print(solution(roman))

roman = 'MDCLXVI'

print(solution(roman))

roman = 'MCMXC'
print(solution(roman))

#%%

def decompose(n):
    # your code
    
    print(n**2)
    solution = n - 1
    
    numList = []

    numList.append(1)
    numList.append((n-1)**2)
    

    print(numList)
    return solution

#%%
n = 22

decompose(n)


#%%

# if char appears once, then (, if it appears more than once, then )

def duplicate_encode(word):
    #your code here

    """
    coded = ''

    for x in word:
        if word.count(x) > 1:
            coded += ")"
        else:
            coded += "("

    return coded
    """
    return ''.join(")" if word.lower().count(x) > 1 else "(" for x in word)

#%%


duplicate_encode('lol')

#%%

# max contiguous sub-array sum

def maxSequence(arr):
	# ... 
   
   numList = []
   
   for x in range(len(arr)-1):
       numList.append(arr[x] + arr[x+1])
       
     
   return numList
       
        

#%%
maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# should be 6: [4, -1, 2, 1]



#%%
"""

choose a text in capital letters including or not digits and non alphabetic characters,

shift each letter by a given number but the transformed letter must be a letter (circular shift),

replace each digit by its complement to 9,

keep such as non alphabetic and non digit characters,

downcase each letter in odd position, 
upcase each letter in even position (the first character is in position 0),
reverse the whole result.

"""

def play_pass(s, n):
    
    
    alphabet = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O',
                'P','Q','R','S','T','U','V','W','X','Y','Z']
                
    nums = '0123456789'
    
    
    shiftedLetter = ''    
    
    for char in s:
        if char in alphabet:
            print(char)
            
            idx = alphabet.index(char)
            print(idx)
            
            remainder = idx + n
            print(remainder)
            
            if remainder > 25:
                shiftedLetter += alphabet[remainder - len(alphabet)]
                
            else:
                shiftedLetter += alphabet[remainder]
                
        else:
            shiftedLetter += char
    
    print("shiftedLetter:",shiftedLetter)        
    shiftedLetter2 = ''
    
    for char in shiftedLetter:
        if char in nums:
            shiftedLetter2 += str(9 - int(char))
        else:
            shiftedLetter2 += char
    
    print("shiftedLetter2:",shiftedLetter2)
        
    shiftedLetter3 = ''
    
    for idx, char in enumerate(shiftedLetter2):
        if   idx % 2 != 0 and char in alphabet:
            shiftedLetter3 += char.lower()
            
        elif idx % 2 == 0 and char in alphabet:
            shiftedLetter3 += char.upper()
            
        else:
            shiftedLetter3 += char
    
    print("shiftedLetter3:",shiftedLetter3)
    shiftedLetter4 = ''
    
    for char in reversed(shiftedLetter3):
        shiftedLetter4 += char
            
    
    return shiftedLetter4
    

#%%

play_pass("I LOVE YOU!!!", 1)  #, "!!!vPz fWpM J")


#%%

"""

Given two arrays of strings a1 and a2 return a sorted array r in lexicographical 
order of the strings of a1 which are substrings of strings of a2.

Example 1:

a1 = ["arp", "live", "strong"]

a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

returns ["arp", "live", "strong"]

Example 2:

a1 = ["tarp", "mice", "bull"]

a2 = ["lively", "alive", "harp", "sharp", "armstrong"]

returns []

"""


#%%

def in_array(array1, array2):    
    
return sorted(list(set([y for y in array1 for x in array2 if x.find(y) >-1])))
    
#%%
    
a1 = ["arp", "live", "strong"]

a2 = ["lively", "alive", "harp", "sharp", "armstrong"]


a1 = ['cod', 'code', 'wars', 'ewar'] 
a2 = ['lively', 'alive', 'harp', 'sharp', 'armstrong', 'codewars']

in_array(a1, a2)

#%%

'triplets is a list of triplets from the secrent string. Return the string.'
def recoverSecret(triplets):
    solution = ''

    letterList = []

    for x in triplets:
        for y in x:
            if y not in letterList:
                letterList.append(y)
     

    for letter in letterList:
        for x in triplets:
            if letter in x:
                print(letter,x.index(letter))
    
    dictionary = {}
            
    for i in triplets:
        for x,y in enumerate(i):
            dictionary[y]=x
        

    print(dictionary)            
       
    # for each letter
    # find the letters after it
    # recursive function?

    return solution

#%%
secret = "whatisup"

triplets = [
  ['t','u','p'],  
  ['w','h','i'],  
  ['t','s','u'],  
  ['a','t','s'],  
  ['h','a','p'],  
  ['t','i','s'],  
  ['w','h','s']   
]  

combined = []

for x in triplets:
    for y in x:
        if y not in combined:
            combined.append(y)

secret = []

while len(secret) != len(combined):
    for letter in combined:
        if letter not in secret:
            countLettersBefore = 0
            
            for x in triplets:
                for y,z in enumerate(x):
                    if y != 0 and z == letter:
                        countLettersBefore += 1
    	
            if countLettersBefore == 0:
                secret.append(letter)
    
                for q in triplets:
                    if letter in q:
                        q.remove(letter)

#%%
print(secret)
#%%

print(zeroPosition)
print(onePosition)
print(twoPosition)

#%%
 

def recoverSecret(triplets):
    
    combined = []

    for x in triplets:
        for y in x:
            if y not in combined:
                combined.append(y)
    
    secret = ''
    
    while len(secret) != len(combined):
        for letter in combined:
            if letter not in secret:
                countLettersBefore = 0
                
                for x in triplets:
                    for y,z in enumerate(x):
                        if y != 0 and z == letter:
                            countLettersBefore += 1
        	
                if countLettersBefore == 0:
                    secret += letter
        
                    for q in triplets:
                        if letter in q:
                            q.remove(letter)
    return secret
    
triplets = [
  ['t','u','p'],  
  ['w','h','i'],  
  ['t','s','u'],  
  ['a','t','s'],  
  ['h','a','p'],  
  ['t','i','s'],  
  ['w','h','s']   
]   
    
recoverSecret(triplets)  
#%%

test = '12345'

if '1' in test:
    print('yes')

#%%

# MORSE CODE DECODER

def decodeMorse(morseCode):
    # ToDo: Accept dots, dashes and spaces, return human-readable message
    
    return ''.join([MORSE_CODE[x] if x != '*' else ' ' for x in morseCode.lstrip().replace('   ',' * ').split()])


#%%    
# Decore Morse Code 2 
 
bits = '1100110011001100000011000000111111001100111111001111110000000000000011001111110011111100111111000000110011001111110000001111110011001100000011'
 


#%%
def decodeBits(bits):

    bits = bits.strip('0')
    
    zeros = sorted(list(set([x for x in bits.split('1') if '0' in x]))) 
    
    ones = sorted(list(set([x for x in bits.split('0') if '1' in x]))) 
    
    combined = zeros + ones
    
    minLen = min([len(x) for x in combined])
    
    dot = ''
    dash = ''
    
    pauseDotDash = ''
    pauseChar = ''
    pauseWord = ''
    
    for x in range(minLen):
        dot += '1'
        pauseDotDash += '0'
    
    for x in range(minLen*3):
        dash += '1'
        pauseChar += '0'
    
    for x in range(minLen*7):
        pauseWord += '0'

    return bits.replace(dash, '-').replace(dot, '.').replace(pauseWord, '   ').replace(pauseChar, ' ').replace(pauseDotDash, '')
    
    
def decodeMorse(morseCode):
    # ToDo: Accept dots, dashes and spaces, return human-readable message
    return ''.join([MORSE_CODE[x] if x != '*' else ' ' for x in morseCode.lstrip().replace('   ',' * ').split()])

   import re
    
    # remove trailing and leading 0's
    bits = bits.strip('0')
    
    # find the least amount of occurrences of either a 0 or 1, and that is the time hop
    time_unit = min(len(m) for m in re.findall(r'1+|0+', bits))
    
    # hop through the bits and translate to morse
    return bits[::time_unit].replace('111', '-').replace('1','.').replace('0000000','   ').replace('000',' ').replace('0','')

#%%

def convert(inputList, source, target):

    sourceBase = len(source)
    targetBase = len(target)
    
    inputPositions = []
    
    sourceList = [x for x in source]
    targetList = [x for x in target]
    
    print(sourceBase, source)
    print(targetBase, target)    
    
    for x in inputList:
        if x in sourceList:
            inputPositions.append(str(sourceList.index(x)))
    print("inputPositions:",inputPositions)
    
    power = len(inputPositions) - 1
    
    sumsList = []

    for x in inputPositions:
        sumsList.append(int(x)*(sourceBase**power))
        print("x:",x, "power:",power, "sumsList:",sumsList)
        power -= 1
        
    inBase10 = sum(sumsList)    
    print(inBase10)
    def fromBase10(number, endBase):
    
        changed = []    
        divByBase = -1    
        
        while divByBase != 0:
            divByBase = int(number / endBase)     
            
            modByBase = number % endBase  
            
            changed.append(modByBase)
            number = divByBase
            
        return changed[::-1]
    

    changed = fromBase10(inBase10, targetBase)
    print("changed:",changed)
    result = ''

    for x in changed:
        result += target[x]
    
    return result

#%%

convert('15', '0123456789', '01')
#%%
convert('hello', 'abcdefghijklmnopqrstuvwxyz', '0123456789abcdef')

def convert(input, source, target):
    base_in = len(source)
    base_out = len(target)
    acc = 0
    out = ''
    for d in input:
        acc *= base_in
        acc += source.index(d)
    while acc != 0:
        d = target[acc%base_out]
        acc = acc/base_out
        out = d+out
    return out if out else target[0] 
    
#%%
    
# get PINs
"""
┌───┬───┬───┐
│ 1 │ 2 │ 3 │
├───┼───┼───┤
│ 4 │ 5 │ 6 │
├───┼───┼───┤
│ 7 │ 8 │ 9 │
└───┼───┼───┘
    │ 0 │
    └───┘

find all possibilities can be any adjacent #s

1: 2, 4
2: 1, 3, 5
3: 2, 6
4: 1, 5, 7
5: 2,4,6,8
6: 3,5,9
7: 4,8
8: 5,7,9,0
9, 6,8,0
0: 8

"""
def get_pins(observed):

    pinLen = len(observed)
    
    grid = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9'],
    ['' , '0', '' ]
    ]
    
    observedList = [x for x in observed]

    print("observedList:",observedList)
    
    overallList = []
    pinList = []
    
    listOfLists = []    
    
    for num in observed:
        numList = []
        ind = []
        
        for x in grid:
            if num in x:
                ind = [grid.index(x), x.index(num)]

        x = ind[0]
        y = ind[1]
        
        possible = [[x,y],
                    [x+1,y],
                    [x,y+1],
                    [x-1,y],
                    [x,y-1]]  

        possible = [str(grid[x[0]][x[1]]) for x in possible if x[0] >= 0 and x[0] < len(grid) 
                                                           and x[1] >= 0 and x[1] < len(grid[0]) 
                                                           and grid[x[0]][x[1]] != '']    
    
        for x in possible:
            numList.append(x)
    
        numList = list(set(numList))
    
        for x in numList:
            #pinList.append(x * pinLen)
            overallList.append(x)
        
        listOfLists.append(numList)  
    
    print("listOfLists:",listOfLists)
    
    pinList = listOfLists[0]
    print("pinList",pinList)
    
    listOfLists.remove(listOfLists[0])
    print("listOfLists",listOfLists)
    
    newPinList = []

    count = 0
    
    while count < len(listOfLists):        
    
        for x in pinList: 
            for y in listOfLists[count]:
                for z in y:
                    newPinList.append(x + z)
        
        pinList = newPinList
        newPinList = []
        count += 1
               
                
    print("newPinList:",newPinList)
    
    
    if len(listOfLists) == 0:
        return pinList
    else:
        return sorted(list(set(pinList)))
    
get_pins('99')
#%%
from itertools import product

ADJACENTS = ('08', '124', '2135', '326', '4157', '52468', '6359', '748', '85790', '968')

def get_pins(observed):
    return [''.join(p) for p in product(*(ADJACENTS[int(d)] for d in observed))]
    
#%%

import re

def decipher_this(string):
    
    nums = list(set(re.findall('[0-9]+', string)))
    
    for x in nums:
        string = string.replace(x, chr(int(x)))
    
    string = string.split()
    
    newString = []
    
    for x in string:
        if len(x) > 2:
            split = [y for y in x.split()[0]]
            
            split[1], split[-1] = split[-1], split[1]
    
            newString.append(''.join(split)) 
            
        else:        
            newString.append(x) 
        
    return ' '.join(newString)
    
decipher_this('65 119esi 111dl 111lw 108dvei 105n 97n 111ka')

#%%

def decipher_word(word):
    i = sum(map(str.isdigit, word))
    decoded = chr(int(word[:i]))
    if len(word) > i + 1:
        decoded += word[-1]
    if len(word) > i:
        decoded += word[i+1:-1] + word[i:i+1]
    return decoded

def decipher_this(string):
    return ' '.join(map(decipher_word, string.split()))
    
def decipher_this(string):
    words = []
    for word in string.split():
        code = ''.join(char for char in word if char.isdigit())
        new_word = chr(int(code))+''.join(char for char in word if not char.isdigit())
        words.append(new_word[:1]+new_word[-1]+new_word[2:-1]+new_word[1] if len(new_word)>2 else new_word)
    return ' '.join(words)
    
#%%
    
# Who Is Next?
import math

def whoIsNext(names, r):    
    
    name = ''

    if r <= 5:
        name = names[r-1]
        
    elif r >= 6 and r <= 15:
        if r % 2 == 0:
            name = names[int(r/2)-3]
        else:
            name = names[int((r-1)/2)-3]
           
        print(name)
    else:       
        logR = math.log((r + 4) / 10) / math.log(2)
        
        up = math.ceil(logR)
        down = math.floor(logR)
        
        base = 10*(2**down) - 4
        interval = base / 5        
        
        if r >= base and r <= base + interval:
            name = 'Sheldon'
            
        elif r > base + interval     and r <= base + (interval*2):
            name = 'Leonard'
            
        elif r > base + (interval*2) and r <= base + (interval*3):
            name = 'Penny'
            
        elif r > base + (interval*3) and r <= base + (interval*4):
            name = 'Rajesh'
          
        else: 
            name = 'Howard'
    
    return name

    
whoIsNext(["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"], 13)


#%%
S: 6,7,16,17,18,19,   36,37,38,39,40,41,42,43   76
L: 8,9,20,21,22,23,   44,45,46,47,48,49,50,51
P: 10,11,24,25,26,27, 52,53,54,55,56,57,58,59
R: 12,13,28,29,30,31, 60,61,62,63,64,65,66,67
H: 14,15,32,33,34,35, 68,69,70,71,72,73,74,75
#%%
10 * 1
10 * 2 
10 * 4
10 * 8

5 * 2**2

for x in range(0,10):

    print(10*(2**x) - 4)

  
# for each iteration # of total people doubles
#%%
  
#       10*(2**x) - 4 = 1802
#       10*(2**x) = 1806
#       2**x = 180.6
#       x = log(180.6) / log(2)

x = math.log(180.6) / math.log(2)

#%%

# Max Sum Contiguous Subarray

def maxSequence(arr):
    
    arrSum = 0    
    
    if all(x < 0 for x in arr):
        arrSum = 0
    
    elif all(x > 0 for x in arr):
        arrSum = sum(arr)
    
    else:
        for y in range(len(arr)):
            for x in range(y,len(arr)):
                if sum(arr[x:]) > arrSum:
                    arrSum = sum(arr[x:])

        for y in reversed(range(len(arr))):
            for x in reversed(range(y,len(arr))):
                if sum(arr[x:]) > arrSum:
                    arrSum = sum(arr[x:])        

        
        for y in range(len(arr)):
            for x in range(len(arr)):
                if sum(arr[y:x]) > arrSum:
                    arrSum = sum(arr[y:x]) 
    return arrSum
   
#%%
     
maxSequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# should be 6: [4, -1, 2, 1]   
#%%

maxSequence([-1,-2,-3])  

#%%

def maxSequence(arr):
    max,curr=0,0
    for x in arr:
        curr+=x
        if curr<0:curr=0
        if curr>max:max=curr
    return max


#%%

def sum_for_list(lst):
    # Find prime #s that evenly go into any number in the list then...
    # Find the sum of the #s in the list that the same prime # goes into
    # Sort by increasing order of prime #s
    listOfSums = []

    # Find all prime numebers < max(lst)
        # Test each number in list with each prime #
    absList = [abs(x) for x in lst]
    newList = [x for x in range(2,max(absList))]
    
    #print(newList)
    
    newList2 = []
    primeList = []
    
    x = 2
    
    while x*x < max(absList):
        for y in newList[newList.index(x)::x]:     
            if y != x:
                newList2.append(y)
        x+=1
                
    #print(sorted(list(set(newList2))))
    
    primeList = [x for x in newList if x not in newList2]
    
    print(primeList)

    for prime in primeList:
        tempList = []
        
        for num in lst:
           # print(num, prime, num%prime)
            if num % prime == 0:
                tempList.append(num)
                #print(tempList)
        
        if sum(tempList) > 0 or len(tempList) >= 1:
           # print("tempList:",tempList)
            listOfSums.append([prime, sum(tempList)])                

    return listOfSums

I = [12, 15] # result = [[2, 12], [3, 27], [5, 15]]
#%%
I = [-29804] #-4209, -28265, -72769, -31744]

sum_for_list(I)

#%%

newList = [x for x in range(2,31)]

print(newList)

newList2 = []
primeList = []

x = 2

while x*x < max(lst:)
    for y in newList[newList.index(x)::x]:     
        if y != x:
            newList2.append(y)
            
print(newList)
print(sorted(list(set(newList2))))

primeList = [x for x in newList if x not in newList2]


print(primeList)
#%%

#%%

# Prime Factorization

#I: First we divide the number by the smallest prime number which divides the number exactly.

#II: We divide the quotient again by the smallest or the next smallest prime number if it is not exactly divisible by 
# the smallest prime number. We repeat the process again and again till the quotient becomes 1. 
# Remember, we use only prime numbers to divide.

def sum_for_list(lst):
    # Find prime #s that evenly go into any number in the list then...
    # Find the sum of the #s in the list that the same prime # goes into
    # Sort by increasing order of prime #s
    listOfSums = []

    # Find all prime numebers < max(lst)
        # Test each number in list with each prime #
    absList = [abs(x) for x in lst]
    newList = [x for x in range(2,max(absList))]
    
    #print(newList)
    
    newList2 = []
    primeList = []
    
    primeList2 = []
    tempNum = 0
    
    x = 2
    
    while x*x < max(absList):
        for y in newList[newList.index(x)::x]:  
            print(x,y)
            if y != x:
                newList2.append(y)
                
                primeList = [z for z in newList if z < y and z not in newList2]
                
                print(primeList)
                
                while 
                
                
                for num in absList:
                    
                    
                    
                    if num % prime == 0:
                        
                        tempNum = num / prime
                        
                        primeList2.append(prime)
                    
                
        x+=1
                
    print(sorted(list(set(newList2))))
    
    #primeList = [x for x in newList if x not in newList2]
    
    print(primeList)

    for prime in primeList:
        tempList = []
        
        for num in lst:
           # print(num, prime, num%prime)
            if num % prime == 0:
                tempList.append(num)
                #print(tempList)
        
        if sum(tempList) > 0 or len(tempList) >= 1:
           # print("tempList:",tempList)
            listOfSums.append([prime, sum(tempList)])                

    return listOfSums

I = [12, 15]
#%%
sum_for_list(I)


#%%

# Next Bigger Number

def next_bigger(n):
    print(n)
    n = [int(x) for x in str(n)]
    
    nextN = 0

    if len(n) == 1 or all(x == n[0] for x in n) or n == list(reversed(sorted(n))):
        nextN = -1
        print('other conditions')
        
    else:
        print('first else')
        for x in reversed(range(len(n)-1)):
            if n[x] < n[x+1]:
                temp = [z for z in n[x+1:]]
                if len([z for z in temp if z > n[x] and z <= 9]) == 0:
                    print("condition 1")
                    print(n[x], n[x+1])
                    n[x], n[x+1] = n[x+1], n[x]
                    print(n)
                    nextN = int(''.join(str(y) for y in n))
                    break
                else:
                    print("condition2")
                    print(n[x+1])
                    
                    print(temp)
                    tempMin = min([z for z in temp if z > n[x] and z <= 9])
                    
                    print(tempMin)
                    tempToSwap = n[x]
                    
                    n[x] = tempMin
                     
                    temp[temp.index(tempMin)] = tempToSwap
                    
                    print(temp)
                    
                    sortedTemp = list(sorted(temp))
                    print(sortedTemp)
                    combined = n[:x+1] + sortedTemp
                    print(combined)
                    nextN = int(''.join(str(y) for y in combined))
                    break
                
    return nextN

#%%

next_bigger( 85643) 

             86543
should equal 86345

# swap x with next greatest value then sort the rest


#%%
# Need to handle trailing 0's
next_bigger(1234567890) # -> 1234567908

#%%
next_bigger(59884848459853)

#%%
            59884848    4 59853
            59884848    4 83559

#%%
next_bigger(59853) -> 83559

#%%
"""
next_bigger(12)==21
next_bigger(513)==531
next_bigger(2017)==2071

           
If no bigger number can be composed using those digits, return -1:

next_bigger(9)==-1
next_bigger(111)==-1
next_bigger(531)==-1
"""


def next_bigger(n):
  n = str(n)[::-1]
  try:
    i = min(i+1 for i in range(len(n[:-1])) if n[i] > n[i+1])
    j = n[:i].index(min([a for a in n[:i] if a > n[i]]))
    return int(n[i+1::][::-1]+n[j]+''.join(sorted(n[j+1:i+1]+n[:j]))) 
  except:
    return -1



#%%

# Validate a Sudoku Puzzle

puzzle = [
  [7,8,4,  1,5,9,  3,2,6],
  [5,3,9,  6,7,2,  8,4,1],
  [6,1,2,  4,3,8,  7,5,9],

  [9,2,8,  7,1,5,  4,6,3],
  [3,5,7,  8,4,6,  1,9,2],
  [4,6,1,  9,2,3,  5,8,7],

  [8,7,6,  3,9,4,  2,1,5],
  [2,4,3,  5,6,1,  9,7,8],
  [1,9,5,  2,8,7,  6,3,4]
]

#%%


print(len(puzzle[0]))

#%%


def is_valid(puzzle):
    
    valid = True
    testList = [x for x in range(1,10)]
    print(testList)
    
    # Test Inputs
    for x in puzzle:
        for y in x:
            if type(y) != int:
                valid = False
                
    # Test Horizontal           
    if valid != False:
        for x in puzzle:
            print(sorted(x))
            if sorted(x) != testList:
                valid = False
                break
    
    # Test Vertical
    if valid != False:
        for x in list(map(list, zip(*puzzle))):
            print(sorted(x))
            if sorted(x) != testList:
                valid = False
                break
    
    
    # Test Each Sub-Square
    
    return valid

#%%

is_valid(puzzle)
    

#%%

class Sudoku(object):
   
    def is_valid(self):
        
        
        pass


#%%

# Slide down the pyramid with greatest sum 

   /3/
  \7\ 4 
 2 \4\ 6 
8 5 \9\ 3

#%%

def longestSlideDown(pyramid):
    
    currentIndex = 0
    sumList = []
    
    for x, y in enumerate(pyramid):
        
        print("currentIndex:", currentIndex)
        
        if len(y) > 1:
            if currentIndex != 0:
                possibilities = []
                
                possibilities = y[currentIndex-1:currentIndex+2]
            
            elif currentIndex == 0:
                possibilities = []
                
                print("currentIndex:",currentIndex, "currentIndex+1:",currentIndex+2)
                
                possibilities = y[currentIndex:currentIndex+2]           
                print(y[0:1])
                
                
            maxNum = max(possibilities)
            print("possibilities:",possibilities)
            
            sumList.append(maxNum)
            
            print("y:",y,"maxNum:",maxNum,"y.index(maxNum):",y.index(maxNum))
            
            currentIndex = y.index(maxNum)
            
        else:
            sumList.append(y[x])
            
    return sum(sumList)
        

#%%

longestSlideDown([[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]) #-> 23

#%%

[                         [75], 
                        [95, 64], 
                      [17, 47, 82], 
                    [18, 35, 87, 10], 
                   [20, 4, 82, 47, 65], 
                  [19, 1, 23, 75, 3, 34], 
                [88, 2, 77, 73, 7, 63, 67], 
              [99, 65, 4, 28, 6, 16, 70, 92], 
           [41, 41, 26, 56, 83, 40, 80, 70, 33], 
         [41, 48, 72, 33, 47, 32, 37, 16, 94, 29], 
       [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14], 
     [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57], 
   [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48], 
  [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31], 
 [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]

#%%

#
def count_cows(n):
    
    print("n:",n)
    
    totalCows = 0

    if type(n) != int:
        totalCows = None
        
    elif n > 3:
        cowList = [1, 1, 1, 2]
    
        while len(cowList) != n+1:
            cowList.append(cowList[-1] + cowList[-3])
            print(cowList[-1] + cowList[-3])
        
        totalCows = cowList[-1]
  
    elif n == 3:
        totalCows = 2
    
    else:
        totalCows = 1
        
    return totalCows




#%%

count_cows(10)

#%%
count_cows(0)  #// should equal 1
count_cows(1)  #// should equal 1
count_cows(3)  #// should equal 2
count_cows(4)  #// should equal 3
count_cows(10) #// should equal 28
#%%

def count_cows(n):
    if not isinstance(n, int):
        return None
    return 1 if n < 3 else count_cows(n-1) + count_cows(n-3)

#%%

count_cows(10)

#%%

# Strip all text including white space after given comment markers
# strip from marker to \n

def solution(string,markers):

    print("\n -----NEW ITERATION----- \n")
    print(string)
    print(markers)
    if any(x in string for x in markers) == False:
        print("final", string)
        return string.strip(' ')
    
    else:
        for x in markers:
            string = string.replace(x, markers[0])
    
        stringList = [x for x in string]
    
        print(stringList)
    
        start = stringList.index(markers[0])
        print("start:", start)
        coords = []
        
        broken = False
        
        for x, y in enumerate(stringList[start:]):
            coords.append(x + start)
            if y == '\n':
                broken = True
                print("broken")
                break
        print("coords:", coords)
        if len(coords) > 0:
            del stringList[min(coords):max(coords)]
        
        
        if broken == False:
            del stringList[-1:]
        print(''.join(stringList))
    
        if len(stringList) > 1:
            for x, y in enumerate(stringList):
                if y == '\n' and stringList[x-1] == ' ':
                    del stringList[x-1]
    
        return solution(''.join(stringList), markers)

#%%

result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# result should == "apples, pears\ngrapes\nbananas"   
#%%

solution('\n\xc2\xa7',['#', '\xc2\xa7'])          

def solution(string,markers):
    parts = string.split('\n')
    for s in markers:
        parts = [v.split(s)[0].rstrip() for v in parts]
    return '\n'.join(parts)

from re import split, escape


def solution(string, markers):
    if markers:
        pattern = "[" + escape("".join(markers)) + "]"
    else:
        pattern = ''
    return '\n'.join(split(pattern, line)[0].rstrip() for line in string.splitlines())


#%%

import re

def parse_molecule (formula):
    print(formula)
    # need to identify characters for individual elements 
        # 2 upper case in a row vs. upper then lower case vs. upper then something else

    splitOnNums = list(set(re.split('[0-9]',formula)))
    
   # splitOnLetters = 
    
    splitNotLetters = re.split('[^A-Za-z]', formula)
    
    print("splitOnNums:", splitOnNums)
    print("splitNotLetters:", splitNotLetters)
    
    elementList = [x for x in splitNotLetters if x==x.upper() and len(x) == 1 else x]
    
    print("elementList",elementList)
    pass

parse_molecule('Hg2O')

#%%


def black_or_white_key(key_press_count):
    
    color = ''
    
    if key_press_count > 88 and key_press_count % 88 != 0:
        key_press_count %= 88 

        
    elif key_press_count > 88 and key_press_count % 88 == 0:
        color = 'white'
        
    if key_press_count <= 88:
        key_press_count %= 12
      
        if key_press_count in [1,3,4,6,8,9,11]:
          
          color = 'white'
      
        else: 
          color = 'black'
    
    return color
    
def black_or_white_key(key_press_count):
    return "black" if (key_press_count - 1) % 88 % 12 in [1, 4, 6, 9, 11] else "white"
    
#%%
    
    
def who_eats_who(zoo):
    
    zooWords = zoo.split(',')    
    print(zooWords)
    
    animalDict = { 'antelope':['grass'],
                   'big-fish':['little-fish'],
                   'bug':['leaves'],
                   'bear':['big-fish', 'bug', 'chicken', 'cow', 'leaves', 'sheep'],    
                   'chicken': ['bug'],
                   'cow': ['grass'],
                   'fox': ['chicken', 'sheep'],
                   'giraffe': ['leaves'],
                   'lion': ['antelope', 'cow'],
                   'panda': ['leaves'],
                   'sheep': ['grass'],
                   'grass':[],
                   'leaves':[]
                   }
    
    results = []
    stringLen = len(zooWords)       
    breakLoop = False
    while stringLen > 1 and breakLoop != True:
        
        for x,y in enumerate(zooWords):
            print('x',x,'y',y, zooWords)
                
            if x == 0:
                if zooWords[1] in animalDict[y]:
                    results.append(y + " eats " + zooWords[1])
                    del zooWords[1]
                    stringLen = len(zooWords)
                    print(results)

            elif x > 0 and x < len(zooWords) - 1:
            
                if zooWords[x-1] in animalDict[y]:
                    results.append(str(y) + " eats " + str(zooWords[x-1]))
                    del zooWords[x-1]
                    stringLen = len(zooWords)
                    print("break ", results)
                    break
                                  
                elif zooWords[x+1] in animalDict[y]:
                    results.append(str(y) + " eats " + str(zooWords[x+1]))
                    del zooWords[x+1]
                    stringLen = len(zooWords)
                    print("break", results)
                    break
                    
            else:
                if zooWords[x-1] in animalDict[y]:
                    results.append(str(y) + " eats " + str(zooWords[x-1]))
                    del zooWords[x-1]
                    stringLen = len(zooWords)
                    print("break ", results)
                    break
                
                elif x == len(zooWords) - 1:
                    breakLoop = True
    
    if len(zooWords) == 1:        
        results.append(zooWords[0])
    else:
        results.append(",".join(zooWords))    
        
    results.insert(0,zoo)
    return results
        
#%%
        
#who_eats_who("fox,bug,chicken,grass,sheep")
who_eats_who('chicken,fox,leaves,bug,grass,sheep')
