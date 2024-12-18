import time
import math

def binary_search_recursive(func, interval, epsilon=1e-5, log_file="binary_search_log.txt"):

    a, b = interval
    fa = func(a)
    fb = func(b)

    with open(log_file, "a") as f:
        f.write(f"Начало поиска: [{a}, {b}], f(a) = {fa}, f(b) = {fb}\n")

    if fa * fb > 0:
        with open(log_file, "a") as f:
            f.write(f"Корней нет на отрезке [{a}, {b}]\n")
        return None

    start_time = time.time()

    def recursive_search(a, b):
        c = (a + b) / 2
        fc = func(c)
        with open(log_file, "a") as f:
            elapsed_time = time.time() - start_time
            f.write(f"Время: {elapsed_time:.6f} c, x = {c}, f(x) = {fc}\n")

        if abs(fc) < epsilon:
            return c

        if fc * fa < 0:
            return recursive_search(a, c)
        else:
            return recursive_search(c, b)

    result = recursive_search(a, b)
    return result



def binary_search_iterative(func, interval, epsilon=1e-5, log_file="binary_search_log.txt"):

    a, b = interval
    fa = func(a)
    fb = func(b)

    with open(log_file, "a") as f:
        f.write(f"Начало поиска: [{a}, {b}], f(a) = {fa}, f(b) = {fb}\n")

    if fa * fb > 0:
        with open(log_file, "a") as f:
            f.write(f"Корней нет на отрезке [{a}, {b}]\n")
        return None

    start_time = time.time()
    while True:
        c = (a + b) / 2
        fc = func(c)
        with open(log_file, "a") as f:
            elapsed_time = time.time() - start_time
            f.write(f"Время: {elapsed_time:.6f} c, x = {c}, f(x) = {fc}\n")

        if abs(fc) < epsilon:
            return c

        if fc * fa < 0:
            b = c
        else:
            a = c


# Пример использования:
def f(x):
    return x**3 - 2*x - 5

interval = [2, 3]

start_time_recursive = time.time()
root_recursive = binary_search_recursive(f, interval)
end_time_recursive = time.time()

start_time_iterative = time.time()
root_iterative = binary_search_iterative(f, interval)
end_time_iterative = time.time()

print(f"Рекурсивный поиск: корень = {root_recursive}, время = {end_time_recursive - start_time_recursive:.6f} с")
print(f"Итеративный поиск: корень = {root_iterative}, время = {end_time_iterative - start_time_iterative:.6f} с")


