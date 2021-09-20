## Memory Management in Python

In this task, we’re going to do a deep dive into the internals of Python to understand how it handles memory management.

### Memory Is an Empty Book
You can begin by thinking of a computer’s memory as an empty book intended for short stories. There’s nothing written on the pages yet. Eventually, different authors will come along. Each author wants some space to write their story in.

Since they aren’t allowed to write over each other, they must be careful about which pages they write in. Before they begin writing, they consult the manager of the book. The manager then decides where in the book they’re allowed to write.

Since this book is around for a long time, many of the stories in it are no longer relevant. When no one reads or references the stories, they are removed to make room for new stories.

In essence, computer memory is like that empty book. In fact, it’s common to call fixed-length contiguous blocks of memory pages, so this analogy holds pretty well.

The authors are like different **applications or processes** that need to store data in memory. The manager, who decides where the authors can write in the book, plays the role of a **memory manager** of sorts. The person who removed the old stories to make room for new ones is a **garbage collector**.

### Memory Management: From Hardware to Software
Memory management is the process by which applications read and write data. A **memory manager** determines where to put an application’s data. Since there’s a finite chunk of memory, like the pages in our book analogy, the manager has to find some free space and provide it to the application. This process of providing memory is generally called **memory allocation**.

On the flip side, when data is no longer needed, it can be deleted, or **freed**. But freed to where? Where did this “memory” come from?

Somewhere in your computer, there’s a **physical device storing data** when you’re running your Python programs. There are many layers of abstraction that the Python code goes through before the objects actually get to the hardware though.

One of the main layers above the hardware (such as RAM or a hard drive) is the operating system (OS). It **carries out (or denies) requests to read and write memory**.

Above the OS, there are applications, one of which is the default Python implementation.Memory management for your Python code is handled by the Python application.

### The Default Python Implementation
The default Python implementation, CPython, is actually written in the C programming language.

