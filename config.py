# Путь где хранится MNIST
DATA_PATH = 'mnist/'

# Файлы MNIST для обучения и теста
MNIST_NAMES = ['t10k-images.idx3-ubyte', 't10k-labels.idx1-ubyte', 'testing.pickle', 
               'train-images.idx3-ubyte', 'training.pickle', 'train-labels.idx1-ubyte']

# URL на Google Drive для этих файлов
DATA_URL = ['1aqzkZU2c-PFb2MlRdEuDC9Lik3sE4Prp', '1F3UKRk8OYf8ZFL8MDdyrLqb1bo5be98M', '1AIiweoguLz-HXSQJHesQeUYMhog7A51j',
            '1_p5AZDvdPjrh-xXkrxU56hlSoNEhQVF-', '1I73otAs_XQoYnIvrfxeMfAbGZ6pKmSiR', '1nTTBiPxe34LUJddao81O7TRDgmAQ_8M3']

# Количество нейронов
N_NEURONS = 100