 ## GIL in python and single threaded nature of python.

 ### What is Global Interpreter Lock (GIL)?
 The Python Global Interpreter Lock or GIL, in simple words, is a mutex (or a lock) that allows only one thread **to hold the control of the Python interpreter**.

 This means that **only one thread can be in a state of execution at any point in time**. The impact of the GIL isn’t visible to developers who execute single-threaded programs, but it can be a performance bottleneck in CPU-bound and multi-threaded code.

 ### Why GIL?
Python uses reference counting for `memory management`. It means that objects created in Python have a reference count variable that keeps track of the number of references that point to the object. When this count **reaches zero**, The python garbage collector **kicks in and removes that variable from the heap** and the **memory occupied by the object is released**.

Let’s take a look at a brief code example to demonstrate how reference counting works:
```
>>> import sys
>>> a = []
>>> b = a
>>> sys.getrefcount(a)
3
```
In the above example, the reference count for the empty list object [] was 3. The list object was referenced by a, b and the argument passed to sys.getrefcount().

#### What Problem Did the GIL Solve for Python?
The problem was that this reference count variable needed protection from race conditions **where two threads increase or decrease its value simultaneously**. If this happens, it can cause either **leaked memory that is never released** or, even worse, incorrectly release the memory while a reference to that object still exists. This can cause crashes or other “weird” bugs in your Python programs.

This reference count variable can be kept safe by adding locks to all data structures that are shared across threads so that they are not modified inconsistently.

But adding a lock to each object or groups of objects means multiple locks will exist which can cause another problem **Deadlocks** (deadlocks can only happen if there is more than one lock). Another side effect would be **decreased performance** caused by the **repeated acquisition and release of locks**.

The GIL is a **single lock on the interpreter itself** which adds a rule that **execution of any Python bytecode requires acquiring the interpreter lock**. This prevents deadlocks (as there is only one lock) and doesn’t introduce much performance overhead. But it effectively **makes any CPU-bound Python program single-threaded**.

### Why Was the GIL Chosen as the Solution?
Python has been around since the days when operating systems did not have a concept of threads. Python was designed to be **easy-to-use** in order to make development quicker and more and more developers started using it.

A lot of extensions were being written for the existing C libraries whose features were needed in Python. To prevent inconsistent changes, these C extensions required a **thread-safe memory management which the GIL provided**.

The GIL is simple to implement and was easily added to Python. It provides a **performance increase to single-threaded programs as only one lock needs to be managed**.

C libraries that were not thread-safe became easier to integrate. And these C extensions became one of the reasons why Python was readily adopted by different communities.

### The Impact on Multi-Threaded Python Programs
#### Types of multithreaded programs
##### I/O bound program
I/O-bound programs are the ones that **spend time waiting for Input/Output** which can come from a user, file, database, network, etc. I/O-bound programs sometimes have to wait for a significant amount of time till they get what they need from the source due to the fact that the source may need to do its own processing before the input/output is ready, for example, a user thinking about what to enter into an input prompt or a database query running in its own process.

##### CPU-bound program
CPU-bound programs are those that are **pushing the CPU to its limit**. This includes programs that do mathematical computations like matrix multiplications, searching, image processing, etc.

Let’s have a look at a simple CPU-bound program that performs a countdown:
```
# single_threaded.py
import time
from threading import Thread

COUNT = 50000000

def countdown(n):
    while n>0:
        n -= 1

start = time.time()
countdown(COUNT)
end = time.time()

print('Time taken in seconds -', end - start) 
Running this code on a system with 4 cores gave the following output: Time taken in seconds - 6.20024037361145
```
Now Let's modify the code a bit to do to the same countdown using two threads in parallel:
```
# multi_threaded.py
import time
from threading import Thread

COUNT = 50000000

def countdown(n):
    while n>0:
        n -= 1

t1 = Thread(target=countdown, args=(COUNT//2,))
t2 = Thread(target=countdown, args=(COUNT//2,))

start = time.time()
t1.start()
t2.start()
t1.join()
t2.join()
end = time.time()

print('Time taken in seconds -', end - start)
Output: Time taken in seconds - 6.924342632293701
```

As you can see, both versions take almost same amount of time to finish. In the multi-threaded version **the GIL prevented the CPU-bound threads from executing in parellel**.

The GIL does not have much impact on the performance of I/O-bound multi-threaded programs as the lock is shared between threads while they are waiting for I/O.

But a program whose threads are entirely CPU-bound, e.g., a program that processes an image in parts using threads, would not only become single threaded due to the lock but will also see **an increase in execution time**. This increase is the result of **acquire and release overheads added by the lock**.

### Why Hasn’t the GIL Been Removed Yet?
The developers of Python receive a lot of complaints regarding this but a language as popular as Python cannot bring a change as significant as the removal of GIL without causing backward incompatibility issues.

The GIL can obviously be removed and this has been done multiple times in the past by the developers and researchers but all those attempts **broke the existing C extensions which depend heavily on the solution that the GIL provides**.

Of course, there are other solutions to the problem that the GIL solves but some of them **decrease the performance of single-threaded and multi-threaded I/O-bound programs** and some of them are just too difficult.

### GIL improvements with Python 33
We discussed the impact of GIL on “only CPU-bound” and “only I/O-bound” multi-threaded programs but what about the programs where some threads are I/O-bound and some are CPU-bound?

In such programs, Python’s GIL was known **to starve the I/O-bound threads by not giving them a chance to acquire the GIL from CPU-bound threads**.

This was because of a mechanism built into Python that forced threads to release the GIL after a fixed interval of continuous use and if nobody else acquired the GIL, the same thread could continue its use.

The problem in this mechanism was that most of the time the CPU-bound thread would reacquire the GIL itself before other threads could acquire it. This problem was fixed in Python 3.2, by adding a mechanism of looking at the number of GIL acquisition requests by other threads that got dropped and not allowing the current thread to reacquire GIL before other threads got a chance to run.

### How to Deal With Python’s GIL
If the GIL is causing you problems, here a few approaches you can try:

**Multi-processing vs multi-threading**: The most popular way is to use a multi-processing approach where you use multiple processes instead of threads. Each Python process gets **its own Python interpreter and memory space** so the GIL won’t be a problem. Python has a multiprocessing module which lets us create processes easily like this:
```
from multiprocessing import Pool
import time

COUNT = 50000000
def countdown(n):
    while n>0:
        n -= 1

if __name__ == '__main__':
    pool = Pool(processes=2)
    start = time.time()
    r1 = pool.apply_async(countdown, [COUNT//2])
    r2 = pool.apply_async(countdown, [COUNT//2])
    pool.close()
    pool.join()
    end = time.time()
    print('Time taken in seconds -', end - start)
```

The time didn’t drop to half of what we saw above because **process management has its own overheads**. Multiple processes are heavier than multiple threads, so, keep in mind that this could become a **scaling bottleneck**.

Another solution is to use, **Alternative Python interpreters**: Python has multiple interpreter implementations. CPython, Jython, IronPython and PyPy, written in C, Java, C# and Python respectively, are the most popular ones. GIL exists only in the original Python implementation that is CPython. If your program, with its libraries, is available for one of the other implementations then you can try them out as well.