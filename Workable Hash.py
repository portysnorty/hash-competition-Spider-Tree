#dimitri Workman
#steps to look up
#amount of collsions
#length of hash
import random
import string

# Initialize list with lowercase alphabets
#a = list(string.ascii_lowercase)
#print(a)

# Initialize list with uppercase alphabets
#b = list(string.ascii_uppercase)
#print(b)
class Pair:
    ''' Encapsulate letter,count pair as a single entity.
    
    Relational methods make this object comparable
    using built-in operators. 
    '''
    def __init__(self, letter, count = 1):
        self.letter = letter
        self.count = count
    
    def __eq__(self, other):
        if other!=None:
            return self.letter == other.letter
    
    def __hash__(self):
        return hash(self.letter)

    def __ne__(self, other):
        if other!=None:
            return self.letter != other.letter

    def __lt__(self, other):
        return self.letter < other.letter

    def __le__(self, other):
        return self.letter <= other.letter

    def __gt__(self, other):
        return self.letter > other.letter

    def __ge__(self, other):
        return self.letter >= other.letter

    def __repr__(self):
        return f'({self.letter}, {self.count})'
    
    def __str__(self):
        return f'({self.letter}, {self.count})'
    def increase(self):
        self.count+=1


        

        
def buckets(poem,length=100,change=0):
  
    collide=0
  
   
   # print(keyList,len(keyList))
   # for x in mods:
    newlist=[None]*length
    for z in poem:
            key=find_key(z,change)
            index=key%length
            item=Pair(z)
            if newlist[index]==None:
                newlist[index]=item
                #newlist.insert(index,item)
            elif newlist[index].letter == item.letter:
               # print("Index:",index)
                newlist[index].increase()
            else:
                tempMove=index
                tempMove-=1
                collide+=1
                while True: # while it is not None
                    if newlist[tempMove] == None:
                        newlist[tempMove] = item
                        break
                    if newlist[tempMove].letter==item.letter:
                        newlist[tempMove].increase()
                        break
                    tempMove-=1
                    collide+=1
    return length,collide,newlist
        
# bucket exit it out of score once reach as the other min keep leaving
#def bucketScorer(hash):
def searching(word,array,length,change):
    lookups=1
    key=find_key(word,change)
    index=key%length
    
    item=Pair(word)

    if array[index].letter==item.letter:
        return(array[index].count,lookups)
    
    elif index>=0 and index<len(array):
        tempMove=index
        found=True
        while found:
            tempMove-=1
            lookups+=1
            if abs(tempMove)>=len(array):
                return None
            if array[tempMove].letter==item.letter:
                return(array[tempMove].count,lookups)
            
            
def test(word_list,besT,t,i=0):
    try:
        size,collisions,hashBrown = buckets(word_list,t,i)

        totallookUpTimeNew = 0
        sumd = 0
        word_list = set(word_list)
        for x in word_list:
            _,sumd = searching(x,hashBrown,t,i)
            totallookUpTimeNew+=sumd

        something = totallookUpTimeNew+size+collisions
        if besT[1] == 0:
            besT = (t,something,i)
        elif something < besT[1]:
            print(something,'=',totallookUpTimeNew,size,collisions,i)
            besT = (t,something,i)
        
        return besT
    
    except IndexError:
        return besT
    
def words_in(word_list):
    besT = (0,0,0)
    pigsBlood = set(word_list)
    try:
        for i in range(0,100):
            for t in range(210,len(word_list)+1):
                besT = test(word_list, besT, t, i)
    except KeyboardInterrupt:
        pass
    print(besT)
    size,collisions,hashBrown = buckets(word_list,besT[0],besT[2])
    hashBrown.append(besT)
    return size,collisions,hashBrown

    
def lookup_word_count(word,hash):
    besT = hash[-1]
    return searching(word,hash,besT[0],besT[2])

def find_key(word,change):
    GOLDEN_RATIO = 2654436561+change
    key=0
    for i in word:
        key = ((key*GOLDEN_RATIO)+key)+(ord(i)) & 0xFFFFFFFF
    return key        
