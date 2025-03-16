import ctypes

class DynamicArray(object):
    def __init__(self):
        self.n = 0 #eleman sayisi
        self.capacity = 1 #kapsite
        self.A = self.make_array(self.capacity)
        ...
        
    
    def __len__(self):
        return self.n
        
    def __get_item__(self, k):
        if not 0 <= k < self.n:
            return IndexError()
        
        return self.A[k]
    
    def append(self, new_value):
        #eger kapasite dolu ise kapasiteyi iki katina cikar
        if self.n == self.capacity:
            self._resize(2*self.capacity)
        
        self.A[self.n] = new_value #eleman ekleme
        self.n += 1 #elemena sayisini bir attir
        
    def _resize(self, new_cap):
        B = self.make_array(new_cap) #yeni array yap
        
        for k in range(self.n): #eski arraydekileri yeni array a koy 
            B[k] = self.A[k]
            
        self.A = B #array guncelle
        self.capacity = new_cap #kapasite guncelle
        
    
    def make_array(self, new_cap):
        
        return (new_cap*ctypes.py_object)()
    
new_array1 = DynamicArray()

print(new_array1.capacity)

new_array1.append(2)
new_array1.append(3)
new_array1.append(6)

print(new_array1.capacity)

def wordSplit(liste):
    #listeyi ikiye bol
    # ilk dizin ini harflere bol
    # ikinci elemanin kendisini zaten liste
    # ilk dizenin geri kalan elemanlarini ikinci dize icinde ara
    
    word = list((liste[0]))
    word_pool = liste[1].split(',')
    
    k=0
    aranacak_karakterler=''
    for k in range(len(word)):
        aranacak_karakterler += word[k]
        geri_kalan_harfler = liste[0].split(aranacak_karakterler)[1]
        if aranacak_karakterler in word_pool and geri_kalan_harfler in word_pool:
            return [aranacak_karakterler, geri_kalan_harfler]
    
    return 'nothing'
            
    

result = wordSplit(['deeplearn2ing', 'd,dll,a,deep,base,lear,learning'])

print('anlamli kelimler : ', result)

#another way
def wordSplit2(liste):
    word = list(liste[0])
    d = list[1].split(',')
    
    for i in range(1, len(word)):
        c = word[:] # c ile word u esitledi
        c.insert(i,' ')
        
        x,y = ''.join(c).split() # 'de','eplearning'
        if x in d and y in d:
            return x + ' ' + y
    
    return 'nothing'

print(wordSplit(['deeplearning', 'd,dll,a,deep,base,lear,learning']))   