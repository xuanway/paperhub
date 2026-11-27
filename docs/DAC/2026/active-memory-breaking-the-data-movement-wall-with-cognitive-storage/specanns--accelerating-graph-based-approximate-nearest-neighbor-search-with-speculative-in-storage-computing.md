SpecANNS: Accelerating Graph-Based Approximate Nearest Neighbor Search with Speculative In-Storage Computing
Authors：
[Yi Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=030343)，[Yongxin Shen](https://63dac.conference-program.com/?post_type=page&p=15&uid=1051491689561464031)，[Yongbiao Zhu](https://63dac.conference-program.com/?post_type=page&p=15&uid=65195261901369990381)，[Tianyu Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=4102639928273142851)，[Chenlin Ma](https://63dac.conference-program.com/?post_type=page&p=15&uid=4213970674159892189)，[Jiaxian Chen](https://63dac.conference-program.com/?post_type=page&p=15&uid=37582528852818661511)，[Kecheng Huang](https://63dac.conference-program.com/?post_type=page&p=15&uid=9023677625232671802)，[Rui Mao](https://63dac.conference-program.com/?post_type=page&p=15&uid=430343)

## 中文标题

SpecANNS：利用推测式存内计算加速基于图的近似最近邻搜索

## 英文摘要

Graph-based Approximate Nearest Neighbor Search (ANNS) gains increasing attention from both academia and industry. Due to the random node access pattern of graph-based ANNS, long I/O latency has become a significant bottleneck that affects vector search efficiency. The emerging In-Storage Computing (ISC) technique offers a promising solution to alleviate the I/O burden of graph-based ANNS. The system must be carefully designed to fully utilize the computing capabilities of the in-storage Field-Programmable Gate Array (FPGA). This paper presents SpecANNS, a speculative in-storage computing accelerator for graph-based ANNS. SpecANNS computes distances and speculatively identifies neighbor pages that are more likely to be accessed in subsequent hops. To further reduce page read latency, SpecANNS leverages the internal parallelism of NAND flash chips, evenly distributing vectors and their neighbors across multiple flash channels. SpecANNS is implemented on a real Computational Storage Device (CSD) hardware with a user-friendly programming interface. Experimental results demonstrate that SpecANNS significantly reduces ANNS query latency while achieving better energy efficiency than state-of-the-art graph-based ANNS approaches.

## 中文摘要

基于图的近似最近邻搜索（ANNS）日益受到学术界和工业界的关注。由于基于图的 ANNS 采用随机节点访问模式，较长的 I/O 延迟已成为影响向量搜索效率的重要瓶颈。新兴的存内计算（ISC）技术为缓解基于图的 ANNS 的 I/O 负担提供了一种有前景的解决方案。系统必须经过精心设计，才能充分利用存内现场可编程门阵列（FPGA）的计算能力。本文提出了 SpecANNS，一种面向基于图的 ANNS 的推测式存内计算加速器。SpecANNS 计算距离，并推测性地识别在后续跳转中更可能被访问的邻居页。为进一步降低页读取延迟，SpecANNS 利用 NAND 闪存芯片的内部并行性，将向量及其邻居均匀分布到多个闪存通道上。SpecANNS 在真实的计算存储设备（CSD）硬件上实现，并提供了易用的编程接口。实验结果表明，SpecANNS 显著降低了 ANNS 查询延迟，同时相比当前最优的基于图的 ANNS 方法实现了更好的能效。

## 英文关键词

In-Storage Computing, Approximate Nearest Neighbor Search, Accelerator, Computational Storage Device

## 中文关键词

存内计算、近似最近邻搜索、加速器、计算存储设备
