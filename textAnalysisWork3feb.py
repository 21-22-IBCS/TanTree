def main():
    
    f=open("1952-0.txt","r")
    text = f.read()
    lower = text.lower()
    n = lower.replace("\n"," ")
    newList = n.split()
    wList = []
    words = newList.strip("?")
    for w in newList:
            new = w.strip("?")
            wList.append(new)
        
    
    #noBreaks = newList.strip("\n")
    #noBreaks = text.replace(
    #print(newList)
    print(words)
    
    #sinBreaks = newList.strip("\n")
    #print(sinBreaks)
    
    #for i in
    #happy = []
    #happy.append()




    
    
if __name__ == "__main__":
    main()

