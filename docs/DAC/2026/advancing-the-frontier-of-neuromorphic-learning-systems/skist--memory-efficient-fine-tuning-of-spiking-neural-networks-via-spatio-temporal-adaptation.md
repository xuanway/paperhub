SkiST: Memory-Efficient Fine-Tuning of Spiking Neural Networks via Spatio-Temporal Adaptation
Authors：
[Zhibai Huang](https://63dac.conference-program.com/?post_type=page&p=15&uid=7121734561463943769)，[James Yen](https://63dac.conference-program.com/?post_type=page&p=15&uid=5278882381672633809)，[Zhixiang Wei](https://63dac.conference-program.com/?post_type=page&p=15&uid=361148584148878231)，[Yun Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=65465609592923444771)，[Fangxin Liu](https://63dac.conference-program.com/?post_type=page&p=15&uid=318143)，[Zhengwei Qi](https://63dac.conference-program.com/?post_type=page&p=15&uid=814343)

## 中文标题

SkiST：通过时空自适应实现脉冲神经网络的内存高效微调

## 英文摘要

Building high-performance Spiking Neural Networks (SNNs) involves a trade-off among competing paradigms. While unsupervised rules like STDP offer efficiency and ANN-to-SNN conversion provides a simple path, direct training with Backpropagation Through Time (BPTT) is the most effective route for achieving high accuracy. However, BPTT’s effectiveness comes at a steep price: its memory cost scales linearly with timesteps, creating a resource barrier that limits the information capacity and practicality of SNNs. This makes memory-efficient training methods critical for real-world deployment. To this end, we propose the Skipping-Side-Tuning (SkiST) framework, which leverages both spatial and temporal redundancy in SNNs for memory-efficient fine-tuning. On the spatial side, SkiST introduces side networks and applies low-rank approximation with adaptive rank filtering to compress trainable parameters. On the temporal side, it employs Dynamic Sparse BPTT, selectively skipping non-critical timesteps during gradient propagation while compensating for information loss with exponentially decayed gradients. Experiments show SkiST reduces GPU memory by up to 50% over full fine-tuning while maintaining competitive accuracy. On an SNN-based language model, SkiST requires 23.2 GB of memory for 1024-token sequences, compared to 40.3 GB for the baseline, with minimal accuracy degradation. This work enables the deployment of adaptable, efficient spiking models on resource-constrained devices.

## 中文摘要

构建高性能脉冲神经网络（SNN）需要在相互竞争的多种范式之间进行权衡。STDP 等无监督规则高效，ANN 到 SNN 的转换提供了简单途径，而基于时间反向传播（BPTT）的直接训练则是实现高准确率的最有效路线。然而，BPTT 的有效性代价不菲：其内存开销随时间步线性增长，形成资源壁垒，限制了 SNN 的信息容量与实用性。这使得内存高效的训练方法对实际部署至关重要。为此，我们提出 Skipping-Side-Tuning（SkiST）框架，利用 SNN 中的空间与时间冗余实现内存高效的微调。在空间方面，SkiST 引入旁路网络，并应用带有自适应秩滤波的低秩近似来压缩可训练参数。在时间方面，它采用动态稀疏 BPTT，在梯度传播过程中有选择地跳过非关键时间步，并以指数衰减梯度补偿信息损失。实验表明，SkiST 相较全量微调可将 GPU 内存最多降低 50%，同时保持有竞争力的准确率。在基于 SNN 的语言模型上，处理 1024 个 token 的序列时 SkiST 仅需 23.2 GB 内存，而基线需要 40.3 GB，且准确率下降极小。本工作使可适配、高效的脉冲模型得以部署于资源受限的设备上。
