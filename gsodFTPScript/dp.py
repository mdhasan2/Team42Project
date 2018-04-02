import re
import time
import urllib2
import gzip
#import StringIO
import shutil
import tarfile
import os
#https://pythonhow.com/measure-execution-time-python-code/
startTime = time.time()

start = 1901
end   = 1967

response = urllib2.urlopen('ftp://ftp.ncdc.noaa.gov/pub/data/gsod/')
#links = response.read()
lines = response.readlines()
yr = []
for line in lines:
    years = re.split('[\s,;.?!\-:@[\](){}_\*/]',line)
    years = filter(None, years)
    #print words[len(words)-1].isdigit()
    if(years[len(years)-1].isdigit()):
    	if(start<=int(years[len(years)-1])<=end):
    		#print years[len(years)-1
    		yr.append(years[len(years)-1])


for year in yr:
	url = "ftp://ftp.ncdc.noaa.gov/pub/data/gsod/"+year+"/"+"gsod_"+year+".tar"
	response = urllib2.urlopen(url)
	with open("gsod_"+year+".tar", 'w') as outTarfile:
		outTarfile.write(response.read())
	tar = tarfile.open("gsod_"+year+".tar")
	tar.extractall()
	tar.close()
	#print os.listdir('.')
	#files = []
	files = [f for f in os.listdir('.')]
	#print files
	#https://stackoverflow.com/questions/31028815/how-to-unzip-gz-file-using-python
	with open(year, 'wb') as f_out:
		for f in files:
			if(f[-2:] == "gz"):
				with gzip.open(f,'rb') as f_in:
					shutil.copyfileobj(f_in, f_out)
					#https://stackoverflow.com/questions/185936/how-to-delete-the-contents-of-a-folder-in-python
					os.unlink(f)
	os.unlink("gsod_"+year+".tar")


endTime = time.time()
print (endTime - startTime)
