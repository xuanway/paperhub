Marlin: I/O-Efficient Prefix KV Cache Retrieval for Long-Prefix LLM Serving
Authors：
[Guifeng Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=9358608897372060712)，[Shengan Zheng](https://63dac.conference-program.com/?post_type=page&p=15&uid=93998885764835769641)，[Ji Fang](https://63dac.conference-program.com/?post_type=page&p=15&uid=6711656755698680217)，[Yucheng Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=19718461096891477551)，[Shi Shu](https://63dac.conference-program.com/?post_type=page&p=15&uid=62080486695123566601)，[Weihan Kong](https://63dac.conference-program.com/?post_type=page&p=15&uid=57665325702380027031)，[Cong Zhou](https://63dac.conference-program.com/?post_type=page&p=15&uid=48039618468757618421)，[Kaijiang Deng](https://63dac.conference-program.com/?post_type=page&p=15&uid=2592136777495817211)，[Linpeng Huang](https://63dac.conference-program.com/?post_type=page&p=15&uid=657243)

## 中文标题

Marlin：面向长前缀 LLM 服务的高 I/O 效率前缀 KV Cache 检索

## 英文摘要

As large language models (LLMs) are often deployed with long, context-rich prefixes, the prefix KV cache frequently exceeds GPU memory capacity. Although offloading the prefix KV cache to host memory or storage alleviates capacity pressure, it introduces severe I/O stalls that increase Time-to-First-Token (TTFT) latency. To address this challenge, we present Marlin, an I/O-efficient prefix KV cache retrieval system for long-prefix LLM inference. Marlin employs a dispersion-based token selector to precompute a compact, query-agnostic subset of important prefix tokens, and a sensitivity-guided head classifier that assigns different KV retrieval policies to classify prefix-sensitive and query-sensitive heads. An overlap-optimized attention pipeline further hides offload latency by overlapping head-specific KV transfers with attention computation. Experimental results demonstrate that Marlin significantly reduces TTFT compared to state-of-the-art methods while maintaining comparable model accuracy.

## 中文摘要

由于大语言模型（LLM）常以长且富含上下文的前缀进行部署，前缀 KV cache 经常超出 GPU 显存容量。尽管将前缀 KV cache 卸载至主机内存或存储可缓解容量压力，但会引入严重的 I/O 停顿，从而增加首 token 时延（TTFT）。为应对该挑战，我们提出 Marlin，一个面向长前缀 LLM 推理的高 I/O 效率前缀 KV cache 检索系统。Marlin 采用基于离散度的 token 选择器预计算一个紧凑的、与查询无关的重要前缀 token 子集，并使用敏感度引导的 head 分类器，通过分配不同的 KV 检索策略来区分前缀敏感头与查询敏感头。一个重叠优化的注意力流水线进一步将头特定的 KV 传输与注意力计算相重叠，以隐藏卸载延迟。实验结果表明，Marlin 在保持模型精度相当的同时，相比现有最优方法显著降低了 TTFT。

## 英文关键词

LLM, Prefix KV cache, Sparse attention

## 中文关键词

LLM、前缀 KV cache、稀疏注意力
