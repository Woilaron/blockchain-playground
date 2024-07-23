from hashlib import sha256
import time
from random import randint

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def mine(complexity=3):
    start_time = time.time()
    head = randint(0, 1_000_000_000)
    nonce = head
    sha = sha256(str(nonce).encode('utf-8')).hexdigest()
    while sha[:complexity] != '0' * complexity:
        nonce += 1
        sha = sha256(str(nonce).encode('utf-8')).hexdigest()

    print(f'{bcolors.OKGREEN}Mined block{bcolors.ENDC} {sha[:complexity]}{sha[complexity:]} with nonce {nonce}')
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
