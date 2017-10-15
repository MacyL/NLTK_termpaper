# NLTK_termpaper
Here is the code I have wrote for NLTK_termpaper

### Script1.py
The script contains *a crawler* which can download the lyrics from AZlyrics.com as well as *basic calculation*. The output of this program includes a pickle file for the song text, and a plain text file which includes all the basic calculation results.

This is the first script of this project, so there are some functions has been modified in another scripts. Therefore, I suggest to disable the calculation functions. 

Do not include any non-alphabate character to retrieve data.

usage 
```
$python3 script1.py --singer="singer name" --song="song name"
```

### Script2.py
Script2.py calculates the *noun and verb propotion and the variation*. The function of calculating the content-words variation was included in the first script, but this file uses the correct formula. 

There were two ways for calculating the verb variation, the first one is the number of unique verb divided by number of content-words. The second one is the the number of unique verb divided by number of verb. 

The output is a plain text with all the results and a plain text with the abbreviation found in the text. 

usage 
```
$python3 script2.py [input pickle file] [output file name]
```
### Script3.py
