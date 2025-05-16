import gdown
import os
import sys

from config import DATA_PATH, MNIST_NAMES, DATA_URL


def main():
    os.makedirs(DATA_PATH, exist_ok=True)
    
    for mnist_name, url in zip(MNIST_NAMES, DATA_PATH):
        gdown(url, DATA_PATH + mnist_name)


if __name__ == '__main__':
    main()
