import random
def start():
   #print("Keep it logically awesome.")
    
    last = 13
    rnd = random.randint(0, last)
    
    f = open("quotes.txt")
    quotes = f.readlines()
    last = len(quotes) -1
    f.close()

    print(quotes[rnd])


if __name__== "__main__":
  
  start()
