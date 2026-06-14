# Analyzer module for statistical calculations
def average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def variance(numbers):
    """Вычисляет дисперсию списка чисел"""
    if len(numbers) <= 1:
        return 0
    avg = average(numbers)
    return sum((x - avg) ** 2 for x in numbers) / (len(numbers) - 1)

