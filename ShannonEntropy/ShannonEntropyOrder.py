#Modified by: Dalina Beckham
#Purpose: Changed original to determine shannon entropy of words.
#Creator: Bugra Akyildiz
#Source Site: http://bugra.github.io/work/notes/2014-05-16/entropy-perplexity-image-text/

import io
import string
import urllib2
import sys
# 3rd Party
#from PIL import Image
#import numpy as np
import math
#from matplotlib import pyplot as plt
#from scipy import ndimage

#text = "When diversity indices are used in ecology, the types of interest are usually species, but they can also be other categories, such as genera, families, functional types or haplotypes. The entities of interest are usually individual plants or animals, and the measure of abundance can be, for example, number of individuals, biomass or coverage. In demography, the entities of interest can be people, and the types of interest various demographic groups. In information science, the entities can be characters and the types the different letters of the alphabet. The most commonly used diversity indices are simple transformations of the effective number of types (also known as 'true diversity'), but each diversity index can also be interpreted in its own right as a measure corresponding to some real phenomenon (but a different one for each diversity index)"

#for arg in  sys.argv:
#	print arg

#grab file name
print "Calculating Shannon Entropy..."

text = ""
f =open(sys.argv[1], 'r');
for line in f:
#	print line
	text = text + line

#text = "Hi how how are are are you you you you"
#text = "1223334444"
text = text.translate(string.maketrans("",""), string.punctuation)
words = text.split()
#wordset = set(chars)
wordset = set(words)

freq={word: words.count(word) for word in wordset}

print "Word \t\t Count \t Self Information"
word_count_information = []
entropy = 0
for word in wordset:
    probability = freq[word] / float(1.0 * len(words)) 
    self_information = math.log(1.0/probability, 2) 
    entropy += (probability * self_information)
    word_count_information.append([word, freq[word], self_information])

#sort by number of occurences
#sorted_word_count_information = list(sorted(word_count_information, key=lambda k:k[2], reverse=True))
#sorted by alphabet
sorted_word_name_information = list(sorted(word_count_information, key=lambda k:k[0], reverse=False))


#sorted_word_count_information
for ii in sorted_word_name_information:
    # Very inelegant way of formatting
    separation = '\t\t' if len(ii[0]) < 7 else '\t'
    if len(ii[0]) >= 15: separation = '' 
    print("%s %s %s \t %s"%(ii[0], separation, str(ii[1]), str(ii[2])))
print "\n\nEntropy of complete text: {}".format(entropy)

