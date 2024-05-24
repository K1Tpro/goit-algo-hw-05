def caching_fibonacci():
    # Створює порожній словник cache
    cache = {}

    def fibonacci(n):
        # Перевірка на 0
        if n <= 0:
            return 0
        # на 1
        elif n == 1:
            return 1
        # чи є число в кеші
        elif n in cache:
            return cache[n]
        # Прорахунок числа
        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    return fibonacci


# Отримуємо функцію fibonacci
fib = caching_fibonacci()

# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(10))  # Виведе 55
print(fib(15))  # Виведе 610