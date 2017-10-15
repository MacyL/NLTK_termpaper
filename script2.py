import pickle
from nltk import * 
import sys, re
from nltk.corpus import stopwords

####################
# NOTE : Please give it the pickle data and the output name, thank you!
####################

# function 

# this function report the number of words contains abbreviation
# for example "I'm", "You're","I'll" and "father's" (possesive).
# and then remove the abbreviation part from the string.

def abbreviation(tokenlist,returnvalue):
	HaveAbb=[w for w in tokenlist if "'" in w]
	Proportion=len(HaveAbb)/len(tokenlist)	
	dout=[w.split("'")[0] for w in tokenlist]
	if returnvalue=='Abblist':
		return(HaveAbb)
	elif returnvalue=='Proportion':
		return(Proportion)
	elif returnvalue=='Newoutput':
		return(dout)
# remove all the stop words so we can have the lexical words for analysis
def removestop(tokenlist):
	stop=stopwords.words('english')
	dout=[w for w in tokenlist if w not in stop]
	return(dout)

# you can select NN, VBD or VBP etc, up to you. But we don't do more than noun or verb.
def gettag(taglist, tagname):
	tags=[items[0] for items in taglist if items[1]==tagname]
	return(tags) 

def tFrequencyDist(taglist,tagname):
	tags=[items[0] for items in taglist if items[1]==tagname]
	FD=FreqDist(tags)
	return(FD.most_common(30))

if __name__ == "__main__":
	data=pickle.load(open(sys.argv[1], "rb" ) )
	# Preprocess
	dataV2=abbreviation(data,'Newoutput')
	dataV3=removestop(dataV2)
	dataV3=list(filter(None, dataV3))
	dataV4=pos_tag(dataV3)
	# Analysis for Noun
	NNtag=gettag(dataV4,'NN')
	NNproportion=len(NNtag)/len(data) # the noun/original
	NNvariation=len(set(NNtag))/len(dataV4) # #set(noun)/#lexical
	# Analysis for Verb
	VBtag=gettag(dataV4,'VBP')+gettag(dataV4,'VBD')
	VBproportion=len(VBtag)/len(data) # the verb/original
	VBvariation=len(set(VBtag))/len(dataV4) # #set(verb)/#lexical
	VBvariationinVB=len(set(VBtag))/len(VBtag) # #set(verb)/#verb
	# Most common content words
	NNcommon=tFrequencyDist(dataV4,'NN')
	VBPcommon=tFrequencyDist(dataV4,'VBP')
	VBDcommon=tFrequencyDist(dataV4,'VBD')
	# data output 	
	with open('{0}_datav2.txt'.format(sys.argv[2]),'w') as df:
		df.write('Noun proportion:{0}'.format(NNproportion)+'\n')
		df.write('Noun variation:{0}'.format(NNvariation)+'\n')
		df.write('Verb proportion:{0}'.format(VBproportion)+'\n')
		df.write('Verb variation:{0}'.format(VBvariation)+'\n')
		df.write('Verb variation version 2:{0}'.format(VBvariationinVB)+'\n')
	
	# most common content words output 
	with open('{0}_mostcommon.txt'.format(sys.argv[2]),'w') as df:
		df.write('Noun top 30:{0}'.format(NNcommon)+'\n')
		df.write('Verb (present) top 30:{0}'.format(VBPcommon)+'\n')
		df.write('Verb (past) top 30:{0}'.format(VBDcommon)+'\n')

	# temp data output for furture investigation
	with open('{0}_temp.txt'.format(sys.argv[2]),'w') as df:
		df.write('abbreviation list:{0}'.format(abbreviation(data,'Abblist'))+'\n')
		df.write('abbreviation proportion:{0}'.format(abbreviation(data,'Proportion'))+'\n')
		df.write('Noun tag:{0}'.format(NNtag)+'\n')
		df.write('Verb tag:{0}'.format(VBtag)+'\n')
		
