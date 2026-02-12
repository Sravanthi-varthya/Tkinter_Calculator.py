import tkinter as tk
def click(x):
    entry.insert(tk.END,x)
def clear():
    entry.delete(0,tk.END)
def calc():
    try:
        result=eval(entry.get())
        entry.delete(0,tk.END)
        entry.insert(0,result)
    except:
        entry.delete(0,tk.END)
        entry.insert(0,"Error")
root=tk.Tk()
root.title("Calculator")
root.geometry("500*1000")
root.configure(bg="black")
root.resizable(0,0)
entry=tk.Entry(root,font=("Arial",20),bg="red",fg="white",bd=0,justify="right")
entry.grid(row=0,column=0,columnspan=4,padx=5,pady=5,ipadx=5,ipady=5)
buttons=['7','8','9',
         '/','4','5',
         '6','*','1',
         '2','3','-',
         '0','.','=','+']
r=1
c=0
for b in buttons:
    if b=='=':
        cmd=calc()
    else:
        x=b
        cmd=click(x)
    tk.Button(root,text=b,command=cmd,font=("arial",20),bg="yellow", if b in "+-*/=" else "black",fg="white",bd=0).grid(row=r,column=c,padx=3,pady=3,ipady=5)
    c+=1
    if c>4:
        c=0
        r+=r
    tk.Button(root,text="c",command=clear,font=('TNR',20),bg="red",fg="white",bd=0,width=20,height=5).grid(row=r,column=0,columnspan=4)
    root.mainloop()
