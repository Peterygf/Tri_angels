from tkinter import *
from tkinter import ttk
import copy
import  matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np


class Threepoints:  
    """ modeltemplate = [[0.125,1.414],[0.176777,1.414],[0.25,1.414],[0.353553,1.414],[0.5,1.414],[0.707107,1.414]\
        ,[1,1.414],[1.414214,1.414],[2,1.414],[2.828427,1.414],[4,1.414],[5.656854,1.414],[8,1.414],[11.31371,1.414]\
        ,[0.055728,1.618],[0.09017,1.618],[0.145898,1.618],[0.236068,1.618][0.381966,1.618],[0.618034,1.618],\
        [1,1.618],[1.618034,1.618],[2.618034,1.618],[4.236068,1.618],[6.854102,1.618],[11.09017,1.618],[17.94427,1.618],[29.03444,1.618] """

    modeltemplate = [[0.5,1.414],[0.707107,1.414],[1,1.414],[1.414214,1.414],[2,1.414],[2.828427,1.414],[4,1.414],[5.656854,1.414],[8,1.414],[11.31371,1.414],[0.381966,1.618],[0.618034,1.618],[1,1.618],[1.618034,1.618],[2.618034,1.618],[4.236068,1.618],[6.854102,1.618],[11.09017,1.618],[17.94427,1.618],[29.03444,1.618]]

    def __init__(self):
        self.point_a = 0.0 ; self.point_b = 0.0 ; self.point_c = 0.0
        self.full_points = []
        self.similitude_points = []

    def set3points(self,a,b,c):
        self.point_a = a; self.point_b = b; self.point_c = c
        self.cal_points()

    def cal_points(self):
        if self.point_b > self.point_a :     # Save the Moving direction
            direction = 'up'
        else:
            direction = 'down'
        if direction== 'up':                # calculate two bases abs(a-b) or abs(a-c)
            base1 = self.point_b - self.point_a
            base2 = self.point_c - self.point_a
        else:
            base1 = self.point_a - self.point_b
            base2 = self.point_a - self.point_c
        base1_rate = copy.deepcopy(self.modeltemplate)                    # calculate all possible rates
        base2_rate = copy.deepcopy(self.modeltemplate)
        for i in range(len(base1_rate)):
            base1_rate[i][0] = base1_rate[i][0] * base1
        for i in range(len(base2_rate)):
            base2_rate[i][0] = base2_rate[i][0] * base2

        base1_points = []                   # locate all the possible rates to 3 base points
        base2_points = []
        if direction=='up':
            for value,series in base1_rate:
                base1_points.append([self.point_a+value,series])
                base1_points.append([self.point_b+value,series])
                base1_points.append([self.point_c+value,series])
            for value,series in base2_rate:
                base2_points.append([self.point_a+value,series])
                base2_points.append([self.point_b+value,series])
                base2_points.append([self.point_c+value,series])
        else:
            for value,series in base1_rate:
                base1_points.append([self.point_a-value,series])
                base1_points.append([self.point_b-value,series])
                base1_points.append([self.point_c-value,series])
            for value,series in base2_rate:
                base2_points.append([self.point_a-value,series])
                base2_points.append([self.point_b-value,series])
                base2_points.append([self.point_c-value,series])    

        self.full_points = base1_points + base2_points


def output1():
    global precision
    global similitude_points
    global triangel1
    global triangel2
    p1a=0;p1b=0;p1c=0;p2a=0;p2b=0;p2c=0
    try:
        p1a = float(p1.get())
        p1b = float(p2.get())
        p1c = float(p3.get())
        p2a = float(p4.get())
        p2b = float(p5.get())
        p2c = float(p6.get())   
        p_p = p_precision.get()
    except(ValueError):
        text1.delete('1.0','end')
        text1.insert('1.0',"Please input all 6 entries. \n")
    else:
        if p_p == "v_LowPrecision":
            precision = max(abs(p1a-p1b),abs(p2a-p2b))/(100*max(p1a,p1b)/2)
        elif p_p == 'LowPrecision':
            precision = max(abs(p1a-p1b),abs(p2a-p2b))/(100*max(p1a,p1b))
        elif p_p == 'MidPrecision':
            precision = max(abs(p1a-p1b),abs(p2a-p2b))/(100*max(p1a,p1b)*3)
        else:
            precision = max(abs(p1a-p1b),abs(p2a-p2b))/(100*max(p1a,p1b)*6)

        triangel1.set3points(p1a,p1b,p1c)
        triangel2.set3points(p2a,p2b,p2c)

        similitude_points = []
        list_comparations(triangel1.full_points,triangel2.full_points,similitude_points)
        text1.delete('1.0','end')
        text1.insert('1.0',"The result is: (under the precision %.6f"%precision+"\n")
        i=0
        x=[]
        for s1 in similitude_points:
            if s1[0] not in x:
                x.append(s1[0])
        x.sort(reverse = True)

        for s in x:
            print(s)
            if i>3:
                text1.insert('2.0','%.1f'%s+"\n")
                i=1
            else:
                text1.insert('2.0','%.1f'%s+"   ")
                i=i+1


def list_comparations(input_list1,input_list2,output_list):    
    global precision           # define the two values's smilitude standard 
    out_putlist=[]
    for i in input_list1:
        for j in input_list2:
            if abs((i[0]-j[0])/i[0])<=precision:
                output_list.append([j[0],j[1]])

