#This program was my second idea, involving a canvas
from Tkinter import *

class Application:
    def quit(self):
        self.root.destroy()
    
    def __init__(self, dimensions):
        self.root = Tk()
        
        visual = Canvas(self.root, 
                        width=dimensions[1], 
                        height=dimensions[0])
        visual.pack()
        
        bLeave = Button(visual, 
                             text="Quit", 
                             command=self.quit)
        bLeave.pack()
        mainloop()

def dimension(maxRange):
    return [100,10,7]
        
    
    return [length, width, extra]

def main(): 
    maxRange = int(raw_input("What is the max range of numbers you want tested for being prime? ")) 
    primes = [2]

    dimensions = dimension(maxRange)
    visual = Application(dimensions)
    
    #DEBUG
    print 'dimensions: %s' % dimensions
    #ENDDEBUG
    
    print 'Total primes: %d, all primes: %s' % (len(primes), primes) 
    
if __name__ == '__main__':
    main()
    
    exit