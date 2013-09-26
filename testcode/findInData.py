import json

print "opening file"
file = open("rastrackData.json")
print "loading json"
data = json.load(file)
print "json loaded"
for pi in data["pi"]:
    if ("x" in pi) and ("y" in pi) and ("z" in pi):
        if (pi["x"] == -6658) and (pi["y"] == -34) and (pi["z"] == -5804):
            print "found it - " + pi["name"]
#    if pi["x"] == -6658:
#        print "found it"
#print data["pi"][0]["latitude"]
