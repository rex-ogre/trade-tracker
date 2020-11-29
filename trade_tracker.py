#交易紀錄

ID=0
import sqlite3

def cal(trade_item,earn_or_lose,bet,bet_pec):  #實際金額加減 紀錄帳戶情形
    
    global account_pec
    global ID
    earn_or_lose=float(earn_or_lose)
    bet=float(bet)
    bet_pec=float(bet_pec)
    ID+=1
    RR=earn_or_lose/bet #r/r風報比 的結果 一倍R 二倍R之類的
    RR=float(RR)
    result=0.0
    result=bet_pec*RR #帳戶%數+-

  
    #print(RR,earn_or_lose)
    conn=sqlite3.connect('trade_record.db')
    c=conn.cursor()
    data=(trade_item ,RR,earn_or_lose)
    SQL=f"INSERT INTO trade_record VALUES('{ID}','{trade_item}','{earn_or_lose}','{RR}','{bet}','{bet_pec}')"
    
    c.execute(SQL)
    conn.commit()
def init():
    conn=sqlite3.connect('trade_record.db')
    cur=conn.cursor()
    sql=('''CREATE TABLE trade_record(ID,trade_item,earn_or_lose,RR,bet,bet_pec)
    ''')
    cur.execute(sql)
    conn.commit()

def view():
    conn=sqlite3.connect('trade_record.db')
    data=('date','trade item ','RR','number+-')
    c=conn.cursor()
    for row in c.execute('SELECT * FROM trade_record '):
        print(row)
def drop(): #刪除資料庫
    conn=sqlite3.connect('trade_record.db')
    c=conn.cursor()
    c.execute("DROP TABLE trade_record")
