# BMV: Breaking Monolithic Verification for Fast Speculative LLM Inference

**中文标题**：BMV：打破单体式验证以实现快速的投机 LLM 推理

**所属 Session**：[Session 21: New: Verification and Recovery of AI Systems](index.md) · [ATC 2026](../index.md)

**作者**：Dongxu Liu (Huazhong University of Science and Technology), Bing Zhu (Huazhong University of Science and Technology), Xinyu Zhu (Huazhong University of Science and Technology), Long Zheng (Huazhong University of Science and Technology), Xiaofei Liao (Huazhong University of Science and Technology), Hai Jin (Huazhong University of Science and Technology), Jingling Xue (UNSW Sydney)

## 英文摘要
Speculative decoding accelerates autoregressive generation by drafting and verifying multiple tokens in bulk. However, in many existing systems, verification remains monolithic: the candidate tree is processed through all transformer layers and projected over the full vocabulary before acceptance is resolved. This all-or-nothing design wastes verifier work on rejected branches, materializes transient KV state for discarded candidates, and creates pipeline imbalance. We present BMV, a serving system that breaks monolithic verification into staged verifier admission and exact final verification. The key insight is that intermediate target-model states provide evidence for pruning low-confidence branches before full-depth execution. BMV inserts a lightweight pruning stage between drafting and final verification: it performs prefix-guided pruning, preserves reusable KV state for surviving candidates through token-level prefix sharing, and coordinates the stages through a feedback-controlled asynchronous runtime. Final acceptance remains deferred to the exact verifier; pruning affects only speculation opportunities, not committed-token semantics. Across three LLMs (8B–70B) and diverse workloads, BMV achieves up to 5.80× speedup over autoregressive decoding and 1.31× over EAGLE-3 on a single H200 GPU, and improves pipeline throughput by 1.93× on 5×V100. A cost breakdown shows that auxiliary pruning logic adds less than 1% overhead, while verifier-side KV footprint is reduced by 30.9%. With a false negative rate of at most 2.61%, BMV demonstrates that staged verification is practical for scaling speculative LLM serving. The source code of BMV will be released at https://github.com/CGCL-codes/BMV.

## 中文摘要
投机解码通过批量起草并验证多个 token 来加速自回归生成。然而在许多现有系统中，验证仍是单体式的：候选树要先经过所有 transformer 层并在整个词表上投影，之后才确定接受结果。这种全有或全无的设计把验证器的工作浪费在被拒绝的分支上，为被丢弃的候选生成瞬态 KV 状态，并造成流水线不均衡。我们提出 BMV，一个将单体式验证拆分为分阶段验证器准入与精确最终验证的服务系统。其核心洞见是：目标模型的中间状态提供了证据，可在全深度执行之前剪除低置信度的分支。BMV 在起草与最终验证之间插入一个轻量级剪枝阶段：它执行前缀引导的剪枝，通过 token 级前缀共享为存活的候选保留可复用的 KV 状态，并通过反馈控制的异步运行时协调各阶段。最终接受仍交由精确验证器决定；剪枝只影响投机机会，不影响已提交 token 的语义。在三种 LLM（8B–70B）和多样负载上，BMV 在单块 H200 GPU 上相对自回归解码最高取得 5.80× 加速，相对 EAGLE-3 取得 1.31× 加速，并在 5×V100 上将流水线吞吐提升 1.93×。成本分解显示，辅助剪枝逻辑带来的开销低于 1%，而验证器侧的 KV 占用减少 30.9%。在漏判率（false negative rate）至多 2.61% 的情况下，BMV 证明分阶段验证对于扩展投机式 LLM 服务是切实可行的。BMV 的源代码将在 https://github.com/CGCL-codes/BMV 发布。

## 英文关键词
speculative decoding, large language model serving, staged verifier admission, state sharing, pipeline scheduling

## 中文关键词
投机解码，大语言模型服务，分阶段验证器准入，状态共享，流水线调度

## 代码与研究制品

- [项目仓库（代码待发布）](https://github.com/CGCL-codes/BMV)

[返回 Session 21](index.md) · [返回 ATC 2026](../index.md)
