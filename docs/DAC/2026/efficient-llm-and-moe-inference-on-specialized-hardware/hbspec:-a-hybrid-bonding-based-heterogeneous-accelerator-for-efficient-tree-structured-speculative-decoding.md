Hbspec: A Hybrid-Bonding-Based Heterogeneous Accelerator for Efficient Tree-Structured Speculative Decoding
Authors：
[Runze Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=15134824545291320461)，[Qinggang Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=40659363708189088741)，[Haifeng Liu](https://63dac.conference-program.com/?post_type=page&p=15&uid=79163521860891548921)，[Xinyu Zhu](https://63dac.conference-program.com/?post_type=page&p=15&uid=74077250606583231941)，[Chenggang Duan](https://63dac.conference-program.com/?post_type=page&p=15&uid=8984246085541651731)，[Long Zheng](https://63dac.conference-program.com/?post_type=page&p=15&uid=976343)，[Xiaofei Liao](https://63dac.conference-program.com/?post_type=page&p=15&uid=630243)，[Hai Jin](https://63dac.conference-program.com/?post_type=page&p=15&uid=730243)，[Jingling Xue](https://63dac.conference-program.com/?post_type=page&p=15&uid=72647212260742604221)

## 中文标题

HBSpec：面向高效树结构推测解码的混合键合异构加速器

## 英文摘要

Emerging tree-structured speculative decoding has been proposed as a promising alternative to conventional sequence-structured speculative decoding, offering a higher verification success rate and reduced inference latency while exhibiting characteristics of higher computational intensity. However, existing near-memory processing (NMP)-enabled heterogeneous accelerators for large language models (LLMs) typically place processing elements (PEs) on DRAM dies, resulting in limited computation capability, which prevents them from fully accelerating tree-structured speculative decoding. In response, we propose a hybrid-bonding (HB)-based heterogeneous accelerator for tree-structured speculative decoding, called HBSpec, which customizes PEs on the incorporated logic die to enhance NMP computation capacity. HBSpec features a communication-optimized data mapping policy to minimize cross-bank data access overhead inherent in the distributed-memory design adopted in HB. Furthermore, an arithmetic intensity-aware operator scheduler is designed to dynamically assign operators to the most suitable hardware units, while a Tree-KV pool management scheme is introduced to eliminate memory fragmentation caused by discarded speculative branches. Experimental results demonstrate that HBSpec achieves average throughput improvements of 15.56×, 2.36×, and 2.13× over the state-of-the-art NPU-only, NPU+LPDDR, and NPU+HB baselines, respectively.

## 中文摘要

新兴的树结构推测解码被提出作为传统序列结构推测解码的有力替代方案，它具有更高的验证成功率和更低的推理延迟，同时也呈现出计算强度更高的特点。然而，现有面向大语言模型（LLM）的、支持近存处理（NMP）的异构加速器通常将处理单元（PE）置于 DRAM 晶圆上，计算能力受限，无法充分加速树结构推测解码。为此，我们提出基于混合键合（HB）的树结构推测解码异构加速器 HBSpec，它在所集成的逻辑晶圆上定制 PE，以增强 NMP 的计算能力。HBSpec 采用通信优化的数据映射策略，以尽量降低 HB 所采用的分布式存储设计固有的跨 bank 数据访问开销。此外，我们设计了算术强度感知的算子调度器，将算子动态分配给最合适的硬件单元；并引入 Tree-KV 池管理方案，消除被丢弃的推测分支所造成的存储碎片。实验结果表明，HBSpec 相比当前最先进的仅 NPU、NPU+LPDDR 与 NPU+HB 基线，平均吞吐分别提升 15.56×、2.36× 和 2.13×。
