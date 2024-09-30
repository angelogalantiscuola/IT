%% Begin Waypoint %%
- [[async and await]]
- [[concurrency vs parallelism]]
- [[coroutines]]

%% End Waypoint %%


Modern versions of Python have support for **asynchronous code** using something called **coroutines**, with **`async` and `await`** syntax.

## Asynchronous code
Asynchronous code just means that the language has a way to tell the computer / program that at some point in the code, it will have to **wait for something else to finish** somewhere else. Let's say that _something else_ is called "slow-file".
So, during that time, the computer can go and do some other work, while "slow-file" finishes.

That wait for something else normally refers to **I/O operations that are relatively slow** (compared to the speed of the processor and the RAM memory), like waiting for:

- the **data from the client** to be sent through the network
- the data sent by your program to be **received by the client** through the network
- the contents of a **file** in the disk to be **read** by the system and given to your program
- the contents your program gave to the system to be **written to disk**
- a **remote API** operation
- a **database operation** to finish

As the execution time is consumed mostly by waiting for I/O operations, they call them **I/O bound operations**.

