from tkinter import *
from tkinter import ttk
import tkinter as tk
from tkinter import messagebox as mb
from PIL import ImageTk, Image
import cx_Oracle
conn=cx_Oracle.connect('hr/hr@//localhost:1521/xe')
cur=conn.cursor()

f = []
cur.execute("SELECT F_ID FROM FIR")
for r in cur.fetchall():
    f.append(str(r[0]))
c = []
cur.execute("SELECT C_ID FROM CRIME")
for r in cur.fetchall():
    c.append(str(r[0]))
cr = []
cur.execute("SELECT CR_ID FROM CRIMINAL")
for r in cur.fetchall():
    cr.append(str(r[0]))
p = []
cur.execute("SELECT P_ID FROM POLICE")
for r in cur.fetchall():
    p.append(str(r[0]))
s = []
cur.execute("SELECT S_ID FROM SUSPECT")
for r in cur.fetchall():
    s.append(str(r[0]))
ca = []
cur.execute("SELECT CASE_ID FROM COURT")
for r in cur.fetchall():
    ca.append(str(r[0]))

vf = []
cur.execute("SELECT F_ID FROM VICTIM")
for r in cur.fetchall():
    ca.append(str(r[0]))
    

def Alogin():
    uname=username.get()
    pwd=password.get()
    if uname=='' or pwd=='':
        message.set("fill the empty field!!!")
    else:
        if uname=="admin" and pwd=="stuthi":
            message.set("Login success")
            u.delete(0,END)
            p.delete(0,END)
            openAdminWindow()
            #login_screen.destroy()
            
        else:
            message.set("Wrong username or password!!!")

def Ulogin():
    #global l
    uname=username.get()
    global pwrd
    pwrd=password.get()
    if uname=='' or pwrd=='':
        message.set("fill the empty field!!!")
    else:
        if uname=="user" and pwrd in f:
            #and pwrd in l:
            message.set("Login success")
            u.delete(0,END)
            p.delete(0,END)
            openUserWindow()
        else:
            message.set("Wrong username or password!!!")

