fp = open('output.txt', 'w')

for x in range(9999):
    fp.writelines('hashmap.insert('+'"'+str(x)+'",'+str(x)+')\n')

fp.close()
