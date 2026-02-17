import threading
def numbers():
    for i in range(5):
        print("number" , i)

def letters():
    for k in "ABCDE":
        print("letter", k)

t1 = threading.Thread(target=numbers)
t2 = threading.Thread(target=letters)
t1.start()
t2.start()
t1.join()
t2.join()
print("thread terminated")
