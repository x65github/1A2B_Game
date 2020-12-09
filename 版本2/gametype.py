import threading,time,datetime,os
def breakTime():
    game_Time=startTime+datetime.timedelta(seconds=2)#測試版本:使用2秒
    while True:
        if datetime.datetime.now()>=game_Time :
            print("已使用30分鐘，建議休息5分鐘")
            if gType=='1':
                print("因為為家長保護模式，已強制暫停5分鐘")
                breakTime=game_Time+datetime.timedelta(seconds=5)#測試版本:暫停5秒
                while breakTime >= datetime.datetime.now() :
                    print(breakTime)
                    print(datetime.datetime.now())
                    breakOn = breakTime-datetime.datetime.now()
                    breakOn=str(breakOn).split(':')
                    print(breakOn)
                    break_endSecond=breakOn[2]
                    print(break_endSecond)
                    breakOn[2]=break_endSecond[0:2]
                    breakOn[2]
                    x=input("")
                    print(f"離休息時間還剩下{breakOn[1]}分{breakOn[2]}秒")
                    if x == '-1' :
                        os._exit()
                
            else:
                x=input("非家長使用模式，請問需要休息5分鐘嗎?(請輸入Y/N)")
                while x !='Y' and x !='y' and x !='N' and x !='n' :
                    x=input("請輸入Y/N")
                if x =='Y' or x=='y' :
                    break_Time=startTime+datetime.timedelta(seconds=5)#測試版本:暫停5秒
                    while breakTime >= datetime.datetime.now() :
                        breakOn = breakTime-datetime.datetime.now()
                        breakOn=str(breakOn).split(':')
                        break_endSecond=breakOn[2]
                        breakOn[2]=break_endSecond[0:2]
                        breakOn[2]
                        print(f"離休息時間還剩下{breakOn[1]}分{breakOn[2]}秒")
                else:
                    print("好的，請記得休息喔\n"+
                          "提醒:此時間並未記錄在遊戲時間內\n")
                    break_endTime=datetime.datetime.now()-gTime
            game_Time=startTime+datetime.timedelta(seconds=2)#測試版本:使用2秒
            continue
        else:
            pass
                   
startTime=datetime.datetime.now()
gType=input("請選擇遊戲模式1.家長保護模式2.一般模式: ")
t=threading.Thread(target=breakTime)
#t.setDaemon(True)
t.start()

time.sleep(10)
