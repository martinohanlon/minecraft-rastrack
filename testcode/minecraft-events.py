#www.stuffaboutcode.com
#Raspberry Pi, Minecraft API - the basics

#import the minecraft.py module from the minecraft directory
import minecraft.minecraft as minecraft
#import minecraft block module
import minecraft.block as block
#import time, so delays can be used
import time

if __name__ == "__main__":

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
                # do something with the block
                print blockHit.pos.x
                print blockHit.pos.y
                print blockHit.pos.z
                print blockHit.face
                print blockHit.type
                print blockHit.entityId
