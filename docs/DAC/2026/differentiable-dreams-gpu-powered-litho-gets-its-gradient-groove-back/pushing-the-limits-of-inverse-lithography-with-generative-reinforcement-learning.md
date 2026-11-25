Pushing the Limits of Inverse Lithography with Generative Reinforcement Learning
Authors：
[Haoyu Yang](https://63dac.conference-program.com/?post_type=page&p=15&uid=857643)，[Haoxing Ren](https://63dac.conference-program.com/?post_type=page&p=15&uid=172643)

## 中文标题

以生成式强化学习推动反向光刻的极限

## 英文摘要

Inverse lithography (ILT) is critical for modern semiconductor manufacturing but suffers from highly non-convex objectives that often trap optimization in poor local minima. Generative AI has been explored to warm-start ILT, yet most approaches train deterministic image-to-image translators to mimic sub-optimal datasets, providing limited guidance for escaping non-convex traps during refinement. We reformulate mask synthesis as conditional sampling: a generator learns a distribution over masks conditioned on the design and proposes multiple candidates. The generator is first pretrained with WGAN plus a reconstruction loss, then fine-tuned using Group Relative Policy Optimization (GRPO) with an ILT-guided imitation loss. At inference, we sample a small batch of masks, run fast batched ILT refinement, evaluate lithography metrics (e.g., EPE, process window), and select the best candidate. On LithoBench dataset, the proposed hybrid framework reduces EPE violations under a 3 nm tolerance and roughly doubles throughput versus a strong numerical ILT baseline, while improving final mask quality. We also present over 20% EPE improvement on ICCAD13 contest cases with 3× speedup over the SOTA numerical ILT solver. By learning to propose ILT-friendly initializations, our approach mitigates non-convexity and advances beyond what traditional solvers or GenAI can achieve.

## 中文摘要

反向光刻（ILT）对现代半导体制造至关重要，但其高度非凸的目标常常使优化陷入较差的局部极小值。生成式 AI 已被探索用于为 ILT 提供热启动，然而多数方法训练确定性的图像到图像转换器来模仿次优数据集，在细化过程中对逃离非凸陷阱的引导作用有限。我们将掩模合成重新表述为条件采样：生成器学习以设计为条件的掩模分布，并提议多个候选。生成器首先使用 WGAN 加重建损失进行预训练，然后使用组相对策略优化（GRPO）结合 ILT 引导的模仿损失进行微调。在推理时，我们采样一小批掩模，运行快速的批量 ILT 细化，评估光刻指标（如 EPE、工艺窗口），并选出最佳候选。在 LithoBench 数据集上，所提出的混合框架在 3 nm 容差下减少了 EPE 违例，与强数值 ILT 基线相比吞吐量约翻倍，同时提升了最终掩模质量。我们还在 ICCAD13 竞赛案例上取得了超过 20% 的 EPE 改善，相比 SOTA 数值 ILT 求解器加速 3 倍。通过学习提议对 ILT 友好的初始化，我们的方法缓解了非凸性，并超越了传统求解器或生成式 AI 所能达到的水平。
