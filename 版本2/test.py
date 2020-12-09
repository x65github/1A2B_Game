import threading,time,datetime,os

def breakTime():
    game_Time=startTime+datetime.timedelta(seconds=4)#測試版本:使用4秒
    while True:
        y=input("無限迴圈中，輸入-1會直接停掉程式碼")
        if y == '-1' :
            os._exit(0)
        if datetime.datetime.now()>=game_Time :
            print("已使用30分鐘，建議休息5分鐘")
            if gType=='1':
                print("因為為家長保護模式，已強制休息5分鐘")
                breakTime=game_Time+datetime.timedelta(seconds=5)#測試版本:暫停5秒
                print(breakTime)
                print(datetime.datetime.now())
                while breakTime >= datetime.datetime.now() :
                    breakOn = breakTime-datetime.datetime.now()
                    breakOn=str(breakOn).split(':')
                    break_endSecond=breakOn[2]
                    breakOn[2]=break_endSecond[0:2]
                    x=input("輸入任意鍵可顯示剩下的時間")
                    print(f"離休息時間還剩下{breakOn[1]}分{breakOn[2]}秒")
            else:
                x=input("為一般模式，請問需要休息5分鐘嗎?(請輸入Y/N)")
                while x !='Y' and x !='y' and x !='N' and x !='n' :
                    x=input("請輸入Y/N")
                if x =='Y' or x=='y' :
                    print("開始休息5分鐘")
                    breakTime=game_Time+datetime.timedelta(seconds=5)#測試版本:暫停5秒
                    while breakTime >= datetime.datetime.now() :
                        breakOn = breakTime-datetime.datetime.now()
                        breakOn=str(breakOn).split(':')
                        break_endSecond=breakOn[2]
                        breakOn[2]=break_endSecond[0:2]
                        x=input(f"離休息時間還剩下{breakOn[1]}分{breakOn[2]}秒")
                else:
                    print("好的，請記得休息喔\n"+
                          "提醒:此時間並未記錄在遊戲時間內\n")
                    break_endTime=datetime.datetime.now()-game_Time
                    game_Time=datetime.datetime.now()+datetime.timedelta(seconds=4)#測試版本:使用2秒
                    continue
            game_Time=datetime.datetime.now()+datetime.timedelta(seconds=4)#測試版本:使用2秒
            print("休息時間已結束\n"+
                  "提醒:此時間並未記錄在遊戲時間內\n")
        continue

startTime=datetime.datetime.now()
gtype=input("請選擇遊戲模式1.家長保護模式2.一般模式: ")
while gtype != '1' and gtype != '2':
    gtype=input("請輸入1或2: ")
t=threading.Thread(target=breakTime)
t.setDaemon(True)
t.start()
x='1'
while x =='1' :
    x=input("hihi")
os._exit(0)
#t.join()
