def print_gugudan():
    for i in range(2, 10):
        print(f"\n{i}단:")
        for j in range(1, 10):
            print(f"{i} x {j} = {i*j}")

if __name__ == "__main__":
    print("구구단을 출력합니다!")
    print_gugudan() 