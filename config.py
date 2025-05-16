# Путь где хранится MNIST
DATA_PATH = 'mnist/'

# Файлы MNIST для обучения и теста
MNIST_NAMES = ['t10k-images.idx3-ubyte', 't10k-labels.idx1-ubyte', 'testing.pickle', 
               'train-images.idx3-ubyte', 'training.pickle', 'train-labels.idx1-ubyte']

# URL на Google Drive для этих файлов
DATA_URL = ['1aqzkZU2c-PFb2MlRdEuDC9Lik3sE4Prp', '1F3UKRk8OYf8ZFL8MDdyrLqb1bo5be98M', '1AIiweoguLz-HXSQJHesQeUYMhog7A51j',
            '1_p5AZDvdPjrh-xXkrxU56hlSoNEhQVF-', '1I73otAs_XQoYnIvrfxeMfAbGZ6pKmSiR', '1nTTBiPxe34LUJddao81O7TRDgmAQ_8M3']


# Фиксированный seed
SEED = 42

# Количество нейронов
N_NEURONS = 100

# Интервал оценки точности/через сколько итераций считается точность
ACCURACY_UPDATE_INTERVAL = 10000

# Параметры графа Watts-Strogatz
N_NODES = N_NEURONS    # Количество вершин, должно быть равным количеству нейронов в скрытом слое
K_NODES = int(N_NEURONS * 0.8)    # Количество соседних вершин для одной вершины, при значениях близки к N_NODES - будет полносвязный граф
P_DIRECTION = 0.1    # Вероятность перенаправления ребра, p=0 - регулярный граф, p=1 - полностью случайный