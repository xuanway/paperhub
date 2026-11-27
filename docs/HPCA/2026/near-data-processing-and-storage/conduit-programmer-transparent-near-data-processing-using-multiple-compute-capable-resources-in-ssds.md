---
title: "Conduit: Programmer-Transparent Near-Data Processing Using Multiple Compute-Capable Resources in SSDs"
description: "HPCA 2026 · Near-Data Processing and Storage"
tags:
  - "HPCA2026"
  - "Near-Data Processing and Storage"
---

# Conduit: Programmer-Transparent Near-Data Processing Using Multiple Compute-Capable Resources in SSDs

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: Near-Data Processing and Storage。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · Near-Data Processing and Storage</p>
</div>

**论文链接**：
**作者**：Rakesh Nadig ETH Zurich , Vamanan Arulchelvan ETH Zurich , Mayank Kabra ETH Zurich , Harshita Gupta ETH Zurich , Rahul Bera ETH Zurich , Nika Mansouri Ghiasi ETH Zurich , Nanditha Rao ETH Zurich , Qingcai Jiang ETH Zurich , Andreas Kosmas Kakolyris ETH Zurich , Yu Liang ETH Zurich , Mohammad Sadrosadati ETH Zürich , Onur Mutlu ETH Zurich
**会议**：HPCA 2026

---

## 中文标题

Conduit：利用 SSD 中多种可计算资源实现编程透明的近数据处理

## 英文摘要

Near-data processing (NDP) mitigates the data movement bottleneck in modern computing systems by performing computation close to where the data resides. Solid-state drives (SSDs) are well suited for NDP because they: (1) store large application datasets that exceed main memory capacity, and (2) contain multiple heterogeneous computation resources, e.g., general-purpose embedded cores in the SSD controller, DRAM chips, and NAND flash chips, which enable three NDP paradigms: in-storage processing (ISP), processing using DRAM in the SSD (PuD-SSD), and in-flash processing (IFP). These resources offer massive internal parallelism and enable in-place computation, which reduces data movement across the memory hierarchy. A large body of prior SSD-based NDP techniques operate in isolation, mapping computations to only one or two NDP paradigms (i.e., ISP, PuD-SSD, or IFP) within the SSD. These techniques (1) are tailored to specific workloads or kernels, (2) do not offload computations across all three NDP paradigms in the SSD and thus fail to exploit the full computational potential of an SSD, and (3) lack programmer-transparency, often requiring significant manual effort to identify offloadable code regions and map them to the SSD computation resources, which limits their general applicability and ease of deployment. While several prior works propose techniques to partition computation between the host and near-memory accelerators, adapting these techniques to SSDs offers limited benefits because they (1) ignore the heterogeneity of the SSD computation resources, and (2) make offloading decisions based on limited factors such as bandwidth utilization, data movement cost, or memory intensity, while ignoring key factors such as resource utilization. We propose Conduit, a general-purpose, programmer-transparent NDP framework for SSDs that accelerates a broad range of workloads by leveraging available SSD computation resources. Conduit operates in two stages. At compile time, Conduit executes a custom compiler (e.g., LLVM) pass that (i) vectorizes suitable application code segments into single-instruction multiple-data (SIMD) operations that align with the SSD’s page layout, and (ii) embeds metadata (e.g., operation type, operand sizes) into the vectorized instructions to guide runtime offloading decisions. At runtime, within the SSD, Conduit performs instruction-granularity offloading by evaluating six key application and system features (e.g., operation type, computation resource utilization, data dependence delay), and uses a cost function to select the most suitable SSD computation resource to execute each vectorized instruction. We evaluate Conduit and two prior NDP offloading techniques using an in-house event-driven SSD simulator on six data-intensive applications (e.g., large language model inference and training, encryption). Conduit outperforms the best-performing prior offloading policy by 1.8× and reduces energy consumption by 46%, with small latency and storage overheads, and no additional hardware cost.

## 中文摘要

近数据处理（NDP）在数据所在处执行计算，缓解现代计算系统的数据搬运瓶颈。固态硬盘（SSD）适合 NDP，因为它（1）存储超出主存容量的大型应用数据集，（2）包含多种异构计算资源，如 SSD 控制器中的通用嵌入式核、DRAM 芯片与 NAND 闪存芯片，可支持三种 NDP 范式：存内处理（ISP）、利用 SSD 内 DRAM 的处理（PuD-SSD）与闪存内处理（IFP）。这些资源提供巨大的内部并行性并支持原位计算，减少跨存储层次的数据搬运。已有基于 SSD 的 NDP 技术多彼此孤立，只将计算映射到一两种范式；它们针对特定负载或内核定制，未在三种范式间卸载计算，无法发挥 SSD 的全部计算潜力，且缺乏编程透明性，常需大量人工识别可卸载代码区域。为此我们提出 Conduit，一个通用、编程透明的 SSD NDP 框架。编译期，Conduit 执行自定义编译（如 LLVM）pass，将合适的代码段向量化为与 SSD 页布局对齐的 SIMD 操作，并把操作类型、操作数大小等元数据嵌入向量化指令；运行期在 SSD 内以指令粒度卸载，评估操作类型、资源利用率、数据依赖延迟等六项特征，并用代价函数为每条向量化指令选择最合适的计算资源。我们在自研事件驱动 SSD 模拟器上，针对大语言模型推理与训练、加密等六个数据密集型应用进行评估。相比最佳已有卸载策略，Conduit 性能提升 1.8 倍、能耗降低 46%，时延与存储开销很小，且无额外硬件成本。
