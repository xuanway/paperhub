---
title: "Maya: Optimizing Deep Learning Training Workloads using GPU Runtime Emulation"
description: "EuroSys 2026 · GPU Systems, Graph Computing & Applied ML · Srihas Yarlagadda (Georgia Institute of Technology), Amey Agrawal (Georgia Insti"
tags:
  - "EuroSys2026"
  - "GPU Systems, Graph Computing & Applied ML"
---

# Maya: Optimizing Deep Learning Training Workloads using GPU Runtime Emulation

**中文标题：** Maya：利用 GPU 运行时模拟优化深度学习训练负载

**所属 Session：** [Session 12.3: GPU Systems, Graph Computing & Applied ML](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：GPU Systems, Graph Computing & Applied ML。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · GPU Systems, Graph Computing & Applied ML</p>
</div>

**作者**：Srihas Yarlagadda (Georgia Institute of Technology), Amey Agrawal (Georgia Institute of Technology), Elton Pinto (Georgia Institute of Technology), Hakesh Darapaneni (Georgia Institute of Technology), Mitali Meratwal (Georgia Institute of Technology), Shivam Mittal (Georgia Institute of Technology), Pranavi Bajjuri (Georgia Institute of Technology), Srinivas Sridharan (Nvidia Inc.), Alexey Tumanov (Georgia Institute of Technology)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3769366)

## 英文摘要

Training large foundation models costs hundreds of millions of dollars, making deployment optimization critical. Current approaches require machine learning engineers to manually craft training recipes through error-prone trial-and-error on expensive compute clusters. To enable efficient exploration of training configurations, researchers have developed performance modeling systems. However, these systems force users to translate their workloads into custom specification languages, introducing a fundamental semantic gap between the actual workload and its representation. This gap creates an inherent tradeoff: systems must either support a narrow set of workloads to maintain usability, require complex specifications that limit practical adoption, or compromise prediction accuracy with simplified performance models.

We present Maya, a performance modeling system that eliminates these tradeoffs through transparent device emulation. By operating at the narrow interface between training frameworks and accelerator devices, Maya can capture complete workload behavior without requiring code modifications or translations. Maya intercepts device API calls from unmodified training code to directly observe low-level operations, enabling accurate performance prediction while maintaining both ease of use and generality. Our evaluation shows Maya achieves less than 5% prediction error across diverse models and optimization strategies, identifying configurations that reduce training costs by up to 56% compared to existing approaches.

## 中文摘要

训练大型基础模型的成本高达数亿美元，因此部署优化至关重要。当前方法需要机器学习工程师在昂贵的计算集群上通过易错的反复试错来手工制定训练方案。为支持高效探索训练配置，研究者开发了性能建模系统。然而，这些系统迫使用户将负载翻译为定制的描述语言，从而在实际负载与其表示之间引入根本性的语义鸿沟。这一鸿沟造成固有的权衡：系统要么只支持少量负载以保持易用性，要么要求复杂的描述从而限制实际采用，要么以简化的性能模型牺牲预测精度。

我们提出 Maya，一个通过透明设备模拟消除上述权衡的性能建模系统。Maya 作用于训练框架与加速器设备之间的狭窄接口，因而无需修改或翻译代码即可捕获完整的负载行为。Maya 拦截来自未修改训练代码的设备 API 调用，直接观测底层操作，从而在保持易用性与通用性的同时实现准确的性能预测。我们的评估表明，Maya 在多种模型与优化策略上的预测误差低于 5%，并能识别出相较现有方法最多降低 56% 训练成本的配置。

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
