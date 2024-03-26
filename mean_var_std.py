import numpy as np

def calculate(list):
    try:
        a = list[0:3]
        b = list[3:6]
        c = list[6:9]
        matriz = np.array([a,b,c])
        
        #mean
        mean_axis1 = np.mean(matriz, axis=0).tolist()
        mean_axis2 = np.mean(matriz, axis=1).tolist()
        mean_flat = np.mean(matriz)
        
        #var
        variance_axis1 = np.var(matriz, axis=0).tolist()
        variance_axis2 = np.var(matriz, axis=1).tolist()
        variance_flat = np.var(matriz)
        
        #std
        standardev_axis1 = np.std(matriz, axis=0).tolist()
        standardev_axis2 = np.std(matriz, axis=1).tolist()
        standardev_flat = np.std(matriz)
        
        #max
        max_axis1 = np.max(matriz, axis=0).tolist()
        max_axis2 = np.max(matriz, axis=1).tolist()
        max_flat = np.max(matriz)
        
        #min
        min_axis1 = np.min(matriz, axis=0).tolist()
        min_axis2 = np.min(matriz, axis=1).tolist()
        min_flat = np.min(matriz)
        
        #sum
        sum_axis1 = np.sum(matriz, axis=0).tolist()
        sum_axis2 = np.sum(matriz, axis=1).tolist()
        sum_flat = np.sum(matriz)
        
        
        calculations = {
            'mean': [mean_axis1, mean_axis2, mean_flat], 
            'variance': [variance_axis1, variance_axis2, variance_flat], 
            'standard deviation': [standardev_axis1, standardev_axis2, standardev_flat],
            'max': [max_axis1, max_axis2, max_flat],
            'min': [min_axis1, min_axis2, min_flat],
            'sum': [sum_axis1, sum_axis2, sum_flat]
        }
        
        return calculations
    except:
        raise ValueError("List must contain nine numbers.")