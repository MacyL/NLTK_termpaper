import nltk 
from nltk import *
import pickle 
import pandas as pd
import re

#########
# task: most common words
#########
monogramlist=[]
bigramlist=[]
trigramlist=[]

myrange=[i for j in (range(1,11), range(91, 101)) for i in j]

for i in myrange:
	data=pickle.load(open('2015_{0}_token_list.txt'.format(i), 'rb'))
	temp=list(filter(None,data))
	temp=[re.sub('[?.,!]','',w) for w in temp]
	monogramlist.extend(temp)
	bigramlist.extend(list(ngrams(temp,2)))
	trigramlist.extend(list(ngrams(temp,3)))

FD1=FreqDist(monogramlist)
FD2=FreqDist(bigramlist)
FD3=FreqDist(trigramlist)

with open('2015_total_monogram_listv2.txt','w') as f:
	f.write(str(monogramlist))

with open('2015_total_bigram_listv2.txt','w') as fii:
	fii.write(str(bigramlist))

with open('2015_total_trigram_listv2.txt','w') as fiii:
	fiii.write(str(trigramlist))			


results=pd.DataFrame({'Unigram 2015': FD1.most_common(30),
	'Bigram 2015': FD2.most_common(30),
	'Trigram 2015': FD3.most_common(30)})

results.to_csv('2015_gram_summary.tsv',sep='\t')

