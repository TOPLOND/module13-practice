import threading

def find_sum(numbers):
    print(f"Сумма: {sum(numbers)}")

def find_average(numbers):
    print(f"Среднее арифметическое: {sum(numbers) / len(numbers)}")

numbers = list(map(int, input("Введите числа через пробел: ").split()))

thread1 = threading.Thread(target=find_sum, args=(numbers,))
thread2 = threading.Thread(target=find_average, args=(numbers,))

thread1.start()
thread2.start()

thread1.join()
thread2.join()
