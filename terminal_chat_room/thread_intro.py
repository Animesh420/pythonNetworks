import threading

# Threading allows us to speed up programs by executing multiple tasks at the SAME time.
# Each task will run on its own thread
# Each thread can run simultaneously and share data with each other
# Every thread when you start it must do SOMETHING, which  we can define with a function
# Our threads will target these functions
# When we start the thread the target function will be run


def func1():
    for x in range(10):
        print("ONE ")


def func2():
    for x in range(10):
        print("TWO ")


def func3():
    for x in range(10):
        print("THREE ")

# Linear execution of all functions
# func1()
# func2()
# func3()

# Concurrent execution of functions


t1 = threading.Thread(target=func1)
t2 = threading.Thread(target=func2)
t3 = threading.Thread(target=func3)

t1.start()
t2.start()
t3.start()


t1.join()
t2.join()
t3.join()
print("Threading finished")
