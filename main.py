## Basic use of daemon thread

from os import getpid

from threading import Thread, active_count, current_thread
from time import sleep


def thread_loop():
    ''' Run a loop in a thread indefinately until main thread concludes
    '''
    while True:
        #print("[Thread feedback]: Running...")
        print(f"Current thread: {current_thread()}")
        sleep(2)

def main_loop():
    ''' Simulated work perform by the main thread
    '''
    for _ in range(4):
        #print("[MAIN thread feedback]: Running...")
        print(f"Current thread: {current_thread()}")
        sleep(1)


def main():
    print(f"Number of threads BEFORE secondary thread instantiation: {active_count()}")
    print(f"Current thread: {current_thread()}")

    t = Thread(target=thread_loop)
    t.daemon = True ## Setting the thread as daemon thread
    t.start()

    print(f"Number of threads AFTER secondary thread instantiation: {active_count()}")

    main_loop()

    print("main() concludes")


if __name__ == "__main__":
    print(f"process_id: {getpid()}") ## Safeguard

    main()

    print(f"Number of threads BEFORE ending process: {active_count()}") ## Both threads still exist until process itself concludes 
