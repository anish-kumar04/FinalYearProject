from tkinter import *
#from tkinter import messagebox
from tkinter import scrolledtext

root = Tk()
root.title("Monitoring System")
root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
root.configure(background="rosy brown")

#design of root window
btnDataSet=Button(root, text='Load Dataset', font=("arial",16,'bold'), width=20)
btnRSW=Button(root, text='Remove Stop Words', font=("arial",16,'bold'), width=20)
btnLem=Button(root, text='Lemmatization', font=("arial",16,'bold'), width=20)
btnSA=Button(root, text='Sentiment Analysis', font=("arial",16,'bold'), width=20)
btnCheck=Button(root, text='Check', font=("arial",16,'bold'), width=20)
display=scrolledtext.ScrolledText(root,width=180,height=40)

btnDataSet.place(x=20, y=20)
btnRSW.place(x=300, y=20)
btnLem.place(x=580,y=20)
btnSA.place(x=860, y=20)
btnCheck.place(x=1140, y=20)
display.place(x=10, y=90)

root.mainloop()