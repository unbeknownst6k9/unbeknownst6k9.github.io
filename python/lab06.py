'''
ID box
CMPT 200 lab6
name: Timothy Kwan
3050244

CREDIT:
read_content copied from lab 01
'''
'''
purpose: create a binary search tree then take a .txt document and sort it into a binary search tree
parameter: take in a .txt document
pre: must be a .txt document
post: a binary search tree is created
return: none
'''
class BST :
    '''
    purpose: create to node object as the root or children within the binary search tree
    parameter: value
    pre: any input
    post: create node object
    return: none
    '''
    class _Node :
        def __init__(self, value, left = None, right = None) :
            self._value = value
            self._left = left
            self._right = right
            self._times = 1
        #if the node is being called again it will add 1 as word count
        def increment(self):
            self._times +=1
            
    #this is the BST class
    def __init__(self):
        self._root = None
        self._content = None
        self._totalnum = 0
    #read the file content from user's input
    def read_content(self,string):
        try:
            file_object = open(string, 'r')
            content = file_object.read()
            file_object.close()
            content = content.split()
            punctuation = '''!()[]{};:"\,<>./?@#$%^&*_~'''
            for num in range(len(content)):
                word = content[num]
                for alpha in word:
                    if alpha in punctuation:
                        word = word.replace(alpha,'')
                content[num] = word.upper()
                
            #print(content)
            for i in content:
                self._totalnum +=1
                self.insert(i)
            return 1
        
        except:
            return 0
        
     #return true if the tree is empty
    def isEmpty(self):
        return self._root == None
    #search the input value and return the root. If nothing found then return none
    def search(self, value) :
        probe = self._root
        while (probe != None) :
            if value == probe._value :
                return probe
            if value <= probe._value :
                probe = probe._left
            else :
                probe = probe._right
        return None     
    #search and print according to option. mode 1 is for option and mode is for option 3
    def printSearch(self,value,mode=0):
        find = self.search(value)
        if find != None and mode == 1:
            return str(find._times)
        elif find != None and mode == 3:
            percentage = (find._times/self._totalnum)*100
            return 'The word '+value+' is in the document.\n'+' This word shows up '+str(find._times)+' times\n'+' The frequence of this word in the document is '+str(percentage)+'%'
        else:
            return '0'
    #insert a node into the binary search tree
    def insert(self, value) :
        if self.isEmpty() :
            self._root = self._Node(value)
            return
        parent = None#to keep track of parent
        #we need above information to adjust 
        #link of parent of new ndoe later
        probe = self._root
        while (probe != None) :
            if self.search(value) != None:
                add = self.search(value)
                add.increment()
                return
            if value <= probe._value :#go to left tree
                parent = probe#before we go to child, save parent
                probe = probe._left
            else :#go to right tree
                parent = probe#before we go to child, save parent
                probe = probe._right
        if (value <= parent._value) :#new value will be new left child
            parent._left = self._Node(value)
        else :#new value will be new right child
            parent._right = self._Node(value)
                    
    
    #delete a node in a binary tree
    def delete(self, value) :
        parent = None
        probe = self._root
        while(probe != None) :
            if value == probe._value :
                break
            if value < probe._value :
                parent = probe
                probe = probe._left
            else :
                parent = probe
                probe = probe._right
        if probe == None :
            raise NotPresent("Attempt to delete nonexistent value.")
        # At this point, probe points at the node to be deleted and 
        # parent to the parent of this node.
        if (probe._left != None and probe._right != None):
            # Two children present; find the successor
            parentSu = probe
            su = probe._right#WE'LL LOOK FOR LEFTMOST IN RIGHT SUBTREE
            while (su._left != None) :
                parentSu = su
                su = su._left
            # At this point, su points to the successor of probe
            # Copy su value to probe value and delete node su
            probe._value = su._value
            if parentSu == probe :#if su is child of probe then su has no left child (loop was not executed)
                parentSu._right = su._right#bypass su
            else :#su has right child and loop was executed
                parentSu._left = su._right#
            return
        # We are in the case 0 or 1 child
        newChild = probe._left
        if newChild == None : newChild = probe._right
        if parent == None :
            # We are deleting the root
            self._root = newChild
        else:
            if probe == parent._left:
                parent._left = newChild
            else:
                parent._right = newChild
    #call the recursive in order function
    def inOrder(self) :
        self.recInOrder(self._root)
    #print everything inside the binary search tree
    def recInOrder(self,node) :
        if node == None : return
        self.recInOrder(node._left)
        print(node._value,node._times)
        self.recInOrder(node._right)            
#exception class which is used to handle exception error
class NotPresent(Exception) :
    pass

def main():
    '''
    purpose: user interface for the document
    parameter: a .txt file and option selection from 1 - 4
    pre: prompt the user for .txt file then prompt the user for action
    post: the function respond to the user accordingly
    return: none
    '''
    name = input('please enter the filename: ')
    Tree = BST()
    file = Tree.read_content(name)
    exit_type = '1'
    while file < True:
        print(' File does not exist.\n',
              '1. Enter another file name\n',
              '2. Exit')
        exit_type = input('Please enter selection: ')
        if exit_type == '1':
            name = input('Please enter the filename: ')
            file = Tree.read_content(name)
        elif exit_type == '2':
            return
    print('File read success.')
    exit = ''
    while exit != '4':
        print(' 1. get number of unique words\n',
          '2. print all unique words in alphabetical\n',
          '3. find the status of a specific word\n',
          '4. exit\n')
        
        exit = input('Please enter 1 to 4: ')
        if exit == '1':
            value = input('Please enter a specific word: ').upper()
            print('\nThe number of this specific word is:',Tree.printSearch(value,1),'\n')
        elif exit == '2':
            Tree.inOrder()
        elif exit =='3':
            value = input('Please enter a specific word: ').upper()
            if Tree.printSearch(value,3) != '0':
                print('\n',Tree.printSearch(value,3),'\n')
            else:
                print('\nThe word does not exist.\n')
        elif exit =='4':
            print('\nThank you for using the service.\n')
            return