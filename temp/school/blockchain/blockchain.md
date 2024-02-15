%% Begin Waypoint %%
- [coin, stablecoin and token](./coin,%20stablecoin%20and%20token.md)
- [cryptocurrencies categories](./cryptocurrencies%20categories.md)
- [defi](./defi.md)
- [layer 2 scaling solutions](./layer%202%20scaling%20solutions.md)
- [nft](./nft.md)
- [the scalability trilemma](./the%20scalability%20trilemma.md)

%% End Waypoint %%

# Blockchain

Just think of blockchain as an operating system (like Windows or Mac OS) and Bitcoin as an application that runs on that operating system. Simple!

## Purpose

- The main purpose of the blockchain is to allow fast, secure and transparent **peer-to-peer transactions.**
- It is a trusted, decentralized network that allows for the transfer of digital values such as currency and data.
- Blockchain technology is secured with cryptographic techniques

## How does it work

- The Bitcoin blockchain is a database (known as a “ledger”) that consists only of Bitcoin transaction records. There is no central location that holds the database, instead, it is shared across a huge network of computers.
- So, for new transactions to be added to the database, the nodes must agree that the transaction is real and valid.
- Once the nodes agree that the transaction is real, it is then added to a “block” (which is why it is called a blockchain) and is placed below the previous block of transactions in the ledger.
- The way that traditional (non-blockchain) ledgers work is very similar to the way you would share a Microsoft Word document with your friend:
- In a blockchain system, however, all users can view the changes while they are being made.

[Blockchain Explained: Ultimate Guide on How Blockchain Works](https://www.bitdegree.org/crypto/tutorials/blockchain-explained)

## Block explorer

The block explorer is a blockchain search engine that allows you to search for a particular piece of information on the blockchain.

The activities carried out on crypto blockchains are known as transactions, which occur when cryptocurrencies are sent to and from wallet addresses. Each transaction is recorded onto a digital ledger, known as a blockchain.

Blocks on the blockchain are collections of transactions that were processed and approved by a group of third-parties known as miners

## Proof of work

A proof of work is a piece of data which is difficult (costly, time-consuming) to produce but easy for others to verify and which satisfies certain requirements. Producing a proof of work can be a random process with low probability so that a lot of trial and error is required on average before a valid proof of work is generated. Bitcoin uses the Hashcash proof of work system.

<aside>
💡 The idea builds on a security property of cryptographic hashes, that they are designed to be hard to invert. 
You can compute y from x cheaply y=H(x) but it's very hard to find x given only y. 
A full hash inversion has a known computationally infeasible brute-force running time, being O(2^k) where k is the hash size eg SHA256, k=256, and if a pre-image was found anyone could very efficiently verify it by computing one hash, so **there is a huge asymmetry in full pre-image mining (computationally infeasible) vs verification (a single hash invocation).**

</aside>

## Proof of stake

The Proof of Stake (PoS) concept states that a person can mine or validate block transactions according to how many coins they hold. This means that the more coins owned by a miner, the more mining power they have.

### Disadvantages of proof of stake

- However, most proof of stake cryptocurrency blockchains have high thresholds when it comes to the minimum stake you need to put down to connect to it as an independent computer
- Moreover, most proof of stake cryptocurrencies had something called a pre-mine which is where a bunch of coins or tokens are minted in advance and distributed to the team and large investors

Consequently, most proof of stake cryptocurrencies are more centralized than Bitcoin and Ethereum since the average user is stuck delegating to a validator or staking pool belonging to the team and VCs

[Proof of Work vs. Proof of Stake: Beginner's Guide!! 👨‍🏫](https://www.youtube.com/watch?v=08vnE2_cAeQ&t=191s)

## The Four Blockchain Generations

1. The **Bitcoin** blockchain is usually known as the first generation of blockchain (it’s not surprising). The main utilization of these blockchains is to process transactions. The first generation blockchains are based on Proof-of-Work algorithm.
2. The second generation of blockchains is based on Proof-of-Work, too, but they have wider functionality if we compare them to the first generation. For example, the Ethereum blockchain is capable of processing smart contracts, maintaining dApps (decentralized applications),
    - The **Ethereum** platform is not just a cryptocurrency, but a digital ecosystem that can be used as a basis for other decentralized projects.
    - Ethereum made it possible and easy to write up an ERC20 token and create a brand new cryptocurrency based on the Ethereum blockchain.
    - Probably the most important innovation brought with Ethereum were smart contracts. Smart contracts provide security to transactions automatically controlling the execution of all conditions by all actors and processing the transaction as the result of this execution.
    - Ethereum has the same serious problem as Bitcoin — scalability.
3. The third generation blockchains (for example **Cardano**) have higher scalability, higher speed of transactions, and consume less energy.
    - It’s fair to say that in many cases the third generation blockchains are the result of working on more efficient blockchain-like solutions.
    - Another feature common for the third generation of blockchains is the ability to process crosschain transactions.
    - The Proof-of-Work is usually replaced by other consensus mechanisms (e.g. Proof-of-Stake).
4. The fourth generation is just a hypothetical technology, there are different views on what will be considered as the next generation of the blockchain.
    - Does it even exist? Probably no. But people say that most likely when the third generation meets AI we will have the fourth generation.

[The Four Blockchain Generations](https://medium.com/the-capital/the-four-blockchain-generations-5627ef666f3b)