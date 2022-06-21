def NOT(a):
    return not(a)
def AND(a,b):
    return a and b
def OR(a,b):
    return a or b
def NAND(a,b):
    return NOT(AND(a,b))
def NOR(a,b):
    return NOT(OR(a,b))
def XOR(a,b):
    return AND(OR(a,b),NOT(AND(a,b)))
def XNOR(a,b):
    return NOT(XOR(a,b))
def AND3(a,b,c):
    return AND(AND(a,b),c)
def OR3(a,b,c):
    return OR(OR(a,b),c)
def NAND3(a,b,c):
    return NAND(NAND(a,b),c)

def Bools2DEC3(a,b,c):
    if a==False and b==False and c==False:
        return 0
    if a==False and b==False and c==True:
        return 1
    if a==False and b==True and c==False:
        return 2
    if a==False and b==True and c==True:
        return 3
    if a==True and b==False and c==False:
        return 4
    if a==True and b==False and c==True:
        return 5
    if a==True and b==True and c==False:
        return 6
    if a==True and b==True and c==True:
        return 7
def DEC2Bools3(y):
    if y==0:
        return (False,False,False)
    if y==1:
        return (False,False,True)
    if y==2:
        return (False,True,False)
    if y==3:
        return (False,True,True)
    if y==4:
        return (True,False,False)
    if y==5:
        return (True,False,True)
    if y==6:
        return (True,True,False)
    if y==7:
        return (True,True,True)
def bool2str(a):
    if a==True:
        return "1"
    if a==False:
        return "0"
def Truth_Table3(y):
    print("TRUTH TABLE")
    print("|l |a|b|c| y|")
    l = 0
    for yy in y:
        a = DEC2Bools3(l)[0]
        b = DEC2Bools3(l)[1]
        c = DEC2Bools3(l)[2]
        print("|"+str(l)+" |"+bool2str(a)+"|"+bool2str(b)+"|"+bool2str(c)+"| "+bool2str(yy)+"|")
        l = l+1

if __name__ == '__main__':
    a = [False,True]
    b = [False,True]
    c = [False,True]
    # y = a'b'c+a'bc'+ab'c'
    y = []
    for aa in a:
        for bb in b:
            for cc in c:
                y1 = AND(AND(NOT(aa),NOT(bb)),cc)
                y2 = AND(AND(NOT(aa),NOT(cc)),bb)
                y3 = AND(AND(NOT(bb),NOT(cc)),aa)
                yy = OR(OR(y1,y2),y3)
                y.append(yy)
    # g = b'c+ab'+ac
    g = []
    for aa in a:
        for bb in b:
            for cc in c:
                g1 = AND(NOT(bb),cc)
                g2 = AND(aa,NOT(bb))
                g3 = AND(cc,aa)
                gg = OR3(g1,g2,g3)
                g.append(gg)
    Truth_Table3(y)
    print("\n")
    Truth_Table3(g)
