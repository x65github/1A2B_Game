import random,os
from MainList import List

def BuildAns(unit):
    ans=[]
    ans.append(random.randint(1,9))
    for i in range(int(unit)-1):
        ans.append(random.randint(0,9))
    return ans

def guess(ans,unit):
    guessNum=[]
    for i in range(int(unit)):
        while True:
            print(f'請輸入你猜的第{i+1}位數字，呼叫選單請輸入-1，放棄(不產生紀錄)請輸入-2:  ')
            try:
                y=int(input(""))
                if y == -1 :
                    List()
                elif y == -2:
                    print(f"正確答案為{ans}")
                    x=input("輸入任意值以結束程式")
                    os._exit(0)
                else:
                    guessNum.append(y)
                    break
            except :
                print("請輸入數字!!")
    a=0
    b=0
    for i in range(int(unit)):
        for j in range(int(unit)):
            if ans[i] == guessNum[j]:
                if i==j:
                    a=a+1
                else:
                    b=b+1
    if a==int(unit):
        return(False)
    else:
        print(f"{guessNum}的結果為{a}A{b}B")
        return(True)

