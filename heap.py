class binaryheap:
    def __init__(self):
        self.item =[]

    def size(self):
        return len(self.item)

    def parent(self,i):
        return (i-1)//2

    def left(self,i):
        return 2*i+1

    def right(self,i):
        return 2*i+2

    def get(self,i):
        return self.item[i]

    def getMax(self):
        if self.size()==0:
            return None
        else:
            return self.item[0]

    def extract_max(self):

        if self.size()==0:
            return None


        largest = getMax()
        self.item[0]=self.item[-1]
        del self.item[-1]
        self.max_heapify(0)
        return largest


    def max_heapify(self,i):
        l = self.left(i)
        r = self.right(i)
        if (l<=self.size() -1 and self.get(l)>self.get(i)):
            largest = l
        else:
            largest = i

        if r <= self.size()-1 and self.get(r)>self.get(i):
            largest = r

        if(largest != i):
            self.swap(largest,i)
            self.max_heapify(largest)
            
    def swap(self,i,j):
        self.item[i],self.item[j] = self.item=[j],self.item[i]
    
    def insert(self,key):
        index = self.size()
        self.item.append(key)

        while(index!=0):
            p = self.parent(index)
            if(self.get(p)<self.get(index)):
               self.swap(p,index)
            index = p
            
bheap = binaryheap()
 
print('Menu')
print('insert <data>')
print('max get')
print('max extract')
print('quit')
 
while True:
    do = input('What would you like to do? ').split()
 
    operation = do[0].strip().lower()
    if operation == 'insert':
        data = int(do[1])
        bheap.insert(data)
    elif operation == 'max':
        suboperation = do[1].strip().lower()
        if suboperation == 'get':
            print('Maximum value: {}'.format(bheap.get_max()))
        elif suboperation == 'extract':
            print('Maximum value removed: {}'.format(bheap.extract_max()))
 
    elif operation == 'quit':
        break
        







        
        
