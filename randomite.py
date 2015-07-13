from mcpi import minecraft
from mcpi import block
from mcpi import event
import random

mc = minecraft.Minecraft.create()

playerObj = mc.player.getPos()

blockObj = block.Block(247)

mc.setBlock(playerObj.x + 1, playerObj.y, playerObj.z, blockObj.id)

def parseBlockEvent(event):
    eventList = event.replace('','').split(',')
    return {
        'type': eventList[0],
        'x': int(eventList[1]),
        'y': int(eventList[2]),
        'z': int(eventList[3]),
        'id': int(eventList[4]),
}

while True:
    blockEvents = mc.events.pollBlockHits()
    if blockEvents:
        for blockEvent in blockEvents:
            Hit = parseBlockEvent(str(blockEvent))
            blockHit = mc.getBlock( Hit['x'],
                                    Hit['y'],
                                    Hit['z'])
            
            if blockHit == 247:
                ranblock = [1,2,3,4,5,6,7,8,10,12,13,14,15,16,17,18,19,20,21,22,24,30,31,35,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,53,54,56,57,58,60,61,62,64,65,67,71,73,78,79,80,81,82,83,85,89,98,102,103,107,246];
                mc.setBlock(Hit['x'], Hit['y'], Hit['z'], ranblock[random.randint(0,len(ranblock)-1)])
                

    
            




