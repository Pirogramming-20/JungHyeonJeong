num = 0
start_number = 1
A = True #A의 차례인지 체크

while start_number <= 31:
    while True:
        try: 
            num = int(input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :"))
            if num not in [1, 2, 3]:
                print("1, 2, 3 중 하나를 입력하세요")
                continue
            break
        except ValueError:
            print("정수를 입력하세요")

    if A == True:
        for i in range(num):
            print("playerA : ", start_number)
            start_number += 1
            if start_number == 32:
                break
        A = False
        continue
    
    if A == False:
        for i in range(num):
            print("playerB : ", start_number)
            start_number += 1
            if start_number == 32:
                break
        A = True
        continue