The Python language is defined in a [reference manual](https://docs.python.org/3/reference/index.html) written in English. However, that manual isn’t all that useful by itself. You still need something **to interpret written code based on the rules in the manual**.

You also need something **to actually execute interpreted code on a computer**. The default Python implementation fulfills both of those requirements. It converts your Python code into instructions that it then runs on a virtual machine.

Python is an interpreted programming language. Your Python code actually gets **compiled down to more computer-readable instructions called bytecode**. These instructions get interpreted by a virtual machine when you run your code.

Have you ever seen a `.pyc` file or a `__pycache__` folder? That’s the bytecode that gets interpreted by the virtual machine.

It’s important to note that there are implementations other than `CPython`. [Jython](http://www.jython.org/) compiles down to Java bytecode to run on the Java Virtual Machine. Then there’s [PyPy](https://pypy.org/).

### Basic understanding of CPython

We will focus on the memory management done by the default implementation of Python, CPython. The memory management algorithms and structures exist in the CPython code, in C. which does not natively support object-oriented programming.

You may have heard that everything in **Python is an object**, even types such as int and str. Well, it’s true on an implementation level in CPython. There is a struct(custom data type that groups together different data types) called a **PyObject**, which every other object in CPython uses.

The PyObject, the grand-daddy of all objects in Python, contains only two things:
* **ob_refcnt**: reference count
* **ob_type**: pointer to another type

The reference count is used for **garbage collection**. Then you have a [pointer](https://realpython.com/pointers-in-python/) to the actual object type. That object type is just another struct that describes a Python object (such as a dict or int).

Each object has its own object-specific **memory allocator that knows how to get the memory to store that object**. Each object also has an object-specific **memory deallocator that “frees” the memory** once it’s no longer needed.

However, there’s an important factor in all this talk about allocating and freeing memory. Memory is a **shared resource** on the computer, and bad things can happen if **two different processes try to write to the same location at the same time**

One solution to this problem is a single, global lock (GIL) on the interpreter when a thread is interacting with the shared resource (the page in the book). In other words, only one author can write at a time..

Python’s GIL accomplishes this by **locking the entire interpreter**, meaning that it’s not possible for another thread to step on the current one. When CPython handles memory, it uses the GIL to ensure that it does so safely.

### Garbage collection
Let’s revisit the book analogy and assume that some of the stories in the book are getting very old. No one is reading or referencing those stories anymore. If no one is reading something or referencing it in their own work, you could get rid of it to make room for new writing.

That old, unreferenced writing could be compared to an object in Python whose **reference count has dropped to 0**. Remember that every object in Python has a reference count and a pointer to a type.

The reference count gets increased for a few different reasons. For example, the reference count will increase if you **assign it to another variable or pass the object as an argument or nclude the object in a list etc...**.

### CPython’s Memory Management
We’re going to dive deep into CPython’s memory architecture and algorithms, so buckle up.

As mentioned before, there are layers of abstraction from the physical hardware to CPython. The operating system (OS) abstracts the physical memory and creates a virtual memory layer that applications (including Python) can access. An OS-specific virtual memory manager carves out a chunk of memory for the Python process.

Python uses a portion of the memory for internal use and non-object memory. The other portion is dedicated to object storage (int, dict, and the like). 

CPython has an object allocator that is responsible for **allocating memory within the object memory area**. This object allocator is where most of the magic happens. It gets called every time a new object needs space allocated or deleted.

Typically, the adding and removing of data for Python objects like list and int doesn’t involve too much data at a time. So the design of the allocator is tuned to work well with small amounts of data at a time. It also tries not to allocate memory until it’s absolutely required.

#### CPython's memory aloocation strategy
Now we’ll look at CPython’s memory allocation strategy. First, we’ll talk about the 3 main pieces and how they relate to each other.

![memory allocation image](https://files.realpython.com/media/memory_management_5.394b85976f34.png)

* **Arenas** are the largest chunks of memory and are aligned on a page boundary in memory. A page boundary is the edge of a fixed-length contiguous chunk of memory that the OS uses. Python assumes the system’s page size is 256 kilobytes.

* **pools** are one virtual memory page (4 kilobytes). These are like the pages in our book analogy. These pools are fragmented into smaller blocks of memory.

* All the **blocks** in a given pool are of the same “size class.” A size class defines a specific block size, given some amount of requested data.

| Request in bytes 	| Size of allocated block  | Size class idx |
| ----------------- | ------------------------ | -------------- |
|       1-8         |      	     8	           |        0       |
|       9-16	    |            16            |        1       |
|       17-24	    |            24	           |        2       |
|       25-32	    |            32	           |        3       |
|       33-40	    |            40	           |        4       |
|       41-48	    |            48	           |        5       |
|       49-56	    |            56	           |        6       |
|         …	        |            …	           |        …       |
|      497-504	    |            504	       |        62      |
|      505-512	    |            512	       |        63      |

For example, if 42 bytes are requested, the data would be placed into a size 48-byte block.

#### Pools
Pools are composed of blocks from a single size class. Each pool maintains a double-linked list to other pools of the same size class. In that way, the algorithm can easily find available space for a given block size, even across different pools.

A `usedpools` list tracks all the pools that have some space available for data for each size class. When a given block size is requested, the algorithm checks this usedpools list for the list of pools for that block size.

Pools themselves must be in one of 3 states: **used, full, or empty**. A `used pool` has available blocks for data to be stored. A `full pool`’s blocks are all allocated and contain data. An `empty pool` has no data stored and can be assigned any size class for blocks when needed.

A `freepools` list keeps track of all the pools in the empty state. But when do empty pools get used?

Assume your code needs an 8-byte chunk of memory. If there are no pools in usedpools of the 8-byte size class, a **fresh empty pool is initialized** to store 8-byte blocks. This new pool then gets added to the usedpools list so it can be used for future requests.

Say a full pool frees some of its blocks because the memory is no longer needed. That pool **would get added back to the usedpools list for its size class**.

You can see now how pools can move between these states (and even memory size classes) freely with this algorithm.

#### Blocks

![memory_blocks_image](https://files.realpython.com/media/memory_management_3.52bffbf302d3.png)

As seen in the diagram above, pools contain a pointer to their “free” blocks of memory. There’s a slight nuance to the way this works. This allocator “strives at all levels (arena, pool, and block) never to touch a piece of memory until it’s actually needed,” according to the comments in the source code.

That means that a pool can have blocks in 3 states. These states can be defined as follows:
* **untouched**: a portion of memory that has not been allocated
* **free**: a portion of memory that was allocated but later made “free” by CPython and that no longer contains relevant data
* **allocated**: a portion of memory that actually contains relevant data

The freeblock pointer points to a singly linked list of free blocks of memory. In other words, a list of available places to put data. If more than the available free blocks are needed, the allocator will get some untouched blocks in the pool.

As the memory manager makes blocks “free,” those now free blocks get added to the front of the freeblock list. The actual list may not be contiguous blocks of memory, like the first nice diagram. It may look something like the diagram below:

![non_contiguous_freeblocks_image](https://files.realpython.com/media/memory_management_4.4a30dfa2d111.png)

#### Arenas
Arenas contain pools. Those pools can be used, full, or empty. Arenas themselves don’t have as explicit states as pools do though.

Arenas are instead organized into a doubly linked list called usable_arenas. The list is sorted by the number of free pools available. The fewer free pools, the closer the arena is to the front of the list.

![arena_image](https://files.realpython.com/media/memory_management_6.60e9761bc158.png)

This means that the arena that is the most full of data will be selected to place new data into. But why not the opposite? Why not place data where there’s the most available space?

This brings us to the idea of truly freeing memory. You’ll notice that I’ve been saying “free” in quotes quite a bit. The reason is that when a block is deemed “free”, that memory is not actually freed back to the operating system. The Python process keeps it allocated and will use it later for new data. Truly freeing memory returns it to the operating system to use.

Arenas are the only things that can truly be freed. So, it stands to reason that those arenas that are closer to being empty should be allowed to become empty. That way, that chunk of memory can be truly freed, reducing the overall memory footprint of your Python program.