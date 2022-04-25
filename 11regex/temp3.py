from threading import Lock

def test():

    if lock1.acquire():
        print('hello world!')

lock1=Lock()
lock1.acquire()

test()
