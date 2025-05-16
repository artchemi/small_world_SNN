# 📁 Навигация по проекту
```
basic/
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
│├── model_basic_train.py
│├── random_conn_generator
│└── utils_data.py
│
├── weights   -   сюда сохраняются веса во время обучения
│├── theta_dir   -   коэффициенты гомеостазиса
││├── theta_A1000.npy
││└── theta_A{i}.npy
││
│└── XeAe_dir   -   межслойные веса
│ ├── XeAe1000.npy
│ └── XeAe{i}.npy
│
├── config.py    -   все параметры модели и обучения настраивать здесь
└── download_MNIST.py   -   загрузка MNIST в папку с Google Drive

```

# 📦 Установка окружения
Установить и активировать окружение можно следующими командами:

```
conda env create -f environment.yml
conda activate Brian2STDP
```

Список основных библиотек и их версий:
```
brian2==2.8.0.4
brian2tools==0.3
cpython==3.10.16
matplotlib==3.10.0
networkx==3.4.2
scipy==1.15.2
numpy==2.1.3
```

# 🛠️ Подготовка данных и модели для обучения
### 1. Загрузка MNIST
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

### 2. Генерация начальных весов модели

Скрипт ```random_conn_generator.py``` создает и сохраняет в папку ```random/``` начальные веса и коэффициенты гомеостазиса модели:
```
python src/random_conn_generator.py
```

### 3. Подготовка параметров модели и обучения

Настройка модели осуществляется в ```config.py```. Там же есть описание этих параметров, которые настраиваются перед запуском обучения.

Запуск обучения осуществляется следующей командой:

```
python model_basic_train.py
```

Результаты по динамике весов сохраняются в ```weights/```.
