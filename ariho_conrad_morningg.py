# Context managers - provide a way to manage resources ,
#a context manager is an object that defines the methods __enter__() and __exit__() 
#which allow you to manage resources (such as files or network connections) in a clean and efficient way.
#  ensuring that they are properly set up and cleaned up.
#  They are commonly used with the 'with'statement.

# Assignment1. A context manager that automatically opens and closes a file

class FileContextManager:
    def __init__(self,filename,mode):
        self.filename = filename
        self.mode= mode

    def __enter__(self):
        self.file = open(self.filename,self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()

# Usage of the file context manager
with FileContextManager('example.txt', 'r') as file:
    contents = file.read()
    print(contents)


# Assignment2.Database connection context manager

import sqlite3

class DatabaseConnection:
    def __init__(self,dbname):
        self.dbname = dbname

    def __enter__(self):
        self.conn = sqlite3.connect(self.dbname)
        return self.conn
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.conn.close()

# Usage of the db connection
with DatabaseConnection('mydatabase.db') as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM mytable")
    results = cursor.fetchall()
    print(results)

# Assignment3.Multithreading and multiprocesssing that allows us to run a fn for diff amts of time

# Multithreading 
# multithreading allows you to execute multiple threads (smaller units of execution) concurrently within a single process. 
# Multithreading can be useful for improving the performance of certain types of applications by utilizing multiple CPU cores or for managing multiple I/O-bound tasks simultaneously.
import threading
import time

def count_down(name, duration):
    print(f"{name} started")
    for i in range(duration, 0,-1):
        print(f"{name}: {i} seconds remaining")
        time.sleep(i)
    print(f"{name} finished")

# Create thread objects
thread1 = threading.Thread(target=count_down,args= ("Thread 1",5))
thread2 = threading.Thread(target=count_down,args= ("Thread 2",3))

# Start the threads
thread1.start()
thread2.start()

# wait for both threads to complete
thread1.join()
thread2.join()

print("Threads completed")

# Multiprocessing ex

import multiprocessing
import time

def count_down(name, duration):
    print(f"{name} started")
    for i in range(duration, 0,-1):
        print(f"{name}: {i} seconds remaining")
        time.sleep(i)
    print(f"{name} finished")

# Creating process objects
process1 = multiprocessing.Process(target=count_down,args= ("Process 1",5))
process2 = multiprocessing.Process(target=count_down,args= ("Process 2",3))

# Starting the process
process1.start()
process2.start()

# waiting for both process to complete
process1.join()
process2.join()



