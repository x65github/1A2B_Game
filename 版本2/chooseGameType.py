def Gametype(gtype):
    if(gtype =='1'):
        print("模式:家長保護模式")
    else:
        print("模式:一般模式")
    sure=input("是否確定要選擇此模式(請輸入Y/N): ")
    while sure !='Y' and sure !='y' and sure !='N' and sure !='b' :
        sure=input("請輸入Y/N")
    if(sure=='N' or sure=='n'):
        gtype=input("請選擇遊戲模式1.家長保護模式2.一般模式: ")
        while gtype == '1' and gtype == '2' :
            gtype=input("請輸入1或2: ")
    else:
        return gtype
