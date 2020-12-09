def oldID():
    id=input("請輸入您的ID名稱: ")
    try:
        f = open("D:\\history.txt")
        for line in f.readlines():
            getId=line
            getId=getId.split(',')
            if id == getId[0]:
                print(f'歡迎{id}回來')
                return id
        f.close()
        print(f"並未找到{id}的資料")
        id=errorID(id)
        return id
    except :
        print("發生預期外的錯誤以至於並未在D槽下方找到history檔\n"+
              "請將檔案先移至D槽並輸入N以重做")
        id=errorID(id)
        return id

def errorID(id):
    while True:
        x=input("若要直接以{}建立一個新id則請輸入Y\n".format(id)+
                "若要輸入一個新的id則請輸入Z\n"+
                "提醒:若已將hisoy檔刪除則已往的紀錄皆不存在\n")
        while x!='Y' and x!='y' and x!='N' and x!='n' and x!='Z' and x!='z':
            x=input("請輸入Y或N或Z: ")
        if x=='N' or x=='n':
            id=oldID()
            return id
        elif x=='Y' or x=='y':
            return id
        else :
            id=newID()
            return id
       
def newID():
    id=input("請輸入您的ID名稱: ")
    while True:
        if id=="":
            id=input("請重新輸入ID名稱: ")
        else:
            sure=input(f"請確認是否要以{id}作為你的id(請輸入Y/N): ")
            if sure=='Y' or sure == 'y':
                print(f"歡迎{id}~")
                return id
            elif sure=='N' or sure == 'n':
                id=input("請輸入您的ID名稱: ")
            else :
                print("請輸入Y/N: ")
