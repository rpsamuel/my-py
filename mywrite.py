import concurrent.futures
import time

def do_something(seconds):
    print(f'Sleeping {seconds} seconds(s)...')
    time.sleep(seconds)
    return f'Done sleeping...{seconds}'

start = time.perf_counter()

with concurrent.futures.ThreadPoolExecutor() as executor:
    secs = [7,6, 5, 4, 3, 2, 1]
    results = executor.map(do_something, secs)
    for result in results:
        print(result)
        
finish = time.perf_counter()
print(f' Processing {len(secs)} threads took {finish-start} seconds')
