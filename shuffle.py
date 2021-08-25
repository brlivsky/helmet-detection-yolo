import random
lines = open('train.txt').readlines()
random.shuffle(lines)
open('train.txt', 'w').writelines(lines)