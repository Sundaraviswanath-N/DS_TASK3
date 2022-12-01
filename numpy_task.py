
import numpy as np
import numpy.random as npr
a=np.zeros((10,10))
for i in range(10):
    for j in range(10):
        a[i][j]=a[i][j]+i+j
print("\n10 × 10 matrix A in which A[i][j] = i + j\n")
print(a+2)

data = np.exp(npr.randn(50, 5))
print("\n50 x 5 Random Numbers\n")
print(data)

print("\nMean - Column wise\n")
mean=np.mean(data,axis=0)
std=np.std(data,axis=0)
print (mean)
print("\nStandard Deviation - Column wise\n")
print (std)
mean_sub=data-mean
print("\nMatrix After Subtracting Mean Off of Each Coulmn\n")
print(mean_sub)
normalized=mean_sub / std
print("\nMatrix After Dividing STD Off of Each Coulmn\n")
print(normalized)
normalized_mean=np.mean(normalized,axis=0)
normalized_std=np.std(normalized,axis=0)
print("\nMean After Normalization\n")

print(normalized_mean)
print("\nSTD After Normalization\n")
print(normalized_std)