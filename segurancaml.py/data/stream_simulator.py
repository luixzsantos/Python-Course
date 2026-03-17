import numpy as np
import time

def stream_data():
    while True:
        X = np.random.rand(1, 6)   # 6 features simuladas
        y = np.random.choice([0, 1])  # 0 = normal | 1 = ataque
        yield X, y
        time.sleep(1)
