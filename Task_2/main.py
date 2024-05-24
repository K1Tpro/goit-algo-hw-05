from typing import Callable, Generator


def generator_numbers(text: str) -> Generator[float, None, None]:
    # Розбиває рядок на елементи через пробіл
    for word in text.split():
        # Перевірка чи є рядок перетворюваним у дійсне число
        try:
            yield float(word)
        except ValueError:
            continue


def sum_profit(text: str, operation: Callable[[str], Generator[float, None, None]]) -> float:
    # Сума всіх дійсних чисел із рядка
    return sum(operation(text))


text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими " \
       "надходженнями 27.45 і 324.00 доларів."
print(sum_profit(text, generator_numbers))
