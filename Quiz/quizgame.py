def loaddata(filename):
    f=open(filename,'r')
    txt=""
    for i in f:
        txt+=i
    f.close()
    return txt

# data=loaddata("questions.txt")

def parsequestions(data):
    lst=[]
    
    datas=data.split('\n')
    for i in datas :
        n=i.split(':')
        dic={}
        dic["question"]=n[0]
        dic["choices"]=n[1].split(",")
        dic["correctoption"]=int(n[2])
        dic["maxmarks"]=int(n[3])
        dic["penality"]=int(n[4])
        lst.append(dic)
    return lst

# questions=parsequestions(data)

def startquiz(questions):
    for q in questions:
        print (q["question"],q["choices"])
        user=int(input('select an option 1 or 2 or 3 or 4: '))
        q["userchoice"]=user
        if user>=1 and user<=4:
           if q["userchoice"]==q["correctoption"]:
               q['score']=q["maxmarks"]
           elif q["userchoice"]!=q["correctoption"]:
                q['score']=q["penality"]
        else:
            print("invalid option")
        print()



    return questions

# questions=startquiz(questions)

def calculatescore(questions):
    totalscore=0
    for q in questions:
        if q["userchoice"]==q["correctoption"]:
            print("correct option")
            totalscore+=q["maxmarks"]
            q['score']=q["maxmarks"]
        elif q["userchoice"]!=q["correctoption"]:
                print("wrong answer")
                totalscore+=q["penality"]

    return totalscore

def runQuiz():
    print("welcome to quiz")
    data=loaddata("questions.txt")
    n=parsequestions(data)
    questions=startquiz(n)
    total=calculatescore(questions)
    print("total score is : ",total)
        


runQuiz()

