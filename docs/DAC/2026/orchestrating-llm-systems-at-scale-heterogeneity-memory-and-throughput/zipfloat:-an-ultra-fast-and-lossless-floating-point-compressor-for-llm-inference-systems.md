Zipfloat: An Ultra-Fast and Lossless Floating-Point Compressor for LLM Inference Systems
Authors：
[Shihao Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=1758068656574149771)，[Xiangyu Zou](https://63dac.conference-program.com/?post_type=page&p=15&uid=035016552205911775)，[Wen Xia](https://63dac.conference-program.com/?post_type=page&p=15&uid=453443)，[Hao Hu](https://63dac.conference-program.com/?post_type=page&p=15&uid=052245063452326801)

## 中文标题

ZipFloat：面向 LLM 推理系统的超高速无损浮点压缩器

## 英文摘要

LLM inference stresses GPU memory with large model weights and KV caches, which requires efficient compression techniques. But existing approaches either sacrifice accuracy (e.g., quantization) or apply serial entropy coding (e.g., DFloat11) that limits throughput. Both constrain the overall inference efficiency. In this work, we propose ZipFloat, an LLM-oriented floating-point compressor that achieves massively parallel com-/decompression while preserving full precision. We observe that weights and KV-cache values in LLMs exhibit strong statistical redundancies, yet existing floating-point formats mask this redundancy and hinder effective compression. To address this, ZipFloat employs ❶Exponent Sparsification, which redefines the binary representation of floating-points to restore compressibility, and ❷Bit-Matrix Packing, which leverages this restored structure with GPU-native parallelism to deliver extreme throughput. Evaluations show that ZipFloat delivers up to 700 GB/s com- /decom-pression throughput, outperforming SOTA methods (e.g., DFloat11) by several orders of magnitude while maintaining comparable compression ratios, thereby reducing over 95% TTFT and improving over 4× inference throughput in LLM systems.

## 中文摘要

LLM 推理因庞大的模型权重与 KV 缓存而给 GPU 内存带来压力，需要高效的压缩技术。但现有方法要么牺牲精度（如量化），要么采用串行熵编码（如 DFloat11）而限制吞吐，二者均制约整体推理效率。本文提出 ZipFloat，一个面向 LLM 的浮点压缩器，在保持全精度的同时实现大规模并行的压缩与解压缩。我们观察到，LLM 中的权重与 KV 缓存值具有强烈的统计冗余，但现有浮点格式掩盖了这种冗余，阻碍了有效压缩。为此，ZipFloat 采用❶指数稀疏化，重新定义浮点数的二进制表示以恢复可压缩性；❷位矩阵打包，借助 GPU 原生并行性利用恢复出的结构，实现极致吞吐。评估表明，ZipFloat 的压缩/解压缩吞吐最高可达 700 GB/s，在保持相当压缩率的同时超越 SOTA 方法（如 DFloat11）数个数量级，从而在 LLM 系统中使 TTFT 降低超过 95%，并将推理吞吐提升 4 倍以上。
