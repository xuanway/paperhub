---
title: "TAO: Tolerance-Aware Optimistic Verification for Floating-Point Neural Networks"
description: "EuroSys 2026 · AI · Jianzhu Yao (Princeton University), Hongxu Su (The Hong Kong University of Scien"
tags:
  - "EuroSys2026"
  - "AI"
---

# TAO: Tolerance-Aware Optimistic Verification for Floating-Point Neural Networks

**中文标题：** TAO：面向浮点神经网络的可容忍度感知乐观验证

**所属 Session：** [Session 5.1: AI](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：AI。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · AI</p>
</div>

**作者**：Jianzhu Yao (Princeton University), Hongxu Su (The Hong Kong University of Science and Technology (Guangzhou)), Taobo Liao (University of Illinois Urbana-Champaign), Zerui Cheng (Princeton University), Huan Zhang (University of Illinois Urbana-Champaign), Xuechao Wang (The Hong Kong University of Science and Technology (Guangzhou)), Pramod Viswanath (Princeton University)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3803612)

## 英文摘要

Neural networks increasingly run on hardware outside the user’s control (cloud GPUs, inference marketplaces, edge specialized accelerators) for both training and inference. Yet ML-as-a-Service reveals little about what actually ran or whether returned outputs faithfully reflect the intended inputs and models. Users lack recourse against service downgrades such as model swaps, quantization, graph rewrites, or discrepancies like altered advertisement embeddings. Verifying outputs is especially difficult because floating-point execution on heterogeneous accelerators is inherently nondeterministic. Existing approaches like zkML, deterministic replay, TEEs, and replication are either impractical for real floating-point neural networks or reintroduce the need to trust the vendor. We present TAO: a Tolerance-Aware Optimistic verification protocol for floating-point neural networks that accepts outputs within principled operator-level acceptance regions rather than requiring bitwise equality. TAO combines two complementary error models: (i) sound per-operator IEEE-754 worst-case bounds and (ii) tight empirical percentile profiles calibrated across hardware types. Discrepancies are resolved via a Merkle-anchored, threshold-guided interactive dispute game that recursively partitions the traced computation graph until one operator remains; at the leaf, adjudication reduces to either a lightweight theoretical-bound check or a small honest-majority vote against empirical thresholds. Unchallenged results finalize after a challenge window, without requiring trusted hardware or deterministic kernels.

We implement TAO as a PyTorch-compatible runtime and a coordinator contract layer; in our prototype, the coordinator is instantiated as an Ethereum smart-contract deployment (Holesky testnet) to quantify coordination cost. The runtime instruments graphs, computes bounds for each operator in real time, and runs unmodified vendor kernels in FP32 with negligible overhead (0.3% additional latency on Qwen3-8B). Our evaluation spans CNNs, Transformers, LLMs, and diffusion models across multiple GPUs (A100, H100, RTX 6000, RTX 4090). Results show that empirical thresholds are 102–103× tighter than theoretical bounds, and bound-aware adversarial attacks achieve 0% success under empirical checks. Together, TAO reconciles scalability with verifiability for real-world heterogeneous ML compute.

## 中文摘要

神经网络越来越多地在用户无法控制的硬件上（云 GPU、推理市场、边缘专用加速器）同时进行训练和推理。然而，机器学习即服务几乎不披露实际运行了什么，也不披露返回的输出是否忠实反映了预期的输入与模型。面对模型替换、量化、图重写等服务降级行为，或广告嵌入被篡改之类的偏差，用户缺乏追责手段。验证输出尤为困难，因为异构加速器上的浮点执行本质上是非确定性的。zkML、确定性重放、TEE 和复制等现有方法，要么对真实的浮点神经网络不可行，要么重新引入了对厂商的信任需求。我们提出 TAO：一种面向浮点神经网络的可容忍度感知乐观验证协议，它接受落在有理论依据的算子级可接受区域内的输出，而不要求逐位相等。TAO 结合了两种互补的误差模型：(i) 可靠的逐算子 IEEE-754 最坏情况边界，以及 (ii) 跨硬件类型校准的紧致经验百分位轮廓。对于分歧，通过一个以 Merkle 锚定、以阈值为引导的交互式争议博弈来解决，该博弈递归地划分被追踪的计算图，直到只剩下一个算子；在叶节点处，裁决归结为轻量级的理论边界检查，或针对经验阈值的小规模诚实多数投票。未被质疑的结果在质疑窗口结束后即可最终确认，无需可信硬件或确定性内核。

我们以 PyTorch 兼容的运行时和协调者合约层实现 TAO；在原型中，协调者被实例化为以太坊智能合约部署（Holesky 测试网），以量化协调开销。该运行时对计算图进行插桩，实时计算每个算子的边界，并以 FP32 运行未经修改的厂商内核，开销可忽略（在 Qwen3-8B 上额外时延为 0.3%）。我们的评估覆盖 CNN、Transformer、LLM 和扩散模型，跨多种 GPU（A100、H100、RTX 6000、RTX 4090）。结果表明，经验阈值比理论边界紧 10²–10³ 倍，且边界感知的对抗攻击在经验检查下的成功率为 0%。综上，TAO 为真实的异构机器学习计算兼顾了可扩展性与可验证性。

**英文关键词：** verifiable computation, floating-point nondeterminism, neural networks, optimistic verification

**中文关键词：** 可验证计算、浮点非确定性、神经网络、乐观验证

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
