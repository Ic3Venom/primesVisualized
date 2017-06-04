#This program was my second idea, involving a canvas
from Tkinter import *

class Application:
    def dimension(self, maxRange, size):
        self.size[0] = sqrt(self.maxRange)
        self.size[2] = self.maxRange%self.size[0]
        try:
            self.size[1] = self.size[0] + self.size[0]//self.size[2]
        except:
            self.size[1] = self.size[0]
        
    def entryGet(self):
        try:
            self.maxRange = int(self.entry.get())
        except TypeError:
            print 'Unknown integer value %s.' % self.maxRange 
    
        self.dimension(self.maxRange, self.size)
        
    def __init__(self, master):
        
        self.size = [0,0,0]
        
        frame = Frame(master)
        frame.pack()
        #Canvas where black dots will be placed
        self.canvas = Canvas(frame, width=self.size[0], height=self.size[1]).pack()
        
        #Text for numRange
        Label(frame, text="Max Number Range:", font=("Helvetica", 10, "bold")).pack(side=LEFT)
        
        #numRange user input
        self.entry = Entry(frame, font=("Helvetica", 10))
        self.entry.pack(side=LEFT)
        
        #numRange user input confirmation
        Button(frame, text='Enter', font=("Helvetica", 10), command=self.entryGet).pack(side=LEFT)

        #Button to exit canvas
        Button(frame, text="Quit", font=("Helvetica", 10), command=master.destroy).pack(side=RIGHT)

        #Ownership
        Label(frame, text="Made by Julian Meyn", font=("Helvetica", 5)).pack(side=RIGHT, anchor=S)
        
        master.mainloop()

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
    visual = Application(root)

    print 'Total primes: %d, all primes: %s' % (len(primes), primes) 
    
if __name__ == '__main__':
    main()
    
    exit
