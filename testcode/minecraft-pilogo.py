#www.stuffaboutcode.com
#Raspberry Pi, Minecraft API - the basics

#import the minecraft.py module from the minecraft directory
import minecraft.minecraft as minecraft
#import minecraft block module
import minecraft.block as block
#import time, so delays can be used
import time

def buildRaspberry(mc,x,y,z):
    #red wool
    mc.setBlock(x+-1,y+0,z+1, block.WOOL.id, 14)
    mc.setBlock(x+1,y+0,z+1, block.WOOL.id, 14)
    mc.setBlock(x+0,y+0,z+0, block.WOOL.id, 14)
    mc.setBlock(x+-2,y+0,z+0, block.WOOL.id, 14)
    mc.setBlock(x+2,y+0,z+0, block.WOOL.id, 14)
    mc.setBlock(x+-1,y+0,z+-1, block.WOOL.id, 14)
    mc.setBlock(x+1,y+0,z+-1, block.WOOL.id, 14)
    mc.setBlock(x+0,y+0,z+2, block.WOOL.id, 14)
    #black wool
    mc.setBlock(x+0,y+0,z+1, block.WOOL.id, 15)
    mc.setBlock(x+-1,y+0,z+0, block.WOOL.id, 15)
    mc.setBlock(x+1,y+0,z+0, block.WOOL.id, 15)
    mc.setBlock(x+0,y+0,z+-1, block.WOOL.id, 15)
    #green wool
    mc.setBlock(x+0,y+0,z+-2, block.WOOL.id, 13)
    mc.setBlock(x+-1,y+0,z+-3, block.WOOL.id, 13)
    mc.setBlock(x+-2,y+0,z+-3, block.WOOL.id, 13)
    mc.setBlock(x+1,y+0,z+-3, block.WOOL.id, 13)
    mc.setBlock(x+2,y+0,z+-3, block.WOOL.id, 13)

if __name__ == "__main__":

    #Connect to minecraft by creating the minecraft object
    # - minecraft needs to be running and in a game
    mc = minecraft.Minecraft.create()
    #x = 202 y = 109 z = -960.0
    buildRaspberry(mc, 202, -39, -960)

#red wool
    #mc.setBlock(-1,0,1, block.WOOL.id, 14)
    #mc.setBlock(1,0,1, block.WOOL.id, 14)
    #mc.setBlock(0,0,0, block.WOOL.id, 14)
    #mc.setBlock(-2,0,0, block.WOOL.id, 14)
    #mc.setBlock(2,0,0, block.WOOL.id, 14)
    #mc.setBlock(-1,0,-1, block.WOOL.id, 14)
    #mc.setBlock(1,0,-1, block.WOOL.id, 14)
    #mc.setBlock(0,0,2, block.WOOL.id, 14)
#black wool
    #mc.setBlock(0,0,1, block.WOOL.id, 15)
    #mc.setBlock(-1,0,0, block.WOOL.id, 15)
    #mc.setBlock(1,0,0, block.WOOL.id, 15)
    #mc.setBlock(0,0,-1, block.WOOL.id, 15)
#green wool
    #mc.setBlock(0,0,-2, block.WOOL.id, 13)
    #mc.setBlock(-1,0,-3, block.WOOL.id, 13)
    #mc.setBlock(-2,0,-3, block.WOOL.id, 13)
    #mc.setBlock(1,0,-3, block.WOOL.id, 13)
    #mc.setBlock(2,0,-3, block.WOOL.id, 13)
