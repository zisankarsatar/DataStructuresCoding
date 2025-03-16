from typing import List


def siklikbulma(string):
    i = 0
    final_string = ""

    while i < len(string):
        c = string[i]
        j = i+1

        compressed = [1,c]
        while j < len(string):
            if string[j] == c:
                compressed[0] += 1
            else:
                break
            j += 1

        final_string += "".join(map(str,compressed))
        i = j

    
    return final_string
            
#print(siklikbulma('kkcccdeeffffffgzzzzzkkk'))


def kayipBasamak(string):
    for i in range(10):
        c = string.replace('x', str(i))
        x = string.index("=")
        if eval(c[:x]) == eval(c[x+1:]):
            return str(i)
        
#print(kayipBasamak("10-x=4"))
#print(kayipBasamak("1x * 11 =121"))
#print(kayipBasamak("1x0 / 3  = 50"))

def rotate(array):
    #Zisan cozum
    # indexcim = array[0]
    # if indexcim < len(array):
    #     new_array = array[indexcim:] + array[:indexcim]
    #     print(new_array)
    
    eski_baslangic = array[0]
    
    yeni_baslangic = [array[eski_baslangic]]
    count = eski_baslangic + 1
    length = len(array)
    
    while count%length != eski_baslangic:
        yeni_baslangic.append(array[count%length])
        count += 1
        
    #print(yeni_baslangic)
    
rotate([5,3,2,3,4,5,2,3])

def arrayCiftleri(array):
    #pairleri belirlemek
     
    i = 0 
    new = ""
    
    for k in range(len(array)):
        new += str(array[k]) + ' '
        
        if k%2 == 1:
            new += ","
        
    new = new.split(" ,")
    #array icinde pair var mi 
    
    depo =[]
    #pair olmayanlari new listeye ekle
    for i in new:
        if i[::-1] not in new:
            for l in i.split():
                depo.append(l)
        elif i == i[::-1] and new.count(i)<2:
            for l in i.split():
                depo.append(l)
            
    
    #retunr ok 
    if depo == []:
        return "ok"
        
    return ",".join(depo)
    
    
#print(arrayCiftleri([5,6,6,5,2,3,3,3,3,2,7,7,8,1,1,8,4,5]))
#print(arrayCiftleri([5,6,6,5,2,3,3,2,8,1,1,8]))
        
        
def twoSum(nums: List[int], target: int) -> List[int]:
        #for dongusu ile 0. indexten baslayarak target hedefi veren var mi ara
        #indexlerini bul
        #conditionlari ekle
        
        i=0
        indexler=[]
        for i in range(len(nums)):
            aranan_sayi = target - nums[i]
            
            if aranan_sayi in nums:
                if aranan_sayi == nums[i]:
                    indices = [k for k, num in enumerate(nums) if num == aranan_sayi]
                    
                    if len(indices) >= 2:
                        indexler.append(indices[0])
                        indexler.append(indices[1])
                        return indexler
                    else:
                        pass
            
                else:    
                    indexler.append(i)
                    indexler.append(nums.index(aranan_sayi))
                    return indexler   
                   
                    
                 
                
#print(twoSum([3,2,4], 6))
#print(twoSum([0,4,3,0], 0))
print(twoSum([-1,-2,-3,-4,-5], -8))