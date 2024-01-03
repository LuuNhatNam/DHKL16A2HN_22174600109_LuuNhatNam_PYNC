class Hcn:
    count=0
    def __init__(self, chieudai, chieurong):
        self.chieudai=chieudai
        self.chieurong=chieurong
        self.V=(self.chieudai + self.chieurong)/2
        self.S=self.chieudai*self.chieurong
        Hcn.count+=1
    
    def Report(self):
        print("Thông tin hình chữ nhật: \
            Chiều dài: %s \
            chiều rộng: %s \
            Chu vi: %s \
            Diện tích: %s"
            %(self.chieudai, self.chieurong, self.V, self.S))
hcn=Hcn(int((input("Nhập chiều dài hcn: ")))\
        ,int(input("Nhập chiều rộng hình chữ nhật: ")))
hcn.Report()