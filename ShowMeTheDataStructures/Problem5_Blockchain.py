import hashlib
import datetime
import time

class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.previous = None
        self.next = None
    
    def calc_hash(self):
        sha = hashlib.sha256()
        sha.update(self.data.encode("utf-8"))
        return sha.hexdigest()


class BlockChain:

    def __init__(self):
        self.head = None
        self.tail = None
    
    def append(self, block):
        if not isinstance(block, Block):
            raise Exception("only Block can be added to blockchain!")
        if self.head is None:
            self.head = block
            self.head.next = None
            self.head.previous = None
            self.tail = self.head
        else:
            self.tail.next = block
            self.tail.next.previous = self.tail
            self.tail.next.previous_hash = self.tail.hash
            self.tail = self.tail.next
    
    def __repr__(self):
        p = self.head
        repr_string = ""

        if p is None:
            return "Empty Block Chain."

        while p is not None:
            repr_string += "Block(time: {}, data: {}, hash: {}, previous hash: {})\n".format(p.timestamp, p.data, p.hash, p.previous_hash)
            p = p.next

        return repr_string    



if __name__ == "__main__":
    
    print("test case 1:\n")
    block_chain = BlockChain()
    block_chain.append(Block(datetime.datetime.now().timestamp(), "Bitcoin", None))
    time.sleep(1)
    block_chain.append(Block(datetime.datetime.now().timestamp(), "EOS", None))
    time.sleep(2)
    block_chain.append(Block(datetime.datetime.now().timestamp(), "Doge", None))
    print(block_chain)

    print("test case 2:\n")
    block_chain = BlockChain()
    print(block_chain)

    print("test case 3:\n")
    block_chain = BlockChain()
    block_chain.append("no block") 

    
