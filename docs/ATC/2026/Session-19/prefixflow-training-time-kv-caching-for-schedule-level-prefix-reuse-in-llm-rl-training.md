# PrefixFlow: Training-Time KV Caching for Schedule-Level Prefix Reuse in LLM RL Training

**中文标题**：PrefixFlow：面向 LLM 强化学习训练中调度级前缀复用的训练期 KV 缓存

**所属 Session**：[Session 19: Model Training](index.md) · [ATC 2026](../index.md)

**作者**：Pengbo Li (Hong Kong University of Science and Technology), Feiyuan Zhang (Hong Kong University of Science and Technology), Guangming Sheng (Tencent), Guangxin He (Hong Kong University of Science and Technology), Di Chai (Shanghai University of Finance and Economics), Ziniu Li (Tencent), Taiqiang Wu (The University of Hong Kong), Han Tian (Hong Kong University of Science and Technology), Wenyu Mao (Tencent), Binhang Yuan (Hong Kong University of Science and Technology), Kai Chen (Hong Kong University of Science and Technology)

## 英文摘要
In reinforcement learning (RL) post-training, one prompt fans out into 𝑁trajectories, yet standard trainers replay the shared prefix’s forward and backward pass 𝑁times; in long-context retrieval-augmented generation (RAG) and multimodal workloads, this repetition dominates training compute. Existing designs reuse the prefix within one computation graph (a packed sequence, fused kernel, or tree traversal); under the trainer’s memory limits and parallelism, their compute savings do not reliably become shorter steps. We present PrefixFlow, which takes the prefix out of that graph and into the training schedule through a training-time KV cache: Phase A runs one prefix forward and caches its keys and values (𝐾/𝑉); Phase B trains suffixes as ordinary microbatches that read only 𝐾/𝑉and write back only their gradients (𝑔𝐾/𝑔𝑉); Phase C runs one delayed prefix backward on the accumulated 𝑔𝐾/𝑔𝑉. Memory and parallelism then become manageable: dormant prefix activations are offloaded during Phase B to free high-bandwidth memory (HBM) for suffixes, and context, pipeline, and data parallelism each schedule the phases through a local rule while tensor and expert parallelism need no change, so saved compute becomes shorter steps under any microbatch split. On dense models, and on mixture-of-experts (MoE) models under Rollout Routing Replay, PrefixFlow matches full-sequence training within bfloat16 (BF16) tolerance. Against an identically configured baseline, it speeds up end-to-end verl RL training on a long-prefix RAG workload by 1.90× (6.1× on the actor update). In controlled sweeps, actor-side speedup grows with prefix ratio and group size, reaching 4.4× at an 83% prefix ratio, while suffix-dominated splits gain little; offloading dormant prefix activations lowers Phase-B peak HBM by up to 59% and extends trainable sequences by 1.66×.

## 中文摘要
在强化学习（RL）后训练中，一个 prompt 会展开为 N 条轨迹，而标准训练器会把共享前缀的前向与反向传播重复重放 N 次；在长上下文检索增强生成（RAG）和多模态负载中，这种重复占据了训练计算的主要部分。现有设计在单个计算图内复用前缀（打包序列、融合内核或树遍历）；在训练器的内存限制与并行方式下，其计算节省并不能可靠地转化为更短的步长。我们提出 PrefixFlow，它通过训练期 KV 缓存把前缀移出该计算图、纳入训练调度：阶段 A 执行一次前缀前向并缓存其键和值（K/V）；阶段 B 将后缀作为普通微批次训练，只读取 K/V 并只回写其梯度（gK/gV）；阶段 C 对累积的 gK/gV 执行一次延迟的前缀反向。于是内存与并行变得可控：在阶段 B 期间将休眠的前缀激活卸载，以释放高带宽内存（HBM）供后缀使用；上下文并行、流水线并行和数据并行各自通过局部规则调度各阶段，而张量并行与专家并行无需改动，因此在任何微批次切分下，节省的计算都能转化为更短的步长。在稠密模型上，以及在 Rollout Routing Replay 下的混合专家（MoE）模型上，PrefixFlow 在 bfloat16（BF16）容差范围内与全序列训练一致。相对于配置相同的基线，它在长前缀 RAG 负载上将端到端 verl RL 训练加速 1.90×（actor 更新部分为 6.1×）。在受控扫描中，actor 侧加速随前缀比例和组大小增长，在前缀比例为 83% 时达到 4.4×，而以后缀为主的切分收益很小；卸载休眠的前缀激活使阶段 B 的峰值 HBM 降低多达 59%，并将可训练序列长度延长 1.66×。

## 英文关键词
large language models, reinforcement learning, prefix reuse, KV caching

## 中文关键词
大语言模型，强化学习，前缀复用，KV 缓存

[返回 Session 19](index.md) · [返回 ATC 2026](../index.md)
