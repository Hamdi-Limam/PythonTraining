## Threading in Python
Python threading allows you to have different parts of your program run concurrently and can simplify your design. If you’ve got some experience in Python and want to speed up your program using threads, then this course is for you!

### What Is a Thread?
A thread is a separate flow of execution. This means that your program will have two things happening at once. But for most Python 3 implementations the different **threads do not actually execute at the same time**: they merely appear to.

It’s tempting to think of threading as having two (or more) different processors running on your program, each one doing an independent task at the same time. That’s almost right. The threads may be running on different processors, but they will **only be running one at a time**.

Getting multiple tasks running simultaneously requires a non-standard implementation of Python, writing some of your code in a different language, or using `multiprocessing` which comes with some extra overhead.

Because of the way CPython implementation of Python works, threading may not speed up all tasks. This is due to interactions with the [GIL](https://realpython.com/python-gil/) that essentially limit one Python thread to run at a time.

Tasks that spend much of their time waiting for external events(I/O bound) are generally good candidates for threading. Problems that require heavy CPU computation(CPU bound) and spend little time waiting for external events might **not run faster at all**.

If you are running a standard Python implementation, writing in only Python, and have a CPU-bound problem, you should check out the `multiprocessing` module instead.

Architecting your program to use threading can also provide gains in design clarity. Most of the examples you’ll learn about in this tutorial are not necessarily going to run faster because they use threads. Using threading in them helps to make the design cleaner and easier to reason about.

### Starting a Thread
Now that you’ve got an idea of what a thread is, let’s learn how to make one. The Python standard library provides `threading`, which contains most of the primitives you’ll see in this course. `Thread`, in this module, nicely encapsulates threads, providing a clean interface to work with them.

To start a separate thread, you create a Thread instance and then tell it to `.start()`.
Example: Check the code of the file `thread.py`
If you look around the [logging](https://realpython.com/python-logging/) statements, you can see that the main section is creating and starting the thread:
```
x = threading.Thread(target=thread_function, args=(1,))
x.start()
```
When you create a Thread, you pass it a function and a tuple containing the arguments to that function. In this case, you’re telling the Thread to run thread_function() and to pass it 1 as an argument.

`thread_function()` itself doesn’t do much. It simply logs some messages with a time.sleep() in between them. When you run this program as it is (with line 21 commented out). You’ll notice that the Thread finished after the Main section of your code did. You’ll come back to why that is and talk about the mysterious line 21 in the next section.

### Daemon Threads
In computer science, a [daemon](https://en.wikipedia.org/wiki/Daemon_(computing)) is a process that runs in the background.

Python `threading` has a more specific meaning for daemon. A **daemon thread will shut down immediately when the program exits**. One way to think about these definitions is to consider the daemon thread a thread that runs in the background without worrying about shutting it down.

If a program is running Threads that are not daemons, then the program will wait for those threads to complete before it terminates. Threads that are daemons, however, are just **killed wherever they are when the program is exiting**.

Let’s look a little more closely at the output of your program above. The last two lines are the interesting bit. When you run the program, you’ll notice that there is a pause (of about 2 seconds) after `__main__` has printed its all done message and before the thread is finished.

This pause is Python waiting for the `non-daemonic thread` to complete. When your Python program ends, part of the shutdown process is to clean up the threading routine.

If you look at the [source for Python threading](https://github.com/python/cpython/blob/df5cdc11123a35065bbf1636251447d0bfe789a5/Lib/threading.py#L1263), you’ll see that `threading._shutdown()` walks through all of the running threads and calls `.join()` on every one that **does not have the daemon flag set**.

So your program waits to exit because the thread itself is waiting in a sleep. As soon as it has completed and printed the message, .join() will return and the program can exit.

Frequently, this behavior is what you want, but there are other options available to us. Let’s first repeat the program with a daemon thread. You do that by changing how you construct the Thread, adding the `daemon=True flag`:
```
x = threading.Thread(target=thread_function, args=(1,), daemon=True)
```
When you run the program now, you should see this output:
```
$ ./daemon_thread.py
Main    : before creating thread
Main    : before running thread
Thread 1: starting
Main    : wait for the thread to finish
Main    : all done
```
The difference here is that the final line of the output is missing. thread_function() did not get a chance to complete. It was a daemon thread, so when `__main__` **reached the end of its code and the program wanted to finish, the daemon was killed**.

### join() a Thread
Daemon threads are handy, but what about when you want to wait for a thread to stop? What about when you want to do that and not exit your program? Now let’s go back to your original program and look at that commented out line:
```
# x.join()
```
To tell one thread to wait for another thread to finish, you call `.join()`. If you uncomment that line, the **main thread will pause and wait for the thread x to complete running**.

Did you test this on the code with the daemon thread or the regular thread? It turns out that it doesn’t matter. If you `.join()` a thread, that statement **will wait until either kind of thread is finished**.

### Working With Many Threads
The example code so far has only been working with two threads: the main thread and one you started with the `threading.Thread` object.

Frequently, you’ll want to start a number of threads and have them do interesting work. Let’s start by looking at the harder way of doing that, and then you’ll move on to an easier method.

The harder way of starting multiple threads is the one you already know.
Check the code of the file `multi_thread.py`.

This code uses the same mechanism you saw above to start a thread, create a Thread object, and then call `.start()`. The program keeps a list of Thread objects so that it can then wait for them later using `.join()`.

If you walk through the output carefully, you’ll see all three threads getting started in the order you might expect, but in this case they finish in the opposite order! Multiple runs will produce different orderings. Look for the `Thread x: finishing` message to tell you when each thread is done.

The **order in which threads are run is determined by the operating system** and can be quite hard to predict. It may (and likely will) vary from run to run, so you need to be aware of that when you design algorithms that use threading.

Fortunately, Python gives you several primitives that you’ll look at later to help coordinate threads and get them running together. Before that, let’s look at how to make managing a group of threads a bit easier.

### Using a ThreadPoolExecutor
There’s an easier way to start up a group of threads than the one you saw above. It’s called a `ThreadPoolExecutor`, and it’s part of the standard library in [concurrent.futures](https://docs.python.org/3/library/concurrent.futures.html).

The easiest way to create it is as a context manager, using the `with statement` to manage the creation and destruction of the pool.
Check the code of the file `multi_thread.py`.

The code creates a ThreadPoolExecutor as a context manager, telling it how many worker threads it wants in the pool. It then uses `.map()` to step through an iterable of things, in your case range(3), passing each one to a thread in the pool.

The end of the with block causes the ThreadPoolExecutor to do a `.join()` on each of the threads in the pool. It is **strongly recommended that you use ThreadPoolExecutor as a context manager** when you can so that you never forget to `.join()` the threads.

Again, notice how Thread 1 finished before Thread 0. The scheduling of threads is done by the operating system and does not follow a plan that’s easy to figure out.

### Race Conditions
Race conditions can occur when two or more threads access a shared piece of data or resource. In this example, you’re going to create a large race condition that happens every time, but be aware that most race conditions are not this obvious. Frequently, they only occur rarely, and they can produce confusing results. As you can imagine, this makes them quite difficult to debug.

For this example, you’re going to write a class that updates a database. Okay, you’re not really going to have a database: you’re just going to fake it, because that’s not the point of this course. Your FakeDatabase will have` .__init__() and .update()` methods. FakeDatabase is keeping track of a single number: `.value`. This is going to be the shared data on which you’ll see the race condition.
Check the code of the file `race_condition.py`.

`.update()` looks a little strange. It’s simulating reading a value from a database(copying .value to a local variable), doing some computation on it, and then writing a new value back to the database(copying the local value back to .value).

The program creates a ThreadPoolExecutor with two threads and then calls .submit() on each of them, telling them to run database.update().

`.submit()` has a signature that allows both positional and named arguments to be passed to the function running in the thread: `.submit(function, *args, **kwargs)`

#### One Thread
Before you dive into this issue with two threads, let’s step back and talk a bit about some details of how threads work.

When you tell your ThreadPoolExecutor to run each thread, you tell it which function to run and what parameters to pass to it: `executor.submit(database.update, index)`. The result of this is that each of the threads in the pool will call database.update(index). 

Each thread is going to have a reference to the same FakeDatabase object, database. Each thread will also have a unique value, index, to make the logging statements a bit easier to read:
![example_image](https://files.realpython.com/media/intro-threading-shared-database.267a5d8c6aa1.png)

When the thread starts running `.update()`, it has its own version of all of the data **local** to the function. In the case of `.update()`, this is `local_copy`. This is definitely a good thing. Otherwise, two threads running the same function would always confuse each other. It means that all variables that are scoped (or local) to a function are thread-safe.

The image below steps through the execution of .update() if only a single thread is run. The statement is shown on the left followed by a diagram showing the values in the thread’s local_copy and the shared database.value:
![single_thread_image](https://files.realpython.com/media/intro-threading-single-thread.6a11288bc199.png)


So far, so good. You ran .update() once and FakeDatabase.value was incremented to one.

#### Two Threads
Getting back to the race condition, the two threads will be running concurrently but not at the same time. They will each have their own version of local_copy and will each point to the same database. It is this **shared database object that is going to cause the problems**.

When Thread 1 calls time.sleep(), it allows the other thread to start running. This is where things get interesting. Thread 2 starts up and does the same operations. It’s also copying database.value into its private local_copy, and this shared database.value has not yet been updated.

When Thread 2 finally goes to sleep, the shared database.value is still unmodified at zero, and both private versions of local_copy have the value one.

Thread 1 now wakes up and saves its version of local_copy and then terminates, giving Thread 2 a final chance to run. Thread 2 has no idea that Thread 1 ran and updated database.value while it was sleeping. It stores its version of local_copy into database.value, also setting it to one.

The two threads have interleaving access to a single shared object, overwriting each other’s results. Similar race conditions can arise when one thread frees memory or closes a file handle before the other thread is finished accessing it.

#### Basic Synchronization Using Lock
There are a number of ways to avoid or solve race conditions. You won’t look at all of them here, but there are a couple that are used frequently. Let’s start with Lock.

To solve your race condition above, you need to find a way to allow only one thread at a time into the read-modify-write section of your code. The most common way to do this is called Lock in Python. In some other languages this same idea is called a `mutex`. Mutex comes from MUTual EXclusion, which is exactly what a Lock does.

A Lock is an object that acts like a hall pass. Only one thread at a time can have the Lock. Any other thread that wants the Lock must wait until the owner of the Lock gives it up.

The basic functions to do this are `.acquire() and .release()`. A thread will call `my_lock.acquire()` to get the lock. If the lock is already held, the calling thread will wait until it is released. There’s an important point here. If one thread gets the lock but never gives it back, your **program will be stuck**. You’ll read more about this later.

Fortunately, Python’s Lock will also operate as a **context manager**, so you can use it in a with statement, and it gets released automatically when the with block exits for any reason.
Let’s look at the FakeDatabase with a Lock added to it. 
Check the code of the file `race_condition.py`.

The big change here is to add a member called `._lock`, which is a `threading.Lock()` object. This `._lock` is initialized in the unlocked state and **locked and released by the with statement**.

It’s worth noting here that the thread running this function will hold on to that Lock until it is completely finished updating the database. In this case, that means it will hold the Lock while it copies, updates, sleeps, and then writes the value back to the database.

#### Deadlock
Before you move on, you should look at a common problem when using Locks. As you saw, if the Lock has already been acquired, a second call to .acquire() will wait until the thread that is holding the Lock calls .release(). What do you think happens when you run this code:
```
import threading

l = threading.Lock()
print("before first acquire")
l.acquire()
print("before second acquire")
l.acquire()
print("acquired lock twice")
```
When the program calls l.acquire() the second time, it hangs waiting for the Lock to be released. In this example, you can fix the deadlock by removing the second call, but deadlocks usually happen from one of two subtle things:
1. An implementation bug where a Lock is not released properly
2. A design issue where a utility function needs to be called by functions that might or might not already have the Lock

The first situation happens sometimes, but **using a Lock as a context manager greatly reduces how often**. It is recommended to write code whenever possible to make use of context managers, as they help to avoid situations where an exception skips you over the .release() call.

The design issue can be a bit trickier in some languages. Thankfully, Python threading has a second object, called `RLock`, that is designed for just this situation. It allows a thread to .`acquire()` an `RLock` multiple times before it calls `.release()`. That thread is still required to call `.release()` the same number of times it called .acquire(), but it should be doing that anyway.

### Producer-Consumer Threading
The Producer-Consumer Problem is a standard computer science problem used to look at threading or process synchronization issues. You’re going to look at a variant of it to get some ideas of what primitives the Python threading module provides.

For this example, you’re going to imagine a program that needs to read messages from a network and write them to disk. The program does not request a message when it wants. It must be listening and accept messages as they come in. The messages will not come in at a regular pace, but will be coming in bursts. This part of the program is called the producer.

On the other side, once you have a message, you need to write it to a database. The database access is slow, but fast enough to keep up to the average pace of messages. It is not fast enough to keep up when a burst of messages comes in. This part is the consumer.

In between the producer and the consumer, you will create a `Pipeline` that will be the part that changes as you learn about different synchronization objects.

That’s the basic layout. Let’s look at a solution using Lock. It doesn’t work perfectly, but it uses tools you already know, so it’s a good place to start.

#### Producer-Consumer Using Lock
To generate a fake message, the producer gets a random number between one and one hundred. It calls .set_message() on the pipeline to send it to the consumer.

The producer also uses a SENTINEL value to signal the consumer to stop after it has sent ten values. This is a little awkward, but don’t worry, you’ll see ways to get rid of this SENTINEL value after you work through this example.
Check the code of the file `producer_cons_lock.py`.

The consumer reads a message from the pipeline and writes it to a fake database, which in this case is just printing it to the display. If it gets the SENTINEL value, it returns from the function, which will terminate the thread.

That seems a bit more manageable. The Pipeline in this version of your code has three members:
1. .message stores the message to pass.
2. .producer_lock is a threading.Lock object that restricts access to the message by the producer thread.
3. .consumer_lock is also a threading.Lock that restricts access to the message by the consumer thread.

Once the consumer has acquired the .consumer_lock, it copies out the value in .message and then calls .release() on the .producer_lock. Releasing this lock is what allows the producer to insert the next message into the pipeline.

Before you go on to .set_message(), there’s something subtle going on in `.get_message()` that’s pretty easy to miss. It might seem tempting to get rid of message and just have the function end with return self.message. See if you can figure out why you don’t want to do that before moving on.

Here’s the answer. As soon as the consumer calls `.producer_lock.release()`, it can be swapped out, and the producer can start running. That could happen before .release() returns! This means that there is a slight possibility that when the function returns self.message, that could actually be the next message generated, so you would lose the first message. This is another example of a **race condition**.

Moving on to `.set_message()`, you can see the opposite side of the transaction. The producer will call this with a message. It will acquire the .producer_lock, set the .message, and the call `.release()` on then consumer_lock, which will allow the consumer to read that value.

At first, you might find it odd that the producer gets two messages before the consumer even runs. If you look back at the producer and `.set_message()`, you will notice that the only place it will wait for a Lock is when it attempts to put the message into the pipeline. This is done after the producer gets the message and logs that it has it.

When the producer attempts to send this second message, it will call `.set_message()` the second time and it will block.

The operating system can swap threads at any time, but it generally lets each thread have a reasonable amount of time to run before swapping it out. That’s why the producer usually runs until it blocks in the second call to `.set_message()`.

Once a thread is blocked, however, the operating system will always swap it out and find a different thread to run. In this case, the only other thread with anything to do is the consumer.

The consumer calls `.get_message()`, which reads the message and calls `.release()` on the .producer_lock, thus allowing the producer to run again the next time threads are swapped.

While it works for this limited test, it is not a great solution to the producer-consumer problem in general because it only allows a single value in the pipeline at a time. When the **producer gets a burst of messages, it will have nowhere to put them**.

#### Producer-Consumer Using Queue
If you want to be able to handle more than one value in the pipeline at a time, you’ll need a data structure for the pipeline that allows the number to grow and shrink as data backs up from the producer.

Python’s standard library has a queue module which, in turn, has a Queue class. Let’s change the Pipeline to use a Queue instead of just a variable protected by a Lock. You’ll also use a different way to stop the worker threads by using a different primitive from Python threading, an **Event**.

Let’s start with the Event. The `threading.Event` object allows one thread to signal an event while many other threads can be waiting for that event to happen. The key usage in this code is that the threads that are waiting for the event do not necessarily need to stop what they are doing, they can just check the status of the Event every once in a while. The triggering of the event can be many things. In this example, the main thread will simply sleep for a while and then `.set()` it.

Check the code of the file `producer_cons_queue.py`.

The produce did not have to change too much. It now will loop until it sees that the event was set on line 3. It also no longer puts the SENTINEL value into the pipeline.

The consumer had to change a little more. While you got to take out the code related to the SENTINEL value, you did have to do a slightly more complicated while condition. Not only does it loop until the event is set, but it also needs to keep looping until the pipeline has been emptied.

Making sure the queue is empty before the consumer finishes prevents another fun issue. If the consumer does exit while the pipeline has messages in it, there are two bad things that can happen. The first is that you **lose those final messages**, but the more serious one is that the **producer can get caught attempting to add a message to a full queue and never return**. This happens if the event gets triggered after the producer has checked the `.is_set()` condition but before it calls `pipeline.set_message()`.

You can see that Pipeline is a subclass of `queue.Queue`. Queue has an optional parameter when initializing to specify a maximum size of the queue.

If you give a positive number for maxsize, it will limit the queue to that number of elements, causing **.put() to block until there are fewer than maxsize elements**. If you don’t specify maxsize, then the queue **will grow to the limits of your computer’s memory**.

`.get_message() and .set_message()` got much smaller. They basically wrap `.get() and .put()` on the Queue. You might be wondering where all of the locking code that prevents the threads from causing race conditions went.

The core devs who wrote the standard library knew that a Queue is frequently used in multi-threading environments and incorporated all of that locking code inside the Queue itself. **Queue is thread-safe**.

ou can see the producer got to create five messages and place four of them on the queue. It got swapped out by the operating system before it could place the fifth one. The consumer then ran and pulled off the first message. 

As the program starts to wrap up, can you see the main thread generating the event which causes the producer to exit immediately. The consumer still has a bunch of work do to, so it keeps running until it has cleaned out the pipeline.

Lock and Queue are handy classes to solve concurrency issues, but there are others provided by the standard library. Before you wrap up this tutorial, let’s do a quick survey of some of them.

### Semaphore
The first Python threading object to look at is threading.Semaphore. A Semaphore is a counter with a few special properties. The first one is that the counting is atomic. This means that there is a guarantee that the operating system will not swap out the thread in the middle of incrementing or decrementing the counter.

The internal counter is incremented when you call .release() and decremented when you call .acquire().

The next special property is that if a thread calls .acquire() when the counter is zero, that thread will block until a different thread calls .release() and increments the counter to one.

Semaphores are frequently used to protect a resource that has a limited capacity. An example would be if you have a pool of connections and want to limit the size of that pool to a specific number.

### Barrier
A threading.Barrier can be used to keep a fixed number of threads in sync. When creating a Barrier, the caller must specify how many threads will be synchronizing on it. Each thread calls .wait() on the Barrier. They all will remain blocked until the specified number of threads are waiting, and then the are all released at the same time.

Remember that threads are scheduled by the operating system so, even though all of the threads are released simultaneously, they will be scheduled to run one at a time.

One use for a Barrier is to allow a pool of threads to initialize themselves. Having the threads wait on a Barrier after they are initialized will ensure that none of the threads start running before all of the threads are finished with their initialization.