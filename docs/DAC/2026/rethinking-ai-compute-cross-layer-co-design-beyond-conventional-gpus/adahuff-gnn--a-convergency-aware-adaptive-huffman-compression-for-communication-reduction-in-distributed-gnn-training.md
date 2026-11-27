Adahuff-GNN: A Convergency-Aware Adaptive Huffman Compression for Communication Reduction in Distributed GNN Training
Authors：
[Zhiyu Sun](https://63dac.conference-program.com/?post_type=page&p=15&uid=10196860666304438921)，[Jihe Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=0462694480782453985)，[zhaohui jia](https://63dac.conference-program.com/?post_type=page&p=15&uid=312732089653002127)，[Yuanhua Xiao](https://63dac.conference-program.com/?post_type=page&p=15&uid=67524933178136143721)，[Linying Wu](https://63dac.conference-program.com/?post_type=page&p=15&uid=8410064780896283229)，[Danghui Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=050443)

## 中文标题

AdaHuff-GNN：面向分布式 GNN 训练通信削减的收敛感知自适应 Huffman 压缩

## 英文摘要

Distributed training of Graph Neural Networks (GNNs) is hindered by communication overhead from exchanging embeddings and gradients. Existing quantization methods mitigate this cost by using shared bit widths at the layer or group level, followed by node-level uniform quantization, but such coarse granularity cannot fully exploit redundancy in long-tailed communication distributions. Entropy compression is well suited to these distributions, but static entropy compression schemes become less effective when training induces untracked distribution shifts. To address this issue, AdaHuff-GNN, a convergency-aware adaptive Huffman compression framework, is proposed to apply entropy compression to reduce communication cost in distributed GNN training. Within AdaHuff-GNN, loss-triggered codebook reconstruction and coarse-to-fine adaptive selection of codebook sizes jointly produce stage-wise codebooks that track distribution shifts. Binning-assisted clustering and conflict-free decoding reduce codec overhead on the communication critical path. Experiments show that AdaHuff-GNN reduces communication volume by 2.87× and shortens training epoch time by 37.5% over state-of-the-art methods without degrading model accuracy.

## 中文摘要

图神经网络（GNN）的分布式训练受制于交换嵌入与梯度所带来的通信开销。现有量化方法通过在层或组级别采用共享位宽，再辅以节点级均匀量化来缓解这一开销，但这种粗粒度方式无法充分利用长尾通信分布中的冗余。熵压缩非常契合此类分布，但当训练引发未被跟踪的分布漂移时，静态熵压缩方案的效果会下降。为此，本文提出 AdaHuff-GNN，一种收敛感知的自适应 Huffman 压缩框架，利用熵压缩降低分布式 GNN 训练中的通信开销。在 AdaHuff-GNN 中，由损失触发的码本重建与码本尺寸的由粗到细自适应选择共同生成可跟踪分布漂移的分阶段码本；分箱辅助聚类与无冲突解码则降低了通信关键路径上的编解码开销。实验表明，在不降低模型精度的前提下，AdaHuff-GNN 相较当前最优方法将通信量减少 2.87×，并将单轮训练时间缩短 37.5%。

## 英文关键词

Graph neural network, distributed training, communication compression, Huffman coding

## 中文关键词

图神经网络、分布式训练、通信压缩、Huffman 编码
