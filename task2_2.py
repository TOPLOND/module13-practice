import threading

def find_sum_repeated(numbers):
    for _ in range(5):
        print(f"Сумма: {sum(numbers)}")

def find_average_repeated(numbers):
    for _ in range(5):
        print(f"Среднее арифметическое: {sum(numbers) / len(numbers)}")

numbers = list(map(int, input("Введите числа через пробел: ").split()))

thread1 = threading.Thread(target=find_sum_repeated, args=(numbers,))
thread2 = threading.Thread(target=find_average_repeated, args=(numbers,))

thread1.start()
thread2.start()

thread1.join()
thread2.join()
