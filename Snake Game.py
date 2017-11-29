#SNAKE GAME
import random
from tkinter import *





class SnakeGUI():
    def __init__(self):
        self.root=Tk()
        self.root.geometry('600x700')
        self.root.title("THE SNAKE GAME")
        self.RUN=False
        self.dx=0
        self.dy=0
        self.delay=200
        self.width=600
        self.height=600
        self.topframe=Frame(self.root)
        self.topframe.pack()
        self.botframe=Frame(self.root, width=self.width*20, height=self.height*20)
        self.botframe.pack(side=BOTTOM)
        self.canvas=Canvas(self.botframe,width=600, height=600,  bg='black')
        self.canvas.pack()
        self.points=Label(self.topframe, text='Score: ' )
        self.points.pack(side=LEFT)
        self.root.bind('<Up>',self.up)
        self.root.bind('<Down>',self.down)
        self.root.bind('<Left>',self.left)
        self.root.bind('<Right>',self.right)
        self.root.bind('<w>',self.up)
        self.root.bind('<s>',self.down)
        self.root.bind('<a>',self.left)
        self.root.bind('<d>',self.right)
        self.root.bind('<space>',self.spacebar)
        
        self.button=Button(self.botframe,  text= 'Start ' ,command=self.Begin )
        self.button.pack(side=RIGHT)
        
        
        

        
        self.root.mainloop()
    
    def Begin(self):
        self.dx=20
        self.canvas.delete(ALL)
        self.snakegrowth=[(50,60, self.canvas.create_rectangle(80,60,100,80, fill='red'))]
       
        self.point=0
        
        self.x=80
        self.y=60
        self.tempx=random.randrange(0,500,20)
        self.tempy=random.randrange(0,500,20)
        self.RUN=True
        self.run()
        self.food()
        self.head()
        
        if (self.button['text']=='Restart') and (self.RUN==False):
           
            self.RUN=True
            
        elif self.RUN==True:
           
            self.button['text']='Pause'

        
    
        
  
        
        
    def head(self):
        self.newfood()
        
        
        if len(self.snakegrowth) > 0:
            self.canvas.delete(self.snakegrowth[-1][2])
            del self.snakegrowth[-1]

        if self.x>self.width*20 or self.x*20 <0:
            self.canvas.create_text(200,300, text='GAME OVER!!!, score: ' +str(len(self.snakegrowth)),fill='gold')
           
            self.button['text'] = 'RESTART?'
            self.RUN=False

        if self.y>self.height*20 or self.y*20 <0:
            self.canvas.create_text(200,300, text='GAME OVER!!!, score: ' +str(len(self.snakegrowth)),fill='gold')
            
            self.button['text'] = 'RESTART?'
            self.RUN=False

        if self.x==self.width*20 or self.x*20 <0:
            self.canvas.create_text(200,300, text='GAME OVER!!!, score: ' +str(len(self.snakegrowth)),fill='gold')
           
            self.button['text'] = 'RESTART?'
            self.RUN=False    
        if self.y==self.width*20 or self.y*20 <0:
            self.canvas.create_text(200,300, text='GAME OVER!!!, score: ' +str(len(self.snakegrowth)),fill='gold')
           
            self.button['text'] = 'RESTART?'
            self.RUN=False    
        for i in range(len(self.snakegrowth)):
            if self.x==self.snakegrowth[i][0] and self.y == self.snakegrowth[i][1] and i!=0:
                self.canvas.create_text(200,300, text='You hit yourself. GAME OVER!!!, score: ' +str(len(self.snakegrowth)),fill='gold')
                
                self.button['text'] = 'RESTART?'
                self.RUN=False

        self.x+=self.dx
        self.y+=self.dy
        snakegrow= self.canvas.create_rectangle(self.x, self.y, self.x+20, self.y+20, fill='red', tag='dog')
        self.snakegrowth.insert(0,(self.x,self.y,snakegrow))
        
        if self.RUN==True:
            self.canvas.after(self.delay,self.head)                               
                
       
    def food(self):
        self.a=self.tempx= random.randrange(0,500,20)
        self.b=self.tempy=random.randrange(0,500,20)
        self.canvas.create_oval(self.tempx,self.tempy,self.a+20,self.b+20, fill='Orange', tag='mouse')
    

    def newfood(self):
        
        for j in self.snakegrowth:
            
            if self.canvas.coords('mouse')==self.canvas.coords(j[2]):
                self.canvas.delete('mouse')
                self.food()
                self.delay-=4
               
                self.grow()
                
                
    def grow(self):
        
        self.x+=self.dx
        self.y+=self.dy
        snakegrow= self.canvas.create_rectangle(self.x, self.y, self.x+20, self.y+20, fill='red', tag='dog')
        self.snakegrowth.insert(0,(self.x,self.y,snakegrow))
        
        
        
    def up(self,event):
        self.dx=0
        self.dy=-20

    def down(self,event):
        self.dx=0
        self.dy=20
    def left(self,event):
        self.dx=-20
        self.dy=0
    def right(self,event):
        self.dx=20
        self.dy=0
    def move(self):
        if self.up == True:
            self.y+20
            #self.tempy-self.finx
            
         
    def run(self):
        if self.RUN is True:
            self.points['text']='Number of points earned: ' + str(self.point)
        
    def begin_again(self):
           if self.Begin['text']== 'Restart':
               self.restart()
           elif self.RUN==False:
               self.RUN=True
               self.Begin['text']='Pause'
               self.head()
               self.Pause()
           else:
               self.RUN=False 
               self.Begin['text'] = 'Pause'               
           if self.x>self.width*20 or self.x*20<0:
               self.restart()
           if self.y>self.height*20 or self.y*20<0:
               self.restart()
    def Pause(self):
        self.RUN=True
    def spacebar(self,event):
      if self.RUN==False:
          self.RUN=True
          self.Begin['text']= 'Start'
          self.head()
      else:
          self.RUN=False
          self.Begin['text']= 'Start'
    def Restart(self):
        self.root.destroy()
        SnakeGUI()
