from hashlib import sha256
import time
from random import randint


def mine(complexity=3):
    start_time = time.time()
    head = randint(0, 1_000_000_000)
    nonce = head
    sha = sha256(str(nonce).encode('utf-8')).hexdigest()
    while sha[:complexity] != '0' * complexity:
        nonce += 1
        sha = sha256(str(nonce).encode('utf-8')).hexdigest()

    print(f'Mined block {sha[:complexity]}{sha[complexity:]} with nonce {nonce}')
    end_time = time.time()

    return end_time - start_time


complexity = 2
for i in range(100):
    mean_time = 0
    for j in range(5):
        mean_time += mine(complexity)
    mean_time /= 5
    print(f'\tMean time for this chain part {mean_time: .2f}')
    if mean_time > 10:
        print(f'Decreased complexity : {complexity} -> {complexity - 1}')
        complexity -= 1
    elif mean_time < 10:
        print(f'Increased complexity : {complexity} -> {complexity + 1}')
        complexity += 1
    time.sleep(3)
