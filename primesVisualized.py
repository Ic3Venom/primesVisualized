#This program was my second idea, involving a canvas
from Tkinter import *

class Application:
    def quit(self):
        self.root.destroy()
    
    def dimension(self):
        self.maxRange = self.entry.get()
        
        
    def __init__(self, master):
        frame = Frame(master)
        frame.grid()
        
        #Canvas where black dots will be placed
        self.canvas = Canvas(frame, width=1000, height=1000).grid(row=1) 
        
        #Button to exit canvas
        self.terminate = Button(frame, text="Quit", command=frame.quit).grid(row=2, column=3)
        
        #Text for numRange
        Label(frame, text="Max Number Range:").grid(row=2, column=0, sticky="w")
        
        #numRange user input
        self.entry = Entry(frame)
        self.entry.grid(row=2, column=1, sticky= W)
        
        #numRange user input confirmation
        self.confirm = Button(frame, text='Enter', command=self.dimension).grid(row=2, column=2, sticky="w")
        
        mainloop()

def main(): 
    primes = [2]
    root = Tk()
    visual = Application(root)
    
    print 'Total primes: %d, all primes: %s' % (len(primes), primes) 
    
if __name__ == '__main__':
    main()
    
    exit
