import threading

def find_max(numbers):
    print(f"Максимум: {max(numbers)}")

def find_min(numbers):
    print(f"Минимум: {min(numbers)}")

numbers = list(map(int, input("Введите числа через пробел: ").split()))

thread1 = threading.Thread(target=find_max, args=(numbers,))
thread2 = threading.Thread(target=find_min, args=(numbers,))

thread1.start()
thread2.start()

thread1.join()
thread2.join()
