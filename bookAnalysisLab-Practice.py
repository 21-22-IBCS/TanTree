def main():
    
    f=open("1952-0.txt","r")
    bigS=f.read()
    sampleList=bigS.split(" ")
    newList=[]
    for e in sampleList:
        tempList = e.split("\n")
        for t in tempList:
            newList.append(t)
        theList=[]
        count=0
    for w in newList:
            if w == "***":
                count = count + 1
            if count == 2:
                theList.append(w)


    for i in range(55):
        print(newList[i])

    myStr = "apple"
    x = myStr.replace("a","b")
    #print(x)

    #for w in list:
        #if len(w) > 0:
    
    
    
if __name__ == "__main__":
    main()
