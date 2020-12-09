import sys,GameHistory
   
def PlayType(ptype):
    while True:
        if (ptype =='1') :
            print("玩法:一般玩法")
        elif (ptype =='2') :
            print("玩法:限時(3分鐘)玩法")
        else:
            print("玩法:限次數玩法(10次)")
        sure=input("是否確定要選擇此玩法(請輸入Y/N): ")
        if(sure=='N' or sure=='n'):
            ptype=input(f"請選擇遊戲玩法1.一般玩法2.限時玩法3.限次數玩法: ")
            while True:
                if(ptype == '1' or ptype == '2'  or ptype == '3' ):
                    break
                else:
                    ptype=input("請輸入1或2或3: ")
            continue
        elif (sure=='Y'or sure=='y') :
            return ptype
        else:
            sure=input("請輸入Y/N")

def List():           
    x=input("請輸入選項:0.結束遊戲1.返回當前遊戲進度2.查看紀錄: ")
    if(x=='0'):
        sure=input("確認是否要離開遊戲(請輸入Y/N): ")
    elif(x=='1'):
        sure=input("確認是否要返回當前遊戲進度(請輸入Y/N): ")
    else:
        sure=input("確認是否要查看紀錄(請輸入Y/N): ")
    while True:
        if(sure=='Y' or sure=='y'):
            if x=='0':
                sys.exit()
            elif x=='1':
                break
            else:
                GameHistory.History()
                break
        elif(sure=='N'or sure=='n'):
            x=input("請輸入選項:0.結束遊戲1.返回當前遊戲進度2.查看紀錄: ")
        else:
            sure=input("請輸入Y/N: ")
