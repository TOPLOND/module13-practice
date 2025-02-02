import threading

def find_max_repeated(numbers):
    for _ in range(5):
        print(f"Максимум: {max(numbers)}")

def find_min_repeated(numbers):
    for _ in range(5):
        print(f"Минимум: {min(numbers)}")

numbers = list(map(int, input("Введите числа через пробел: ").split()))

thread1 = threading.Thread(target=find_max_repeated, args=(numbers,))
thread2 = threading.Thread(target=find_min_repeated, args=(numbers,))

thread1.start()
thread2.start()

thread1.join()
thread2.join()
