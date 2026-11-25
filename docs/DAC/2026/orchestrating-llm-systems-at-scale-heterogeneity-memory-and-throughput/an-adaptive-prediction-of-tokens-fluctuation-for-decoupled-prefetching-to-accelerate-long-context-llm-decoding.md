An Adaptive Prediction of Tokens Fluctuation for Decoupled Prefetching to Accelerate Long-Context LLM Decoding
Authors：
[Yuanhua Xiao](https://63dac.conference-program.com/?post_type=page&p=15&uid=67524933178136143721)，[Jihe Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=0462694480782453985)，[Zhiyu Sun](https://63dac.conference-program.com/?post_type=page&p=15&uid=10196860666304438921)，[Linying Wu](https://63dac.conference-program.com/?post_type=page&p=15&uid=8410064780896283229)，[Danghui Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=050443)

## 中文标题

基于自适应 Token 波动预测的解耦预取以加速长上下文 LLM 解码

## 英文摘要

The prohibitively slow speed of long-context LLM decoding is a critical bottleneck, caused by massive Key-Value (KV) access that saturates memory bandwidth. Existing solutions fail due to a fundamental trade-off: static predictors cannot handle the Tokens Fluctuation, leading to permanent accuracy loss from irreversible eviction, while an on-the-fly scoring method creates a synchronous bottleneck that stalls the entire pipeline. This paper presents a co-designed system that breaks this trade-off by leveraging an Adaptive Prediction algorithm to enable a fully Decoupled Prefetching architecture. The proposed Adaptive Prediction model first mirrors the nature of Tokens Fluctuation, enabling a lightweight, reuse-based recovery mechanism that solves irreversible eviction. This high-fidelity prediction then unlocks the Decoupled Prefetching system, which completely hides data transfer latency and eliminates the synchronous bottleneck. On long-context LLM decoding tasks, the proposed system matches the accuracy of a full KV cache with just 256 tokens, while achieving an average 2.50x end-to-end speedup.

## 中文摘要

长上下文 LLM 解码速度极为缓慢，已成为关键瓶颈，其成因是海量的键值（KV）访问饱和了内存带宽。现有方案因一个根本性权衡而失效：静态预测器无法应对 Token 波动，不可逆的逐出因而造成永久性精度损失；而即时评分方法则形成同步瓶颈，使整条流水线停滞。本文提出一个协同设计的系统，利用自适应预测算法构建完全解耦的预取架构，从而打破该权衡。所提出的自适应预测模型首先刻画了 Token 波动的内在规律，从而实现轻量级、基于重用的恢复机制，解决了不可逆逐出问题；这种高保真预测进而支撑解耦预取系统，完全隐藏数据传输延迟并消除同步瓶颈。在长上下文 LLM 解码任务上，所提系统仅用 256 个 token 即达到完整 KV 缓存的精度，同时实现平均 2.50 倍的端到端加速。

## 英文关键词

Large language models, Decoding, KV Cache Compression, Memory management, Efficient Inference

## 中文关键词

大语言模型、解码、KV 缓存压缩、内存管理、高效推理
