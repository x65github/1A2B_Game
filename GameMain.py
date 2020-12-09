import GetID,Guess,GameHistory,datetime,threading,time,os
from MainList import PlayType,List

def breakTime():
    game_Time=startTime+datetime.timedelta(seconds=30)
    while True:
        if datetime.datetime.now()>=game_Time :
            print("已使用30分鐘，建議休息5分鐘\n")
            game_Time=datetime.datetime.now()+datetime.timedelta(minutes=30)
            
ans=input("Wellcome請問已有用過此版的1A2B了嗎?(請輸入Y/N): ")
while True:
    if(ans == 'Y' or ans == 'y'):
        break
    elif(ans =='N' or ans =='n'):
        import GameRule
        print("\n在D檔產生記錄檔中...")
        GameHistory.Record()
        print("已在D槽下方產生一個history檔,以後所有的遊戲資料將都會放在裡面\n")
        break
    else:
        ans=input("請輸入Y或N: ")
if (ans =='N' or ans =='n'):
    userID=GetID.newID()
else:
    sure=input("請問要使用舊的ID名稱嗎?(請輸入Y/N): ")
    while True:
        if(sure=='Y' or sure=='y'):
            userID=GetID.oldID()
            break
        elif(sure=='N'or sure=='n'):
            userID=GetID.newID()
            break
        else:
            sure=input("請輸入Y或N，大小寫都可:")

ptype=input(f"請選擇遊戲玩法1.一般玩法2.限時玩法3.限次數玩法: ")
while ptype != '1' and ptype != '2' and ptype != '3':
    ptype=input("請輸入1或2或3: ")
                
if ptype == '1':
    ptype=PlayType('1')
    ptype="一般玩法"
elif ptype == '2':
    ptype=PlayType('2')
    ptype="限時玩法"
else:
    ptype=PlayType('3')
    ptype="限次數玩法"
    
x=int(input(f"請選擇要玩幾位數:"))
while True:
    sure=input(f"確認是否要玩{x}位數的1A2B(請輸入Y/N): ")
    if(sure=='N'or sure=='n'):
        x=input(f"請選擇要玩幾位數: ")
        continue
    elif(sure=='Y' or sure=='y'):
        ans=Guess.BuildAns(x)
        break
    else:
        sure=input("請輸入Y/N: ")

music=input('輸入-1則不會有背景音樂\n'+
        '輸入其它的則會撥放以電腦預設的音樂播放程式播放預設音樂\n'+
        '提醒:若要更改預設音樂請將音檔放入game資料夾中並"覆蓋"掉song.mp3檔\n')

if music != '-1' :
    os.system("song.mp3")

print("遊戲開始，請開始猜數字:")
startTime = datetime.datetime.now()
breakt=threading.Thread(target=breakTime)
breakt.setDaemon(True)
breakt.start()

if ptype=="限時玩法":
    gTime=startTime+datetime.timedelta(minutes = 3 )
    while datetime.datetime.now()<gTime:
            gameOn=Guess.guess(ans,x)
            if not gameOn:
               GameHistory.Win(userID,startTime,ptype,x)
    print(f"已超過時間，正確答案為{ans}")
    GameHistory.Lose(userID,startTime,ptype,x)
    
elif ptype=="限次數玩法":
    for i in range(10):
        if (10-i) <= 5:
            print(f"還剩下{10-i}次機會，請加油")
        gameOn=Guess.guess(ans,x)
        if gameOn == False :
            GameHistory.Win(userID,startTime,ptype,x)               
    print(f"已超過10次，正確答案為{ans}")
    GameHistory.Lose(userID,startTime,ptype,x)
        
else:
    gameOn=True
    while gameOn:
        gameOn=Guess.guess(ans,x)
    GameHistory.Win(userID,startTime,ptype,x)
