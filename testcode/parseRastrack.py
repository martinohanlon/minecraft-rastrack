
import json
import urllib2
#get the data from rastrack
aResp = urllib2.urlopen("http://www.rastrack.co.uk/data2.php")
page = aResp.read()
#replace escape char \
page = page.replace("\\", " ")
#strip the 'var data = ' bit and load into json object
rastrackData = json.loads(page[11:])
rastrackData["pi"][0]["mydata"] = 123
#for pi in rastrackData["pi"]:
#    print pi["longitude"]
#    print pi["latitude"]
print rastrackData["pi"][0]["mydata"] 
outputFile = open("rastrackData.json", "w")
json.dump(rastrackData, outputFile)
