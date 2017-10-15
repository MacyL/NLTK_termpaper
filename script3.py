# library 
from bs4 import BeautifulSoup
from nltk import *
from nltk.tokenize import RegexpTokenizer,sent_tokenize
from urllib import request
from collections import Counter
import re 
import sys, getopt
import pickle

###############
# Task : calculate the digits. 
###############

def crawler(argv):
	singer=''
	song=''
	try:
		opts, args=getopt.getopt(argv,'x',['singer=','song='])
	except getopt.GetoptError:
		print('Usuage : script.py --singer=<singer name> --song=<song name>')
		sys.exit(2)
	for opt, arg in opts:
		if opt in ("--singer"):
			singer=arg
		elif opt in ("--song"):
			song=arg
	singer=singer.lower().replace(" ", "")
	song=song.lower().replace(" ","")
	url='https://www.azlyrics.com/lyrics/{0}/{1}.html'.format(singer,song)
	response=request.urlopen(url)
	soup=BeautifulSoup(response, 'html.parser')
	raw=soup.find_all('div',attrs={'class':None})[1]
	raw=raw.get_text()
	raw=re.sub("[\(\[].*?[\)\]]", "", raw)
	raw=raw.replace('\r','')
	raw=raw.replace('\n',' ')
	return(raw) # this returns a string type of data

def DigitsAnalysis(raw,function):
	if function=='Original':
		rawLen=len(raw) # original length, without any processing. 
		return(rawLen)
	elif function=='Includespace':
		rawPR=re.sub(r'[!?.,]','',raw) # remove punctuation.
		rawPRLen=len(rawPR) # length without punctuation, but include white space.
		return(rawPRLen)
	elif function=='Tokenize':	
		tokenizer = RegexpTokenizer('\s+', gaps=True)
		rawPR=re.sub(r'[!?.,]','',raw)
		tokens=tokenizer.tokenize(rawPR)
		words=[w.lower() for w in tokens]
		words=list(filter(None, words))
		# count the average word length. 
		Average=sum([len(w) for w in words])/len(words) # understand the average length of words
		Max=max([len(w) for w in words])
		Min=min([len(w) for w in words])
		return((Max, Average, Min))
	
	#print('{0},{1}'.format(singer,song))
	
def CreatFilename(name):
	name=name.split(',')
	name=[re.sub('singer|song','',w) for w in name]
	regex = re.compile('[^a-zA-Z]')
	name=[regex.sub('',w) for w in name]
	#name=list(filter(None,[re.sub("'| ","",w) for w in re.split("--|=",name)]))
	#string=['singer','song']
	#name=[x for x in name if x not in string]
	return(name)

if __name__ == "__main__":
	data=crawler(sys.argv[1:])
	name=str(sys.argv[1:])
	name=CreatFilename(name)
	check3=DigitsAnalysis(data,'Tokenize')
	with open('{0}_{1}_datav3.txt'.format(name[0],name[1]),'w') as df:	
		df.write('Total character number:{0}'.format(DigitsAnalysis(data,'Original'))+'\n')
		df.write('Exclude sentence-end punctuation:{0}'.format(DigitsAnalysis(data,'Includespace'))+'\n')
		df.write('Max:{0}'.format(check3[0])+'\n')
		df.write('Average:{0}'.format(check3[1])+'\n')
		df.write('Min:{0}'.format(check3[2])+'\n')
	

	





