import threading

def write_even(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]
    with open("even_numbers.txt", "w") as file:
        file.write("\n".join(map(str, even_numbers)))
    print(f"Количество четных чисел: {len(even_numbers)}")

def write_odd(numbers):
    odd_numbers = [num for num in numbers if num % 2 != 0]
    with open("odd_numbers.txt", "w") as file:
        file.write("\n".join(map(str, odd_numbers)))
    print(f"Количество нечетных чисел: {len(odd_numbers)}")

file_path = input("Введите путь к файлу: ")
with open(file_path, "r") as file:
    numbers = list(map(int, file.read().split()))

thread1 = threading.Thread(target=write_even, args=(numbers,))
thread2 = threading.Thread(target=write_odd, args=(numbers,))

thread1.start()
thread2.start()

thread1.join()
thread2.join()
