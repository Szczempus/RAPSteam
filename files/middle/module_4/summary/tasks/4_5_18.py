import time


def measure_time():
    """Mierzy czas wykonania operacji."""
    start = time.time()
    sum(range(1000000))
    end = time.time()
    return end - start


print(measure_time())  # Output: czas w sekundach
