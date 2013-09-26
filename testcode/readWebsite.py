import urllib2

def getDataFromWebpage(url, keyValues, phraseToFind, dataLenght):
    #replace keys in url with values
    for keyValue in keyValues:
        url = url.replace(keyValue[0], keyValue[1])
    #get webpage
    #print url
    aResp = urllib2.urlopen(url)
    page = aResp.read()
    #print page
    #strip data from webpage
    phrasePos = page.find(phraseToFind)
    dataStart = phrasePos+len(phraseToFind)
    dataEnd = dataStart + page[dataStart:].find('"')
    #gridRef = page[phrasePos+len(phraseToFind):phrasePos+len(phraseToFind)+dataLenght]
    gridRef = page[dataStart:dataEnd]
    return page[phrasePos+len(phraseToFind):phrasePos+len(phraseToFind)+dataLenght]

#website of the David Whale gps co-ords to OS grid reference calc
gridrefUrl = "http://www.thinkingbinaries.com/test/gpsmap/geodesic.php5?latitude=[lat]&longitude=[lon]&a_latlong=calc&gridreflet=&gridrefEN="
gridRef = getDataFromWebpage(gridrefUrl, [["[lat]", "52.506605"],["[lon]", "-2.179364"]],  '<input type="text" name="gridreflet" value="', 10)
#convert 8 number grid ref to 6 e.g. SO87828991 to SO878899
gridRef = gridRef[:5] + gridRef[6:9]
print gridRef


#put our [lat] and [lon] in
#gridrefUrl = gridrefUrl.replace("[lat]", "52.506605")
#gridrefUrl = gridrefUrl.replace("[lon]", "-2.179364")
#call the website
#aResp = urllib2.urlopen(gridrefUrl)
#gridrefPage = aResp.read()
#print gridrefPage
#find the data we are looking for
#phraseToFind = '<input type="text" name="gridreflet" value="'
#dataLenght = 10
#phrasePos = gridrefPage.find(phraseToFind)
#print phrasePos
#print gridrefPage[phrasePos+len(phraseToFind):phrasePos+len(phraseToFind)+dataLenght]
