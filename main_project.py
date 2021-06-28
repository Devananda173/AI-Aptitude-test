from tkinter import*
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
import PySimpleGUI as pt
df=pd.read_csv('exams (2).csv')
career=pd.read_csv('Career_Choices.csv')
x=df[['aptitude score']]
y=df[['GradePoints']]
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.3)
rf=RandomForestRegressor()
model=rf.fit(np.array(x_train).reshape(-1,1),np.array(y_train).reshape(-1,1))

pt.theme('DarkTeal9')
layout=[[pt.Text('Rate yourself on the scale of (0-5)on the basis of the following skills',size=(30,0))
        ],[pt.Text('Mathematical ability',size=(40,0)),pt.InputText(key='maths')
            ],
           [pt.Text('Biological sciences',size=(40,0)),pt.InputText(key='bio')
            ],
           [pt.Text('Problem solving',size=(40,0)),pt.InputText(key='ps')
            ],
           [pt.Text('Management and rescerch',size=(40,0)),pt.InputText(key='rnd')
            ],
           [pt.Text('Finance',size=(40,0)),pt.InputText(key='finance')
            ],
           [pt.Button('Submit')]
        ]
window=pt.Window('Form',layout)
while True:
    event,value=window.read()
    
    if event==pt.WIN_CLOSED:
        break
    if event=="Submit":
        cal=value['maths']+value['bio']+value['ps']+value['rnd']+value['finance']
        print(cal)
        cal*=4
       
        r=np.array(rf.predict(np.array([[cal]])))
        print(r)
        root=Tk()
        root.geometry('600x600')
        Label(root, font=("Harlow Solid Italic", 30),text="This interface will provide many Career Options for the students based on there aptitude",fg="black").pack()
        Label(root, font=("Copperplate Gothic Bold", 40),text="Prediction",fg="white",bg="red").pack(pady=30,fill="x")
        if r>=0.9 and r<=1.0 :
            Label(root, font=("Dubai Medium",20),text="Medical    | Engineering      | Management        | Mathematician       | Lawyer  | Data Scientist    | Mobile Application Developer",fg="white" ,bg="black").pack(fill="x")
            Label(root,font=("Dubai Medium",20),text="Pharmacy    | Executive Director      | Researcher     | AI/ML Specialist      | Professor    | Bioinformatics    | Chartered Accountancy",fg="white" ,bg="black").pack(fill="x")
        if (r >=0.7 and r<=0.9) or (r>=0.9 and r<=1.0):
            Label(root,font=("Dubai Medium",20) ,text="HR    | Teaching Assistant    | Sound Engineering    | Sports Officer    | Content Writer    | Brand Analyst    | Campus Ambassador",fg="white" ,bg="black").pack(fill="x")
            Label(root,font=("Dubai Medium",20) ,text="Lab Assistant   | 3-D Modelling   | Web Development    | Finance     | Editor    | Associate   | Digital Sculptor    | Big Data Analyst",fg="white" ,bg="black").pack(fill="x")
        if (r>= 0.5 and r<=0.7) or (r>=0.9 and r<=1.0) or (r >=0.7 and r<=0.9):
            Label(root,font=("Dubai Medium",20) ,text="Sales     | Center head for sports     | Designer     | Marketing    | Pathology    | Blockchain Development     | Humanities    | Mining",fg="white" ,bg="black").pack(fill="x")
            Label(root,font=("Dubai Medium",20) ,text="Anchoring    | Game Development    | Cryptography    | Program Manager    | Journalism     | Copy Writing    | Content Production",fg="white" ,bg="black").pack(fill="x")
        if (r>=0.4 and r<=0.5) or (r>= 0.5 and r<=0.7) or (r>=0.9 and r<=1.0) or (r >=0.7 and r<=0.9):
            Label(root,font=("Dubai Medium",20) ,text="Hotel Management    | Milk Processing Operator    | Plant Engineering    | Nutritionist   | Physical Education   | Podcast Production",fg="white" ,bg="black").pack(fill="x")
            Label(root,font=("Dubai Medium",20) ,text="Enterpreneur     | Psychiatrist     | Receptionist    | Voiceover    | Singing    | Acting    | Dietician     | Culinary Arts    | Choreography",fg="white" ,bg="black").pack(fill="x")    
        if (r>=0.1 and r<=0.4) or (r>=0.4 and r<=0.5) or (r>= 0.5 and r<=0.7) or (r>=0.9 and r<=1.0) or (r >=0.7 and r<=0.9):
            Label(root,font=("Dubai Medium",20) ,text="Ayurveda     | Mountaineer     | Wrestler     | Archer     | Coach     | Chef     | Caterer     | Environmentalist     | Event Manager",fg="white" ,bg="black").pack(fill="x")
            Label(root,font=("Dubai Medium",20) ,text="Interior designing      | Trainer      | Farmer      | Youtuber      | Social Media Influencer      | Food Processing Superviser",fg="white" ,bg="black").pack(fill="x")
            Label(root,font=("Dubai Medium",20) ,text="---X---X---X---X---X---X---",fg="white" ,bg="red").pack(fill="x",pady=10)
        
        
        
        
        break
root.mainloop()
window.close()   

