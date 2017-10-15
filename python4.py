import pickle
from nltk import * 
import sys, re
from nltk.corpus import stopwords

def NLTKfunctionwords(tokenlist,value):
	stop=stopwords.words('english')
	# we need to create a new tokenlist.  
	Newlist=[w.split("'") for w in tokenlist]
	Newlist=[item for sublist in Newlist for item in sublist]
	getfunct=[w for w in Newlist if w in stop]
	if value=='list':
		return(getfunct)
	if value=='proportion':
		result=len(getfunct)/len(Newlist)
		return(result)
	if value=='variation':
		result=len(set(getfunct))/len(getfunct)
		return(result)
	
def CNLPfunctionwords(tokenlist,value):
	with open('stopwords_list.txt','r') as f:
		stop=f.readlines()
		stops=[re.sub('\n','',w) for w in stop]
		f.close()
	getfunct=[w for w in tokenlist if w in stops]
	if value=='list':
		return(getfunct)
	if value=='proportion':
		result=len(getfunct)/len(tokenlist)
		return(result)
	if value=='variation':
		result=len(set(getfunct))/len(getfunct)
		return(result)

if __name__ == "__main__":
	data=pickle.load(open(sys.argv[1], "rb" ) )
	# save.
	with open('{0}_datav4.txt'.format(sys.argv[2]),'w') as f:
		f.write("NLTK function words proportion:{0}".format(NLTKfunctionwords(data,'proportion'))+'\n')
		f.write("NLTK function words variation:{0}".format(NLTKfunctionwords(data,'variation'))+'\n')
		f.write("CoreNLP function words proportion:{0}".format(CNLPfunctionwords(data,'proportion'))+'\n')
		f.write("CoreNLP function words variation:{0}".format(CNLPfunctionwords(data,'variation'))+'\n')
	with open('{0}_tempv4.txt'.format(sys.argv[2]),'w') as f:
		f.write("NLTK function words:{0}".format(NLTKfunctionwords(data,'list'))+'\n')
		f.write("CoreNLP function words:{0}".format(CNLPfunctionwords(data,'list'))+'\n')
