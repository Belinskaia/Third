import multiprocessing


def worker():
    LIST.append('item')


LIST = []


if __name__ == "__main__":
    processes = [
        multiprocessing.Process(target=worker)
        for _ in range(5)
    ]
    for p in processes:
        p.start()
    for p in processes:
        p.join()
    print(LIST)
'''LIST является пустым, так как созданные процессы являются параллельными и имют различные участки памяти просто так недоступные друг другу, в связи с этим 
измения в LIST не отражаются'''
