class tam_giac:
    def __init__(self,canh1,canh2,canh3) :
            self.canh1=canh1
            self.canh2=canh2
            self.canh3=canh3
        
    def display(self):
        print("obj là tam giác có 3 cạnh lần lượt là: %s %s %s"%(self.canh1,self.canh2,self.canh3))
    def ktra(self):
        if self.canh1+self.canh2<self.canh3 or self.canh3 + self.canh1 < self.canh2 or self.canh2+self.canh3 < self.canh1:
            return False
        return True

class tam_giacv(tam_giac):
    def __init__(self, canh1, canh2, canh3):
        super().__init__(canh1, canh2, canh3)
        if tam_giacv.ktra(self):
            if canh1^2==canh2^2+canh3 ^2 or canh2^2==canh3 ^2+canh1^2 or canh3 ^2==canh1^2+canh2^2:
                print("đây là 3 cạnh của tam giác vuông")
class tam_giacc(tam_giac):
    def __init__(self,canh1, canh2, canh3):
        super().__init__(canh1, canh2, canh3)
        if tam_giacc.ktra(self):
            if canh1==canh2 or canh1==canh3 or canh2==canh3 :
                print('đây là 3 cạnh của tam giác cân')
    def display(self):
        print("obj là tam giác có 3 cạnh lần lượt là: %s %s %s"%(self.canh1,self.canh2,self.canh3))
class tam_giacd(tam_giacc):
    def __init__(self, canh1, canh2, canh3):
        super().__init__(canh1, canh2, canh3)
        if tam_giacd.ktra(self):
            if canh1==canh2 & canh1== canh3:
                print("đây là 3 cạnh của tam giác đều")
    def display(self):
        print("obj là tam giác có 3 cạnh lần lượt là: %s %s %s"%(self.canh1,self.canh2,self.canh3))
obj=tam_giacd(15,15,15)
if obj.ktra():
    obj.display()
else:
    print("đây không phải 3 cạnh của 1 tam giác!!")
    