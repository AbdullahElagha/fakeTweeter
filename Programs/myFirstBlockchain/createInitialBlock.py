import hashlib   # using: blockStructure
import datetime  # using: initial block
i


def createInitialBlock():

    return blockStructure(0, datetime.datetime.now(), "This is the first block", "0")


createInitialBlock()