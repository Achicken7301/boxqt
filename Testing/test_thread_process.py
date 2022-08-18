import time
import concurrent.futures


def do_something():
    print("Start doing")
    time.sleep(1)
    print("Done sleeping")

def main():
    with concurrent.futures.ThreadPoolExecutor() as executor:
        executor.submit(do_something)
        executor.submit(do_something)
                  
   


if __name__ == '__main__':
    main()