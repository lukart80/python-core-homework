import time
from statistics import mean
from ex2 import fetcher

CALL_COUNT = 10


def benchmark(num):
    """
    Совершает num прогонов переданной функции и выводит в консоль время каждого прогона и среднее время всех прогонов

    :param num: число итераций
    :return: функцию обёртку
    """

    def wrapper(func):
        # put your code here
        exec_data = []

        def _decorator(*args, **kwargs):
            for i in range(num):
                start_time = time.time()
                func(*args, **kwargs)
                finish_time = time.time()
                total_time = finish_time - start_time
                exec_data.append(total_time)
            for i, exec_time in enumerate(exec_data):
                print(f'Время выполнения функции в {i+1}-раз - {exec_time}')
            print(f'Среднее время выполнения функции - {mean(exec_data)}')

        return _decorator

    return wrapper


@benchmark(CALL_COUNT)
def fetch_page(url):
    fetcher.get(url)


if __name__ == '__main__':
    fetch_page('www.google.com')
