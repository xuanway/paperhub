REACT: Rapid Error-Tolerant Activation Compressor for Efficient Transformer Training
Authors：
[Seungyong Lee](https://63dac.conference-program.com/?post_type=page&p=15&uid=67257936049642814841)，[Geonu Yun](https://63dac.conference-program.com/?post_type=page&p=15&uid=89876580065114057371)，[Xuan Truong Nguyen](https://63dac.conference-program.com/?post_type=page&p=15&uid=53254707789065279161)，[Hyuk-Jae Lee](https://63dac.conference-program.com/?post_type=page&p=15&uid=957143)

## 中文标题

REACT：面向高效 Transformer 训练的低开销容错激活压缩器

## 英文摘要

Training large language models (LLMs) poses considerable challenges due to long training times, extensive memory requirements, and substantial bandwidth demands. Activation compression is a promising approach to reduce the memory footprint since activation memory accounts for the majority of memory usage in LLM training with large batch sizes and long context lengths. However, because reducing data size increases the amount of information per bit, it may become sensitive to a fault, which could adversely affect the model convergence and accuracy. In this work, we demonstrate that compression can enhance robustness to bit errors and present REACT, a Rapid Error-tolerant Activation Compressor for efficient Transformer training, which not only reduces memory usage but also enhances error tolerance. Using base-delta encoding, which stores only the differences between data, it minimize data size while significantly reducing the number of error-vulnerable bits. Additionally, an error-limiting encoding scheme is incorporated to address remaining vulnerable bits. Experimental results show that REACT maintains accuracy under bit error rate 1000× higher while achieving a 4× reduction in activation memory, with negligible performance overhead.

## 中文摘要

训练大语言模型（LLM）面临训练时间长、存储需求大以及带宽需求高等诸多挑战。激活压缩是降低内存占用的一种有前景的方法，因为在大批量尺寸和长上下文长度下的 LLM 训练中，激活内存占据了内存使用的主要部分。然而，减小数据尺寸会提高每比特所承载的信息量，因而可能对故障更为敏感，进而可能影响模型的收敛与精度。在本工作中，我们证明压缩能够增强对位错误的鲁棒性，并提出 REACT，一种面向高效 Transformer 训练的快速容错激活压缩器，它既降低内存占用又增强容错能力。REACT 采用基-差分编码（base-delta encoding），仅存储数据之间的差值，从而在最小化数据尺寸的同时显著减少易受错误影响的比特数量。此外，还引入了错误限制编码方案以处理剩余易受影响的比特。实验结果表明，REACT 在位错误率高 1000× 的情况下仍能保持精度，同时实现 4× 的激活内存压缩，且性能开销可忽略不计。

## 英文关键词

Data compression, Error tolerance, Large language model

## 中文关键词

数据压缩、容错、大语言模型
