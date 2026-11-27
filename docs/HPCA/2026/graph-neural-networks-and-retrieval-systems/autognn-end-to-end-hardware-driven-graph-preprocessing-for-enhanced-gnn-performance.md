---
title: "AutoGNN: End-to-End Hardware-Driven Graph Preprocessing for Enhanced GNN Performance"
description: "HPCA 2026 · Graph Neural Networks and Retrieval Systems"
tags:
  - "HPCA2026"
  - "Graph Neural Networks and Retrieval Systems"
---

# AutoGNN: End-to-End Hardware-Driven Graph Preprocessing for Enhanced GNN Performance

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: Graph Neural Networks and Retrieval Systems。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · Graph Neural Networks and Retrieval Systems</p>
</div>

**论文链接**：
**作者**：Seungkwan Kang KAIST , Seungjun Lee KAIST , Donghyun Gouk Panmnesia , Miryeong Kwon Panmnesia , Hyunkyu Choi Panmnesia , Junhyeok Jang Panmnesia , Sangwon Lee Panmnesia , Huiwon Choi KAIST , Jie Zhang Peking University , Wonil Choi Hanyang University , Mahmut Taylan Kandemir Pennsylvania State University , Myoungsoo Jung KAIST
**会议**：HPCA 2026

---

## 中文标题

AutoGNN：面向 GNN 性能提升的端到端硬件驱动图预处理

## 英文摘要

Graph neural network (GNN) inference faces significant bottlenecks in preprocessing, which often dominate overall inference latency. We introduce AutoGNN, an FPGA-based accelerator designed to address these challenges by leveraging FPGA’s reconfigurability and specialized components. AutoGNN adapts to diverse graph inputs, efficiently performing computationally intensive tasks such as graph conversion and sampling. By utilizing components like adder trees, AutoGNN executes reduction operations in constant time, overcoming the limitations of serialization and synchronization on GPUs. AutoGNN integrates unified processing elements (UPEs) and single-cycle reducers (SCRs) to streamline GNN preprocessing. UPEs enable scalable parallel processing for edge sorting and unique vertex selection, while SCRs efficiently handle sequential tasks such as pointer array construction and subgraph reindexing. A user-level software framework dynamically profiles graph inputs, determines optimal configurations, and reprograms AutoGNN to handle varying workloads. Implemented on a 7nm enterprise FPGA, AutoGNN achieves up to 9.0× and 2.1× speedup compared to conventional and GPU-accelerated preprocessing systems, respectively, enabling high-performance GNN preprocessing across diverse datasets.

## 中文摘要

图神经网络（GNN）推理在预处理阶段面临显著瓶颈，预处理往往主导整体推理时延。我们提出 AutoGNN，一个基于 FPGA 的加速器，利用 FPGA 的可重构性与专用部件来应对这些挑战。AutoGNN 可适配多样化的图输入，高效完成图转换与采样等计算密集型任务。借助加法树等部件，AutoGNN 以常数时间执行归约操作，克服了 GPU 上串行化与同步的限制。AutoGNN 集成统一处理单元（UPE）与单周期归约器（SCR）来简化 GNN 预处理。UPE 为边排序与唯一顶点选择提供可扩展的并行处理，SCR 则高效处理指针数组构建与子图重索引等顺序任务。用户级软件框架动态剖析图输入、确定最优配置并重新编程 AutoGNN 以应对不同负载。AutoGNN 实现在 7nm 企业级 FPGA 上，相比传统预处理系统与 GPU 加速的预处理系统分别取得最高 9.0 倍与 2.1 倍的加速比，可在多样数据集上实现高性能的 GNN 预处理。
