import numpy as np
import seaborn as sns
import gzip
from scipy.stats import norm
from matplotlib import pyplot as plt

sns.set()

# creating KL divergence formula 
def KL_Divergence(p, q):
    return np.sum(np.where(p != 0, p * np.log(p / q), 0))


with gzip.open('C:\\ClueWeb09\\2008-01-01', 'rb') as f:
    file_content = f.read()
    x = f.readline()
    trecCW = norm.pdf(x, 0, 2)
    q = norm.pdf(x, 2, 2)

plt.title('KL(P||Q) = %1.3f' % kl_divergence(p, q))
plt.plot(x, p)
plt.plot(x, q, c='red')

q = norm.pdf(x, 5, 4)
plt.title('KL(P||Q) = %1.3f' % kl_divergence(p, q))
plt.plot(x, p)
plt.plot(x, q, c='red')


q = norm.pdf(x, 5, 4)
plt.title('KL(P||Q) = %1.3f' % kl_divergence(q, p))
plt.plot(x, p)
plt.plot(x, q, c='red')