def openAdminWindow():
    newWindow = Toplevel(login_screen)
    #newWindow=Tk()
    newWindow.title("Admin Page")
    tabControl=ttk.Notebook(newWindow)
    newWindow.geometry("1250x600")

    def crime():
        tabC=ttk.Frame(tabControl)
        canvas=Canvas(tabC,width=1250,height=600)
        canvas.pack(fill="both",expand=True)
        canvas.img=ImageTk.PhotoImage(Image.open("crime.png"))
        canvas.create_image(0,0,image=canvas.img,anchor='nw')
        tabC_newWindow=canvas.create_window(0,90,anchor="nw",window=tabC)
        tabControl.add(tabC,text='Crime')
        t1 = ttk.Treeview(canvas, selectmode ='browse',height=7)
        t1.pack(side ='right')
        verscrlbar = ttk.Scrollbar(canvas,orient ="vertical",command = t1.yview)
        verscrlbar.place(x=1250,y=200,width=20,height=130)
        verscrlbar.pack(side ='right', fill ='x')
        t1.configure(xscrollcommand = verscrlbar.set)
        t1["columns"] = ("1","2","3","4","5","6")
        t1['show'] = 'headings'
        t1.heading("1", text ="C_id")
        t1.heading("2", text ="C_name")
        t1.heading("3", text ="Category")
        t1.heading("4", text ="Crime_spot")
        t1.heading("5", text ="Incident_date")
        t1.heading("6", text ="Incident_time")
        cur.execute("SELECT C_ID,C_NAME,CATEGORY,CRIME_SPOT,TO_CHAR(Incident_date,'DD-MM-YYYY'),Incident_time FROM CRIME")
        i=0
        for r in cur:
            t1.insert('',i,text="",values=(r[0],r[1],r[2],r[3],r[4],r[5]))
            i=i+1
        t1.pack()
        
        #t1.insert('','end',text="1",values=('V217','MURDER','VIOLENT','DUMAS BEACH','04/27/1991','09:20 AM'))
        C_id=tk.StringVar()
        C_name=tk.StringVar()
        Cat=tk.StringVar()
        Cspot=tk.StringVar()
        Idate=tk.StringVar()
        Itime=tk.StringVar()
        c_id = Label(tabC,text = "C_id")
        c_id.place(x = 30,y = 450)  
        e1 = Entry(tabC,textvariable=C_id,width = 15)
        e1.place(x = 80,y = 450)
        c_name = Label(tabC,text = "C_name")
        c_name.place(x = 210,y = 450)  
        e2 = Entry(tabC,textvariable=C_name,width = 15)
        e2.place(x = 270,y = 450)
        cat = Label(tabC,text = "Category")
        cat.place(x = 400,y = 450)  
        e3 = Entry(tabC,textvariable=Cat,width = 15)
        e3.place(x = 480,y = 450)
        cspot = Label(tabC,text = "Crime_spot")
        cspot.place(x = 600,y = 450)  
        e4 = Entry(tabC,textvariable=Cspot,width = 15)
        e4.place(x = 680,y = 450)
        idate = Label(tabC,text = "Incident_date")
        idate.place(x = 800,y = 450)
        e5 = Entry(tabC,textvariable=Idate,width = 15)
        e5.place(x = 890,y = 450)
        itime = Label(tabC,text = "Incident_time")
        itime.place(x = 1000,y = 450)
        e6 = Entry(tabC,textvariable=Itime,width = 15)
        e6.place(x = 1090,y = 450)
        def addData():
            nonlocal e1,e2,e3,e4,e5,e6
            Cid=C_id.get()
            Cname=C_name.get()
            Category=Cat.get()
            C_spot=Cspot.get()
            I_date=Idate.get()
            I_time=Itime.get()
            if len(Cid)==0 or len(Cname)==0 or len(Category)==0 or len(C_spot)==0:
                mb.showwarning("Warning","Enter values")
            elif str(Cid) in c:
                mb.showwarning("Warning","C_id already present")
            else:

                stmt1="INSERT INTO CRIME VALUES(:1,:2,:3,:4,TO_DATE(:5,'DD-MM-YYYY'),:6)"
                cur.execute(stmt1,(Cid,Cname,Category,C_spot,I_date,I_time))
                conn.commit()
                t1.insert('','end',text="",values=(Cid,Cname,Category,C_spot,I_date,I_time))
                e1.delete(0,END)
                e2.delete(0,END)
                e3.delete(0,END)
                e4.delete(0,END)
                e5.delete(0,END)
                e6.delete(0,END)
                mb.showinfo("success","Values added")
                newWindow.destroy()
                openAdminWindow()
        add1=Button(tabC, text="Add", width=10, height=1, bg="grey",command=addData)
        add1.place(x=250,y=500)


        def delete_data(t1):
            if not t1.focus():
                mb.showwarning("Warning","Select a row")
            else:
                selected_item=t1.selection()[0]
                Cid=t1.item(selected_item)['values'][0]
                del_query="DELETE FROM CRIME WHERE C_id=:id"
                sel_data=(Cid,)
                cur.execute(del_query,sel_data)
                conn.commit()
                t1.delete(selected_item)
                c.remove(str(Cid))
                mb.showinfo("success","Values deleted")
        del1=Button(tabC, text="Delete", width=10, height=1, bg="grey",command=lambda:delete_data(t1))
        del1.place(x=500,y=500)

        def select_data(t1):
            curItem=t1.focus()
            if not t1.focus():
                mb.showwarning("Warning","Select a row")
            else:
                values=t1.item(curItem,"values")
                e1.insert(0,values[0])
                e2.insert(0,values[1])
                e3.insert(0,values[2])
                e4.insert(0,values[3])
                e5.insert(0,values[4])
                e6.insert(0,values[5])

                def update_data():
                    nonlocal e1,e2,e3,e4,e5,e6,curItem,values
                    Cid=C_id.get()
                    Cname=C_name.get()
                    Category=Cat.get()
                    C_spot=Cspot.get()
                    I_date=Idate.get()
                    I_time=Itime.get()
                    t1.item(curItem,values=(values[0],Cname,Category,C_spot,I_date,I_time))
                    qry="UPDATE CRIME SET C_name= :1,Category= :2,Crime_spot= :3,Incident_date= TO_DATE(:4,'DD-MM-YYYY'),Incident_time= :5 WHERE C_ID= :6"
                    cur.execute(qry,(Cname,Category,C_spot,I_date,I_time,values[0]))
                    conn.commit()
                    e1.delete(0,END)
                    e2.delete(0,END)
                    e3.delete(0,END)
                    e4.delete(0,END)
                    e5.delete(0,END)
                    e6.delete(0,END)
                    mb.showinfo("success","Values updated")

                save1=Button(tabC, text="Save", width=10, height=1, bg="grey",command=lambda:update_data())
                save1.place(x=1000,y=500)
            
        upd1=Button(tabC, text="Update", width=10, height=1, bg="grey",command=lambda:select_data(t1))
        upd1.place(x=750,y=500)

    def victim():
        tabV=ttk.Frame(tabControl)
        canvas=Canvas(tabV,width=1250,height=600)
        canvas.pack(fill="both",expand=True)
        canvas.img=ImageTk.PhotoImage(Image.open("victim.png"))
        canvas.create_image(0,0,image=canvas.img,anchor='nw')
        tabV_newWindow=canvas.create_window(0,90,anchor="nw",window=tabV)
        tabV.place(x=0,y=90)
        tabControl.add(tabV,text='Victim')
        t2 = ttk.Treeview(canvas, selectmode ='browse',height=7)
        t2.place(x=150,y=150)
        #t2.pack()
        verscrlbar = ttk.Scrollbar(canvas,orient ="vertical",command = t2.yview)
        verscrlbar.place(x=1250,y=200,width=20,height=130)
        verscrlbar.pack(side ='right', fill ='x')
        t2.configure(xscrollcommand = verscrlbar.set)
        t2["columns"] = ("1","2","3","4")
        t2['show'] = 'headings'
        t2.heading("1", text ="V_name")
        t2.heading("2", text ="V_age")
        t2.heading("3", text ="F_id")
        t2.heading("4", text ="Gender")
        
        cur.execute("SELECT * FROM VICTIM")
        i=0
        for r in cur:
            t2.insert('',i,text="",values=(r[0],r[1],r[2],r[3]))
            i=i+1
        t2.pack()
        def data():
            cur.execute("SELECT F_ID FROM VICTIM")
            data = []
            for r in cur.fetchall():
                data.append(r[0])
            return data
        v_name=tk.StringVar()
        v_age=tk.StringVar()
        fr_id =tk.StringVar()
        gend=tk.StringVar()
        V_name = Label(tabV,text = "V_name").place(x = 30,y = 450)  
        v1 = Entry(tabV,textvariable=v_name,width = 15)
        v1.place(x = 80,y = 450)
        V_age = Label(tabV,text = "V_age").place(x = 210,y = 450)  
        v2= Entry(tabV,textvariable=v_age,width = 15)
        v2.place(x = 270,y = 450)
        F_id = Label(tabV,text = "F_id").place(x = 420,y = 450)
        var= StringVar()
        v3 = ttk.Combobox( canvas ,textvariable= var )
        v3['values']= f
        v3.place(x = 480,y = 450)
        #v3.pack()
        Gender = Label(tabV,text = "Gender").place(x = 650,y = 450)  
        v4 = Entry(tabV,textvariable=gend,width = 15)
        v4.place(x = 700,y = 450)

        def insert_data2():
            nonlocal v1,v2,v3,v4
            Vname=v_name.get()
            Fid=var.get()
            Vage=v_age.get()
            Gen=gend.get()
            if len(Vname)==0 or len(Fid)==0 or len(Vage)==0 or len(Gen)==0:
                mb.showwarning("Warning","Enter values")
            elif str(Fid) in data():
                mb.showwarning("Warning","F_id already present")
            else:
                stmt2="INSERT INTO VICTIM VALUES(:1,:2,:3,:4)"
                cur.execute(stmt2,(Vname,Vage,Fid,Gen))
                conn.commit()
                t2.insert('','end',text="",values=(Vname,Vage,Fid,Gen))
                
                v1.delete(0,END)
                v2.delete(0,END)
                v3.set('')
                v4.delete(0,END)
                mb.showinfo("success","Values added")
                
        Button(tabV, text="Add", width=10, height=1, bg="grey",command=insert_data2).place(x=250,y=500)

        def delete_data(t2):
            if not t2.focus():
                mb.showwarning("Warning","Select a row")
            else:
                selected_item=t2.selection()[0]
                Fid=t2.item(selected_item)['values'][2]
                del_query="DELETE FROM VICTIM WHERE F_id=:id"
                sel_data=(Fid,)
                cur.execute(del_query,sel_data)
                conn.commit()
                t2.delete(selected_item)
                mb.showinfo("success","Values deleted")
        del2=Button(tabV, text="Delete",width=10, height=1, bg="grey",command=lambda:delete_data(t2))
        del2.place(x=500,y=500)
        
        def select_data(t2):
            curItem=t2.focus()
            if not t2.focus():
                mb.showwarning("Warning","Select a row")
            else:
                values=t2.item(curItem,"values")
                v1.insert(0,values[0])
                v2.insert(0,values[1])
                v3.insert(0,values[2])
                v4.insert(0,values[3])

                def update_data():
                    nonlocal v1,v2,v3,v4,curItem,values
                    Vname=v_name.get()
                    Vage=v_age.get()
                    Fid=var.get()
                    Gen=gend.get()
                    t2.item(curItem,values=(Vname,Vage,values[2],Gen))
                    qry="UPDATE VICTIM SET V_name= :1,V_age= :2,Gender= :3 WHERE F_ID= :4"
                    cur.execute(qry,(Vname,str(Vage),Gen,values[2]))
                    conn.commit()
                    v1.delete(0,END)
                    v2.delete(0,END)
                    v3.set('')
                    v4.delete(0,END)
                    mb.showinfo("success","Values updated")
            
                save2=Button(tabV, text="Save", width=10, height=1, bg="grey",command=lambda:update_data())
                save2.place(x=1000,y=500)
            
        upd2=Button(tabV, text="Update", width=10, height=1, bg="grey",command=lambda:select_data(t2))
        upd2.place(x=750,y=500)
        
    def criminal():
        tabCr=ttk.Frame(tabControl)
        canvas=Canvas(tabCr,width=1250,height=600)
        canvas.pack(fill="both",expand=True)
        canvas.img=ImageTk.PhotoImage(Image.open("criminal.png"))
        canvas.create_image(0,0,image=canvas.img,anchor='nw')
        tabCr_newWindow=canvas.create_window(0,90,anchor="nw",window=tabCr)
        tabControl.add(tabCr,text='Criminal')
        t3 = ttk.Treeview(canvas, selectmode ='browse',height=7)
        t3.place(x=80,y=150)
        t3.pack(side ='right')
        verscrlbar = ttk.Scrollbar(canvas,orient ="vertical",command = t3.yview)
        verscrlbar.pack(side ='right', fill ='x')
        t3.configure(xscrollcommand = verscrlbar.set)
        t3["columns"] = ("1","2","3","4","5","6","7")
        t3['show'] = 'headings'
        t3.column("1",anchor=CENTER,stretch=NO,width=160)
        t3.column("2",anchor=CENTER,stretch=NO,width=160)
        t3.column("3",anchor=CENTER,stretch=NO,width=160)
        t3.column("4",anchor=CENTER,stretch=NO,width=160)
        t3.column("5",anchor=CENTER,stretch=NO,width=160)
        t3.column("6",anchor=CENTER,stretch=NO,width=160)
        t3.column("7",anchor=CENTER,stretch=NO,width=160)

        t3.heading("1", text ="F_name")
        t3.heading("2", text ="Minit")
        t3.heading("3", text ="L_name")
        t3.heading("4", text ="Cr_id")
        t3.heading("5", text ="Crime_id")
        t3.heading("6", text ="Gender")
        t3.heading("7", text ="Status")

        cur.execute("SELECT * FROM CRIMINAL")
        i=0
        for r in cur:
            t3.insert('',i,text="",values=(r[0],r[1],r[2],r[3],r[4],r[5],r[6]))
            i=i+1
        t3.pack()
        def data():
            cur.execute("SELECT CR_ID FROM CRIMINAL")
            data = []
            for r in cur.fetchall():
                data.append(r[0])
            return data        
        f_name=tk.StringVar()
        minit=tk.StringVar()
        l_name=tk.StringVar()
        cr_id=tk.StringVar()
        crime_id=tk.StringVar()
        gndr=tk.StringVar()
        stat=tk.StringVar()
        F_name = Label(tabCr,text = "F_name").place(x = 30,y = 450)  
        c1 = Entry(tabCr,textvariable=f_name,width = 15)
        c1.place(x = 80,y = 450)
        Minit = Label(tabCr,text = "Minit").place(x = 210,y = 450)  
        c2 = Entry(tabCr,textvariable=minit,width = 15)
        c2.place(x = 250,y = 450)
        L_name = Label(tabCr,text = "L_name").place(x = 380,y = 450)  
        c3 = Entry(tabCr,textvariable=l_name,width = 15)
        c3.place(x = 435,y = 450)
        Cr_id = Label(tabCr,text = "Cr_id").place(x = 550,y = 450)  
        c4 = Entry(tabCr,textvariable=cr_id,width = 15)
        c4.place(x = 590,y = 450)
        Crime_id = Label(tabCr,text = "Crime_id").place(x = 715,y = 450)  
        #c5 = Entry(tabCr,textvariable=crime_id,width = 15)
        crime_id= StringVar()
        c5 = ttk.Combobox( canvas ,textvariable= crime_id )
        c5['values']= cr
        c5.place(x = 775,y = 450)
        #c5.pack()
        Gender = Label(tabCr,text = "Gender").place(x = 920,y = 450)  
        c6 = Entry(tabCr,textvariable=gndr,width = 15)
        c6.place(x = 970,y = 450)
        Status = Label(tabCr,text = "Status").place(x = 1090,y = 450)  
        c7 = Entry(tabCr,textvariable=stat,width = 15)
        c7.place(x = 1140,y = 450)
        def insert_data3():
            nonlocal c1,c2,c3,c4,c5,c6,c7
            Fname=f_name.get()
            Minit=minit.get()
            Lname=l_name.get()
            crim=cr_id.get()
            Crimeid=crime_id.get()
            Ge=gndr.get()
            St=stat.get()
            if len(Fname)==0 or len(Lname)==0 or len(crim)==0 or len(Crimeid)==0 or len(Ge)==0:
                mb.showwarning("Warning","Enter values")
            elif str(crim) in data():
                mb.showwarning("Warning","Cr_id already present")
            else:
                '''if len(Fname)==0:
                    mb.showerror("Error","F_name is empty")
                elif len(Lname)==0:
                    mb.showerror("Error","L_name is empty")'''
                stmt3="INSERT INTO CRIMINAL VALUES(:1,:2,:3,:4,:5,:6,:7)"
                cur.execute(stmt3,(Fname,Minit,Lname,crim,Crimeid,Ge,St))
                conn.commit()
                t3.insert('','end',text="",values=(Fname,Minit,Lname,crim,Crimeid,Ge,St))
                c1.delete(0,END)
                c2.delete(0,END)
                c3.delete(0,END)
                c4.delete(0,END)
                c5.set('')
                c6.delete(0,END)
                c7.delete(0,END)
                mb.showinfo("success","Values added")
                newWindow.destroy()
                openAdminWindow()
        Button(tabCr, text="Add", width=10, height=1, bg="grey",command=insert_data3).place(x=250,y=500)

        def delete_data(t3):
            if not t3.focus():
                mb.showwarning("Warning","Select a row")
            else:
                selected_item=t3.selection()[0]
                crim=t3.item(selected_item)['values'][3]
                del_query="DELETE FROM CRIMINAL WHERE Cr_id=:id"
                sel_data=(crim,)
                cur.execute(del_query,sel_data)
                conn.commit()
                t3.delete(selected_item)
                mb.showinfo("success","Values deleted")
                cr.remove(str(crim))
        del3=Button(tabCr, text="Delete", width=10, height=1, bg="grey",command=lambda:delete_data(t3))
        del3.place(x=500,y=500)

        def select_data(t3):
            curItem=t3.focus()
            if not t3.focus():
                mb.showwarning("Warning","Select a row")
            else:
                values=t3.item(curItem,"values")
                
                c1.insert(0,values[0])
                c2.insert(0,values[1])
                c3.insert(0,values[2])
                c4.insert(0,values[3])
                c5.insert(0,values[4])
                c6.insert(0,values[5])
                c7.insert(0,values[6])

                def update_data():
                    nonlocal c1,c2,c3,c4,c5,c6,c7,curItem,values
                    Fname=f_name.get()
                    Minit=minit.get()
                    Lname=l_name.get()
                    crim=cr_id.get()
                    Crimeid=crime_id.get()
                    Ge=gndr.get()
                    St=stat.get()

                    t3.item(curItem,values=(Fname,Minit,Lname,values[3],values[4],Ge,St))
                    qry="UPDATE CRIMINAL SET F_name= :1,Minit= :2,L_name= :3,Gender= :4,Status= :5 WHERE Cr_id= :6"
                    cur.execute(qry,(Fname,Minit,Lname,Ge,St,values[3]))
                    conn.commit()
                    c1.delete(0,END)
                    c2.delete(0,END)
                    c3.delete(0,END)
                    c4.delete(0,END)
                    c5.set('')
                    c6.delete(0,END)
                    c7.delete(0,END)
                    mb.showinfo("success","Values updated")
            
                save3=Button(tabCr, text="Save", width=10, height=1, bg="grey",command=lambda:update_data())
                save3.place(x=1000,y=500)
            
        upd3=Button(tabCr, text="Update", width=10, height=1, bg="grey",command=lambda:select_data(t3))
        upd3.place(x=750,y=500)



    def fir():
        tabF=ttk.Frame(tabControl)
        canvas=Canvas(tabF,width=1250,height=600)
        canvas.pack(fill="both",expand=True)
        canvas.img=ImageTk.PhotoImage(Image.open("fir.png"))
        canvas.create_image(0,0,image=canvas.img,anchor='nw')
        tabF_newWindow=canvas.create_window(0,90,anchor="nw",window=tabF)
        tabControl.add(tabF,text='FIR')
        t4 = ttk.Treeview(canvas, selectmode ='browse',height=7)
        t4.place(x=130,y=150)
        t4.pack(side ='right')
        verscrlbar = ttk.Scrollbar(canvas,orient ="vertical",command = t4.yview)
        verscrlbar.pack(side ='right', fill ='x')
        t4.configure(xscrollcommand = verscrlbar.set)
        t4["columns"] = ("1","2","3","4","5")
        t4['show'] = 'headings'
        t4.heading("1", text ="F_id")
        t4.heading("2", text ="Lodged_date")
        t4.heading("3", text ="Lodged_time")
        t4.heading("4", text ="Cr_id")
        t4.heading("5", text ="Crime_id")
        cur.execute("SELECT F_id,TO_CHAR(Lodged_date,'DD-MM-YYYY'),Lodged_time,Cr_id,Crime_id FROM FIR")
        i=0
        for r in cur:
            t4.insert('',i,text="",values=(r[0],r[1],r[2],r[3],r[4]))
            i=i+1
        t4.pack()
        def data():
            cur.execute("SELECT F_ID FROM FIR")
            data = []
            for r in cur.fetchall():
                data.append(r[0])
            return data 
        
        f_id=tk.StringVar()
        l_date=tk.StringVar()
        l_time=tk.StringVar()
        cd=tk.StringVar()
        crimeid=tk.StringVar()
        F_id = Label(tabF,text = "F_id").place(x = 30,y = 450)  
        f1 = Entry(tabF,textvariable=f_id,width = 15)
        f1.place(x = 80,y = 450)
        Lodged_date = Label(tabF,text = "Lodged_date").place(x = 210,y = 450)  
        f2 = Entry(tabF,textvariable=l_date,width = 15)
        f2.place(x = 290,y = 450)
        Lodged_time = Label(tabF,text = "Lodged_time").place(x = 400,y = 450)  
        f3 = Entry(tabF,textvariable=l_time,width = 15)
        f3.place(x = 480,y = 450)
        Cr_id = Label(tabF,text = "Cr_id").place(x = 620,y = 450)  
        #f4 = Entry(tabF,textvariable=cd,width = 15)
        cd= StringVar()
        f4 = ttk.Combobox( canvas ,textvariable= cd )
        f4['values']= cr
        f4.place(x = 680,y = 450)
        Crime_id = Label(tabF,text = "Crime_id").place(x = 820,y = 450)  
        #f5 = Entry(tabF,textvariable=crimeid,width = 15)
        crimeid= StringVar()
        f5 = ttk.Combobox( canvas ,textvariable= crimeid )
        f5['values']= c
        f5.place(x = 900,y = 450)  
        def insert_data4():
            nonlocal f1,f2,f3,f4,f5
            F_id=f_id.get()
            L_date=l_date.get()
            L_time=l_time.get()
            Cd=cd.get()
            Crimeid=crimeid.get()
            if len(F_id)==0 or len(L_date)==0 or len(L_time)==0:
                mb.showwarning("Warning","Enter values")
            elif str(F_id) in data():
                mb.showwarning("Warning","F_id already present")
            else:
                stmt4="INSERT INTO FIR VALUES(:1,TO_DATE(:2,'DD-MM-YYYY'),:3,:4,:5)"
                cur.execute(stmt4,(F_id,L_date,L_time,Cd,Crimeid))
                conn.commit()
                
                t4.insert('','end',text="",values=(F_id,L_date,L_time,Cd,Crimeid))
                
                f1.delete(0,END)
                f2.delete(0,END)
                f3.delete(0,END)
                f4.set('')
                f5.set('')
                mb.showinfo("success","Values added")
                newWindow.destroy()
                openAdminWindow()
        Button(tabF, text="Add", width=10, height=1, bg="grey",command=insert_data4).place(x=250,y=500)

        def delete_data(t4):
            if not t4.focus():
                mb.showwarning("Warning","Select a row")
            else:
                selected_item=t4.selection()[0]
                Fid=t4.item(selected_item)['values'][0]
                del_query="DELETE FROM FIR WHERE F_id=:id"
                sel_data=(Fid,)
                cur.execute(del_query,sel_data)
                conn.commit()
                t4.delete(selected_item)
                mb.showinfo("success","Values deleted")
                f.remove(str(F_id))
        del4=Button(tabF, text="Delete", width=10, height=1, bg="grey",command=lambda:delete_data(t4))
        del4.place(x=500,y=500)

        def select_data(t4):
            curItem=t4.focus()
            if not t4.focus():
                mb.showwarning("Warning","Select a row")
            else:
                values=t4.item(curItem,"values")
                f1.insert(0,values[0])
                f2.insert(0,values[1])
                f3.insert(0,values[2])
                f4.insert(0,values[3])
                f5.insert(0,values[4])
                def update_data():
                    nonlocal f1,f2,f3,f4,f5,curItem,values
                    F_id=f_id.get()
                    L_date=l_date.get()
                    L_time=l_time.get()
                    Cd=cd.get()
                    Crimeid=crimeid.get()

                    t4.item(curItem,values=(values[0],L_date,L_time,Cd,Crimeid))
                    qry="UPDATE FIR SET Lodged_date= TO_DATE(:1,'DD-MM-YYYY'),Lodged_time= :2,Cr_id=:3,Crime_id=:4 WHERE F_id= :5 "
                    cur.execute(qry,(L_date,L_time,Cd,Crimeid,values[0]))
                    conn.commit()
                    f1.delete(0,END)
                    f2.delete(0,END)
                    f3.delete(0,END)
                    f4.set('')
                    f5.set('')
                    mb.showinfo("success","Values updated")
            
                save4=Button(tabF, text="Save", width=10, height=1, bg="grey",command=lambda:update_data())
                save4.place(x=1000,y=500)
            
        upd4=Button(tabF, text="Update", width=10, height=1, bg="grey",command=lambda:select_data(t4))
        upd4.place(x=750,y=500)


    def police():
        tabP=ttk.Frame(tabControl)
        canvas=Canvas(tabP,width=1250,height=600)
        canvas.pack(fill="both",expand=True)
        canvas.img=ImageTk.PhotoImage(Image.open("pol.png"))
        canvas.create_image(0,0,image=canvas.img,anchor='nw')
        tabP_newWindow=canvas.create_window(0,90,anchor="nw",window=tabP)
        tabControl.add(tabP,text='Police')
        Button(tabP, text="Add", width=10, height=1, bg="grey").place(x=250,y=500)
        Button(tabP, text="Delete", width=10, height=1, bg="grey").place(x=500,y=500)
        t5 = ttk.Treeview(canvas, selectmode ='browse',height=7)
        t5.pack(side ='right')
        verscrlbar = ttk.Scrollbar(canvas,orient ="vertical",command = t5.yview)
        verscrlbar.pack(side ='right', fill ='x')
        t5.configure(xscrollcommand = verscrlbar.set)
        t5["columns"] = ("1","2","3","4","5","6")
        t5['show'] = 'headings'
        t5.heading("1", text ="P_name")
        t5.heading("2", text ="P_id")
        t5.heading("3", text ="Crime_id")
        t5.heading("4", text ="Gender")
        t5.heading("5", text ="P_age")
        t5.heading("6", text ="F_id")
        cur.execute("SELECT * FROM POLICE")
        i=0
        for r in cur:
            t5.insert('',i,text="",values=(r[0],r[1],r[2],r[3],r[4],r[5]))
            i=i+1
        t5.pack()
        def data():
            cur.execute("SELECT P_ID FROM POLICE")
            data = []
            for r in cur.fetchall():
                data.append(r[0])
            return data
        def data1():
            cur.execute("SELECT C_ID FROM CRIME")
            data = []
            for r in cur.fetchall():
                data.append(r[0])
            return data
        pname=tk.StringVar()
        pid=tk.StringVar()
        c_i=tk.StringVar()
        g=tk.StringVar()
        age=tk.StringVar()
        fid=tk.StringVar()
        P_name = Label(tabP,text = "P_name").place(x = 30,y = 450)  
        p1 = Entry(tabP,textvariable=pname,width = 15)
        p1.place(x = 80,y = 450)
        P_id = Label(tabP,text = "P_id").place(x = 210,y = 450)  
        p2 = Entry(tabP,textvariable=pid,width = 15)
        p2.place(x = 270,y = 450)
        Crime_id = Label(tabP,text = "Crime_id").place(x = 400,y = 450)  
        #p3 = Entry(tabP,textvariable=c_i,width = 15)
        c_i= StringVar()
        p3 = ttk.Combobox( canvas ,textvariable= c_i )
        p3['values']= c
        p3.place(x = 470,y = 450)
        Gender = Label(tabP,text = "Gender").place(x = 620,y = 450)  
        p4 = Entry(tabP,textvariable=g,width = 15)
        p4.place(x = 680,y = 450)
        P_age = Label(tabP,text = "P_age").place(x = 820,y = 450)  
        p5 = Entry(tabP,textvariable=age,width = 15)
        p5.place(x = 890,y = 450)
        F_id = Label(tabP,text = "F_id").place(x = 1020,y = 450)  
        #p6 = Entry(tabP,textvariable=fid,width = 15)
        fid= StringVar()
        p6 = ttk.Combobox( canvas ,textvariable= fid )
        p6['values']= f
        p6.place(x = 1060,y = 450)
        #p6.pack()
        def addData5():
            nonlocal p1,p2,p3,p4,p5,p6
            Pname=pname.get()
            Pid=pid.get()
            cid=c_i.get()
            Ge=g.get()
            Age=age.get()
            Fid=fid.get()
            if len(str(Pname))==0 or len(str(Pid))==0 or len(str(cid))==0 or len(str(Ge))==0 or len(str(Age))==0 or len(str(Fid))==0:
                mb.showwarning("Warning","Enter values")
            
            #elif Pid in data():
                #mb.showwarning("Warning","P_id already present")
            else:
                stmt5="INSERT INTO POLICE VALUES(:1,:2,:3,:4,:5,:6)"
                cur.execute(stmt5,(Pname,Pid,cid,Ge,Age,Fid))
                conn.commit()
                
                t5.insert('','end',text="",values=(Pname,Pid,cid,Ge,Age,Fid))
                
                p1.delete(0,END)
                p2.delete(0,END)
                p3.set('')
                p4.delete(0,END)
                p5.delete(0,END)
                p6.set('')
                mb.showinfo("success","Values added")
                newWindow.destroy()
                openAdminWindow()
        Button(tabP, text="Add", width=10, height=1, bg="grey",command=addData5).place(x=250,y=500)

        def delete_data(t5):
            if not t5.focus():
                mb.showwarning("Warning","Select a row")
            else:
                selected_item=t5.selection()[0]
                Pid=t5.item(selected_item)['values'][1]
                del_query="DELETE FROM POLICE WHERE P_id=:id"
                sel_data=(Pid,)
                cur.execute(del_query,sel_data)
                conn.commit()
                t5.delete(selected_item)
                mb.showinfo("success","Values deleted")
        del5=Button(tabP, text="Delete", width=10, height=1, bg="grey",command=lambda:delete_data(t5))
        del5.place(x=500,y=500)

        def select_data(t5):
            curItem=t5.focus()
            if not t5.focus():
                mb.showwarning("Warning","Select a row")
            else:
                values=t5.item(curItem,"values")
                p1.insert(0,values[0])
                p2.insert(0,values[1])
                p3.insert(0,values[2])
                p4.insert(0,values[3])
                p5.insert(0,values[4])
                p6.insert(0,values[5])
                
                def update_data():
                    nonlocal p1,p2,p3,p4,p5,p6,curItem,values
                    Pname=pname.get()
                    Pid=pid.get()
                    cid=c_i.get()
                    Ge=g.get()
                    Age=age.get()
                    Fid=fid.get()

                    t5.item(curItem,values=(Pname,values[1],values[2],Ge,Age,values[5]))
                    qry="UPDATE POLICE SET P_name= :1,Gender= :2,P_age= :3 WHERE P_id= :4"
                    cur.execute(qry,(Pname,Ge,Age,values[1]))
                    conn.commit()
                    p1.delete(0,END)
                    p2.delete(0,END)
                    p3.set('')
                    p4.delete(0,END)
                    p5.delete(0,END)
                    p6.set('')
                    mb.showinfo("success","Values updated")
                save5=Button(tabP, text="Save", width=10, height=1, bg="grey",command=lambda:update_data())
                save5.place(x=1000,y=500)
            
        upd5=Button(tabP, text="Update", width=10, height=1, bg="grey",command=lambda:select_data(t5))
        upd5.place(x=750,y=500)


    def suspect():
        tabS=ttk.Frame(tabControl)
        canvas=Canvas(tabS,width=1250,height=600)
        canvas.pack(fill="both",expand=True)
        canvas.img=ImageTk.PhotoImage(Image.open("suspect.png"))
        canvas.create_image(0,0,image=canvas.img,anchor='nw')
        tabS_newWindow=canvas.create_window(0,90,anchor="nw",window=tabS)
        tabControl.add(tabS,text='Suspect')
        Button(tabS, text="Add", width=10, height=1, bg="grey").place(x=250,y=500)
        Button(tabS, text="Delete", width=10, height=1, bg="grey").place(x=500,y=500)
        t6 = ttk.Treeview(canvas, selectmode ='browse',height=7)
        t6.pack(side ='right')
        verscrlbar = ttk.Scrollbar(canvas,orient ="vertical",command = t6.yview)
        verscrlbar.pack(side ='right', fill ='x')
        t6.configure(xscrollcommand = verscrlbar.set)
        t6["columns"] = ("1","2","3","4","5","6")
        t6['show'] = 'headings'
        t6.heading("1", text ="Crime_id")
        t6.heading("2", text ="S_name")
        t6.heading("3", text ="S_id")
        t6.heading("4", text ="Crime_history")
        t6.heading("5", text ="Gender")
        t6.heading("6", text ="Case_id")
        cur.execute("SELECT * FROM SUSPECT")
        i=0
        for r in cur:
            t6.insert('',i,text="",values=(r[0],r[1],r[2],r[3],r[4],r[5]))
            i=i+1
        t6.pack()
        def data():
            cur.execute("SELECT S_ID FROM SUSPECT")
            data = []
            for r in cur.fetchall():
                data.append(r[0])
            return data
        def data1():
            cur.execute("SELECT CASE_ID FROM COURT")
            data = []
            for r in cur.fetchall():
                data.append(r[0])
            return data
        
        cri_id=tk.StringVar()
        s_name=tk.StringVar()
        s_id=tk.StringVar()
        history=tk.StringVar()
        gen=tk.StringVar()
        court=tk.StringVar()
        Crime_id = Label(tabS,text = "Crime_id").place(x = 30,y = 450)  
        #s1 = Entry(tabS,textvariable=cri_id,width = 15)
        cri_id= StringVar()
        s1 = ttk.Combobox( canvas ,textvariable= cri_id )
        s1['values']= c
        s1.place(x = 90,y = 450)
        #s1.pack()
        S_name = Label(tabS,text = "S_name").place(x = 250,y = 450)  
        s2 = Entry(tabS,textvariable=s_name,width = 15)
        s2.place(x = 310,y = 450)
        S_id = Label(tabS,text = "S_id").place(x = 440,y = 450)  
        s3 = Entry(tabS,textvariable=s_id,width = 15)
        s3.place(x = 480,y = 450)
        Crime_history = Label(tabS,text = "Crime_history").place(x = 600,y = 450)  
        s4 = Entry(tabS,textvariable=history,width = 15)
        s4.place(x = 680,y = 450)
        Gender = Label(tabS,text = "Gender").place(x = 820,y = 450)  
        s5 = Entry(tabS,textvariable=gen,width = 15)
        s5.place(x = 870,y = 450)
        Court_id = Label(tabS,text = "Case_id").place(x = 1000,y = 450)  
        #s6 = Entry(tabS,textvariable=court,width = 15)
        court= StringVar()
        s6 = ttk.Combobox( canvas ,textvariable= court )
        s6['values']= ca
        s6.place(x = 1060,y = 450)
        #s6.pack()
        def addData6():
            nonlocal s1,s2,s3,s4,s5,s6
            crime=cri_id.get()
            sname=s_name.get()
            sid=s_id.get()
            His=history.get()
            gender=gen.get()
            cour=court.get()
            if len(sid)==0 or len(sname)==0 or len(gender)==0:
                mb.showwarning("Warning","Enter values.")
            elif str(sid) in data():
                mb.showwarning("Warning","S_id already present")
            else:

                stmt6="INSERT INTO SUSPECT VALUES(:1,:2,:3,:4,:5,:6)"
                cur.execute(stmt6,(crime,sname,sid,His,gender,cour))
                conn.commit()
                
                t6.insert('','end',text="",values=(crime,sname,sid,His,gender,cour))
                s1.set('')
                s2.delete(0,END)
                s3.delete(0,END)
                s4.delete(0,END)
                s5.delete(0,END)
                s6.set('')
                mb.showinfo("success","Values added")
                newWindow.destroy()
                openAdminWindow()
        Button(tabS, text="Add", width=10, height=1, bg="grey",command=addData6).place(x=250,y=500)

        def delete_data(t6):
            if not t6.focus():
                mb.showwarning("Warning","Select a row")
            else:
                selected_item=t6.selection()[0]
                sid=t6.item(selected_item)['values'][2]
                del_query="DELETE FROM SUSPECT WHERE S_id=:id"
                sel_data=(sid,)
                cur.execute(del_query,sel_data)
                conn.commit()
                t6.delete(selected_item)
                mb.showinfo("success","Values deleted")
                s.remove(str(sid))
        del6=Button(tabS, text="Delete", width=10, height=1, bg="grey",command=lambda:delete_data(t6))
        del6.place(x=500,y=500)

        def select_data(t6):
            curItem=t6.focus()
            if not t6.focus():
                mb.showwarning("Warning","Select a row")
            else:
                values=t6.item(curItem,"values")
                
                s1.insert(0,values[0])
                s2.insert(0,values[1])
                s3.insert(0,values[2])
                s4.insert(0,values[3])
                s5.insert(0,values[4])
                s6.insert(0,values[5])
                
                def update_data():
                    nonlocal s1,s2,s3,s4,s5,s6,curItem,values
                    crime=cri_id.get()
                    sname=s_name.get()
                    sid=s_id.get()
                    His=history.get()
                    gender=gen.get()
                    cour=court.get()

                    t6.item(curItem,values=(values[0],sname,values[2],His,gender,cour))
                    qry="UPDATE SUSPECT SET S_name= :1,Crime_history= :2,Gender= :3,Case_id=:4 WHERE S_id= :5"
                    cur.execute(qry,(sname,His,gender,cour,values[2]))
                    conn.commit()
                    s1.set('')
                    s2.delete(0,END)
                    s3.delete(0,END)
                    s4.delete(0,END)
                    s5.delete(0,END)
                    s6.set('')
                    mb.showinfo("success","Values updated")
                save6=Button(tabS, text="Save", width=10, height=1, bg="grey",command=lambda:update_data())
                save6.place(x=1000,y=500)
            
        upd6=Button(tabS, text="Update", width=10, height=1, bg="grey",command=lambda:select_data(t6))
        upd6.place(x=750,y=500)


    def suspectson():
        tabSu=ttk.Frame(tabControl)
        canvas=Canvas(tabSu,width=1250,height=600)
        canvas.pack(fill="both",expand=True)
        canvas.img=ImageTk.PhotoImage(Image.open("sus.png"))
        canvas.create_image(0,0,image=canvas.img,anchor='nw')
        tabSu_newWindow=canvas.create_window(0,90,anchor="nw",window=tabSu)
        tabControl.add(tabSu,text='Suspects on')
        t7 = ttk.Treeview(canvas, selectmode ='browse',height=7)
        t7.place(x=150,y=150)
        #t7.pack()
        verscrlbar = ttk.Scrollbar(canvas,orient ="vertical",command = t7.yview)
        verscrlbar.pack(side ='right', fill ='x')
        t7.configure(xscrollcommand = verscrlbar.set)
        t7["columns"] = ("1","2","3")
        t7['show'] = 'headings'
        t7.heading("1", text ="P_id")
        t7.heading("2", text ="S_id")
        t7.heading("3", text ="Proof")
        cur.execute("SELECT * FROM SUSPECTS_ON")
        i=0
        for r in cur:
            t7.insert('',i,text="",values=(r[0],r[1],r[2]))
            i=i+1
        t7.pack()
        def data():
            cur.execute("SELECT P_ID FROM POLICE")
            data = []
            for r in cur.fetchall():
                data.append(r[0])
            return data
        def data1():
            cur.execute("SELECT S_ID FROM SUSPECT")
            data = []
            for r in cur.fetchall():
                data.append(r[0])
            return data
        
        po_id=tk.StringVar()
        su_id=tk.StringVar()
        proof=tk.StringVar()
        P_id = Label(tabSu,text = "P_id").place(x = 50,y = 450)  
        #S1 = Entry(tabSu,textvariable=po_id,width = 15)
        po_id= StringVar()
        S1 = ttk.Combobox( canvas ,textvariable= po_id )
        S1['values']= data()
        S1.place(x = 100,y = 450)
        #S1.pack()
        S_id = Label(tabSu,text = "S_id").place(x = 300,y = 450)  
        #S2 = Entry(tabSu,textvariable=su_id,width = 15)
        su_id= StringVar()
        S2 = ttk.Combobox( canvas ,textvariable= su_id )
        S2['values']= s
        S2.place(x = 370,y = 450)
        #S1.pack()
        Proof = Label(tabSu,text = "proof").place(x = 550,y = 450)  
        S3 = Entry(tabSu,textvariable=proof,width = 15)
        S3.place(x = 600,y = 450)
        def addData7():
            nonlocal S1,S2,S3
            pid=po_id.get()
            sid=su_id.get()
            pr=proof.get()
            if len(pid)==0 or len(sid)==0:
                mb.showwarning("warning","Enter values.")
            else:
                
                '''elif len(sid)==0:
                    mb.showerror("Error","S_id is empty")'''

                stmt7="INSERT INTO SUSPECTS_ON VALUES(:1,:2,:3)"
                cur.execute(stmt7,(pid,sid,pr))
                conn.commit()
                
                t7.insert('','end',text="",values=(pid,sid,pr))
                S1.set('')
                S2.set('')
                S3.delete(0,END)
                mb.showinfo("success","Values added")
        Button(tabSu, text="Add", width=10, height=1, bg="grey",command=addData7).place(x=250,y=500)

        def delete_data(t7):
            if not t7.focus():
                mb.showwarning("Warning","Select a row")
            else:
                selected_item=t7.selection()[0]
                sid=t7.item(selected_item)['values'][1]
                del_query="DELETE FROM SUSPECTS_ON WHERE S_id=:1"
                sel_data=(sid,)
                cur.execute(del_query,sel_data)
                conn.commit()
                t7.delete(selected_item)
                mb.showinfo("success","Values deleted")
        del7=Button(tabSu, text="Delete", width=10, height=1, bg="grey",command=lambda:delete_data(t7))
        del7.place(x=500,y=500)

        def select_data(t7):
            curItem=t7.focus()
            if not t7.focus():
                mb.showwarning("Warning","Select a row")
            else:
                values=t7.item(curItem,"values")
                
                S1.insert(0,values[0])
                S2.insert(0,values[1])
                S3.insert(0,values[2])

                def update_data():
                    nonlocal S1,S2,S3,curItem,values
                    pid=po_id.get()
                    sid=su_id.get()
                    pr=proof.get()

                    t7.item(curItem,values=(values[0],values[1],pr))
                    qry="UPDATE SUSPECTS_ON SET Proof= :1 WHERE P_id= :2 AND S_id= :3"
                    cur.execute(qry,(pr,values[0],values[1]))
                    conn.commit()
                    S1.set('')
                    S2.set('')
                    S3.delete(0,END)
                    mb.showinfo("success","Values updated")
                save7=Button(tabSu, text="Save", width=10, height=1, bg="grey",command=lambda:update_data())
                save7.place(x=1000,y=500)
            
        upd7=Button(tabSu, text="Update", width=10, height=1, bg="grey",command=lambda:select_data(t7))
        upd7.place(x=750,y=500)


    def court():
        tabCo=ttk.Frame(tabControl)
        canvas=Canvas(tabCo,width=1250,height=600)
        canvas.pack(fill="both",expand=True)
        canvas.img=ImageTk.PhotoImage(Image.open("court.png"))
        canvas.create_image(0,0,image=canvas.img,anchor='nw')
        tabCo_newWindow=canvas.create_window(0,90,anchor="nw",window=tabCo)
        tabControl.add(tabCo,text='Court')
        t8 = ttk.Treeview(canvas, selectmode ='browse',height=7)
        t8.place(x=150,y=150)
        #t8.pack()
        verscrlbar = ttk.Scrollbar(canvas,orient ="vertical",command = t8.yview)
        verscrlbar.pack(side ='right', fill ='x')
        t8.configure(xscrollcommand = verscrlbar.set)
        t8["columns"] = ("1","2","3","4")
        t8['show'] = 'headings'
        t8.heading("1", text ="Court_name")
        t8.heading("2", text ="Case_id")
        t8.heading("3", text ="Level")
        t8.heading("4", text ="Crime_id")
        cur.execute("SELECT * FROM COURT")
        i=0
        for r in cur:
            t8.insert('',i,text="",values=(r[0],r[1],r[2],r[3]))
            i=i+1
        def data():
            cur.execute("SELECT CASE_ID FROM COURT")
            data = []
            for r in cur.fetchall():
                data.append(r[0])
            return data
        box=['HIGH','SUBORDINATE','DISTRICT']
        t8.pack()
        coname=tk.StringVar()
        ca_id=tk.StringVar()
        lev=tk.StringVar()
        crime=tk.StringVar()
        Court_name = Label(tabCo,text = "Court_name").place(x = 30,y = 450)  
        C1 = Entry(tabCo,textvariable=coname,width = 15)
        C1.place(x = 120,y = 450)
        Case_id = Label(tabCo,text = "Case_id").place(x = 230,y = 450)  
        C2 = Entry(tabCo,textvariable=ca_id,width = 15)
        C2.place(x = 290,y = 450)
        Level = Label(tabCo,text = "Level").place(x = 420,y = 450)
        lev= StringVar()
        C3 = ttk.Combobox( canvas ,textvariable= lev )
        C3['values']=box
        #C3 = Entry(tabCo,textvariable=lev,width = 15)
        C3.place(x = 480,y = 450)
        Crime_id = Label(tabCo,text = "Crime_id").place(x = 650,y = 450)  
        #C4 = Entry(tabCo,textvariable=crime,width = 15)
        crime= StringVar()
        C4 = ttk.Combobox( canvas ,textvariable= crime )
        C4['values']= c
        C4.place(x = 730,y = 450)
        #C4.pack()
        def addData8():
            nonlocal C1,C2,C3
            courname=coname.get()
            case=ca_id.get()
            if len(case)==0:
                mb.showerror("Error","Case_id is empty")
            elif str(case) in data():
                mb.showwarning("Warning","Case_id already present")
            else:
                clev=lev.get()
                crim=crime.get()

                stmt8="INSERT INTO COURT VALUES(:1,:2,:3,:4)"
                cur.execute(stmt8,(courname,case,clev,crim))
                conn.commit()
                
                t8.insert('','end',text="",values=(courname,case,clev,crim))
                C1.delete(0,END)
                C2.delete(0,END)
                C3.set('')
                C4.set('')
                mb.showinfo("success","Values added")
                newWindow.destroy()
                openAdminWindow()
        Button(tabCo, text="Add", width=10, height=1, bg="grey",command=addData8).place(x=250,y=500)

        def delete_data(t8):
            if not t8.focus():
                mb.showwarning("Warning","Select a row")
            else:
                selected_item=t8.selection()[0]
                Courtname=t8.item(selected_item)['values'][0]
                del_query="DELETE FROM COURT WHERE Court_name=:id"
                sel_data=(Courtname,)
                cur.execute(del_query,sel_data)
                conn.commit()
                t8.delete(selected_item)
                mb.showinfo("success","Values deleted")
                ca.remove(str(case))
        del8=Button(tabCo, text="Delete", width=10, height=1, bg="grey",command=lambda:delete_data(t8))
        del8.place(x=500,y=500)

        def select_data(t8):
            curItem=t8.focus()
            if not t8.focus():
                mb.showwarning("Warning","Select a row")
            else:
                values=t8.item(curItem,"values")
                C1.insert(0,values[0])
                C2.insert(0,values[1])
                C3.insert(0,values[2])
                C4.insert(0,values[3])
                
                def update_data():
                    nonlocal C1,C2,C3,C4,curItem,values
                    courname=coname.get()
                    case=ca_id.get()
                    clev=lev.get()
                    crim=crime.get()

                    t8.item(curItem,values=(courname,values[1],clev,values[3]))
                    qry="UPDATE COURT SET Court_name= :1,TYPE= :2 WHERE Case_id= :3"
                    cur.execute(qry,(courname,clev,values[1]))
                    conn.commit()
                    C1.delete(0,END)
                    C2.delete(0,END)
                    C3.set('')
                    C4.set('')
                    mb.showinfo("success","Values updated")
                save8=Button(tabCo, text="Save", width=10, height=1, bg="grey",command=lambda:update_data())
                save8.place(x=1000,y=500)
            
        upd8=Button(tabCo, text="Update", width=10, height=1, bg="grey",command=lambda:select_data(t8))
        upd8.place(x=750,y=500)


    crime()
    victim()
    criminal()
    fir()
    police()
    suspect()
    suspectson()
    court()
    tabControl.pack(expand=1,fill="both")

