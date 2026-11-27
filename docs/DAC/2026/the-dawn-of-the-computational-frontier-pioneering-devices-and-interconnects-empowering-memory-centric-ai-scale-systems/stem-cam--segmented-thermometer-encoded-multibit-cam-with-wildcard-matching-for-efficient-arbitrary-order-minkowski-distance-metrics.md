STEM-CAM: Segmented Thermometer-Encoded Multibit CAM with Wildcard Matching for Efficient Arbitrary-Order Minkowski Distance Metrics
Authors：
[Zeyu Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=66430289532703733511)，[Weikai Xu](https://63dac.conference-program.com/?post_type=page&p=15&uid=00425602680868299111)，[Changyue Hao](https://63dac.conference-program.com/?post_type=page&p=15&uid=62829907376184824661)，[Qianqian Huang](https://63dac.conference-program.com/?post_type=page&p=15&uid=506253253669092643)，[Ru Huang](https://63dac.conference-program.com/?post_type=page&p=15&uid=314343)

## 中文标题

STEM-CAM：支持通配符匹配的分段温度计编码多比特 CAM，面向高效的任意阶 Minkowski 距离度量

## 英文摘要

Minkowski distance metrics (e.g., 𝐿0, 𝐿1, 𝐿2) have emerged as fundamental primitives for similarity measurement, data retrieval, and decision-making in advanced AI applications, such as large language models and embodied intelligence. For hardware implementations, conventional digital circuits suffer from limited parallelism, high energy consumption and latency. Alternatively, content addressable memory (CAM) architecture natively supports large-scale distance metrics in parallel. However, existing CAM-based designs primarily support only 𝐿0 and 𝐿1 distances, with limited scalability and configurability. In this work, we propose a segmented thermometer-encoded multibit CAM architecture, dubbed as STEM-CAM, which enables configurable arbitrary-order Minkowski distance metrics. By segmenting the distance norm and augmenting the thermometer encoding with wildcard matching mechanism, STEM-CAM enables a unified and scalable encoding of feature vectors that supports arbitrary-order Minkowski distance metrics within the CAM array, while significantly enhancing encoding efficiency with a bit-compression scheme. Moreover, a novel ultra-compact FeFET-based encoding-aware multibit CAM cell is proposed for efficient hardware mapping of STEM-CAM, enabling multiple encoding bits to be stored in a single CAM cell, thereby further improving area-and energy-efficiency. With comprehensive experimental results, we demonstrate STEM-CAM with 11.6 ∼2496× area-energy-delay product (AEDP) reduction over conventional digital and NVM-based designs for Minkowski distance metrics, as well as high accuracy comparable to software, showing its great potential for distance-based AI applications.

## 中文摘要

Minkowski 距离度量（如 L0、L1、L2）已成为大语言模型与具身智能等前沿人工智能应用中相似性度量、数据检索与决策的基本算子。在硬件实现方面，传统数字电路受限于并行度不足、能耗与延迟偏高。相比之下，内容可寻址存储器（CAM）架构原生支持大规模距离度量的并行计算。然而，现有基于 CAM 的设计大多仅支持 L0 与 L1 距离，可扩展性与可配置性有限。本文提出一种分段温度计编码的多比特 CAM 架构，命名为 STEM-CAM，可实现可配置的任意阶 Minkowski 距离度量。通过对距离范数进行分段，并以通配符匹配机制增强温度计编码，STEM-CAM 能够在 CAM 阵列内以统一且可扩展的方式编码特征向量，支持任意阶 Minkowski 距离度量，同时借助位压缩方案显著提升编码效率。此外，我们提出一种新型超紧凑的、基于 FeFET 的编码感知多比特 CAM 单元，用于 STEM-CAM 的高效硬件映射，使单个 CAM 单元即可存储多个编码位，从而进一步提升面积与能效。充分的实验结果表明，相比传统数字设计与基于 NVM 的设计，STEM-CAM 在 Minkowski 距离度量上使面积-能耗-延迟积（AEDP）降低 11.6 至 2496 倍，并能达到与软件相当的高精度，展现出其在基于距离的 AI 应用中的巨大潜力。
