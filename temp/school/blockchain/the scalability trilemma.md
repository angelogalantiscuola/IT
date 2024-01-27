# The Scalability Trilemma

The scalability trilemma says that there are three properties that a blockchain try to have, and that, if you stick to "simple" techniques, you can only get two of those three.

![https://vitalik.ca/images/sharding-files/trilemma.png](https://vitalik.ca/images/sharding-files/trilemma.png)

- **Scalability**: the chain can process more transactions than a single regular node (think: a consumer laptop) can verify.
- **Decentralization**: the chain can run without any trust dependencies on a small group of large centralized actors. This is typically interpreted to mean that there should not be any trust (or even honest-majority assumption) of a set of nodes that you cannot join with just a consumer laptop.
- **Security**: the chain can resist a large percentage of participating nodes trying to attack it (ideally 50%; anything above 25% is fine, 5% is definitely *not* fine).

Sharding is a technique that gets you all three.

[](https://vitalik.ca/general/2021/04/07/sharding.html)

## Bitcoin scalability

The battle for a scalable solution is the blockchain’s moon race. Bitcoin processes 4.6 transactions per second. Visa does around 1,700 transactions per second on average (based on a calculation derived from the official claim of over 150 million transactions per day). The potential for adoption is there but is bottlenecked currently by scalability.

Currently, the block size is set 1MB (1,048,576 bytes — although through SegWit, that size can scale to up to a theoretical 4MB) and the average transaction size is 380.04 bytes

The current Bitcoin block generation time is 10 minutes; i.e., every ten minutes, a new block is mined. In ten minutes (600 seconds), Bitcoin can average around 2,759.12 transactions based on previous assumptions. In other words, the Bitcoin blockchain can currently guarantee only 4.6 transactions per second.

### Existing and Future Approaches to Solve Scalability

1. Batch Payments into One Transaction

2. Bitcoin Cash

3. The Lightning Network

4. EOS & Other High-Performance Blockchains

5. bloXroute

[The Blockchain Scalability Problem & the Race for Visa-Like Transaction Speed](https://towardsdatascience.com/the-blockchain-scalability-problem-the-race-for-visa-like-transaction-speed-5cce48f9d44)