import asyncio
import random
from time import time


async def main(url):
    print(f'下载 {url} ......')
    await asyncio.sleep(random.random())
    print(f'{url} 下载完毕！')


if __name__ == '__main__':
    st = time()
    loop = asyncio.get_event_loop()
    func = [main(i) for i in range(1, 100)]
    loop.run_until_complete(asyncio.wait(func))
    loop.close()
    et = time()

    print(f'用时{et - st :.4f}')
