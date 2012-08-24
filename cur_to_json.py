# Author: Greg Mann
# 6/27/12
# JBEI

# Converting output of Curated Glycol Mod data into JSON format

import json
import re

filename = './curated.txt'

fo = open(filename, 'rU')
wo = open('./MASCP.Curated.txt', 'w')

jsonwrite = {}
jsonseq = []
currentagi = ''
firstrun = True

for line in fo:
    line = line.strip('\n')
    line = re.sub(r'\s+', ' ', line)
    linelist = line.split(' ')
    if linelist[0] != currentagi:
        if firstrun == False:
            jsonwrite['agi'] = currentagi
            jsonwrite['peptides'] = jsonseq
            wo.write(currentagi + ',' + json.dumps(jsonwrite) + '\n')
            jsonseq = []
            jsonwrite = {}
        else:
            firstrun = False
        currentagi = linelist[0]
    
    de_index = []
    ox_index= []
    i = -1
    count = 0
    for char in linelist[3]:    
	if char == '(': continue
	if char == ')': continue
	if char == 'x': continue
	if char == 'e': continue
	if char == 'o': 
	    ox_index.append(i)
	    continue
	if char == 'd':
    	    de_index.append(i) 
	    continue
	i = i + 1
    jsonseq.append({'sequence': linelist[1], 'score': linelist[2], 'mod_sequence': linelist[3], 'charge': linelist[4], 'm/z': linelist[5], 'mass_error': linelist[6], 'de_index': de_index, 'ox_index': ox_index})

fo.close()
wo.close()
