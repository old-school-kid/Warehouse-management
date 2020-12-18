from hashlib import sha256
import json
import time

class Block:
    def __init__(self, index, transactions, timestamp, previous_hash):
        '''constructor'''
        self.index=index
        self.transactions = transactions
        self.timestam = timestamp
        self.previous_hash = previous_hash

    def compute_hash(self):
        '''
        returns hash of instance by converting it to json
        '''
        block_string=json.dumps(self.__dict__, sort_keys=True)
        return sha256(block_string.encode()).hexdigest()

class Blockchain:
    difficulty=2

    def __init__(self):
        '''constructor'''
        self.unconfirmed_transactions = [] # data to add to blockchain
        self.chain =[]
        self.create_genesis_block()

    def create_genesis_block(self):
        '''
        creates the first block, index0, previous hash 0, and has
        a valid hash
        '''
        genesis_block = Block(0,[],time.time(),"0") 
        genesis_block.hash = genesis_block.compute_hash()
        self.chain.append(genesis_block)

    def add_block(self, block, proof):
        '''
        adds block to chain after verification:
        1. check if proof is valid
        2. previous hash is 
        '''
        previous_hash = self.last_block.hash

        if previous_hash !=block.previous_hash:
            return False

        if not self.is_valid_proof(block, proof):
            return False

        block.hash = proof
        self.chain.append(block)
        return True

    @property
    def last_block(self):
        '''
        quickly retrive most recent block
        '''
        return self.chain[-1]

    def proof_of_work(self,block):
        '''
        function tries different values of nonce to
        get a hash that satisfies difficulty criteria
        '''
        block.nonce = 0

        computed_hash = block.compute_hash()
        while not computed_hash.startswith('0' * Blockchain.difficulty):
            block.nonce+=1
            computed_hash = block.compute_hash()

        return computed_hash

    def is_valid_proof(self, block, block_hash):
        '''
        check if block_hash is valid hash of block 
        and satisfies difficulty criteria
        '''
        return (block_hash.startswith('0'* Blockchain.difficulty) and 
                block_hash == block.compute_hash())

    def add_new_transaction(self, transaction):
        self.unconfirmed_transactions.append(transaction)

    def mine(self):
        '''
        add pending transactions in  unconfirmed_transactions
        and add them to blockchain after proof_of_work
        '''
        if not self.unconfirmed_transactions:
            return False

        last_block = self.last_block

        new_block = Block(
            index= last_block.index +1,
            transactions=self.unconfirmed_transactions,
            timestamp=time.time(),
            previous_hash=last_block.hash
        )

        proof = self.proof_of_work(new_block)
        self.add_block(new_block,proof)
        self.unconfirmed_transactions = []
        return new_block.index

#mining: unconfirmed transactions -> block-> computimng proof of work
#create API and use with flask.
