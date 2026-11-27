M²CAM: A Multi-Level Memristor-Based Self-Adaptive CAM Architecture for Genome Processing Acceleration
Authors：
[Yang Han](https://63dac.conference-program.com/?post_type=page&p=15&uid=05335206403759789041)，[Lianfeng Yu](https://63dac.conference-program.com/?post_type=page&p=15&uid=1532404407257658344)，[Teng Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=9244593965564133568)，[Bowen Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=64583327155840532181)，[Yihang Zhu](https://63dac.conference-program.com/?post_type=page&p=15&uid=4797163057874016678)，[Lei Cai](https://63dac.conference-program.com/?post_type=page&p=15&uid=28257773504747793161)，[Yaoyu Tao](https://63dac.conference-program.com/?post_type=page&p=15&uid=2009983080015340538)，[Yuchao Yang](https://63dac.conference-program.com/?post_type=page&p=15&uid=2470983435883587473)

## 中文标题

M²CAM：一种面向基因组处理加速的基于多值忆阻器的自适应内容寻址存储器架构

## 英文摘要

Genomic analysis workflows, such as single-cell RNA sequencing (scRNA-seq), demand massive sequence matching and classifications, yet are fundamentally limited by the data movement overhead and bandwidth bottleneck of von Neumann architectures. Although in-memory computing (IMC) has emerged as a promising solution, most existing IMC-based genome accelerators rely on digital encoding schemes, which introduce excessive hardware overhead and limit processing efficiency. This work presents a Multi-level Memristor-based Self-adaptive CAM (content addressable memory) Architecture (M2CAM) for genome processing acceleration. Unlike conventional digital approaches, the proposed design leverages analog CAM encoding based on multi-level memristor conductance states, enabling compact representation of nucleotides with significantly reduced device count and improved parallelism. Furthermore, a self-adaptive error correction mechanism dynamically adjusts matching precision through hierarchical operation modes, ensuring robust sequence matching under device variations. A parallelized genome classification framework is developed to demonstrate the system’s efficiency, using single-cell RNA sequencing as a representative application. Experimental results show that the proposed architecture achieves a 50% ∼ 75% reduction in device usage, while on real scRNA-seq datasets, M2CAM delivers 131.2× ∼ 3088.9× and 161.2× ∼ 269.6× improvements in energy consumption and latency, compared with CPU/GPU and traditional bioinformatics tools (e.g., STAR).

## 中文摘要

基因组分析流程（如单细胞 RNA 测序，scRNA-seq）需要海量的序列匹配与分类，但其根本上受限于冯·诺依曼架构的数据搬运开销与带宽瓶颈。尽管存内计算（IMC）已成为颇具前景的解决方案，现有基于 IMC 的基因组加速器却大多依赖数字编码方案，带来过高的硬件开销并限制了处理效率。本工作提出一种基于多值忆阻器的自适应内容寻址存储器（CAM）架构（M²CAM），用于基因组处理加速。与传统数字方法不同，所提出的设计利用基于多值忆阻器电导态的模拟 CAM 编码，以显著减少的器件数量实现核苷酸的紧凑表示，并提升并行性。此外，一种自适应纠错机制通过分层操作模式动态调整匹配精度，确保在器件波动下仍能实现稳健的序列匹配。我们以单细胞 RNA 测序作为代表性应用，构建了并行化基因组分类框架以展示系统效率。实验结果表明，所提架构使器件使用量减少 50%∼75%；在真实 scRNA-seq 数据集上，与 CPU/GPU 及传统生物信息学工具（如 STAR）相比，M²CAM 在能耗与延迟上分别取得 131.2×∼3088.9× 与 161.2×∼269.6× 的提升。

## 英文关键词

In-Memory Computing, Multi-level Memristor, Analog CAM Encoding, Self-Adaptive Error Correction, Parallelized Classification Architecture, Single-cell RNA Sequencing, Barcode

## 中文关键词

存内计算、多值忆阻器、模拟 CAM 编码、自适应纠错、并行化分类架构、单细胞 RNA 测序、条码
