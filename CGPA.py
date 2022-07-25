from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
import json
from functools import partial
from scrollFrame import *

# ----- CHANGE YOUR GRADE POINTS and ADD YOUR GRADES HERE ----- #
#GRADES = {
#    'A+': 9,
#    'A': 8,
#    'B+': 7,
#    'B': 6,
#    'C+': 5,
#    'C': 4,
#    'E': 0,
#    'F': 0,
#    'G': 0,
#    'I': 0,
#}

GRADES = {
'EX': 10,
    'A': 9,
    'B': 8,
    'C': 7,
    'D': 6
}
# ------ #

GRADE = tuple([k for k in GRADES.keys()])

class Login:
    def __init__(self, root):
        self.root = root
        root.resizable(False,False)
        self.root.title("Login")
        head = Frame(root)
        head.pack(fill='x', pady=10)
        Label(head, text='Welcome to K.RAMAKRISHNAN College of Engineering', font="constantia 12", fg="dark slate gray").pack(padx=2)
        Label(head, text='CGPA Calculator', font="constantia 12", fg="dark slate gray").pack(padx=2)
        Label(head, text=' -BY Department of Information Technology', font="constantia 11", fg="dark slate gray").pack(padx=2)
          
        sideFrame = Frame(self.root)
        sideFrame.pack(side='left',padx=10, pady=10)
        frame = Frame(self.root)
        frame.pack(side='right', padx=10, pady=10)
        

        nl = LabelFrame(frame, text='Name', font="constantia 10")
        nl.pack(anchor='w')
        name = Entry(nl, font="constantia 10", width=40)
        name.pack()

        rl = LabelFrame(frame, text='Roll No', font="constantia 10")
        rl.pack(anchor='w')
        roll_no = Entry(rl, font="constantia 10", width=40)
        roll_no.pack()

        # pl = LabelFrame(frame, text='Password', font="constantia 10")
        # pl.pack(anchor='w')
        # password = Entry(pl, font="constantia 10", width=40, show='*')
        # password.pack()
        

        Button(frame, text='Login', font="constantia 10", bg='lightgreen', command=lambda: self.login(name.get(), roll_no.get())).pack(anchor='w', padx=2, pady=2)
        image = PhotoImage(file='user.png')
        image.zoom(8, 8)
        Label(sideFrame, image=image).pack()  


        self.root.mainloop()
    
    def login(self, n, r):
        found = True
        det = []
        # print(n, r, p)
        # with open("users.json", 'r') as file:
        #     users = json.loads(file.read())
        #     for user in users:
        #         # print(user)
        #         if user['name'].lower() == n.lower() and user['roll_no'].lower() == r.lower() and user['password'] == p:
        #             found = True
        #             det = [user['name'], user['roll_no']]
        #    
        if n == "": 
            showinfo("ERROR", "Please enter your Name to login!")
            return
        elif r == "": 
            showinfo("ERROR", "Please enter your Roll No. to login!")
            return
        # elif p == "": 
        #     showinfo("ERROR", "Please enter the password to login!")
        #     return

        if found:
            self.root.destroy()
            # GPA(Tk(), det[0], det[1])
            GPA(Tk(), n.upper(), r.upper())

