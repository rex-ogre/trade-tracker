import tkinter as tk
from tkinter import messagebox
from docopt import docopt
from trade_tracker import  *
#使用後心得: 可以增加id 這樣刪除資料也比較方便 然後還可以增加一鍵刪除 
#如果可以列出RR 跟損益的加總 也會方便記錄一點
import sys

from tkinter import ttk
window = tk.Tk()
window.title('trade_tracker')
window.geometry('800x500')

#frame 一下
frm=tk.Frame(window)
frm.pack()
frm_item=tk.Frame(frm)
frm_item.pack()
frm_earn_or_lose=tk.Frame(frm)
frm_earn_or_lose.pack()
frm_bet=tk.Frame(frm)
frm_bet.pack()
frm_bet_pec=tk.Frame(frm)
frm_bet_pec.pack()
frm_tree=tk.Frame(frm)


frm_tree.pack(side='bottom')

#設置label
id_label= tk.Label(window, text='ID', font=('Arial', 10), width=15, height=2)
item_label=tk.Label(frm_item, text='交易品項', font=('Arial', 10), width=15, height=2)
item_label.pack()
earn_or_lose_label=tk.Label(frm_earn_or_lose, text='損益', font=('Arial', 10), width=15, height=2)
earn_or_lose_label.pack()
bet_label=tk.Label(frm_bet, text='預計止損金額', font=('Arial', 10), width=15, height=2)
bet_label.pack()
bet_pec_label=tk.Label(frm_bet_pec, text='止損金額占帳戶比', font=('Arial', 10), width=15, height=2)
bet_pec_label.pack()
#設置entry
id_entry=tk.Entry(window,show=None,)

item_entry=tk.Entry(frm_item,show=None)
item_entry.pack()
earn_or_lose_entry=tk.Entry(frm_earn_or_lose,show=None)
earn_or_lose_entry.pack()
bet_entry=tk.Entry(frm_bet,show=None)
bet_entry.pack()
bet_pec_entry=tk.Entry(frm_bet_pec,show=None)
bet_pec_entry.pack()

def del_data():
    conn = sqlite3.connect("trade_record.db")
    cur = conn.cursor()
    for selected_item in tree.selection():
        print(selected_item)  # it prints the selected row id
        cur.execute("DELETE FROM trade_record WHERE ID=?", (tree.set(selected_item, '#1'),))
        conn.commit()
        tree.delete(selected_item)
    conn.close()
def delall_data():
    conn = sqlite3.connect("trade_record.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM trade_record")
    conn.commit()
    for x in tree.get_children():
        tree.delete(x)

    conn.close()
def submit_to_cal():
    global ID
    ID=ID+1
    var_item=item_entry.get()
    var_earnlose=earn_or_lose_entry.get()
    var_bet=bet_entry.get()
    var_bet_pec=bet_pec_entry.get()
    cal(var_item,var_earnlose,var_bet,var_bet_pec)
    var_earnlose=float(var_earnlose)
    var_bet=float(var_bet)
    RR=var_earnlose/var_bet
    
    var_list=[ID,var_item,var_earnlose,RR,var_bet,var_bet_pec]
    tree.insert('','end',values=var_list)

#顯示資料列表 tree
tree=ttk.Treeview(frm_tree,show="headings")
tree["columns"]=('ID','交易品項','損益','RR','預計止損金額','止損金額占帳戶比')
tree.column("ID", width=100,)
tree.column("交易品項", width=100,)
tree.column("損益", width=100,)
tree.column("RR", width=100,)
tree.column("預計止損金額", width=100,)
tree.column("止損金額占帳戶比", width=150,)
tree.heading("ID", text='ID')

tree.heading("交易品項",text="交易品項",)
tree.heading("損益", text="損益",)
tree.heading("RR",text='RR' )
tree.heading("預計止損金額", text="預計止損金額",)
tree.heading("止損金額占帳戶比", text="止損金額占帳戶比",)

conn=sqlite3.connect('trade_record.db')
    
c=conn.cursor()
cr=c.execute('''CREATE TABLE IF NOT EXISTS trade_record(ID,trade_item,earn_or_lose,RR,bet,bet_pec)
    ''')
i=c.execute('SELECT * FROM trade_record ')
for row in i:
   # I suppose the first column of your table is ID
   tree.insert('', 'end', values=(row[0],row[1],row[2],row[3],row[4],row[5])) 
c.close()
tree.pack(side='right')
#設置button

submit_button=tk.Button(window,text='上傳資料',width=15,heigh=2,command=submit_to_cal)
submit_button.pack(side='bottom')

del_button=tk.Button(window,text='刪除資料',width=15,heigh=2,command=del_data)
del_button.place(x=0,y=0)
delall_button=tk.Button(window,text='刪除全部',width=15,heigh=2,command=delall_data)
delall_button.place(x=0,y=100)

window.mainloop()
