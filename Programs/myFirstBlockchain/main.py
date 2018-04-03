import hashlib              # using: Block
import datetime             # using: initial block
from flask import Flask     # using node
from flask import request   # using node
import string               # using createWallet
import random               # using createWallet


class Block:   # a class for the structure of our blocks
    def __init__(self, index, timeStamp, data, previousHash):
        self.index = index
        self.timeStamp = timeStamp
        self.data = data
        self.previousHash = previousHash
        self.hash = self.hashBlock()

    def hashBlock(self):
        hashVal = hashlib.sha256()   # create 256 bit hash variable

        # update the hash variable with the contents of the block
        hashVal.update(str(self.index).encode('utf-8')
                       + str(self.timeStamp).encode('utf-8')
                       + str(self.data).encode('utf-8')
                       + str(self.previousHash).encode('utf-8'))
        return hashVal.hexdigest()     # return the final block value

class Wallet:
    def __init__(self, name, address, value):
        self.name = name
        self.address = address
        self.value = value



node = Flask(__name__)

nodeTransactions = []


@node.route('/txion', methods=['POST'])
def transaction():
    if request.method == 'POST':
        newTransaction = request.get_json()     # extract transaction data
        nodeTransactions.append(newTransaction) # add transaction to txn list
        print("Transaction: ")
        print("Amount: {}\n".format(newTransaction['amount']))
        print("To: {}".format(newTransaction['to']))
        print("From: {}".format(newTransaction['from']))
        return "Transaction  successful"



# blocks in a blockchain rely on information from the previous block
# so how is the first block generated?
# we must manually create this first block before we can start to build on it


# def createWallet(size=40, chars=string.ascii_lowercase + string.digits):
#     walletOwner = input("Enter your name to generate a wallet")
#     randKey = ''.join(random.choice(chars) for _ in range(size))
#     walletType = "u_dkt_"
#     print("Public key for {}:\n".format(walletOwner) + walletType + randKey + "\n")
#
# createWallet()


def createInitialBlock():

    return Block(0, datetime.datetime.now(), "This is the first block", "0")


def nextBlock(lastBlock):
    currentIndex = lastBlock.index + 1
    currentTimeStamp = datetime.datetime.now()
    currentData = ("This is block number " + str(currentIndex))
    currentHash = lastBlock.hash
    return Block(currentIndex, currentTimeStamp, currentData, currentHash)


blockchain = [createInitialBlock()]     # initialize the blockchain
previousBlock = blockchain[0]           # create the first block

blockchainSize = 10

for x in range(0, blockchainSize):
    addBlock = nextBlock(previousBlock) # create the next block
    blockchain.append(addBlock)         # add the new block to the chain
    previousBlock = addBlock            # queue up the current block to add the next block

    print("Block #{} has been added, hash value is {} \n".format(addBlock.index, addBlock.hash))



tempWallet = "u_dkt_x2w3rxzt8v6jiqfnu87urzq0ynptmqv3dhkaw45o"


def proofOfWork(lastProof):     # this will be the proof of work alghorithm
    i = lastProof + 1           # incrememnt until the condition to mine a block is met
    while(i % 7 != 0 and i % lastProof):
        i += 1
        print(i)

@node.route("/mine", methods=["GET"])
def mine():
    lastBlock = blockchain[len(blockchain) - 1]
    lastProof = lastBlock.data["proof of work"]


