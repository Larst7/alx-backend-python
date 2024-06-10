0x01. Python - Async
Description
This project focuses on asynchronous programming in Python using the asyncio module. The primary objective is to understand and implement asynchronous coroutines, execute them concurrently, create asyncio tasks, and measure execution time.

Learning Objectives
By the end of this project, you should be able to explain the following concepts without any external help:

async and await syntax
How to execute an async program with asyncio
How to run concurrent coroutines
How to create asyncio tasks
How to use the random module
Resources
Async IO in Python: A Complete Walkthrough
asyncio - Asynchronous I/O
random.uniform
Requirements
A README.md file at the root of the project directory is mandatory.
Allowed editors: vi, vim, emacs.
All your files will be interpreted/compiled on Ubuntu 18.04 LTS using Python 3 (version 3.7).
All your files should end with a new line.
All your files must be executable.
The length of your files will be tested using wc.
The first line of all your files should be exactly #!/usr/bin/env python3.
Your code should use the pycodestyle style (version 2.5.x).
All your functions and coroutines must be type-annotated.
All your modules should have documentation.
All your functions should have documentation.
Project Structure
plaintext
Copy code
0x01-python_async_function/
├── 0-basic_async_syntax.py
├── 0-main.py
├── 1-concurrent_coroutines.py
├── 1-main.py
├── 2-measure_runtime.py
├── 2-main.py
├── 3-tasks.py
├── 3-main.py
├── 4-tasks.py
├── 4-main.py
└── README.md
Tasks
Task 0: The basics of async
Write an asynchronous coroutine that takes an integer argument max_delay (default value 10) named wait_random that waits for a random delay between 0 and max_delay (inclusive) seconds and eventually returns it.

File: 0-basic_async_syntax.py
Example:

python
Copy code
import asyncio
from 0-basic_async_syntax import wait_random

print(asyncio.run(wait_random()))
print(asyncio.run(wait_random(5)))
print(asyncio.run(wait_random(15)))
Task 1: Let's execute multiple coroutines at the same time with async
Import wait_random from the previous file and write an async routine called wait_n that takes in 2 int arguments (n and max_delay). You will spawn wait_random n times with the specified max_delay.

File: 1-concurrent_coroutines.py
Example:

python
Copy code
import asyncio
from 1-concurrent_coroutines import wait_n

print(asyncio.run(wait_n(5, 5)))
print(asyncio.run(wait_n(10, 7)))
print(asyncio.run(wait_n(10, 0)))
Task 2: Measure the runtime
From the previous file, import wait_n into 2-measure_runtime.py. Create a measure_time function with integers n and max_delay as arguments that measures the total execution time for wait_n(n, max_delay) and returns total_time / n.

File: 2-measure_runtime.py
Example:

python
Copy code
from 2-measure_runtime import measure_time

n = 5
max_delay = 9

print(measure_time(n, max_delay))
Task 3: Tasks
Import wait_random from 0-basic_async_syntax. Write a function (do not create an async function) task_wait_random that takes an integer max_delay and returns an asyncio.Task.

File: 3-tasks.py
Example:

python
Copy code
import asyncio
from 3-tasks import task_wait_random

async def test(max_delay: int) -> float:
    task = task_wait_random(max_delay)
    await task
    print(task.__class__)

asyncio.run(test(5))
Task 4: Tasks
Take the code from wait_n and alter it into a new function task_wait_n. The code is nearly identical to wait_n except task_wait_random is being called.

File: 4-tasks.py
Example:

python
Copy code
import asyncio
from 4-tasks import task_wait_n

n = 5
max_delay = 6
print(asyncio.run(task_wait_n(n, max_delay)))
GitHub Repository
Repository: alx-backend-python
Directory: 0x01-python_async_function

