# Asyncio / threading mix

# Our client is in dire need of a solution. We do have it. There is one caveat – his whole platform so far is written
# in asyncio while the function that would help him is synchronous. We need a solution to that predicament.

# This situation is simulated in the following manner:
# - We provide functions sync_f() and async_g() via sys.stdin.
# - These function accept an optional parameter, but don't do anything with it. Both functions return an integer.
# - The goal is to write the code in such a way that both sync_f() and async_g() are evaluated in parallel.

# Due to a bug in the test evaluation platform, multiprocessing cannot be reliably evaluated. Please, do not use processes
# for this task. Also – understanding functions sync_f() and async_g() is neither required nor needed. Trying
# to read through them will cost you time, which will decrease your score.


# Asyncio  threading mix.Our client is in dire need of a solution. We do have it. There is one caveat – his whole platform so far is written
# in asyncio while the function that would help him is synchronous. We need a solution to that predicament.

# This situation is simulated in the following manner:
# - We provide functions sync_f() and async_g() via sys.stdin.
# - These function accept an optional parameter, but don't do anything with it. Both functions return an integer.
# - The goal is to write the code in such a way that both sync_f() and async_g() are evaluated in parallel.

# Due to a bug in the test evaluation platform, multiprocessing cannot be reliably evaluated. Please, do not use processes
# for this task. Also – understanding functions sync_f() and async_g() is neither required nor needed. Trying
# to read through them will cost you time, which will decrease your score.


# Sample Input
# # please
# # please
# # please

# # do not try to read this
# # it is not required to understand it but
# # reading through it will take time
# # which will decrease your score
import asyncio
import threading
import time
from concurrent.futures import ProcessPoolExecutor

def sync_f(a=None):
    print('start1')
    # time.sleep is bugged, this is an ugly-but-working way of getting an actual sleep.
    lock = threading.Lock()
    lock.acquire(blocking=False)
    lock.acquire(timeout=3)
    print('endstart1')
    return 2

async def async_g(a=None):
    print('start2')
    await asyncio.sleep(3)
    print('endstart2')
    return 1


async def main(loop):
    tasks = []
    tasks.append(loop.run_in_executor(None, sync_f) )
    tasks.append(async_g())
    response = await asyncio.gather(*tasks, return_exceptions=True)
    print(max(*response))


if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main(loop))
