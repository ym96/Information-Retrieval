# Information-Retrieval
 8470 project

Note: The project is currently in its development stage. There will be more stable versions rolled out soon. 

# A Quick Overview:
The Web is a dynamic retrieval setting. An important part of this dynamics is due to the ranking incentives of Web pages’ authors. That is, some are interested in having their pages highly ranked for queries of interest. As a result, they might respond to induced rankings by modifying their documents so as to improve their future ranking — a practice also known as search engine optimization.

The ranking incentives of many authors of Web pages play an important role in the Web dynamics.
Authors who opt to have their pages highly ranked for queries of interest often respond to rankings for these queries by manipulating their pages

The motivation behind this is to better understand and further explore Web dynamics with respect to the inherent competitive retrieval setting which is driven by rank-incentivized authors.

The paper provides a novel dataset for performing Web dynamics analysis by examining temporal changes on documents. More details on the historical snapshots ClueWeb09 data can be found here https://github.com/hscw09dataset/hscw09


Dataset:
While the options to leverage additional dataset for this study are not readily available
due to access restrictions and additional charges, the public version of TREC’s ClueWeb09
data was used for studying rank-incentivized web dynamics [2]. The data contains the
historical snapshots from 2008, of a set of documents initially retreived for each of the 1-
200 titles of topics from TREC’s ClueWeb09 dataset that served as queries. A big advantage
of the original work is that the paper creates a novel dataset for the study composed of real
web documents which can also be used to better understand, and research Web dynamics
based on incentivized page ranks. The use of past versions of documents gives authors the
ability to compare them with occurrence in future

Indexing Processed data:
The goal is to set the properties based on the extracted ClueWeb09 data so that the index
parser from Indri toolkit can use it to process. Once the data for the entire year is indexed,
KL Divergence is applied on it to check for similarities between different months of the
same document. Drichlet smoothing rules are then applied on the processed data based
on the following retrieval parameters:
• Index – this is the identifier to the index generated by LucindriIndexer
• Count – this documents the max number of items that can be supplied to the query
• Query – one of the query language by Indri that it executes on
• Rule – mentions the rule on which smoothing should be set to

This mainly relies on KL divergence measure, which is the amount of information lost when q(x) is applied to 
approximate p(x). 


