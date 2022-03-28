


class Q3B:
    def Switch(self,input):
        default = "error"
        return  getattr(self, 'case_' + str(input), lambda: default)()
    
    def case_CSC1008(self):
        return "DSA"
 
    def case_1009(self):
        return "OOP"
 
    def case_1010(self):
        return "NETWORK"


def main():
    s = Q3B()
    print("Hello Glasglow!")  
    Q2()
    print(s.Switch("CSC1009"))
    Q3C()
    

def Q2():
    x = int(input("input x:"))
    y = int(input("input y:"))
    avg = (x+y)/2
    print(avg)

def Q3C():
    for i in range(102,66,-1):
        if i%2 != 0:
            print(i)
    
if __name__ == '__main__':
        main() 
    

    
    
    
    
    
     