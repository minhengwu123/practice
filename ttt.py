import tkinter as tk
import itertools
from tkinter import messagebox

class Qipan(tk.Tk):
    def __init__(self):
        super(Qipan,self).__init__()
        self.title('qipan')
        self.geometry('{}x{}'.format(H*P, W*P))
        self._build()
        self._update()
        self.player1 = Player()
        self.player1.turn = True
        self.player2 = Player()

    def _build(self):
        self.canvas = tk.Canvas(self,bg='white', height = H*P, width = W*P)
        for c in range(0, W*P, P):
            x0,y0,x1,y1 = c,0,c,H*P
            self.canvas.create_line(x0,y0,x1,y1)
        for r in range(0,H*P, P):
            x0,y0,x1,y1 = 0,r,H*P, r
            self.canvas.create_line(x0,y0,x1,y1)
        self.canvas.pack()

    def _update(self):
        mid_points = [P/2,P/2+P,P/2+2*P]
        self.floors = ['左上','左左','左下','中上','中中','中下','右上','右右','右下']
        self.buttons = {}
        position = list(itertools.product(mid_points,mid_points))
        for i in range(len(self.floors)):
            self.buttons[self.floors[i]] = Anniu(self, text = ' ', command = lambda f = i: self.hit(f))
            x,y = position[i]
            self.canvas.create_window(x,y, window = self.buttons[self.floors[i]])

    def hit(self, ind):
        if self.player1.turn == True:
            if self.buttons[self.floors[ind]].clicked == False:
                self.buttons[self.floors[ind]].config(text = 'X')
                self.buttons[self.floors[ind]].clicked = True
                self.checker()
                self.player1.turn = False
                self.player2.turn = True
        else:
            if self.buttons[self.floors[ind]].clicked == False:
                self.buttons[self.floors[ind]].config(text = 'O')
                self.buttons[self.floors[ind]].clicked = True
                self.checker()
                self.player2.turn = False
                self.player1.turn = True

    def checker(self):
        if (self.buttons['左上']['text'] == 'X' and  self.buttons['左左']['text'] == 'X' and self.buttons['左下']['text'] == 'X') or \
            (self.buttons['左上']['text'] == 'X' and self.buttons['中上']['text'] == 'X' and self.buttons['右上']['text'] == 'X') or \
            (self.buttons['左上']['text'] == 'X' and self.buttons['中中']['text'] == 'X' and self.buttons['右下']['text'] == 'X') or \
            (self.buttons['中上']['text'] == 'X' and self.buttons['中中']['text'] == 'X' and self.buttons['中下']['text'] == 'X') or \
            (self.buttons['右上']['text'] == 'X' and self.buttons['中中']['text'] == 'X' and self.buttons['左下']['text'] == 'X') or \
            (self.buttons['右上']['text'] == 'X' and self.buttons['右右']['text'] == 'X' and self.buttons['右下']['text'] == 'X') or \
            (self.buttons['左左']['text'] == 'X' and self.buttons['右右']['text'] == 'X' and self.buttons['右右']['text'] == 'X') or \
            (self.buttons['左下']['text'] == 'X' and self.buttons['中下']['text'] == 'X' and self.buttons['右下']['text'] == 'X'):
            messagebox.showinfo(message = 'game ended， X win')
            self.destroy()
        else:
            if (self.buttons['左上']['text'] == 'O' and  self.buttons['左左']['text'] == 'O' and self.buttons['左下']['text'] == 'O') or \
            (self.buttons['左上']['text'] == 'O' and self.buttons['中上']['text'] == 'O' and self.buttons['右上']['text'] == 'O') or \
            (self.buttons['左上']['text'] == 'O' and self.buttons['中中']['text'] == 'O' and self.buttons['右下']['text'] == 'O') or \
            (self.buttons['中上']['text'] == 'O' and self.buttons['中中']['text'] == 'O' and self.buttons['中下']['text'] == 'O') or \
            (self.buttons['右上']['text'] == 'O' and self.buttons['中中']['text'] == 'O' and self.buttons['左下']['text'] == 'O') or \
            (self.buttons['右上']['text'] == 'O' and self.buttons['右右']['text'] == 'O' and self.buttons['右下']['text'] == 'O') or \
            (self.buttons['左左']['text'] == 'O' and self.buttons['右右']['text'] == 'O' and self.buttons['右右']['text'] == 'O') or \
            (self.buttons['左下']['text'] == 'O' and self.buttons['中下']['text'] == 'O' and self.buttons['右下']['text'] == 'O'):
                messagebox.showinfo(message = 'game ended， O win')
                self.destroy()



class Anniu(tk.Button):
    def __init__(self, *args,**kwargs):
        tk.Button.__init__(self,*args, **kwargs)
        self.clicked = False

class Player():
    def __init__(self):
        self.turn = None
        self.own = []


if __name__ == '__main__':
    H = 3
    W = 3
    P = 40
    env = Qipan()
    env.mainloop()