def openUserWindow():                                             #USER WINDOW
    #nonlocal pwd
    newWindow = Toplevel(login_screen)
    #newWindow=Tk()
    newWindow.title("User Page")
    tabControl=ttk.Notebook(newWindow)
    newWindow.geometry("1250x600")

    def ucrime():
        tabC=ttk.Frame(tabControl)
        canvas=Canvas(tabC,width=1250,height=600)
        canvas.pack(fill="both",expand=True)
        canvas.img=ImageTk.PhotoImage(Image.open("crime.png"))
        canvas.create_image(0,0,image=canvas.img,anchor='nw')
        tabC_newWindow=canvas.create_window(0,90,anchor="nw",window=tabC)
        tabControl.add(tabC,text='Crime')
        Label(tabC, text="Details of the crime",font=("Arial", 12),width=50,height=2,bg="yellow",fg="black").place(x=300,y=120)
        t1 = ttk.Treeview(canvas, selectmode ='browse',height=5)
        t1.pack(side ='right')
        verscrlbar = ttk.Scrollbar(canvas,orient ="vertical",command = t1.yview)
        verscrlbar.pack(side ='right', fill ='x')
        t1.configure(xscrollcommand = verscrlbar.set)
        t1["columns"] = ("1","2","3","4","5","6")
        t1['show'] = 'headings'
        t1.heading("1", text ="C_id")
        t1.heading("2", text ="C_name")
        t1.heading("3", text ="Category")
        t1.heading("4", text ="Crime_spot")
        t1.heading("5", text ="Incident_date")
        t1.heading("6", text ="Incident_time")
        qry="SELECT Crime_id FROM FIR WHERE F_ID = :pw"
        cur.execute(qry,{'pw':pwrd})
        c=cur.fetchone()
        query="SELECT C_id,C_name,Category,Crime_spot,Incident_date,Incident_time FROM CRIME WHERE C_ID = :id"
        cur.execute(query,{'id':c[0]})
        for r in cur:
            t1.insert('',0,text="",values=(r[0],r[1],r[2],r[3],r[4],r[5]))
        t1.pack()
        conn.commit()
        
        
    def uvictim():
        tabV=ttk.Frame(tabControl)
        canvas=Canvas(tabV,width=1250,height=600)
        canvas.pack(fill="both",expand=True)
        canvas.img=ImageTk.PhotoImage(Image.open("victim.png"))
        canvas.create_image(0,0,image=canvas.img,anchor='nw')
        tabV_newWindow=canvas.create_window(0,90,anchor="nw",window=tabV)
        tabControl.add(tabV,text='Victim')
        #Label(login_screen, text="Username * ",bg="grey",fg="white").place(x=200,y=120)
        t2 = ttk.Treeview(canvas, selectmode ='browse',height=5)
        t2.place(x=150,y=150)
        t2.pack(side ='right')
        verscrlbar = ttk.Scrollbar(canvas,orient ="vertical",command = t2.yview)
        verscrlbar.pack(side ='right', fill ='x')
        t2.configure(xscrollcommand = verscrlbar.set)
        t2["columns"] = ("1","2","3","4")
        t2['show'] = 'headings'
        t2.heading("1", text ="V_name")
        t2.heading("2", text ="V_age")
        t2.heading("3", text ="F_id")
        t2.heading("4", text ="Gender")
        v_name=tk.StringVar()
        v_age=tk.StringVar()
        f_id =tk.StringVar()
        gend=tk.StringVar()
        V_name = Label(tabV,text = "V_name").place(x = 30,y = 450)  
        v1 = Entry(tabV,width = 15,textvariable=v_name)
        v1.place(x = 80,y = 450)
        V_age = Label(tabV,text = "V_age").place(x = 210,y = 450)  
        v2 = Entry(tabV,width = 15,textvariable=v_age)
        v2.place(x = 270,y = 450)
        F_id = Label(tabV,text = "F_id").place(x = 400,y = 450)
        v3 = Entry( tabV ,width = 15,textvariable=f_id)
        v3.place(x = 480,y = 450)
        Gender = Label(tabV,text = "Gender").place(x = 600,y = 450)  
        v4 = Entry(tabV,textvariable=gend,width = 15)
        v4.place(x = 680,y = 450)
        query="SELECT V_name,V_age,F_id,Gender FROM VICTIM WHERE F_ID = :pw"
        cur.execute(query,{'pw':pwrd})
        for r in cur:
            t2.insert('',0,text="",values=(r[0],r[1],r[2],r[3]))
        t2.pack()
        conn.commit()
        
        def select_data(t2):
            curItem=t2.focus()
            if not t2.focus():
                mb.showwarning("Warning","Select a row")
            else:
                values=t2.item(curItem,"values")
                v1.insert(0,values[0])
                v2.insert(0,values[1])
                v3.insert(0,values[2])
                v4.insert(0,values[3])

                def update_data():
                    nonlocal v1,v2,v3,v4,curItem,values
                    Vname=v_name.get()
                    Vage=v_age.get()
                    Fid=f_id.get()
                    Gen=gend.get()
                    t2.item(curItem,values=(Vname,Vage,values[2],Gen))
                    qry="UPDATE VICTIM SET V_name= :1,V_age= :2,Gender= :3 WHERE F_ID= :4"
                    cur.execute(qry,(Vname,str(Vage),Gen,values[2]))
                    conn.commit()
                    v1.delete(0,END)
                    v2.delete(0,END)
                    v3.delete(0,END)
                    v4.delete(0,END)
                    mb.showinfo("success","Values updated")
            
                save2=Button(tabV, text="Save", width=10, height=1, bg="grey",command=lambda:update_data())
                save2.place(x=1000,y=500)
            
        upd2=Button(tabV, text="Update", width=10, height=1, bg="grey",command=lambda:select_data(t2))
        upd2.place(x=750,y=500)

    def ufir():
        tabF=ttk.Frame(tabControl)
        canvas=Canvas(tabF,width=1250,height=600)
        canvas.pack(fill="both",expand=True)
        canvas.img=ImageTk.PhotoImage(Image.open("fir.png"))
        canvas.create_image(0,0,image=canvas.img,anchor='nw')
        tabF_newWindow=canvas.create_window(0,90,anchor="nw",window=tabF)
        tabControl.add(tabF,text='FIR')
        Label(tabF, text="Your FIR details.",font=("Arial", 12),width=50,height=2,bg="brown",fg="white").place(x=300,y=120)
        t3 = ttk.Treeview(canvas, selectmode ='browse',height=5)
        t3.place(x=150,y=150)
        t3.pack(side ='right')
        verscrlbar = ttk.Scrollbar(canvas,orient ="vertical",command = t3.yview)
        verscrlbar.pack(side ='right', fill ='x')
        t3.configure(xscrollcommand = verscrlbar.set)
        t3["columns"] = ("1","2","3","4","5")
        t3['show'] = 'headings'
        t3.heading("1", text ="F_id")
        t3.heading("2", text ="Lodged_date")
        t3.heading("3", text ="Lodged_time")
        t3.heading("4", text ="Cr_id")
        t3.heading("5", text ="Crime_id")
        query="SELECT F_id,Lodged_date,Lodged_time,Cr_id,Crime_id FROM FIR WHERE F_ID = :pw"
        cur.execute(query,{'pw':pwrd})
        for r in cur:
            t3.insert('',0,text="",values=(r[0],r[1],r[2],r[3],r[4]))
        t3.pack()
        conn.commit()
        #row=cur.fetchall()
        #print(row)
        #t3.insert('',0,text="",values=(row))
        
    def upolice():
        tabP=ttk.Frame(tabControl)
        canvas=Canvas(tabP,width=1250,height=600)
        canvas.pack(fill="both",expand=True)
        canvas.img=ImageTk.PhotoImage(Image.open("pol.png"))
        canvas.create_image(0,0,image=canvas.img,anchor='nw')
        tabP_newWindow=canvas.create_window(0,90,anchor="nw",window=tabP)
        tabControl.add(tabP,text='Police')
        Label(tabP, text="Details of police assigned to your case.",font=("Arial", 12),width=50,height=2,bg="grey",fg="white").place(x=300,y=120)
        t4 = ttk.Treeview(canvas, selectmode ='browse',height=7)
        t4.place(x=150,y=150)
        t4.pack(side ='right')
        verscrlbar = ttk.Scrollbar(canvas,orient ="vertical",command = t4.yview)
        verscrlbar.pack(side ='right', fill ='x')
        t4.configure(xscrollcommand = verscrlbar.set)
        t4["columns"] = ("1","2","3","4","5","6")
        t4['show'] = 'headings'
        t4.heading("1", text ="P_name")
        t4.heading("2", text ="P_id")
        t4.heading("3", text ="Crime_id")
        t4.heading("4", text ="Gender")
        t4.heading("5", text ="P_age")
        t4.heading("6", text ="F_id")
        query="SELECT P_name,P_id,Crime_id,Gender,P_age,F_id FROM POLICE WHERE F_ID = :pw"
        cur.execute(query,{'pw':pwrd})
        for r in cur:
            t4.insert('',0,text="",values=(r[0],r[1],r[2],r[3],r[4],r[5]))
        t4.pack()
        conn.commit()
    ucrime()
    uvictim()
    ufir()
    upolice()
    tabControl.pack(expand=1,fill="both")

