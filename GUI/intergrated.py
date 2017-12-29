from tkinter import *

class App:
	
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()
        Label(frame, text='레이블').grid(row=0, column=0)
        Entry(frame, text='엔트리').grid(row=0, column=1)
        Button(frame, text='버튼', command=self.convert).grid(row=0, column=2)
        check_var = StringVar()
        check = Checkbutton(frame, text='확인버튼', variable=check_var, onvalue='Y', offvalue='N')
        check.grid(row=1, column=0)
        #Listbox
        listbox = Listbox(frame, height=3, selectmode=SINGLE)
        for item in ['빨강', '녹색', '파랑', '노랑', '핑크']:
            listbox.insert(END, item)
        listbox.grid(row=1, column=1)
        #Radiobutton set
        radio_frame = Frame(frame)
        radio_selection = StringVar()
        b1 = Radiobutton(radio_frame, text='portrait', 
            variable=radio_selection, value='P')
        b1.pack(side=LEFT)
        b2 = Radiobutton(radio_frame, text='landscape', 
            variable=radio_selection, value='L')
        b2.pack(side=LEFT)
        radio_frame.grid(row=1, column=2)
        #Scale
        scale_var = IntVar()
        Scale(frame, from_=1, to=20, orient=HORIZONTAL,
              variable=scale_var).grid(row=2, column=0)
        Label(frame, textvariable=scale_var, 
              font=("Helvetica", 72)).grid(row=2, column=1)
        #Message
        message = Message(frame, 
              text='이 곳은 메시지가 출력되는 창입니다.')
        message.grid(row=2, column=2)
        #Spinbox
        Spinbox(frame, values=('a','b','c')).grid(row=3, column=1)

    def convert(self) :
        print("Don't touch my button!!!")

    
root = Tk()
root.wm_title('Kitchen Sink')
app = App(root)
root.mainloop()
