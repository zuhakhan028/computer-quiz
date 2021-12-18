print("Welcome to my Quiz Game!")

Playing=input("Do you want to play? ")
print(Playing)

print("Lets Play!")
score=0

ques_1=input("1.What deos a CPU stands for? : ")
if ques_1.lower()=="central processing unit":
    print("correct!")
    score+=1
else:
        print("incorrect!")

ques_2=input("2.What deos a RAM stands for? : ")
if ques_2.lower()=="random access memory":
    print("correct!")
    score+=1
else:
        print("incorrect!")

ques_3=input("3.What deos a GUI stands for? : ")
if ques_3.lower()=="graphical user interface":
    print("correct!")
    score+=1
else:
        print("incorrect!")

ques_4=input("4.what does GPU stands for : ")
if ques_4.lower()=="graphic processing unit":
    print("correct!")
    score+=1
else:
        print("incorrect!")

ques_5=input("5.what do you call a portable computer : ")
if ques_5.lower()=="laptop":
    print("correct!")
    score+=1
else:
        print("incorrect!")

print("you got {} answers correct".format(score))
print("you got {} % ".format((score/5*100)))

if score>3:
    print("well done!")
else:
    print("Come back more prepared")



print("THANK YOU FOR PLAYING!")