def verify4points():
    global precision
    p1a=0;p1b=0;p1c=0;p1d=0
    try:
        p1a = float(p1.get())
        p1b = float(p2.get())
        p1c = float(p3.get())
        p1d = float(p7.get())
    except(ValueError):
        text1.insert('1.0',"please input right values in all the left 4 entries.\n")
    else:
        p_p = p_precision.get()
        if p_p == "v_LowPrecision":
            precision = abs(p1a-p1b)/(100*max(p1a,p1b)/2)
        elif p_p == 'LowPrecision':
            precision = abs(p1a-p1b)/(100*max(p1a,p1b))
        elif p_p == 'MidPrecision':
            precision = abs(p1a-p1b)/(100*max(p1a,p1b)*3)
        else:
            precision = abs(p1a-p1b)/(100*max(p1a,p1b)*6)

        triangel1 = Threepoints()
        triangel1.set3points(p1a,p1b,p1c)
        output_list = []
        list_comparations(triangel1.full_points,[[p1d,0]],output_list)
        text1.delete("1.0",'end')
        if len(output_list)>0:   
            s=''    
            for i in output_list:
                s=s+str(i[0])+" / "
            text1.insert('1.0','4th Point Passed\nThe point is: '+s+'\n')

        else:
            text1.insert('1.0','No resonance\n')
        text1.insert('end',"with the precision of %.6f"%precision)

def drawline():
    global similitude_points
    global triangel1
    global triangel2

    fig,ax = plt.subplots()
    y1=[triangel1.point_a,triangel1.point_b,triangel1.point_c,triangel2.point_a,triangel2.point_b,triangel2.point_c]
    y2=[]
    j=0
    base = similitude_points[0][0]
    for i in similitude_points:
        y2.append(i[0])

    ax.plot(y1)   
    y2 = sorted(y2)
    ax.plot(y2)
    plt.show()

def check3points():  # checkout the resonance series of the 3 points
    p1a=0;p1b=0;p1c=0
    try:
        p1a = float(p1.get())
        p1b = float(p2.get())
        p1c = float(p3.get())
    except(ValueError):
        text1.delete('1.0','end')
        text1.insert('1.0',"please input right values in all the left 3 entries.\n")
    else:
        a = abs(p1a-p1b)
        b = abs(p1b-p1c)
        c = abs(p1a-p1c)
        text1.delete('1.0','end')
        x=a/b;y=b/a
        text1.insert('1.0',"a|b     %.2f    %.2f\n"%(x,y))
        x=b/c;y=c/b
        text1.insert('2.0',"b|c     %.2f    %.2f\n"%(x,y))
        x=a/c;y=c/a
        text1.insert('3.0',"a|c     %.2f    %.2f\n"%(x,y))




triangel1 = Threepoints()
triangel2 = Threepoints()
precision = 0.0
apply_precision = 0.0
rootwindow = Tk()
rootwindow.attributes("-topmost",1)
rootwindow.title("TriAngls/Peter20220817")
frame1 = ttk.Frame(rootwindow,padding="20 10 0 10")
frame1.title="Verify & Predict"

p1 = StringVar()
p2 = StringVar()
p3 = StringVar()
p4 = StringVar()
p5 = StringVar()
p6 = StringVar()
p7 = StringVar()
p_precision = StringVar()
output = StringVar()
ent1 = ttk.Entry(frame1,textvariable=p1)
ent1.insert(0,"4058.18")
ent2 = ttk.Entry(frame1,textvariable=p2)
ent2.insert(0,"4108.16")
ent3 = ttk.Entry(frame1,textvariable=p3)
ent3.insert(0,"4064.66")
ent4 = ttk.Entry(frame1,textvariable=p4)
ent4.insert(0,"4064.66")
ent5 = ttk.Entry(frame1,textvariable=p5)
ent5.insert(0,"4121.62")
ent6 = ttk.Entry(frame1,textvariable=p6)
ent6.insert(0,"4098.98")
ent7 = ttk.Entry(frame1,textvariable=p7)
but1 = ttk.Button(frame1,text="Predict1",command = output1)
but2 = ttk.Button(frame1,text="Verify",command = verify4points)
text1 = Text(frame1,height=9,width=47)
but3 = ttk.Button(frame1,text="Draw",command = drawline)
comb1 = ttk.Combobox(frame1,textvariable=p_precision,width=10,values = ["v_LowPrecision","LowPrecision","MidPrecision","HighPrecision"])
comb1.current(1)
but4 = ttk.Button(frame1,text="Check3PointsStyle",command=check3points)


ent1.grid(row=0,column = 1)
ent2.grid(row=1,column = 1)
ent3.grid(row=2,column = 1)
ent4.grid(row=0,column = 3,padx = 0)
ent5.grid(row=1,column = 3,padx = 0)
ent6.grid(row=2,column = 3,padx = 0)
ent7.grid(row=4,column = 1,pady=0)
but1.grid(row=0,column=2,padx = 50,sticky=EW)
but2.grid(row = 5,column=1)
text1.grid(row=3,column = 2,columnspan=3,rowspan = 4,sticky=W,padx=20,pady=10)
but3.grid(row=9, column= 3,sticky=EW,padx = 30)
comb1.grid(row=2,column =2)
comb1.state(['readonly'])
but4.grid(row=3,column=1,pady=10)

frame1.grid(column=0,row=0)
rootwindow.mainloop()
