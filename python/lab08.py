'''
ID box
Timothy Kwan
3050244
'''
import ctypes
'''
purpose: Table class create the hash table array
parameter: the capacity (if any) the pre-set limit is 500
pre: the number of capacity of the list, and any Key and value
post: a list of hash table array
return: none
'''
class Table:
    '''
    purpose: a sub-class to create the node object 
    parameter: key and the value
    pre: key and value
    post: an object that contains the key and value
    return: none
    '''
    class _Node:
        def __init__(self,K,v):
            self._Key = K
            self._value = v
            self._delete = False #False means it exist
            return
        #return the status of that key
        def getStat(self):
            return self._delete
        #change the status of the key to deleted
        def changeStat(self):
            self._delete = True
            return
        #debug function: return the Key when called
        def getKey(self):
            return self._Key
        #debug function: return the value when called
        def getValue(self):
            return self._value
        #print function
        def __str__(self):
            return str(self._Key)+' '+str(self._value)
        
    #the beginning of the Table class
    def __init__(self,cap=500):
        self._capacity = (cap*ctypes.py_object)()
        #grow the table when size reach 2/3
        self._size = 0
        for i in range(len(self._capacity)):
            self._capacity[i] = None
        return
    #return Capacity size instead of the capacity array
    def getCapacitySize(self):
        return len(self._capacity)
    #return the size of the list
    def getSize(self):
        return self._size
    
    def getCapacity(self):
        return self._capacity
    
    #this is called when the size reach 2/3 of capacity
    #double the capacity of the hash array list
    def doubler(self,oldarray):
        newarray = (len(self._capacity)*2*ctypes.py_object)()
        new_lenght = len(newarray)
        a=0
        for i in range(new_lenght):#create a new list
            newarray[i] = None
        for i in range(len(oldarray)):#put the old data into new data list
            if oldarray[i]!=None:
                ind = abs(hash(oldarray[i].getKey()))%new_lenght
                while newarray[ind] != None:
                    a+=1
                    ind = abs(hash(oldarray[i].getKey())+a)%new_lenght
                newarray[ind] = oldarray[i]
                a=0
        return newarray
    
    #store a new key as a node into the list
    def store(self,Key,value):
        #store the key value if key is presented old value is replaced 
        #this will grow the capacity as well
        if self._size >= (len(self._capacity)*2//3):
            self._capacity = self.doubler(self._capacity)
            
        new = Table._Node(Key,value)
        i= 0
        while (i< len(self._capacity)):
            ind = abs(hash(Key)+i)%len(self._capacity)
            if self._capacity[ind] != None and self._capacity[ind].getKey() != Key:
                i+=1
            elif self._capacity[ind] != None and self._capacity[ind].getKey() == Key:
                self._capacity[ind] = new
                return
            else:
                self._capacity[ind] = new
                self._size+=1
        return
    #return the value of input key and return nothing if key does not exist or deleted
    def get(self,Key):
        #return the value associated with the Key otherwise return None
        ind = abs(hash(Key))%len(self._capacity)
        i = 0
        while (i<len(self._capacity) and self._capacity[ind] != None):
            #if self._capacity[ind].getKey() == Key and not self._capacity[ind].getStat():
            if self.exist(self._capacity[ind].getKey()):
                return self._capacity[ind].getValue()
            i+=1
            ind = (ind+1)%len(self._capacity)
        return
    
    #change getStat of the key into True as a mark of deleted
    def delete(self,Key):
        #delete keys from table
        #the reason the delete cannot be none is that
        #if the search goes through none it will stops searching
        ind = abs(hash(Key))%len(self._capacity)
        i=0
        while (i<len(self._capacity) and self._capacity[ind] != None):
            if self._capacity[ind].getStat():
                return
            if self._capacity[ind].getKey() == Key:
                #print(self._capacity[ind])
                self._capacity[ind].changeStat()
                self._size-=1
                return self._capacity[ind]
            i+=1
            ind = (ind+1)%len(self._capacity)
        return
    
    #print all the key that is not deleted and is in the list
    def keys(self):
        #return a list of the keys in the table
        key_list = []
        length = len(self._capacity)
        i=0
        while (i<length):
            if self._capacity[i] != None and not self._capacity[i].getStat():
                    #print(self._capacity[i].getKey(),self._capacity[i].getValue())
                    key_list.append(self._capacity[i].getKey())
            i+=1
        return key_list
    
    #return the True if the input key exist or not deleted, and false otherwise
    def exist(self,Key):
        ind = abs(hash(Key))%len(self._capacity)
        i=0
        while self._capacity[ind] !=None:
            if not self._capacity[ind].getStat() and self._capacity[ind].getKey() == Key:
                return True
            ind = (ind+1)%len(self._capacity)
            i+=1
        return False
    
    #print every single keys and their values in the list; exclud the deleted key.
    def print_table(self):
        #prints-key value pair in table
        for i in self._capacity:
            if i != None and not i.getStat():
                print(i)
        return