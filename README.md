# Краткая структура проекта
```
small_world/
│
├── mnist
│├── t10k-images.idx3-ubyte
│├── t10k-labels.idx1-ubyte
│├── testing.pickle
│├── train-images.idx3-ubyte
│├── training.pickle
│└── train-labels.idx1-ubyte
│
├── random   -   инициализированные веса модели
│├── AeAi.npy
│├── AiAe.npy
│├── XeAe.npy   -   межслойные веса
│└── XeAi.npy
│
├── old_results   -   старые результаты экспериментов
│├── XXX
│└── XXX
│
├── src
│├── evaluation.py
│├── model_SW.py
│├── random_conn_generator
│└── utils_data.py
│
├── weights   -   сюда сохраняются веса во время обучения
│├── small_world   -   внутрислойные веса в слое возбуждающих нейронов
││├── AeSW_0.npy
││└── AeSW_{i}.npy
││
│├── theta_dir   -   коэффициенты гомеостазиса
││├── theta_A1000.npy
││└── theta_A{i}.npy
││
│└── XeAe_dir   -   межслойные веса
│ ├── XeAe1000.npy
│ └── XeAe{i}.npy
│
├── config.py    -   все параметры модели и обучения настраивать здесь
├── download_MNIST.py   -   загрузка MNIST в папку с Google Drive
├── 
```

# Установка окружения
Установить окружение можно следующей командой:

```
conda env create -f environment.yml
```
# Подготовка данных и модели для обучения
Для дальнейшей работы необходимо скачать MNIST. Это можно сделать через скрипт ```download_MNIST.py```:

```
python downoload_MNIST.py
```

Либо по ссылке на Google Drive:
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


Настройка модели осуществляется в ```config.py```. Там же есть описание этих параметров. Далее можно добавить новые параметры в конфиг.