class GPA:
    def __init__(self, root, name, roll_no):
        self.root = root
        self.root.title("CGPA")
        height = self.root.winfo_screenheight() - 100
        width = self.root.winfo_screenwidth()
        self.root.geometry("%dx%d" % (width, height))
        mainFrame = Frame(self.root, bg="lavender")
        mainFrame.pack()
        head = Frame(mainFrame)
        head.pack(fill='x', padx=4, pady=2)
        headBy = Frame(head)
        headBy.pack(side='left')
        Label(headBy, text='CGPA Calculator', font="constantia 12", fg="dark slate gray").pack(anchor='w', padx=2, pady=2)
        Label(headBy, text=' -BY Department of Information Technology', font="constantia 11", fg="dark slate gray").pack(anchor='w', padx=2, pady=2)
        headAns = Frame(head)
        headAns.pack(side='left', anchor='w', padx=15)
        Label(headAns, text='CGPA: ', font="constantia 11").pack(anchor='w',side='left')
        self.CGPA = Label(headAns, text='0.0', font="constantia 12", bg='lightgreen', width=10)
        self.CGPA.pack(anchor='w', padx=4, pady=2, side='left')
        
        Button(headAns, text='Calculate CGPA',font="constantia 10", bg="lightgreen", command=self.calculateCGPA).pack()

        header = LabelFrame(mainFrame, text='Student Details', font="constantia 11", bg="lavender")
        header.pack(padx=12, pady=2, fill='x')

        Label(header, text='Name: ' + name, font="constantia 10", bg="lavender").pack(side='left', anchor='w', padx=2, pady=2)
        Label(header, text=' | ', font="constantia 10", bg="lavender").pack(side='left', anchor='w', padx=2, pady=2)
        Label(header, text='Roll No: ' + roll_no, font="constantia 10", bg="lavender").pack(side='left', anchor='w', padx=2, pady=2)
        
        body = ScrollableFrame(mainFrame, width=width, height=height)
        #body.attributes('-fullscreen', True)
        body.pack(padx=4,pady=4, fill=BOTH, expand=YES)

        # body = Frame(mainFrame, bg='misty rose', highlightbackground='gray',highlightthickness='1')
        # body.pack(padx=4,pady=4)
        # bodyLeft = Frame(body, bg='misty rose')
        # bodyLeft.pack(side='left',padx=5, pady=5, anchor='w')
        
        # bodyRight = Frame(body, bg='misty rose')
        # bodyRight.pack(side='right',padx=5, pady=5, anchor='w')

        with open('semesters.json', 'r') as file:
            self.data = json.loads(file.read())

            for i in range(len(self.data)):
                if i%2 == 0:
                    subBody = Frame(body.frame, bg='misty rose')
                    subBody.pack(side='left', padx=5, pady=5, anchor='nw')
                sem = self.data[i]
                sem['GPA'] = 0.0
                # print(sem)
                # if (i < 2):
                #     semFrame = Frame(bodyLeft, bg="misty rose", highlightbackground='gray',highlightthickness='1')
                #     semFrame.pack(anchor='sw', fill=BOTH)
                # else:
                #     semFrame = Frame(bodyRight, bg="misty rose", highlightbackground='gray',highlightthickness='1')
                #     semFrame.pack(anchor='nw', fill=BOTH)
                semFrame = Frame(subBody, bg="misty rose", highlightbackground='gray',highlightthickness='1')
                semFrame.pack(anchor='nw', fill=BOTH)
                Label(semFrame, text='Semester ' + str(sem['sem']), font="constantia 10", bg="misty rose").grid(row=0, columnspan=4, sticky='W', pady=4)
                Label(semFrame, text='Course Code', font="constantia 10", bg='lightgreen').grid(row=1, column=0, sticky='NESW')
                Label(semFrame, text='Course Title', font="constantia 10", bg='lightgreen').grid(row=1, column=1, sticky='NESW')
                Label(semFrame, text='Credit', font="constantia 10", bg='lightgreen').grid(row=1, column=2, sticky='NESW')
                Label(semFrame, text='Grade Obtained', font="constantia 10", bg='lightgreen').grid(row=1, column=3, sticky='NESW')
                # ------------
                for c in range(len(sem['courses'])):
                    course = sem['courses'][c]
                    if (len(course['code']) <= 0):
                        course['code'] = ttk.Combobox(semFrame, width=5, justify=CENTER, textvariable = course['code'], postcommand=partial(self.codeChange, sem['courses'][c]))
                        course['code']['values'] = tuple([j['code'] for j in course['extra']])
                        course['code'].bind('<<ComboboxSelected>>', partial(self.codeChange, course))
                        course['code'].grid(row=c+2, column=0, sticky='nsew', padx=2)
                    else:
                        Label(semFrame, text=course['code'], font="constantia 10", bg="misty rose").grid(row=c+2, column=0)
                    course['title'] = Label(semFrame, text=course['title'], font="constantia 10", bg="misty rose")
                    course['title'].grid(row=c+2, column=1, sticky='w')
                    Label(semFrame, text=course['credits'], font="constantia 10", bg="misty rose").grid(row=c+2, column=2)
                    sem['courses'][c]['grade'] = StringVar()
                    e = ttk.Combobox(semFrame, textvariable = sem['courses'][c]['grade'])
                    e['values'] = GRADE
                    # e = Entry(semFrame, font="constantia 10", bg="misty rose")
                    e.grid(row=c+2, column=3)
                Button(semFrame, text='Calculate GPA', command=partial(self.calculate, i), font="constantia 9", bg="lightgreen").grid(row=len(sem['courses'])+2)
                sem['GPA'] = Label(semFrame, text="0.0", font="constantia 10")
                sem["GPA"].grid(row=len(sem['courses'])+2, column=1, pady=2, sticky='NESW')
                

        self.root.mainloop()
    
    def getExtra(self, code, extra):
        for i in range(len(extra)):
            if (extra[i]['code'] == code):
                return i
        return -1
    
    def codeChange(self, sem, event):
        # print("CHANGE", sem['code'].get())
        sem['title']['text'] = sem['extra'][self.getExtra(sem['code'].get(), sem['extra'])]['title']
        # print(sem['code'].get())
    
    def calculate(self, index):
        # print(index)
        gradePoints = 0
        for d in self.data[index]['courses']:
            if (len(d['grade'].get()) <= 0):
                showerror('ERROR', "Please select Grade for all the courses!")
                return
            gradePoints += (d['credits'] * GRADES[d['grade'].get()])
            # print(d['grade'].get())
        GPA = gradePoints / self.data[index]['totalCredits']
        self.data[index]['GPA']['text'] = round(GPA, 2)
        print(gradePoints, self.data[index]['totalCredits'],  GPA)
    
    def calculateCGPA(self):
        totalCredits = 0
        gradePoints = 0
        cnt = 0
        for d in self.data:
            if d['GPA']['text'] != '0.0':
                cnt += 1
            else:
                if cnt > 0: break
        if cnt < 2: 
            showinfo('INFO', "Please calculate atleast 2 following semesters GPA or even semesters GPA!")
            return
        lastGradePoints = 0
        for i in range(len(self.data)):
            d = self.data[i]
            # if d['GPA']['text'] == '0.0':
            #     showinfo('INFO', "Please first calculate all semester GPA!")
            #     return
            totalCredits += int(d['totalCredits'])
            lastGradePoints = gradePoints
            for c in d['courses']:
                if (len(c['grade'].get()) <= 0):
                    if (i < 2):
                        showerror('ERROR', "Please select Grades for atleast 2 semesters!")
                        return
                    gradePoints = lastGradePoints
                    totalCredits -= int(d['totalCredits'])
                    break
                gradePoints += (c['credits'] * GRADES[c['grade'].get()])
        CGPA = gradePoints / totalCredits
        print(totalCredits, gradePoints, CGPA)
        self.CGPA['text'] = round(CGPA, 2)

        
if __name__ == '__main__':
    # GPA(Tk(), '-', '-')
    Login(Tk())


