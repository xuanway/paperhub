REFLEX: Rewrite-Free Row-Aligned Sparse Attention for Efficient LLM Execution on PIM
Authors：
[Juhong Park](https://63dac.conference-program.com/?post_type=page&p=15&uid=84990009752672568951)，[Yintao He](https://63dac.conference-program.com/?post_type=page&p=15&uid=9739721775974041393)，[Sangheum Yeon](https://63dac.conference-program.com/?post_type=page&p=15&uid=1639206273187420754)，[Yiran Chen](https://63dac.conference-program.com/?post_type=page&p=15&uid=712143)，[Jong Hwan Ko](https://63dac.conference-program.com/?post_type=page&p=15&uid=41391686944773726741)

## 中文标题

REFLEX：面向 PIM 上高效 LLM 执行的无重写行对齐稀疏注意力

## 英文摘要

Large language models (LLMs) face decoding bottlenecks as attention repeatedly accesses the key-value (KV) cache. Sparse attention and processing-in-memory (PIM) each reduce data movement, but their naive integration produces irregular KV accesses that span multiple DRAM rows, leading to unnecessary activations and cache rewrites. We present REFLEX, a rewrite-free sparse attention framework that colocates required KV entries in a single DRAM row and applies activation-aware scheduling for PIM execution. REFLEX preserves accuracy without hardware changes, achieving up to 1.64× throughput and 1.36× energy efficiency on PIM, and 1.37× throughput in GPU-PIM systems.

## 中文摘要

大语言模型（LLM）在解码阶段面临瓶颈，因为注意力会反复访问键值（KV）缓存。稀疏注意力与存内计算（PIM）各自都能减少数据搬移，但二者的简单结合会产生跨多个 DRAM 行的不规则 KV 访问，导致不必要的激活与缓存重写。我们提出 REFLEX，一种无重写的稀疏注意力框架，它将所需的 KV 条目共置于单个 DRAM 行中，并采用激活感知调度来执行 PIM。REFLEX 无需硬件改动即可保持精度，在 PIM 上实现最高 1.64 倍的吞吐提升和 1.36 倍的能效提升，在 GPU-PIM 系统中实现 1.37 倍的吞吐提升。

## 英文关键词

LLM, processing-in-memory (PIM), DRAM, sparse attention

## 中文关键词

LLM、存内计算（PIM）、DRAM、稀疏注意力
