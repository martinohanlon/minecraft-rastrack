#www.stuffaboutcode.com
#Raspberry Pi, Minecraft API - the basics

#import the minecraft.py module from the minecraft directory
import minecraft.minecraft as minecraft
#import minecraft block module
import minecraft.block as block
#import time, so delays can be used
import time
#import json, to load rastrack data
import json

if __name__ == "__main__":

    #Load json file
    print "opening file"
    file = open("rastrackData.json")
    print "loading json"
    data = json.load(file)
    print "json loaded"

    #Connect to minecraft by creating the minecraft object
    # - minecraft needs to be running and in a game
    mc = minecraft.Minecraft.create()

    while True:
        #Get the block hit events
        blockHits = mc.events.pollBlockHits()
        # if a block has been hit
        if blockHits:
            # for each block that has been hit
            for blockHit in blockHits:
                # see if the xyz is in our json file
                for pi in data["pi"]:
                    if ("x" in pi) and ("y" in pi) and ("z" in pi):
                        if (pi["x"] == blockHit.pos.x) and (pi["y"] == blockHit.pos.y) and (pi["z"] == blockHit.pos.z):
                            mc.postToChat("This Pi belongs to " + pi["name"] + " lon:" + str(pi["longitude"]) + " lat:" + str(pi["latitude"]))
    #sleep for a bit to give things a rest!
    time.sleep(0.1)
