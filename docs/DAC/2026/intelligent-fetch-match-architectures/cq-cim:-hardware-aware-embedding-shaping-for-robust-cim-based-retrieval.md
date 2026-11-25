CQ-CiM: Hardware-Aware Embedding Shaping for Robust CiM-Based Retrieval
Authors：
[Xinzhao Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=1878377323191651464)，[Alptekin Vardar](https://63dac.conference-program.com/?post_type=page&p=15&uid=2708954154945124011)，[Franz Müller](https://63dac.conference-program.com/?post_type=page&p=15&uid=9818580274463955283)，[Navya Goli](https://63dac.conference-program.com/?post_type=page&p=15&uid=3004988013028208508)，[Umamaheswara Tida](https://63dac.conference-program.com/?post_type=page&p=15&uid=206143)，[Kai Ni](https://63dac.conference-program.com/?post_type=page&p=15&uid=11469543746745622151)，[X. Sharon Hu](https://63dac.conference-program.com/?post_type=page&p=15&uid=316243)，[Thomas Kämpfe](https://63dac.conference-program.com/?post_type=page&p=15&uid=4467628931237674746)，[Ruiyang Qin](https://63dac.conference-program.com/?post_type=page&p=15&uid=734843)

## 中文标题

CQ-CiM：面向鲁棒 CiM 检索的硬件感知嵌入整形

## 英文摘要

Deploying Retrieval-Augmented Generation (RAG) on edge devices is in high demand, but is hindered by the latency of massive data movement and computation on traditional architectures. Compute-in-Memory (CiM) architectures address this bottleneck by performing vector search directly within their crossbar structure. However, CiM’s adoption for RAG is limited by a fundamental “representation gap,” as high-precision, high-dimension embeddings are incompatible with CiM’s low-precision, low-dimension array constraints. This gap is compounded by the diversity of CiM implementations (e.g., SRAM, ReRAM, FeFET), each with unique designs (e.g., 2-bit cells, 512x512 arrays). Consequently, RAG data must be naively reshaped to fit each target implementation. Current data shaping methods handle dimension and precision disjointly, which degrades data fidelity. This not only negates the advantages of CiM for RAG but also confuses hardware designers, making it unclear if a failure is due to the circuit design or the degraded input data. As a result, CiM adoption remains limited. In this paper, we introduce CQ-CiM, a unified, hardware-aware data shaping framework that jointly learns Compression and Quantization to produce CiM-compatible low-bit embeddings for diverse CiM designs. To the best of our knowledge, this is the first work to shape data for comprehensive CiM usage on RAG.

## 中文摘要

在边缘设备上部署检索增强生成（RAG）需求旺盛，但受限于传统架构中庞大数据搬移与计算所带来的延迟。存内计算（CiM）架构通过在其交叉阵列结构内直接执行向量搜索来化解这一瓶颈。然而，CiM 在 RAG 中的应用受制于根本性的「表示鸿沟」：高精度、高维的嵌入与 CiM 低精度、低维的阵列约束并不兼容。这一鸿沟还因 CiM 实现方式的多样性（如 SRAM、ReRAM、FeFET）而进一步加剧，每种实现都有其独特设计（如 2 bit 单元、512x512 阵列）。因此，RAG 数据必须经过简单重塑才能适配每一种目标实现。现有数据整形方法将维度与精度分开处理，损害了数据保真度。这不仅抵消了 CiM 对 RAG 的优势，也使硬件设计者难以判断失效究竟源于电路设计还是劣化的输入数据。其结果是 CiM 的采用依然受限。本文提出 CQ-CiM，一个统一的、硬件感知的数据整形框架，联合学习压缩与量化，为多样的 CiM 设计生成 CiM 兼容的低比特嵌入。据我们所知，这是首个为 RAG 上全面使用 CiM 而进行数据整形的工作。