def Loginform():
    global login_screen
    login_screen = Tk()
    login_screen.resizable(False,False)
    canvas=Canvas(login_screen,width=900,height=600)
    image=ImageTk.PhotoImage(Image.open("C:\\Users\\LENOVO\\Desktop\\DBMS\\crime.png"))
    canvas.create_image(0,0,anchor=NW,image=image)
    canvas.pack(fill="both", expand=True)

    login_screen.title("CRIME RECORD MANAGEMENT SYSTEM")
    login_screen.geometry("900x600")
    global  message
    global username
    global password
    global u,p
    username = StringVar()
    password = StringVar()
    message=StringVar()
    Label(login_screen, text="CRIME RECORD MANAGEMENT SYSTEM",font=("Arial", 15),width=50,height=2,bg="grey",fg="white").place(x=200,y=100)
    Label(canvas,width="300", text="Please enter details below", bg="grey",fg="white").pack()
    Label(login_screen, text="Username * ",font=("Arial", 10),bg="grey",fg="white").place(x=300,y=200)
    u=Entry(login_screen, textvariable=username)
    u.place(x=490,y=200)
    Label(login_screen, text="Password * ",font=("Arial", 10),bg="grey",fg="white").place(x=300,y=280)
    p=Entry(login_screen, textvariable=password ,show="*")
    p.place(x=490,y=280)
    Label(login_screen, text="",bg="black",fg="white",font=("Arial", 10),textvariable=message).place(x=390,y=350)
    Button(login_screen, text="Victim login",font=("Arial", 13), width=12, height=2, bg="grey",fg="white",command=Ulogin).place(x=300,y=400)
    Button(login_screen, text="Police login",font=("Arial", 13), width=12, height=2, bg="grey",fg="white",command=Alogin).place(x=490,y=400)
    login_screen.mainloop()
#openUserWindow()

Loginform()

