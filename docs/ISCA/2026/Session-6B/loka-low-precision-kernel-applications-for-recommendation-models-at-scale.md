---
title: "LoKA: Low-precision Kernel Applications for Recommendation Models At Scale"
description: "ISCA 2026 · Session 6B · LoKA: Low-precision Kernel Applications for Recommendation Models At Scale"
tags:
  - "ISCA2026"
  - "Session 6B"
  - "Deep Learning / Memory Acceleration"
---

# LoKA: Low-precision Kernel Applications for Recommendation Models At Scale

**中文标题：** LoKA: 面向大规模推荐模型的低精度内核应用

**所属 Session：** [Session 6B](index.md) · [ISCA 2026](../index.md)

**作者：** Liang Luo, Yinbin Ma, Quanyu Zhu, Vasiliy Kuznetsov, Yuxin Chen, Jian Jiao, Jiecao Yu, Buyun Zhang, Tongyi Tang, Xiaohan Wei, Yanli Zhao, Zeliang Chen, Yuchen Hao, Venkatesh Ranganathan, Sandeep Parab, Yantao Yao, Maxim Naumov, Chunzhi Yang, Shen Li, Ellie Wen, Wenlin Chen, Chunqiang Tang

**来源：** ISCA 2026 · [官方日程](https://www.iscaconf.org/isca2026/program/)

## 英文摘要

Recent GPU generations deliver significantly higher FLOPs using lower-precision arithmetic, such as FP8. While successfully applied to large language models (LLMs), its adoption in large recommendation models (LRMs) has been limited. This is because LRMs are numerically sensitive, dominated by small matrix multiplications (GEMMs) followed by normalization, and trained in communication-intensive environments. Applying FP8 directly to LRMs often degrades model quality and prolongs training time. These challenges are inherent to LRM workloads and cannot be resolved merely by introducing better FP8 kernels. Instead, a system-model co-design approach is needed to successfully integrate FP8. We present LoKA (Low-precision Kernel Applications), a framework that makes FP8 practical for LRMs through three principles: profile under realistic distributions to know where low precision is safe, co-design model components with hardware to expand where it is safe, and orchestrate across kernel libraries to maximize the gains. Concretely, LoKA Probe is a statistically grounded, online benchmarking method that learns activation and weight statistics, and quantifies per-layer errors. This process pinpoints safe and unsafe, fast and slow sites for FP8 adoption. LoKA Mods is a set of reusable model adaptations that improve both numerical stability and execution efficiency with FP8. LoKA Dispatch is a runtime that leverages the statistical insights from LoKA Probe to select the fastest FP8 kernel that satisfies the accuracy requirements. Deployed on production LRMs that serve billions of users with advertising recommendations at a major social media company, LoKA delivers up to 20% higher training throughput and 40% faster inference on heterogeneous GPUs (H100, B200, GB200, MI300X and MI350X) in production environment, with no quality loss, turning FP8 from a model-quality risk into a reliable performance lever for LRMs at scale.

## 中文摘要

近几代 GPU 使用如 FP8 等低精度算术提供显著更高的 FLOPs。虽然已成功应用于大语言模型（LLM），其在大规模推荐模型（LRM）中的应用仍然有限。这是因为 LRM 对数值敏感、以小矩阵乘法（GEMM）及随后的归一化为主，并且在通信密集的环境中训练。将 FP8 直接应用于 LRM 常常降低模型质量并延长训练时间。这些挑战是 LRM 工作负载固有的，仅靠引入更好的 FP8 内核无法解决。相反，需要系统与模型协同设计的方法才能成功集成 FP8。我们提出 LoKA（Low-precision Kernel Applications），一个通过三项原则使 FP8 对 LRM 切实可用的框架：在真实分布下进行剖析以了解低精度在何处安全，与硬件协同设计模型组件以扩大安全范围，并在内核库之间进行编排以最大化收益。具体而言，LoKA Probe 是一种基于统计的在线基准测试方法，学习激活值与权重统计量，并量化逐层误差，该过程可精确指出适合与不适合采用 FP8 的位置以及快慢位置。LoKA Mods 是一组可复用的模型适配，使用 FP8 同时提升数值稳定性和执行效率。LoKA Dispatch 是一个运行时，利用 LoKA Probe 的统计洞见来选择满足精度要求的最快 FP8 内核。LoKA 部署在某大型社交媒体公司为数十亿用户提供广告推荐服务的生产 LRM 上，在生产环境的异构 GPU（H100、B200、GB200、MI300X 和 MI350X）上实现最高 20% 的训练吞吐提升和 40% 的推理加速，且无质量损失，使 FP8 从模型质量风险转变为大规模 LRM 的可靠性能杠杆。


## 相关链接

- [ISCA 2026 Main Program](https://www.iscaconf.org/isca2026/program/)

[返回 Session 6B](index.md) · [返回 ISCA 2026](../index.md)
