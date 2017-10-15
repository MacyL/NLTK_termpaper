# NLTK_termpaper
Here is the code I have wrote for NLTK_termpaper

### script1.py
This script contains **a crawler** which can download the lyrics from AZlyrics.com as well as **basic calculation**. The output of this program includes a pickle file for the song text, and a plain text file which includes all the basic calculation results.

This is the first script of this project, so there are some functions has been modified in another scripts. Therefore, I suggest to disable the calculation functions. 

Do not include any non-alphabate character to retrieve data.

usage 
```
$python3 script1.py --singer="singer name" --song="song name"
```

### script2.py
The script2.py calculates the **noun and verb propotion and the variation**. The function of calculating the content-words variation was included in the first script, but this file uses the correct formula. 

There were two ways for calculating the verb variation, the first one is the number of unique verb divided by number of content-words. The second one is the the number of unique verb divided by number of verb. 

The output is a plain text with all the results and a plain text with the abbreviation found in the text. 

usage 
```
$python3 script2.py [input pickle file] [output file name]
```
### script3.py
To conduct the Byte-based analysis, we download the songtext again without too much modification on the song text and then calculate the **total digits**, **Maximum token length** and **Minimum token length**. The output is a plain text for displaying results.

usage 
```
$python3 script3.py --singer="singer name" --song="song name"
```

### script4.py
Apart from content words, we also calculated the function words. This script extracts the function words according to NLTK corpus and CoreNLP corpus. The input is the pickle file which produced by **script1.py** and the output will be two plain text files. The first output is the resutls and the second output is the list of function words we extracted. 

usage 
```
$python3 script4.py [input pickle file] [output file name]
```

### script5.py
This script taks a series of files as input and calcualte the **top 30 most frequent words, bigrams, trigrams.** The input file names are hard coded in the script. It is command line executable script, however, it is not flexible when using. This python code requires modification before applying on any other project. 

usage 
```
$python3 script5.py
```




