# Краткая структура проекта
```
small_world/
├── mnist
│├── t10k-images.idx3-ubyte
│├── t10k-labels.idx1-ubyte
│├── testing.pickle
│├── train-images.idx3-ubyte
│├── training.pickle
│└── train-labels.idx1-ubyte
├── random   -   инициализированные веса модели
│├── AeAi.npy   -   Межслойные веса (?)
│├── AiAe.npy
│├── XeAe.npy
│└── XeAi.npy
├── results   -   результаты экспериментов
│├── XXX
│└── XXX
├── src
│├── evaluation.py
│├── model_SW.py
│├── random_conn_generator
│└── utils_data.py
├── config.py    -   все параметры модели и обучения настраивать здесь
├── download_MNIST.py   -   загрузка MNIST в папку с Google Drive
├── 
```


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
