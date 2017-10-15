# library 
from bs4 import BeautifulSoup
from nltk import *
from nltk.tokenize import RegexpTokenizer,sent_tokenize
from urllib import request
from collections import Counter
import re 
import sys, getopt
import pickle
# functions
def crawler(argv):
	singer=''
	song=''
	#print(singer)
	#print(name)

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
	raw=re.sub(r'[!?.,]','',raw)
	tokenizer = RegexpTokenizer('\s+', gaps=True)
	tokens=tokenizer.tokenize(raw)
	words=[w.lower() for w in tokens]
	return(words)
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

def Ngrams(tokenlist,N):
	myngrams=list(ngrams(tokenlist,N))
	return(myngrams)

def FrequencyDist(tokenlist):
	FD=FreqDist(tokenlist)
	return(FD.most_common(30))

def tFrequencyDist(taglist,tagname):
	tags=[items[0] for items in taglist if items[1]==tagname]
	FD=FreqDist(tags)
	return(FD.most_common(30))

def TTR(tokenlist):
	Type=len([t for t,v in Counter(tokenlist).items()])
	TTRs=Type/len(tokenlist)		
	return(TTRs)

def POSTTR(tokenlist,taglist):
	posTTR=len(taglist)/len(tokenlist)
	return(posTTR)
# code.
if __name__ == "__main__":
	data=crawler(sys.argv[1:])
	name=str(sys.argv[1:])
	name=CreatFilename(name)
	with open('{0}_{1}_token_list.txt'.format(name[0],name[1]),'wb') as pf:
		pickle.dump(data,pf)

	print(len(data))
	monogramTTR=TTR(data)
	twogramTTR=TTR(Ngrams(data,2))
	trigramTTR=TTR(Ngrams(data,3))
	tags=pos_tag(data)
	NNFD=tFrequencyDist(tags,'NN')
	VBPFD=tFrequencyDist(tags,'VBP')
	VBDFD=tFrequencyDist(tags,'VBD')
	cTTRList=list()
	for c in ['NN','VBP','VBD']:
		ctags=[items[0] for items in tags if items[1]==c]
		uctags=[t for t,v in Counter(ctags).items()]
		cTTR=POSTTR(data,uctags)
		cTTRList.append((c,cTTR))
		#print('{0} TTR:{1}'.format(c,cTTR))
	
	VBTTR=cTTRList[1]+cTTRList[2]
	
	with open('{0}_{1}_data.txt'.format(name[0],name[1]),'w') as df:
		df.write('Length:{0}'.format(len(data))+'\n')
		df.write('Monogram:{0}'.format(FrequencyDist(Ngrams(data,1)))+'\n')
		df.write('Bigram:{0}'.format(FrequencyDist(Ngrams(data,2)))+'\n')
		df.write('Trigram:{0}'.format(FrequencyDist(Ngrams(data,3)))+'\n')
		df.write('Top 30 Noun :{0}'.format(tFrequencyDist(tags,'NN'))+'\n')
		df.write('Top 30 Verb (present):{0}'.format(tFrequencyDist(tags,'VBP'))+'\n')
		df.write('Top 30 Verb (Past):{0}'.format(tFrequencyDist(tags,'VBD'))+'\n')
		df.write('MonogramTTR:{0}'.format(monogramTTR)+'\n')
		df.write('BigramsTTR:{0}'.format(twogramTTR)+'\n')
		df.write('TrigramsTTR:{0}'.format(trigramTTR)+'\n')
		df.write('Noun variation:{0}'.format(cTTRList[0])+'\n')
		df.write('Verb variation:{0}'.format(VBTTR)+'\n')
		df.close()
	#print('one gram TTR:{0}'.format(onegramTTR))
	#print('Bigram TTR:{0}'.format(twogramTTR))
	#print('Top 30 Noun')
	#print(tFrequencyDist(tags,'NN'))
	#print('Top 30 Verb')
	#print(tFrequencyDist(tags,'VBP'))
	#print(tFrequencyDist(tags,'VBD'))
		
	
	

