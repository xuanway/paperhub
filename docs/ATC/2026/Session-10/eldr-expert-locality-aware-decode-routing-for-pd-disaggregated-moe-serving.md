# ELDR: Expert-Locality-Aware Decode Routing for PD-Disaggregated MoE Serving

**中文标题**：ELDR：面向 PD 分离式 MoE 服务的专家局部性感知解码路由

**所属 Session**：[Session 10: LLM Inference II](index.md) · [ATC 2026](../index.md)

**作者**：Sangjin Choi (KAIST), Sukmin Cho (KAIST), Yifan Xiong (Microsoft Research), Ziyue Yang (Shanghai Xingyunzhili Artificial Intelligence Institute), Youngjin Kwon (KAIST), Peng Cheng (Microsoft Research)

## 英文摘要
Equal load does not mean equal decode latency in prefill– decode (PD) disaggregated mixture-of-experts (MoE) serving. In bandwidth-bound decode, more distinct experts mean more weight loads and higher latency. We present ELDR, a lossless, expert-locality-aware decode router. Prefill signatures predict decode expert usage. Balanced 𝐾-means fits per-decoder centroids with background refitting. Locality-band routing selects the least-loaded worker among close matches. A block-granular cache keeps signatures exact under prefix caching. We evaluate ELDR in vLLM on up to 40 GPUs. Across three MoE models on 12 public task benchmarks and multilingual WildChat, it reduces median time-per-output-token (TPOT) by 5.4–14.5% on average across request rates and up to 17.8% over the best of four load-balancing baselines, preserving model outputs and token-to-expert assignments.

## 中文摘要
在预填充–解码（PD）分离的专家混合（MoE）服务中，负载相等并不意味着解码延迟相等。在带宽受限的解码中，不同的专家越多，意味着权重加载越多、延迟越高。我们提出 ELDR，一种无损的、专家局部性感知的解码路由器。预填充签名预测解码阶段的专家使用情况。均衡 K-means 为每个解码器拟合质心并在后台重新拟合。局部性带（locality-band）路由在接近匹配的候选中选择负载最低的工作节点。块粒度的缓存使签名在前缀缓存下保持精确。我们在 vLLM 中于最多 40 块 GPU 上评估 ELDR。在三款 MoE 模型、12 个公开任务基准和多语言 WildChat 上，它在各请求速率下平均将输出每 token 时间（TPOT）的中位数降低 5.4–14.5%，相比四个负载均衡基线中最好的一个降低最多 17.8%，同时保持模型输出和 token 到专家的分配不变。

## 英文关键词
MoE serving, PD disaggregation, expert locality

## 中文关键词
MoE 服务，PD 分离，专家局部性

[返回 Session 10](index.md) · [返回 ATC 2026](../index.md)
