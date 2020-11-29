#######################################################################################
## Comparing queries that are highly ranked with previous versions of their documents 
## WARC is Web Archive Format for storing web crawls. To study web dynamics of 
## rank-incentivized queries, the data considered is purely in "warc" format. 
# Import relevant libraries 
import warc
import gzip
import numpy as np
import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt
from scipy.stats import norm 

# creating KL divergence formula 
def KL_Divergence(p, q):
    return np.sum(np.where(p != 0, p * np.log(p / q), 0))


# Fetching the indexed ClueWeb data based on LucindiIndex
with gzip.open("C:\ClueWeb09\2008-01-01", "rb") as f1:
    file_content = f1.read()
    x = f1.readline()
    trecCW = norm.pdf(x, 0, 2)
    q = norm.pdf(x, 1, 1)

# 
# clue_web_01_08_df = pd.read_csv('C:\ClueWeb09\2008-01-01\en0000\01.warc.gz', compression='gzip',
#                                  header=1, sep='\t', quotechar='"')


# Access the processed warc files based off of indexes from Indri toolkit
f2 = warc.open("C:\Information Retrieval\ClueWeb09\2008-01-01\en0000\01.warc.gz")
for record in f2:
    print (record['Trec-'], record['Content-Length'])


f3 - warc.open("C:\Information Retrieval\ClueWeb09\2008-02-01\en0000\01.warc.gz")
for record in f3:
    print (record['Trec-'], record['Content-Length'])

# Access document-query-mapppings for the ClueWeb09 web 
# crawls to associate highly ranked queries with corresponding documents
df = pd.read_csv("C:\Information Retrieval\document_query_mapping.tsv", sep="\t")


# Plotting the responses for KL divergence 
plt.title('KL(P||Q) = %1.2f' % KL_Divergence(p, q))
plt.plot(x, p)
plt.plot(x, q, c='blue')

q = norm.pdf(x, 3, 4)
plt.title('KL(P||Q) = %1.2f' % KL_Divergence(p, q))
plt.plot(x, p)
plt.plot(x, q, c='blue')


q = norm.pdf(x, 2, 3)
plt.title('KL(P||Q) = %1.3f' % KL_Divergence(q, p))
plt.plot(x, p)
plt.plot(x, q, c='blue')


