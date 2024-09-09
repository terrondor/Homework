import time
import multiprocessing
import os



def read_info(name):
    if not os.path.isfile(name):
        print(f'Файл не найден: {name}')
        return
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line.strip())
    
if __name__ == '__main__':
    filenames = [f'./module_10_5/file {number}.txt' for number in range(1, 5)]
    
    print(f"Попытка открыть следующие файлы: {filenames}")

    start_time = time.time()
    for filename in filenames:
        read_info(filename)
    linear_elapsed_time = time.time() - start_time
    print(f'{linear_elapsed_time} (линейный)')

    start_time = time.time()
    with multiprocessing.Pool() as pool:
        pool.map(read_info, filenames)
    multi_process_elapsed_time = time.time() - start_time
    print(f'{multi_process_elapsed_time} (многопроцессный)')