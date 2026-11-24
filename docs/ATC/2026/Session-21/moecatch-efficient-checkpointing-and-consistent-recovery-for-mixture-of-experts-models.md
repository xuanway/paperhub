# MoECatch: Efficient Checkpointing and Consistent Recovery for Mixture-of-Experts Models

**中文标题**：MoECatch：面向混合专家模型的高效检查点与一致性恢复

**所属 Session**：[Session 21: New: Verification and Recovery of AI Systems](index.md) · [ATC 2026](../index.md)

**作者**：Guorui Xu (Southeast University), Xiang Liu (Southeast University), Weiwei Wu (Southeast university, P. R. China), Keni Qiu (Capital Normal University), Guang Kou (Defense Innovation Institute), Chenchen Fu (Southeast University), Jianping Wang (City University of Hong Kong)

## 英文摘要
Checkpointing is essential for fault-tolerant large language model training, but it increasingly limits persistence frequency and recovery efficiency as training runs become longer and clusters become larger. This problem is especially acute in Mixture-of-Experts (MoE) systems, where checkpoint bytes are dominated by expert parameters and optimizer states. Conventional checkpointing persists all experts uniformly at every checkpoint, even though expert updates are highly uneven under skewed token routing. This mismatch wastes checkpointing bandwidth on persisting “barely changed experts”, limits attainable checkpoint frequency, and increases rollback cost after failures. To address this mismatch, we present MoECatch, a sparse checkpointing system for MoE training that treats sparse checkpointing as a coupled checkpoint-and-recovery problem. On the checkpoint path, Aging-then-Greedy Expert Selection (AGES) prioritizes which experts to persist under a fixed budget. On the recovery path, Version Catch-Up (VCU) reconstructs stale experts from mixed-version checkpoints while leaving already aligned state unchanged. MoECatch further accelerates recovery through minimum executable-state restoration and asynchronous optimizer staging. We implement MoECatch in the MindSpeed framework. The results show that MoECatch improves attainable checkpoint frequency by up to 2.5× and reduces end-to-end wasted time after failures by up to 22.86%. Across both pretraining and fine-tuning workloads, recovery preserves average downstream-task accuracy relative to full-checkpoint recovery. At the state level, the relative 𝐿2 parameter deviation between the recovered model and the same-iteration full checkpoint does not exceed 0.001%.

## 中文摘要
检查点对容错的大语言模型训练至关重要，但随着训练运行时间变长、集群规模变大，它日益限制持久化频率和恢复效率。这一问题在混合专家（MoE）系统中尤为突出，因为检查点字节主要由专家参数和优化器状态构成。传统检查点在每个检查点都统一持久化所有专家，尽管在倾斜的 token 路由下专家更新极不均衡。这种错配把检查点带宽浪费在持久化“几乎未变的专家”上，限制了可达到的检查点频率，并增加了故障后的回滚成本。为解决这一错配，我们提出 MoECatch，一个面向 MoE 训练的稀疏检查点系统，它将稀疏检查点视为检查点与恢复相互耦合的问题。在检查点路径上，老化后贪心专家选择（AGES）在固定预算下决定优先持久化哪些专家。在恢复路径上，版本追赶（VCU）从混合版本的检查点重建陈旧专家，同时保持已对齐的状态不变。MoECatch 进一步通过最小可执行状态恢复和异步优化器分级来加速恢复。我们在 MindSpeed 框架中实现了 MoECatch。结果表明，MoECatch 将可达到的检查点频率最高提升 2.5×，并将故障后的端到端浪费时间最多减少 22.86%。在预训练和微调负载上，相对于全量检查点恢复，恢复过程仍保持了平均下游任务精度。在状态层面，恢复得到的模型与同一迭代的全量检查点之间的参数相对 L2 偏差不超过 0.001%。

## 英文关键词
Mixture-of-experts, checkpointing, failure recovery

## 中文关键词
混合专家，检查点，故障恢复

[返回 Session 21](index.md) · [返回 ATC 2026](../index.md)
