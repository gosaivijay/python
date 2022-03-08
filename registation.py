from tkinter import *
from tkinter.ttk import * #combo box
from tkinter import scrolledtext #scrolled text

top=Tk()
top.title('Registration Form')
top.geometry('900x450')


label1=Label(top,text='Name',padding=(4,2))
label1.grid(column=0,row=0)
label2=Label(top,text='Password',padding=(4,2))
label2.grid(column=0,row=1)
label3=Label(top,text='Conform Password',padding=(4,2))
label3.grid(column=0,row=3)
label4=Label(top,text='First Name',padding=(4,2))
label4.grid(column=0,row=5)
label5=Label(top,text='Last Name',padding=(4,2))
label5.grid(column=0,row=6)
label6=Label(top,text='Phone ',padding=(4,2))
label6.grid(column=3,row=0)
label7=Label(top,text='Email',padding=(4,2))
label7.grid(column=3,row=1)
label8=Label(top,text='Age',padding=(4,2))
label8.grid(column=3,row=5)

label9=Label(top,text='fees',padding=(4,2))
label9.grid(column=6,row=6)
text9=Entry(top,width=20)
text9.grid(column=7,row=6)


text1=Entry(top,width=20,)
text1.grid(column=1,row=0)
text2=Entry(top,width=20)
text2.grid(column=1,row=1)
text3=Entry(top,width=20)
text3.grid(column=1,row=3)
text4=Entry(top,width=20)
text4.grid(column=1,row=5)
text5=Entry(top,width=20)
text5.grid(column=1,row=6)
text6=Entry(top,width=20)
text6.grid(column=4,row=0)
text7=Entry(top,width=20)
text7.grid(column=4,row=1)
text8=Entry(top,width=20)
text8.grid(column=4,row=5)


#combo box
label10=Label(top,text='City')
label10.grid(column=3,row=3)
combo=Combobox(top)
combo['values']=('Hyderabad','Delhi','Mumbai','Bangalore')
combo.current()
combo.grid(column=4,row=3)

label11=Label(top,text='country')
label11.grid(column=6,row=0)
combo=Combobox(top)
combo['values']=('America','New Zealand','India','Australia','Canada')
combo.current()
combo.grid(column=7,row=0)


label12=Label(top,text='Material Status')
label12.grid(column=6,row=1)
combo=Combobox(top)
combo['values']=('Married','Unmarried',)
combo.current()
combo.grid(column=7,row=1)

#radio button
label13=Label(top,text='Gender')
label13.grid(column=0,row=8)
s=IntVar()
radio1=Radiobutton(top,text='Male',value=1,variable=S)
radio2=Radiobutton(top,text='Female',value=2,variable=S)
radio1.grid(column=1,row=8)
radio2.grid(column=2,row=8)

#list box 14


label14=Label(top,text='Hobbies',padding=(4,2))
label14.grid(column=3,row=6)
lb=Listbox(top)
lb.grid(column=4,row=6)
lb.insert(1,'Reading')
lb.insert(2,'Singing')
lb.insert(3,'Playing')
lb.insert(4,'Sleeping')


#scrolled text

label15=Label(top,text='Address',padding=(4,2))
label15.grid(column=6,row=3)
text=scrolledtext.ScrolledText(top,width=20,height=4)
text.grid(column=7,row=3)



Button(top,text='Submit').grid(column=10,row=9,sticky=W,pady=10)











