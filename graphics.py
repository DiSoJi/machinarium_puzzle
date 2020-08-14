from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from find_sol import *
from state_diag import *
import sys
import time

class Aplicacion():
    def __init__(self):
        self.raiz = Tk()
        self.raiz.title('Machinarium - Outside the prison')
        self.raiz.geometry('980x623')
        self.raiz.resizable(1,1)
        self.auto = -1
        background_image=PhotoImage(file="fondo2.png")
        background_label = Label(self.raiz, image=background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        
        self.test = find_solution()
        self.position=0
        
        s = Style()
        s.configure('My.TFrame', background='#000000')
        self.marco = ttk.Frame(self.raiz, borderwidth=-10,height=50,width=45,style='My.TFrame')
        self.marco.grid(padx=258, pady=190,column=1, row=0)
        background_image2=PhotoImage(file="fondo_frame.png")
        background_label = Label(self.marco, image=background_image2)
        background_label.place(x=0, y=0)
        
        self.marco2 = ttk.Frame(self.raiz, borderwidth=0,height=20,width=50,style='My.TFrame')
        self.marco2.grid(padx=401, ipady=25,column=1, row=0,sticky='s')

        self.marco3 = ttk.Frame(self.raiz, borderwidth=0,height=20,width=50)
        self.marco3.grid(padx=0, pady=130,column=1, row=0,sticky='n')
        
        self.down_arrow=PhotoImage(file="down_arrow2.png",height=32,width=32)
        self.empty=PhotoImage(file="circle2.png",height=32,width=32)
        self.up_arrow=PhotoImage(file="up_arrow2.png",height=32,width=32)
        self.ImageArray=[self.down_arrow,self.down_arrow,self.down_arrow,self.empty,self.up_arrow,self.up_arrow,self.up_arrow]
        
        self.Imagen0=ttk.Label(self.marco, image=self.ImageArray[0],justify=CENTER)
        self.Imagen1=ttk.Label(self.marco, image=self.ImageArray[1],justify=CENTER)
        self.Imagen2=ttk.Label(self.marco, image=self.ImageArray[2],justify=CENTER)
        self.Imagen3=ttk.Label(self.marco, image=self.ImageArray[3],justify=CENTER)
        self.Imagen4=ttk.Label(self.marco, image=self.ImageArray[4],justify=CENTER)
        self.Imagen5=ttk.Label(self.marco, image=self.ImageArray[5],justify=CENTER)
        self.Imagen6=ttk.Label(self.marco, image=self.ImageArray[6],justify=CENTER)
        self.WidgetArray=[self.Imagen0,self.Imagen1,self.Imagen2,self.Imagen3,self.Imagen4,self.Imagen5,self.Imagen6]

        self.Step0=ttk.Label(self.marco3, text="",justify=CENTER)
        
        self.restart1 = ttk.Button(self.marco2, text="Reiniciar", 
                                 padding=(5,5), command=self.InitialState)
        self.exit1 = ttk.Button(self.marco2, text="Salir", 
                                 padding=(5,5), command=quit)
        self.next1 = ttk.Button(self.marco2, text="Siguiente", 
                                 padding=(5,5), command=self.NextState)
        self.back1 = ttk.Button(self.marco2, text="Anterior", 
                                 padding=(5,5), command=self.BackState)
        self.diag = ttk.Button(self.marco2, text="Diagrama", 
                                 padding=(5,5), command=self.openDiag)
        self.automatic1 = ttk.Button(self.marco2, text="Automatico", 
                                 padding=(5,5), command=self.AutomaticState)
        
        self.back1.grid(column=0, row=1)
        self.restart1.grid(column=0, row=2)
        self.exit1.grid(column=0, row=3)
        self.next1.grid(column=1, row=1)
        self.diag.grid(column=1,row=3)
        self.automatic1.grid(column=1, row=2)

        self.Step0.grid(column=2, row=7)
        self.Step0.config(text="Movimiento: 0 / "+str(len(self.test)))
        
        self.WidgetArray[0].grid(column=2, row=0)
        self.WidgetArray[1].grid(column=2, row=1)
        self.WidgetArray[2].grid(column=2, row=2)
        self.WidgetArray[3].grid(column=2, row=3)
        self.WidgetArray[4].grid(column=2, row=4)
        self.WidgetArray[5].grid(column=2, row=5)
        self.WidgetArray[6].grid(column=2, row=6)
        
        self.raiz.mainloop()

    def AutomaticState(self):
        self.cont=0
        self.auto *= -1
        while self.cont<len(self.test) and self.position<len(self.test) and self.auto == 1:
            self.Step0.config(text="Movimiento: "+str(self.cont+1)+" / "+str(len(self.test)))
            self.NextState()
            self.cont+=1
            self.raiz.update()
            time.sleep(1)
        self.auto = -1
            
    def openDiag(self):
        open_app()
        
        
    def InitialState(self):
        self.restart1.config(state=DISABLED)
        self.back1.config(state=DISABLED)
        self.cont=len(self.test)-1
        while (self.cont>=0):
            self.cont-=1
            self.BackState()
        self.Step0.config(text="Movimiento: 0 / "+str(len(self.test)))
            
    
    def NextState(self):
        self.restart1.config(state=NORMAL)
        self.back1.config(state=NORMAL)
        self.restart1.config(state=NORMAL)
        if self.position<len(self.test):
            self.Step0.config(text="Movimiento: "+str(self.position+1)+" / "+str(len(self.test)))
            tokena=self.ImageArray[self.test[self.position][0]]
            tokenb=self.ImageArray[self.test[self.position][1]]
            
            self.ImageArray[self.test[self.position][0]]=tokenb
            self.ImageArray[self.test[self.position][1]]=tokena

            self.WidgetArray[self.test[self.position][0]].config(image=self.ImageArray[self.test[self.position][0]])
            self.WidgetArray[self.test[self.position][1]].config(image=self.ImageArray[self.test[self.position][1]])
            self.position+=1
        else:
            self.next1.config(state=DISABLED)
            
    def BackState(self):
        self.next1.config(state=NORMAL)
        self.restart1.config(state=NORMAL)
        if (self.position<=len(self.test))and(self.position!=0):
            self.position-=1
            self.Step0.config(text="Movimiento: "+str(self.position)+" / "+str(len(self.test)))
            tokena=self.ImageArray[self.test[self.position][0]]
            tokenb=self.ImageArray[self.test[self.position][1]]
            
            self.ImageArray[self.test[self.position][0]]=tokenb
            self.ImageArray[self.test[self.position][1]]=tokena

            self.WidgetArray[self.test[self.position][0]].config(image=self.ImageArray[self.test[self.position][0]])
            self.WidgetArray[self.test[self.position][1]].config(image=self.ImageArray[self.test[self.position][1]])
        else:
            self.Step0.config(text="Movimiento: 0 / "+str(len(self.test)))

def main():
    mi_app = Aplicacion()
    return 0

if __name__ == '__main__':
    main()
