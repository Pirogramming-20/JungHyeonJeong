import random 

num = 0
num_computer = 0
start_number = 1
A = True #컴퓨터의 차례인지 체크

def brGame(player1, player2):
    for i in range(num):
        global start_number
        print(player1," ", start_number)
        start_number += 1
        if start_number == 32:
            print(player2, " win!")
            break

while start_number <= 31:
    if A == True: #컴퓨터 차례
        num_computer = random.randint(1, 3)
        for i in range(num_computer):
            print("computer ", start_number)
            start_number += 1
            if start_number == 32:
                print("player win!")
                break
        A = False
        continue

    while True:
        try: 
            num = int(input("부를 숫자의 개수를 입력하세요(1, 2, 3만 입력 가능) :"))
            if num not in [1, 2, 3]:
                print("1, 2, 3 중 하나를 입력하세요")
                continue
            break
        except ValueError:
            print("정수를 입력하세요")

    if A == False:
        brGame("player", "computer")
        A = True
        continue