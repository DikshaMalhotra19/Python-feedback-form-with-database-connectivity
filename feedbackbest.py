from tkinter import *
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
import tkinter as tk;
class feedbacks:
    def __init__(self,feedback):
        self.feedback=feedback
        self.feedback.geometry("1350x700+0+0")
        self.feedback.configure(bg='gold2')
        title=Label(self.feedback,text="FEEDBACK FORM",font=("times new roman",30,"bold"),bg='coral',fg='black')
        title.pack(side=TOP,fill=X)
        another_frame=tk.Frame(self.feedback,relief=RIDGE,borderwidth=10,bg="salmon")
        another_frame.place(x=20,y=100,width=690,height=560)
        manage_frame=tk.Frame(self.feedback,relief=RIDGE,borderwidth=10,bg="salmon")
        manage_frame.place(x=700,y=100,width=630,height=560);
        self.myvar = tk.StringVar()
        self.var = tk.StringVar()
        self.text=tk.StringVar()
        title=Label(manage_frame,text="HELLO USER!! PLEASE PROVIDE US FEEDBACK",font=("times new roman",18,"bold"),background="brown4",fg='white',borderwidth=10)
        title.pack(side=TOP,fill=X)
        title=Label(another_frame,text="VIEW ALL FEEDBACKS HERE",font=("times new roman",20,"bold"),background="brown4",fg='white',borderwidth=10)
        title.pack(side=TOP,fill=X)
        namelabel = tk.Label(manage_frame, text='Name:',bg='salmon',font=("times new roman",20,"bold"))
        namelabel.place(x=80,y=130)
        entry_name = ttk.Entry(manage_frame, width=18, font=("times new roman",20,"bold"), textvariable=self.myvar)
        entry_name.place(x=160,y=130)
        emaillabel = tk.Label(manage_frame, text='Email:',bg='salmon',font=("times new roman",20,"bold"))
        emaillabel.place(x=280,y=130)
        entry_email = ttk.Entry(manage_frame, width=16, font=("times new roman",20,"bold"), textvariable=self.var)
        entry_email.place(x=360,y=130)
        commentlabel = tk.Label(manage_frame, text='Comment:',bg='salmon', font=("times new roman",20,"bold"))
        commentlabel.place(x=80,y=180)
        self.textcomment = Text(manage_frame, width=70,height=10, font=("times new roman",10,"bold"))
        self.textcomment.place(x=80,y=220)
        self.textcomment.config(wrap ='word')
        submitbutton = tk.Button(manage_frame, text='Submit',width=18,height=2, command=self.insert1,bg='yellow').place(x=100,y=400)
        clearbutton = tk.Button(manage_frame, text='Clear',width=18,height=2, command=self.clear,bg='sky blue').place(x=250,y=400)
        table_frame=tk.Frame(another_frame,relief=RIDGE,bg="pink")
        table_frame.place(x=10,y=70,width=750,height=400)
        scroll_x=tk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=tk.Scrollbar(table_frame,orient=VERTICAL)
        self.student_table=ttk.Treeview(table_frame,columns=("NAME","EMAIL","COMMENT"))
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)
        self.student_table.heading("NAME",text="NAME")
        self.student_table.heading("EMAIL",text="EMAIL")
        self.student_table.heading("COMMENT",text="COMMENT")
        self.student_table['show']='headings';
        self.student_table.column("NAME",width=20)
        self.student_table.column("EMAIL",width=20)
        self.student_table.column("COMMENT",width=50)
        self.student_table.pack(fill=BOTH,expand=2)
        self.fetch_data()
        
    def fetch_data(self):
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="diksha2419",database="feedback");
        mycursor=mydb.cursor();
        mycursor.execute("select * from comment");
        rows=mycursor.fetchall()
        if len (rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for x in rows:
                self.student_table.insert('',END,values=x)
                mydb.commit()
        mydb.close();
    


    def insert1(self):
        name=self.myvar.get();
        email=self.var.get();
        comment= self.textcomment.get("1.0","end")
        print('\t\t\t\t name:',name);
        print('\t\t\t\t email:',email);
        print('\t\t\t\t comment:',comment);
        mydb=mysql.connector.connect(host="localhost",user="root",passwd="diksha2419",database="feedback");
        mycursor=mydb.cursor();
        sql="insert into comment(name,email,comments)values(%s,%s,%s)";
        val=(name,email,comment);
        mycursor.execute(sql,val);
        mydb.commit();
        messagebox.showinfo(title='Submit', message='Thank you for your Feedback, Your Comments Submited')
        self.fetch_data()

    def feedback(self):
         name=self.myvar.get();
         email=self.var.get();
         comment= self.textcomment.get("1.0","end")
         print('\t\t\t\t name:',name);
         print('\t\t\t\t email:',email);
         print('\t\t\t\t comment:',comment);
         mydb=mysql.connector.connect(host="localhost",user="root",passwd="diksha2419",database="feedback");
         mycursor=mydb.cursor();
         sql="insert into comment(name,email,comments)values(%s,%s,%s)";
         val=(name,email,comment);
         mycursor.execute(sql,val);
         mydb.commit();
         messagebox.showinfo(title='Submit', message='Thank you for your Feedback, Your Comments Submited')
         self.fetch_data1()
         self.feed()


    def clear(self):
        messagebox.showinfo(title='clear', message='Do you want to clear?')
        self.myvar.set(" ")
        self.var.set(" ")
        self.textcomment.delete(1.0, END)






feedback=Tk()
object=feedbacks(feedback)
feedback.mainloop()
