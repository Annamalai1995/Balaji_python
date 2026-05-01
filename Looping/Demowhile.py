# for seats  in range(1,16):
# seats=1
# while seats <=18:
#         amt=int(input("Tell us amount to book ticket"))
#         if amt>=190:
#             print("Ticket Booked @",seats)
#             seats+=1
#         else: print("Insufficient amount")    


hire=5
while hire>0:
    skill=input("Tell us skill set you know:")
    poc=int(input("Ho many poc you can done it"))
    if (skill =='java' or skill=='python') and poc>=5:
        print("you are recruited to our company")
        hire-=1
    else:
        print("better luck next time")