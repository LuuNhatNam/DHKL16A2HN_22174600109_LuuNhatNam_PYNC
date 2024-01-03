class Phan_so:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau
    def kiem_tra(self):
        if self.mau == 0:
            return False
        return True
    def show(self):
        if self.tu == 0:
            print(0)
        else:
            print(self.tu, " /", self.mau)
def main():
    x = float(input("nhập tử số : "))
    y = float(input("nhập mẫu số : "))
    z = Phan_so(x,y)
    if z.kiem_tra():
        z.show()
    else:
        print("bạn không thể nhập mẫu số là 0, vui lòng nhập lại : ")
        main()
if __name__ == '__main__':
    main()