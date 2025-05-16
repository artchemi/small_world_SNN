# Подготовка данных и модели для обучения
Для дальнешйнее работы необходимо скачать MNIST. Это можно сделать через скрипт ```download_MNIST.py```:
```python downoload_MNIST.py```, 
либо по ссылке на Google Drive:
https://drive.google.com/drive/folders/1l6ZqFE_87biOBC0kMlGZp43PZs-4bZ2C?usp=sharing


Структура директории ```mnist``` должна выглядеть так:
```
mnist/
├── t10k-images.idx3-ubyte
├── t10k-labels.idx1-ubyte
├── testing.pickle
├── train-images.idx3-ubyte
├── training.pickle
└── train-labels.idx1-ubyte
```


Настройка модели осуществляется в ```config.py```. Для варьирования и постановки экспериментов важны следующие параметры:
