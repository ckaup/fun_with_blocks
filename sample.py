from datetime import datetime

from block_chain import BlockChain, Block


def main():
    main_chain = BlockChain()
    main_chain.add_block(Block(1, datetime(2018, 4, 6), 'Second Block', '0'))

    for block in main_chain:
        print(block)


if __name__ == '__main__':
    main()