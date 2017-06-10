#This program was a result of my first idea of finding primes 

def main(): 
    maxRange = int(raw_input("What is the max range of numbers you want tested for being prime? ")) 
    primes = []
    
    if maxRange % 2 == 0: #To avoid even number decrements
        maxRange -= 1
    
    print maxRange
    with open('primelist', 'wb+') as file:
        for i in xrange(3, maxRange +1, 2):
            for j in xrange(i+1, 3, -2):
                #Something
                    #primes.append(i)
        
    print 'Total primes: %d, all primes: %s' % (len(primes), primes) 
    
if __name__ == '__main__':
    main()
    
    exit