Cryozip: An Efficient Cryogenic Compressor for Quantum Error Correction Syndromes
Authors：
[Guanchen Tao](https://63dac.conference-program.com/?post_type=page&p=15&uid=95821082083721425851)，[Alexander Knapen](https://63dac.conference-program.com/?post_type=page&p=15&uid=0452309826069455376)，[Jacob Mack](https://63dac.conference-program.com/?post_type=page&p=15&uid=22850112543417931341)，[Gokul Subramanian Ravi](https://63dac.conference-program.com/?post_type=page&p=15&uid=73278859203052225271)，[Qirui Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=27405191484153697381)，[Mehdi Saligane](https://63dac.conference-program.com/?post_type=page&p=15&uid=65912187489245049621)，[Dennis Sylvester](https://63dac.conference-program.com/?post_type=page&p=15&uid=3132816083396341068)

## 中文标题

CryoZip：面向量子纠错综合征的高效低温压缩器

## 英文摘要

Scaling fault-tolerant quantum computing is increasingly constrained by the limited bandwidth and power budget across the 4 K-room temperature (RT) interface. We present CryoZip1, a cross-stack cryogenic compression framework that cooperates with a lightweight cryogenic quantum error correction (QEC) predecoder to reduce 4 K-to-RT syndrome transmission under realistic, circuit-level noise. CryoZip targets sparse syndrome vectors with a sliding-window compression architecture sized under strict decoding latency constraints to maximize energy efficiency. We implement and evaluate the design in 22 nm FDSOI characterized at 4 K, using vector-based power, performance, and area analysis to obtain realistic hardware data. CryoZip achieves up to 48× compression—1.8× higher than state-of-the-art compressors—across various QEC codes while delivering 4-26× energy savings. When paired with a QEC predecoder, it yields over 14,238× bandwidth reduction, while energy savings rise to 42× when accounting for realistic QEC interface overheads.

## 中文摘要

可扩展的容错量子计算日益受到 4 K 与室温（RT）之间接口的有限带宽与功耗预算的制约。我们提出 CryoZip，一个跨栈低温压缩框架，它与轻量级的低温量子纠错（QEC）预解码器协同工作，以在真实的电路级噪声下减少 4 K 到 RT 的综合征传输量。CryoZip 面向稀疏综合征向量，采用滑动窗口压缩架构，其规模在严格的解码延迟约束下确定，从而最大化能效。我们在 4 K 下表征的 22 nm FDSOI 工艺中实现并评估该设计，采用基于向量的功耗、性能与面积分析以获得真实的硬件数据。在多种 QEC 码下，CryoZip 实现最高 48 倍压缩，比最先进的压缩器高出 1.8 倍，同时带来 4–26 倍的能耗节省。与 QEC 预解码器配合使用时，带宽缩减超过 14,238 倍；若计入真实的 QEC 接口开销，能耗节省提升至 42 倍。
