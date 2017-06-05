#This program was my second idea, involving a canvas
from Tkinter import *
from ctypes import windll

class Application:
        
    def __init__(self, master, primes):
        self.size = [0,0,0]
        self.primes = []
        self.frame = Frame(master)
        self.frame.pack()
        
        #Canvas where black dots will be placed
        self.img = PhotoImage(width=self.size[1], height=self.size[0])
        self.canvas = Canvas(self.frame, width=self.size[0], height=self.size[1])
        self.canvas.pack()
        
        #Text for numRange
        Label(self.frame, text="Max Number Range:", font=("Helvetica", 10, "bold")).pack(side=LEFT)
        
        #numRange user input
        self.entry = Entry(self.frame, font=("Helvetica", 10))
        self.entry.pack(side=LEFT)
        
        #numRange user input confirmation
        Button(self.frame, text='Enter', font=("Helvetica", 10), command=self.entryGet).pack(side=LEFT)

        #Button to exit canvas
        Button(self.frame, text="Quit", font=("Helvetica", 10), command=master.destroy).pack(side=RIGHT)

        #Ownership
        Label(self.frame, text="Made by Julian Meyn", font=("Helvetica", 5)).pack(side=RIGHT, anchor=S)
        
        self.frame.mainloop()
        
        
    def entryGet(self):
        try:
            self.maxRange = int(self.entry.get())
        except TypeError:
            print 'Unknown integer value %s.' % self.maxRange 
    
        self.size[0] = sqrt(self.maxRange)
        self.size[2] = self.maxRange%self.size[0]
        
        try:
            self.size[1] = self.size[0] + self.size[0]//self.size[2]
        except:
            self.size[1] = self.size[0]
    
        self.img.config(width=self.size[1], height=self.size[0])
        self.canvas.config(height=self.size[0], width=self.size[1], bg='black')    
        self.canvas.create_image((self.size[0], self.size[1]), image=self.img, state='normal')
        self.canvas.update()
        self.solve()
        
    def coordValue(self, value):
        x = value // (self.size[0] - self.size[2]//self.size[0]) 
        value -= x
        y = x
        
        return [x, y]
        

    def firstValue(self, value):
        x = 1
        
        while x <= self.maxRange:
            if self.getPixel(value) == True:
                return x
            else:
                x += 1
    
    
    def getPixel(self, value):
        coords = self.coordValue(value)
        
        dc = windll.user32.GetDC(0)     
        rgb = windll.gdi32.GetPixel(dc,coords[0],coords[1])
        r = rgb & 0xff
        print 'r', r
        if r > 0:
            return True
        else:
            return False
    
    def solve(self):
        n = 2
        
        while n<=self.maxRange: 
            print 'while1'
            repeat = 2 
            guess = self.firstValue(n) + 1
            self.primes.append(guess) 
            
            while repeat * guess <= self.maxRange: 
                print n, self.maxRange, repeat, guess
                self.uncolor(repeat * guess)
                
                repeat += 1 
                if n==10:
                    exit(0)
                
            n += 1
    def uncolor(self, value):
        coords = self.coordValue(value)
        self.img.put('#ffffff', (coords[0], coords[1]))
        
def sqrt(num):
    ans = num
    guess = (ans + 1) // 2
    while guess < ans:
        ans = guess
        guess = (ans + num // ans) // 2
    return ans
            
def main(): 
    primes = [2]
    root = Tk()
    visual = Application(root, primes)
    
    print 'Total primes: %d, all primes: %s' % (len(primes), primes) 
    
if __name__ == '__main__':
    main()
    
    exit
