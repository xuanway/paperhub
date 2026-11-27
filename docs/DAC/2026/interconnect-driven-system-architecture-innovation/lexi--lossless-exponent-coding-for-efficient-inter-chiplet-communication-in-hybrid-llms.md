LEXI: Lossless Exponent Coding for Efficient Inter-Chiplet Communication in Hybrid LLMs
Authors：
[Miao Sun](https://63dac.conference-program.com/?post_type=page&p=15&uid=85848894229716927861)，[Alish Kanani](https://63dac.conference-program.com/?post_type=page&p=15&uid=1978385912665544943)，[Kaushik SHROFF](https://63dac.conference-program.com/?post_type=page&p=15&uid=2530685979128886207)，[Umit Ogras](https://63dac.conference-program.com/?post_type=page&p=15&uid=294443)

## 中文标题

LEXI：用于混合 LLM 中高效芯粒间通信的无损指数编码

## 英文摘要

Data movement overheads increase the inference latency of state-of-the-art large language models (LLMs). These models commonly use bfloat16 (BF16) format for stable training. Floating-point standards allocate eight bits to the exponent, but our profiling reveals that exponent streams exhibit fewer than 3 bits Shannon entropy, indicating high inherent compressibility. To exploit this potential, we propose LEXI, a novel lossless exponent compression scheme based on Huffman coding. LEXI compresses activations and caches on the fly while storing compressed weights for just-in-time decompression near compute, without sacrificing system throughput and model accuracy. The codecs at the ingress and egress ports of network-on-chip routers sustain the maximum link bandwidth via multi-lane LUT decoders, incurring only 0.09% area overhead with GF 22 nm technology. LEXI reduces inter-chiplet communication and end-to-end inference latencies by 33–45% and 30–35% on modern Jamba [23], Zamba [11], and Qwen [3] LLMs implemented on a homogeneous chiplet architecture.

## 中文摘要

数据搬运开销增加了当前最先进大语言模型（LLM）的推理延迟。此类模型通常采用 bfloat16（BF16）格式以保证训练稳定。浮点标准为指数分配 8 位，但我们的剖析显示，指数流的香农熵不足 3 比特，表明其具有很高的内在可压缩性。为挖掘这一潜力，我们提出 LEXI，一种基于 Huffman 编码的新型无损指数压缩方案。LEXI 在线压缩激活值与缓存，同时存储压缩后的权重并在计算单元附近进行即时解压，且不牺牲系统吞吐与模型精度。位于片上网络路由器入口与出口端口的编解码器通过多路 LUT 解码器维持最大链路带宽，在 GF 22nm 工艺下仅引入 0.09% 的面积开销。在同构芯粒架构上实现的现代 Jamba [23]、Zamba [11] 与 Qwen [3] LLM 中，LEXI 将芯粒间通信量与端到端推理延迟分别降低 33–45% 与 30–35%。
