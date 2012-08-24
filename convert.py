############################################################

############################################################
import re

####Open I/O#################################################
infile = './22633491.txt'
input = open(infile, 'rU')

tmpfile = './tair.txt'
lib = open(tmpfile, 'rU')

out = open('./curated.txt', 'w')

##variables
in_iter = []
lib_iter = []

####Main Function#############################################
for line in input:
    line.strip('\n')
    line = re.sub(r'\s+',' ',line)
    linelist = line.split(' ')
    in_iter.append(linelist[4])
    in_iter.append(linelist[5])
    in_iter.append(linelist[6])
    in_iter.append(linelist[7])
    in_iter.append(linelist[8])
    in_iter.append(linelist[9])

for line in lib:
    line.strip('\n')
    line = re.sub(r'\s+', ' ', line)
    linelist = line.split(' ')
    lib_iter.append(linelist[0])
    lib_iter.append(linelist[1])

out.write('agi	unmod_sequence	score	mod_sequence	charge	m/z mass_error\n')

i = 1		
while(i<=len(in_iter)):
    if i == 3001: print('#') 
    if i == 6001: print('##')
    if i == 9001: print('###')
    if i == 12001: print('####')
    if i == 15001: print('#####')
    count = 0
    pep = in_iter[i]
    pep = re.sub('__','',pep)
    pep = re.sub('_','',pep)
    pep = re.sub('\(..\)','',pep)
     
    for j in range(len(lib_iter)):
	if pep in lib_iter[j]:
	    if in_iter[i + 4] in lib_iter[j]:
    		out.write(lib_iter[j-1] +'\t' + pep + '\t' + in_iter[i-1] + '\t' + in_iter[i] + '\t' + in_iter[i+1] + '\t' + in_iter[i+2] + '\t' + in_iter[i+3] +  '\n')
		break
    i = i + 6

####Close I/O#################################################
input.close()
lib.close()
out.close()
