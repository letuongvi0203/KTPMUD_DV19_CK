#Phần 1: lập trình căn bản
#Câu 1a
def check_prime_number(n):

    flag = 1
    if (n <2):
        flag = 0
        return flag  
    for p in range(2, n):
        if n % p == 0:
            flag = 0
            break 
    return flag

check_prime_number(11)

def check_min_2_prime(a):
    
  count=0
  for i in range(0,len(a)):
    if(check_prime_number(a[i])==1):  # nếu a[i ] là số nguyên tố
     count=count+1 # tăng biến đếm
  if count>=2:
    return True
  else :
    return False

#Câu 1b

#mảng không có số nguyên tố
a=[1,4,6,8]
res=check_min_2_prime(a)
res

#mảng có 1 số nguyên tố
a=[1,2,4,6]
res1=check_min_2_prime(a)
res1


#mảng  nhiều hơn  2 số nguyên tố
a=[1,2,3,5]
res2=check_min_2_prime(a)
res2


#mảng có phần tử không phải là số nguyên 

import math
class sothuc:
  real_number_=4
  def __init__(self):
    print(" done")

  def module(self):
    return abs(self.real_number_)


check=sothuc()
#check.real_number_=-17
class sophuc(sothuc):
  image_number=3
  def __init__(self):
    sothuc.__init__(self)
    print(" tao class so phuc")
    def module(self):
      print(" ham module")
      return sqrt(self.image_number**2+self.real_number_**2)

i=sophuc()
res=i.module()
res


#Phần 2
#Câu 1
n = float(input("Moi nhap real_number: "))
m = float(input("Moi nhap image_number: "))
class Sothuc :
    def __init__(self,real_number) :
        self.real_number = real_number
    def gttd(self) :
        return (self.real_number *2) * 0.5

class Sophuc(Sothuc) :
    def __init__(self,real_number, image_number) :
        super().__init__(real_number)
        self.image_number = image_number
    def module(self) :
        return (self.image_number**2 + self.real_number**2) ** 0.5

sothuc = Sothuc(n)
print("Tri tuyet doi co gia tri la: ",sothuc.gttd())

sophuc = Sophuc(n,m)
print("module cua so phuc la: ",sophuc.module())