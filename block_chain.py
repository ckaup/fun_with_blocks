from datetime import datetime
import hashlib


class BlockChain:
    def __init__(self, initial_block=None):
        if initial_block:
            self.chain = [initial_block]
        else:
            self.chain = [Block(0, datetime.now(), 'Initial Block', None)]

    def __iter__(self):
        for block in self.chain:
            yield block

    def add_block(self, block):
        block.previous_hash = self.chain[-1].hash
        self.chain.append(block)


class Block:
    def __init__(self, index, timestamp, data, previous_hash=None):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def __str__(self):
        return '{}: {}'.format(self.index, self.data)

    def calculate_hash(self):
        return hashlib.sha256(b"str(self.index) + self.timestamp + self.data").hexdigest()