import hashlib              # using: Block
import datetime             # using: initial block
from flask import Flask     # using node
from flask import request   # using node


def nextBlock(lastBlock):
    currentIndex = lastBlock.index + 1
    currentTimeStamp = datetime.datetime.now()
    currentData = ("This is block number " + str(currentIndex))
    currentHash = lastBlock.hash
    return Block(currentIndex, currentTimeStamp, currentData, currentHash)