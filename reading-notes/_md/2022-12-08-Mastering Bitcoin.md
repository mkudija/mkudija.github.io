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
_**Summary**: _
- 



## Chapter 7: Advanced Transactions and Scripting
_**Summary**: _



## Chapter 8: The Bitcoin Network
_**Summary**: _



## Chapter 9: The Blockchain
_**Summary**: _



## Chapter 10: Mining and Consensus
_**Summary**: _



## Chapter 11: Bitcoin Security
_**Summary**: _



## Chapter 12: Blockchain Applications
_**Summary**: _




--- 
**Topic**: [[Bitcoin]]

**Source**
- 


**Bibliography**

```query
[[bib]] file:(2022-12-08-Mastering Bitcoin)
```
 

**New Words**

- 

---
Created: [[2022-03-22-Tue]]
Updated: <%+ tp.file.last_modified_date("YYYY-MM-DD-ddd") %>
