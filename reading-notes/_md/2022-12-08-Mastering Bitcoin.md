---
aliases: [Mastering Bitcoin]
title: Mastering Bitcoin
author: Andreas M. Antonopoulos
category: Computers
publisher: "O'Reilly Media, Inc."
total_page: 416
cover_url: http://books.google.com/books/content?id=tponDwAAQBAJ&printsec=frontcover&img=1&zoom=1&edge=curl&source=gbs_api
publish_date: 2017-06-12
isbn10: 1491954345
isbn13: 9781491954348
started: 2022-03-22
finished: 2022-12-08
---
# *[Mastering Bitcoin: Programming on the Open Blockchain](https://www.oreilly.com/library/view/mastering-bitcoin-2nd/9781491954379/)* by [[Andreas M. Antonopoulos]]

<img src="https://learning.oreilly.com/library/cover/9781491954379/250w/" width=150>

`(Boston: O'Reilly, 2014/2017), 416`

This book is, as it claims to be in the preface (xviii), the **_the definitive technical book on cryptocurrencies and bitcoin_**. "Mastering" bitcoin requires more than the introductory read I gave this, but that introductory read is quite helpful for understanding the concepts and a second pass through the examples in the book is a good next step. 

Read the book on Github here: [GitHub - bitcoinbook/bitcoinbook: Mastering Bitcoin 2nd Edition - Programming the Open Blockchain](https://github.com/bitcoinbook/bitcoinbook)

# Notes

<details>
 <summary><i>Contents</i></summary>
<!-- MarkdownTOC autolink="true" -->

- [Preface](#preface)
- [Chapter 1: Introduction](#chapter-1-introduction)
- [Chapter 2: How Bitcoin Works](#chapter-2-how-bitcoin-works)
- [Chapter 3: Bitcoin Core: The Reference Implementation](#chapter-3-bitcoin-core-the-reference-implementation)
- [Chapter 4: Keys, Addresses](#chapter-4-keys-addresses)
- [Chapter 5: Wallets](#chapter-5-wallets)
- [Chapter 6: Transactions](#chapter-6-transactions)
- [Chapter 7: Advanced Transactions and Scripting](#chapter-7-advanced-transactions-and-scripting)
- [Chapter 8: The Bitcoin Network](#chapter-8-the-bitcoin-network)
- [Chapter 9: The Blockchain](#chapter-9-the-blockchain)
- [Chapter 10: Mining and Consensus](#chapter-10-mining-and-consensus)
- [Chapter 11: Bitcoin Security](#chapter-11-bitcoin-security)
- [Chapter 12: Blockchain Applications](#chapter-12-blockchain-applications)
- [The Bitcoin Whitepaper by Satoshi Nakamoto](#the-bitcoin-whitepaper-by-satoshi-nakamoto)

<!-- /MarkdownTOC -->
</details>

## Preface
- this book intended for coders: learn how cryptocurrencies work, how to use them, and how to develop software that works with them (xiii)
- ants on the cover because leafcutter ants form complex, decentralized societies
- "[[Writing]] 500 words a week for four years gave me enough experience to eventually consider becoming an author." (xix)
- "I owe my love of words and books to my mother, Theresa, who raised me in a house with books lining every wall. My mother also bought me my first computer in 1982, despite being a self-described technophobe. My father, Menelaos, a civil engineer who just published his first book at 80 years old, was the one who taught me logical and analytical thinking and a love of science and engineering." (xx)

## Chapter 1: Introduction
_**Summary**: Bitcoin provides the technologies (protocol, blockchain, consensus rules, Proof-of-work) to issue currency and validate transactions in a decentralized manner._
- [[Bitcoin]] is "a collection of concepts and technologies that form the basis of a digital money ecosystem." (1), consisting of:
	- A decentralized peer-to-peer network (the bitcoin protocol)
	- A public transaction ledger (the blockchain)
	- A set of rules for independent transaction validation and currency issuance (consensus rules)
	- A mechanism for reaching global decentralized consensus on the valid blockchain (Proof-of-work algorithm)
- Users of bitcoin own keys that allow them to prove ownership of bitcoin in the bitcoin network 
- Bitcoin mining decentralizes the currency-issuance and clearing functions of a central bank and replaces the need for any central bank
- A wallet is to bitcoin, as a browser is to the internet 
	- A wallet is simply a collection of addresses and the keys that unlock the funds within


## Chapter 2: How Bitcoin Works
_**Summary**: An overview of the basic concepts of bitcoin by following a simple transaction._
- A **transaction** tells the network that the owner of some bitcoin has authorized the transfer to another owner. "Spending" is signing a transaction that transfers value. 
	- Transaction inputs cannot be divided, so the "change" is returned to a new address.
- The transaction is propagated to the network and validated when a new block is **mined** and added to the blockchain
	- Mining uses a proof-of-work algorithm that is asymmetrically hard to solve but easy to verify (generating a SHA256 hash that meets requirements of a number of leading zeroes)


## Chapter 3: Bitcoin Core: The Reference Implementation
_**Summary**: This is a technical chapter for getting setup with a bitcoin developer environment._
- Bitcoin is open source software: [GitHub - bitcoin/bitcoin: Bitcoin Core](https://github.com/bitcoin/bitcoin)


## Chapter 4: Keys, Addresses
_**Summary**: A random number is the private key used to sign transactions, from which is generated a public key that can generate multiple addresses to receive funds._
- "Ownership of bitcoin is established through digital keys, bitcoin addresses, and digital signatures. The digital keys are not actually stored in the network, but are instead created and stored by users in a file, or simple database, called a wallet." (55)
- Bitcoin uses [[Elliptic curve point multiplication]] (56)
- Bitcoin uses public key cryptography to create a key pair (56):
	- **public key (K)**: used to receive funds
	- **private key (k)**: used to sign transactions that spend funds, a number picked at random
	- **address (A)**: generated with hash from public key, displayed in **Base58** (a format developed for bitcoin) or **Base58check** (which includes extra data for error checking) 
		- start with `1` for standard addresses 
		- start with `3` for Pay-to-Script Hash (P2SH, i.e. multisig)

<img src="https://github.com/bitcoinbook/bitcoinbook/raw/develop/images/mbc2_0401.png" width="100%">


## Chapter 5: Wallets
_**Summary**: A wallet is simply a container for private keys._
- Wallets do not contain coins, but rather the keys that allow for the signing of transactions that spend the coins present on the blockchain 
- **Nondeterministic wallet**: each key is independently generated from a random number (must be backed up frequently)
- **Deterministic wallet**: all the keys are derived from a single master key (the *seed*, encoded as a set of *mnemonic code words*)
	- **HD Wallets**: have a tree structure and can produce public keys without the corresponding private key (to create issue a different public key for each transaction)


## Chapter 6: Transactions
_**Summary**: Transactions (data structures that encode the transfer of value publicly on the blockchain) are the most important feature of bitcoin._
- Transaction outputs are the fundamental building block of bitcoin transactions. 
- **UTXO** or *unspent transaction outputs* are how bitcoin is "received", and are indivisible once created 
- A user's "balance" is the sum of all UTXO that the user's wallet can spend 
- The **coinbase transaction** is the first transaction in each block that mints bitcoin for the miner of the block 
- Transaction inputs consist of:
	- `vin`: giving the UTXO(s) that "fund" the transaction; for each, the transaction that UTXO came from, its index, and a `scriptSig` which satisfies the conditions placed on the UTXO to unlock it for spending
- Transaction outputs consist of:
	- `value`: amount of bitcoin, in *satoshis*
	- `scriptPubKey`: the *locking script* or *witness script* which is the cryptographic puzzle determining the conditions required to spend the output 
- Transaction fees are computed based on the size of the transaction in kilobytes (not the value)
	- Fees are the difference between the sum of the inputs and outputs 
- *Script* is the bitcoin transaction script language (stack-based RPN)
	- **Locking script**: a spending condition placed on an output 
	- **Unlocking script**: a script that satisfies the locking script and allows the output to be spent 
- Bitcoin uses **digital signatures**, consisting of an algorithm for creating the signature using a private key, and a algorithm that allows anyone to verify the signature given the public key 


## Chapter 7: Advanced Transactions and Scripting
_**Summary**: Presents some advanced notes on transactions._
- A bug in CHECKMULTISIG requires an extra zero: `0 <Signature B> <Signature C>`
- P2SH means: "pay to a script matching this hash, a script that will be presented later when this output is spent" 
	- complex scripts replaced by shorter fingerprints 
	- shifts complexity to the recipient from the sender 


## Chapter 8: The Bitcoin Network
_**Summary**: The "Bitcoin network" is simply the collection of nodes running the bitcoin P2P protocol._
- A *Bitcoin Relay Network* minimizes latency for miners 
- **SPV** (Simplified Payment Verification) nodes are lightweight nodes that download only the block headers 
	- A privacy risk arises because an SPV node must download certain transactions to verify them 
	- This risk is mitigated with a **Bloom Filter**, a probabilistic search filter that describe a pattern without specifying it exactly
- The **Mempool**, or transaction pool, is the set of unconfirmed transactions 


## Chapter 9: The Blockchain
_**Summary**: The blockchain is the public ledger of all blocks, going back to the Genesis block. _

**Block Structure**

| Size                      | Field               | Description                                           |
| ------------------------- | ------------------- | ----------------------------------------------------- |
| 4 bytes                   | **Block Size**          | The size of the block, in bytes, following this field |
| 80 bytes                  | **Block Header**        | Several fields form the block header                  |
| 1&#x2013;9 bytes (VarInt) | **Transaction Counter** | How many transactions follow                          |
| Variable                  | **Transactions**        | The transactions recorded in this block               |

****
**Block Header**

| Size     | Field               | Description                                                                       |
| -------- | ------------------- | --------------------------------------------------------------------------------- |
| 4 bytes  | **Version**             | A version number to track software/protocol upgrades                              |
| 32 bytes | **Previous Block Hash** | A reference to the hash of the previous (parent) block in the chain               |
| 32 bytes | **Merkle Root**         | A hash of the root of the merkle tree of this block's transactions                |
| 4 bytes  | **Timestamp**           | The approximate creation time of this block (in seconds elapsed since Unix Epoch) |
| 4 bytes  | **Difficulty Target**   | The Proof-of-Work algorithm difficulty target for this block                      |
| 4 bytes  | **Nonce**               | A counter used for the Proof-of-Work algorithm                                    |

- The Genesis block, being the common ancestor of all blocks, can't help but remind me of [[Apostolic succession]]
- The **Merkle Root** is a hashed summary of all transactions in the block 
	- this provides an efficient way to determine if a transaction is in a block 
	- SPV nodes use merkle paths to verify transactions without downloading full blocks 
- Bitcoin has other blockchains for testing (testnet, segnet, regtest)


## Chapter 10: Mining and Consensus
_**Summary**: "Mining is the invention that makes bitcoin special."_
- "**Mining** secures the bitcoin system and enables the emergence of network-wide consensus without a central authority." (213)
- "The reward of newly minted coins and transaction fees is an incentive scheme that aligns the actions of miners with the security of the network while simultaneously implementing the monetary supply." (213)
- "Consensus is an emergent artifact of the asynchronous interaction of thousands of independent nodes." (217)
- The first transaction in each block is the **coinbase transaction** that rewards the miner and creates new bitcoin 
- Mining is the process of hashing the block header repeatedly, changing the nonce, until the resulting hash meets the difficulty target 
- The difficulty is adjusted every 2,016 blocks 
- When multiple forks of the blockchain exist, mining nodes "vote" with their computing power by choosing which chain to extend by mining the next block 
	- Bitcoin's block interval of 10 minutes is a compromise between fast confirmation and settlement times vs higher probability of forks 


## Chapter 11: Bitcoin Security
_**Summary**: "You’ve probably heard the expression, "Possession is nine-tenths of the law." Well, in bitcoin, possession is ten-tenths of the law." (269)_
- The core principle in bitcoin is decentralization
- "Bitcoin’s decentralized security model puts a lot of power in the hands of the users. With that power comes responsibility for maintaining the secrecy of the keys." (270)
- "To take advantage of bitcoin’s unique decentralized security model, you have to avoid the temptation of centralized architectures that might feel familiar but ultimately subvert bitcoin’s security." (271)
- "I personally keep the vast majority of my bitcoin (99% or more) stored on paper wallets, encrypted with BIP-38, with multiple copies locked in safes." (273)
- Practice diversification in your bitcoin storage


## Chapter 12: Blockchain Applications
_**Summary**: An overview of some applications that can be built on top of bitcoin._
- "Colored coins" are certificates of ownership 
- Payment channels are a trustless mechanisms for exchanging bitcoin transactions outside of the blockchain (i.e. Lightning) 
- Has Time Lock Contract (HTLC) allows parties to commit funds to a redeemable secret with an expiration 
- The Lightning Network allows for payments between parties who do not share a payment channel using intermediaries 


## The Bitcoin Whitepaper by Satoshi Nakamoto



--- 
**Topic**: [[Bitcoin]]

**Source**
- 


**Bibliography**

```query
[[bib]] file:(2022-12-08-Mastering Bitcoin)
```

---
Created: [[2022-03-22-Tue]]
Updated: <%+ tp.file.last_modified_date("YYYY-MM-DD-ddd") %>
