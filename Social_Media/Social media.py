def initializeplatform():
    post=[]
    dic={"contents":'',"likes":0,"comments":[]}
    post.append(dic)
    return post
# initializeplatform()

def createpost(platform,content):
    
    
    dic1={"contents":content,"likes":0,"comments":[]}
    platform.append(dic1)
    
    return platform
# platform=initializeplatform()
# content="hello world"
# createpost(platform,content)

def viewtimeline(platform):
    if len(platform)==1:
        return None
    for i in platform[1:]:
        print(i)
    return None

# viewtimeline(platform)


def likepost(platform,postindex):
    n=0

    for i in range(len(platform)):
        if i==postindex:
            n=5622
            platform[i]["likes"]+=1
    
    if n!=5622:  
       print("warning")

    return platform

# likepost(platform,postindex=input())


def commentonpost(platform,postindex,comment):
    n=0
    for i in range(len(platform)):
        if i==postindex:
            n=68
            platform[i]["comments"].append(comment)

    if n!=68:
        print("warning")

    return platform

# commentonpost(platform,postindex=input(),comment=input())

def main():
    platform=initializeplatform()
    while True:
        print("Welcome to the platform")
        print("1. Create a new post.")
        print("2. View the timeline.")
        print("3. Like a post (prompt for post index).")
        print("4.Comment on a post (prompt for post index and comment content).")
        print("5. Exit.")

        
        user=int(input("choose your options:"))

        if user==1:
            content=input("enter content:")
            platform=createpost(platform,content)
            print("-----------")
            print(' ')
        if user==2:
            #platform=createpost(platform,content)
            viewtimeline(platform)
            print("-----------")
            print(' ')
        if user==3:
            #platform=createpost(platform,content)
            postindex=int(input("enter postindex:"))
            platform =likepost(platform,postindex)
            print("-----------")
            print(' ')
        if user==4:
            #platform=createpost(platform,content)
            comment=input("write your comment:")
            postindex=int(input("enter postindex:"))
            platform=commentonpost(platform,postindex,comment)
            print("-----------")
            print(' ')

        if user==5:
            print("bye")
            break

main()













