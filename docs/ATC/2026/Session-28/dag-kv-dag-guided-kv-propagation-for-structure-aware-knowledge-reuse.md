# DAG-KV: DAG-Guided KV Propagation for Structure-Aware Knowledge Reuse

**中文标题**：DAG-KV：DAG 引导的 KV 传播实现结构感知的知识复用

**所属 Session**：[Session 28: LLM Inference IV](index.md) · [ATC 2026](../index.md)

**作者**：Wenbin Zhu (Shandong University), Zhaoyan Shen (Shandong University), Qian Wei (Shandong University), Shujian Zhao (Shandong University), Xin YAO (Huawei Technologies Co., Ltd), Xi Peng (Huawei Technologies Co., Ltd), Wei Zhang (Huawei Technologies Co., Ltd), Renhai Chen (Huawei Technologies Co., Ltd), Gong Zhang (Huawei Technologies Co., Ltd), Hongjun Dai (Shandong University), Dongxiao Yu (Shandong University)

## 英文摘要
Knowledge-augmented LLM serving systems often repeatedly encode retrieved external knowledge, increasing time-to-first-token (TTFT) and wasting computation across requests. Existing reuse-oriented systems reduce this overhead by caching context-derived states, but adapting these states to new queries requires additional recomputation or latent-state routing. Recent knowledge-unit-level reuse methods store fine-grained knowledge units as independently reusable KV tokens, but treat related units as isolated memory items, weakening the dependencies needed for multi-hop reasoning. DAG-KV addresses this limitation by decoupling reusable knowledge content from query-specific knowledge structure. It stores each knowledge unit as an independently reusable KV token, while recovering a compact query-specific DAG over selected tokens at serving time. This DAG guides lightweight attention propagation among KV tokens, allowing related knowledge units to interact along structured reasoning paths without being serialized into the prompt or re-encoded as a joint context. We implement DAG-KV as an end-to-end prototype by adding a localized attention-level propagation step over selected KV tokens in decoder-only LLMs. Across six knowledge-intensive QA datasets, DAG-KV improves the average LLM-Judge score of independent KV-token reuse from 0.36 to 0.55 under Qwen3-4B-Instruct, and approaches the evaluated graph-retrieval RAG baseline with Qwen3-14B-Instruct, while achieving a 9.6× average TTFT speedup over evaluated latent-memory reuse baseline under our single-request evaluation.

## 中文摘要
知识增强的 LLM 服务系统常常反复编码检索到的外部知识，增加首 token 时延（TTFT）并跨请求浪费计算。现有的面向复用的系统通过缓存由上下文派生的状态来降低这一开销，但将这些状态适配到新查询需要额外的重计算或隐状态路由。近期的知识单元级复用方法将细粒度知识单元存储为可独立复用的 KV token，却将相关单元视为孤立的内存项，削弱了多跳推理所需的依赖关系。DAG-KV 通过将可复用的知识内容与查询特定的知识结构解耦来应对这一局限。它将每个知识单元存储为可独立复用的 KV token，同时在服务时针对选中的 token 恢复出一个紧凑的、查询特定的 DAG。该 DAG 引导 KV token 之间轻量级的注意力传播，使相关知识单元能够沿结构化的推理路径交互，而无需被序列化进提示或作为联合上下文重新编码。我们通过在仅解码器 LLM 中对选中的 KV token 增加一个局部化的注意力层传播步骤，将 DAG-KV 实现为端到端原型。在六个知识密集型问答数据集上，DAG-KV 在 Qwen3-4B-Instruct 下将独立 KV-token 复用的平均 LLM-Judge 分数从 0.36 提升到 0.55，并在 Qwen3-14B-Instruct 下接近所评估的图检索 RAG 基线，同时在我们的单请求评估下相比所评估的隐记忆复用基线实现 9.6× 的平均 TTFT 加速。

## 英文关键词
Large language model serving, knowledge reuse, KV caching, retrieval-augmented generation, knowledge graphs, attention propagation

## 中文关键词
大语言模型服务，知识复用，KV 缓存，检索增强生成，知识图谱，注意力传播

[返回 Session 28](index.md) · [返回 ATC 2026](../index.md)
