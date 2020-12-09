import os,datetime

def Record():        
    while True:
        try:
            f = open("D:\\history.txt",mode='a')
            print("id,遊戲時間,遊戲玩法,答案位數,備註",file=f)
            print("",file=f)
            f.close()
            break
        except :
            x=input("無法再D槽產生檔案，有兩種解決辦法:"+
                    "1.產生一個新的檔案(檔名仍為history)\n"+
                    "2.再試一次\n"+
                    "3.放棄此次紀錄並不要建檔(將會損失此次紀錄)")
            if x=='1':
                f = open("D:\\history.txt",mode='w')
                print("id,遊戲時間,遊戲玩法",file=f)
                f.close()
                break
            elif x=='2':
                print("再試一次中...")
                continue
            elif x=='3':
                print("已放棄紀錄")
                status=False
            else:
                continue

def History():
    none=True
    while True:
        try:
            f = open("D:\\history.txt")
        except :
            x=input("發生預期外的錯誤以至於並未在D槽下方找到history檔\n"+
                    "請將檔案先移至D槽並輸入N以重新尋找紀錄\n"+
                    "若已遺失history則請輸入1已返回當前進度\n"+
                    "提醒:若已將hisotory檔刪除則已往的紀錄皆不存在\n")
            while x!='1' and x!='N' and x!='n' :
                x=input("請輸入N或1: ")
            if x=='N' or x=='n':
                continue
        else:
            id = input("若要看全部的紀錄則請至D槽的history檔裡查看\n"+
                        "請輸入要哪個id的紀錄: ")
            while id == '' :
                id= input("請輸入要查詢的id")
            for line in f.readlines():
                nowId=line
                nowId=nowId.split(',')
                if id == nowId[0]:
                    print(line)
                    none=False
            if none :
                print(f"查無{id}的資料\n")
            else:
                print(f"以上是{id}的所有紀錄")
        finally:
            f.close()
            print("即將返回當前遊戲進度...")
            break
          
def Win(id,startTime,ptype,unit):
    print("恭喜你答對了，此次的資料正在放入D槽內的history檔中...")
    gameTime=datetime.datetime.now() - startTime
    gameTime=str(gameTime).split(':')
    gameSencond=gameTime[2]
    gameTime[2]=gameSencond[0:2]
    status=True
    while status:
        try:
            f = open("D:\\history.txt",mode='a')
        except :
            x=input("無法再D槽產生檔案，有兩種解決辦法:"+
                    "1.產生一個新的檔案(檔名仍為history)\n"+
                    "2.再試一次\n"+
                    "3.放棄建檔(將會損失紀錄)")
            if x=='1':
                f = open("D:\\history.txt",mode='w')
                print(f"{id},{gameTime[0]}時{gameTime[1]}分{gameTime[2]}秒,{ptype},{unit}",file=f)
                print("此次的資料可在D槽內的history檔中找到")
                x=input("輸入任意鍵可結束程式")
                f.close()
                os._exit(0)

            elif x=='2':
                print("再試一次中...")
                continue
            elif x=='3':
                print("已放棄建檔")
                status=False
            else:
                continue
        else:
            print(f"{id},{gameTime[0]}時{gameTime[1]}分{gameTime[2]}秒,{ptype},{unit}",file=f)
            f.close()
        finally:
            print("此次的資料可在D槽內的history檔中找到")
            x=input("輸入任意鍵可結束程式")
            os._exit(0)
  
def Lose(id,startTime,ptype,unit):
    startTime=str(startTime).split(':')
    startSencond=startTime[2]
    startTime[2]=startSencond[0:2]
    while True:
        try:
            f = open("D:\\history.txt",mode='a')
        except :
            x=input("發生預期外的錯誤，有兩種解決辦法:"+
                  "1.產生一個新的歷史資料\n"+
                  "2.再試一次\n")
            if x=='1':
                f = open("D:\\history.txt",mode='w')
                print(f"{id},{startTime[0]}時{startTime[1]}分{startTime[2]}秒,{ptype},{unit},失敗",file=f)
                f.close()
            elif x=='2':
                print("再試一次中...")
                continue
            else:
                continue
        else:
            print(f"{id},{startTime[0]}時{startTime[1]}分{startTime[2]}秒,{ptype},{unit},失敗",file=f)
            f.close()
        finally:
            print("此次的資料可在D槽內的history檔中找到")
            x=input("輸入任意鍵可結束程式")
            os._exit(0)        
