def sortNumbers(data, condition):
    n = len(data)
    for i in range(n):
        for j in range(0, n - i - 1):
            if condition == 'ASC':
                if data[j] > data [j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j] 
            elif condition == 'DESC':
                if data[j] < data [j + 1]:
                    data[j], data[j + 1] = data[j + 1], data[j] 
    return data 

def sortData(weights, data, condition):
    if len(weights) != len(data):
        raise ValueError('Invalid input data')
    n = len(weights)
    for i in range(n):
        for j in range(0, n - i - 1):
            if condition == 'ASC':
                if weights[j] > weights[j + 1]:
                    weights[j], weights [j + 1] = weights[j + 1], weights[j]
                    data[j], data[j + 1] = data[j + 1], data[j]
            elif condition == 'DESC':
                if weights[j] < weights[j + 1]:
                    weights[j], weights [j + 1] = weights[j + 1], weights[j]
                    data[j], data[j + 1] = data[j + 1], data[j]
    return data

weights = [3, 2, 4]
data = ['Ford', 'BMW', 'Audi']

sorted_data = sortData(weights, data, 'DESC')
          









