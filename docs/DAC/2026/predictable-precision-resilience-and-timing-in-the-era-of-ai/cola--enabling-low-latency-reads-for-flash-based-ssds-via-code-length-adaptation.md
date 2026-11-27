COLA: Enabling Low-Latency Reads for Flash-Based SSDs via Code Length Adaptation
Authors：
[Zhengyao Ding](https://63dac.conference-program.com/?post_type=page&p=15&uid=3884013867305899716)，[Dingxin Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=5875215785733413157)，[Xiaolu Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=4971851831197923892)，[Patrick P. C. Lee](https://63dac.conference-program.com/?post_type=page&p=15&uid=7458903579435810806)，[Lingling Song](https://63dac.conference-program.com/?post_type=page&p=15&uid=04888144593372453751)，[Rui Lu](https://63dac.conference-program.com/?post_type=page&p=15&uid=27423636854028440041)，[Yichen Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=53767576654680849611)，[Yuchong Hu](https://63dac.conference-program.com/?post_type=page&p=15&uid=7589487054955796938)，[Dan Feng](https://63dac.conference-program.com/?post_type=page&p=15&uid=342343)

## 中文标题

COLA：通过码长自适应实现基于 Flash 的 SSD 低时延读取

## 英文摘要

Flash-based SSDs are prone to bit errors in flash cells. To ensure reliability, SSDs employ error correction codes (ECCs) that encode user data bits into codewords composed of data and redundant parity bits, enabling correction of a limited number of bit errors. In practice, however, the raw bit error rate (RBER) of SSDs fluctuates over time. We observe that for ECCs with a fixed code rate (the fraction of user data bits per codeword), longer codewords provide higher reliability, while shorter codewords offer lower read latency. To this end, we propose COLA, an adaptive coding framework that optimizes the code length (i.e., total number of user data and parity bits per codeword) for individual SSD pages to achieve low-latency reads while maintaining reliability guarantees and constant storage overhead. COLA adopts a failure-aware read mechanism that selectively transfers and decodes failed codewords, and integrates a failure-aware read-latency model to determine actual read operations based on current RBERs and select the optimal code length for each write operation. Evaluation using the MQSim simulation shows that COLA significantly reduces average and tail read latencies compared to the default fixed-code-length approach.

## 中文摘要

基于 Flash 的 SSD 易在闪存单元中产生位错误。为保证可靠性，SSD 采用纠错码（ECC），将用户数据比特编码为由数据位与冗余校验位构成的码字，从而能够纠正有限数量的位错误。然而在实际中，SSD 的原始误码率（RBER）会随时间波动。我们观察到，对于码率（每个码字中用户数据比特所占比例）固定的 ECC，较长的码字提供更高的可靠性，而较短的码字则带来更低的读时延。为此，我们提出 COLA，一个自适应编码框架，针对各个 SSD 页优化码长（即每个码字中用户数据位与校验位的总数），在保持可靠性保证与恒定存储开销的同时实现低时延读取。COLA 采用失效感知的读机制，有选择地传输并解码失效码字，并集成失效感知的读时延模型，根据当前 RBER 确定实际的读操作，并为每次写操作选择最优码长。基于 MQSim 的仿真评估表明，与默认的固定码长方案相比，COLA 显著降低了平均读时延与尾部读时延。
