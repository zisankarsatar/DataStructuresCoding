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
        
    def _resize(self):
        ...
    
    def make_array(self):
        ...