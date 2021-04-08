#编写程序，计算2000000以内的素数之和

import math

def is_prime(number):#is_prime（素数判断）
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:#将2以及所有合数因子排除掉
            return False
        for current in range(3, int(math.sqrt(number) + 1), 2):#直接从3起步，步长为2.在range()函数产生的序列是[3,5,7,9,...]
            if number % current == 0:
                return False
        return True
    return False

def get_primes(number):
    while True:
        if is_prime(number):
            yield number
        number += 1

def solve():
    total = 2
    for next_prime in get_primes(3):  # 2是第一个素数，3是第二个素数，接下来靠+1往上走，靠素数判断方法判断是不是素数，是的话就累加
        if next_prime < 2000000:
            total += next_prime
        else:
            print(total)
            return

if __name__ == '__main__':
    solve()
