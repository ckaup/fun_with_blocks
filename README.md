# Fun with Blocks

This project is a playground for me to play with Block Chain ideas to better understand the technology as a whole.

## Block Chain

The BlockChain class is fairly simple as it only contains the chain of Blocks in a list object.

### BlockChain.add_block

To add a Block to the chain, you can pass a Block object into the `add_block` method of the BlockChain class.

## Block

When creating a Block object, there are some required fields (in this order):

| Property | Description |
|:---:|:---:|
| Index | The position of the Block in the BlockChain |
| Timestamp | The time in which the Block was submitted |
| Data | The data included in the Block |
| Previous Hash | A reference to the previously used hash in the BlockChain |
| Hash | The hash value of the current Block |

### BlockChain.calculate_hash

Returns the hash value of the Block object.