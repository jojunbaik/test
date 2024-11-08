#score = int(input("입력하세요 : "))
#while True:
#    score = int(input("입력하세요 : "))
#    if score >= 90:
#        print("A")
#    elif score >= 80:
#        print("B")
#    elif score >= 70:
#        print("C")
#    elif score >= 60:
#        print("D")
#    else:
#        exit("낙제 프로그램 종료")
#        #break #break는 탈출

for i in range(5): #행
    for j in range(i): #열
        print("*", end = "") #end는 줄바꿈을 안한다.
    print()
