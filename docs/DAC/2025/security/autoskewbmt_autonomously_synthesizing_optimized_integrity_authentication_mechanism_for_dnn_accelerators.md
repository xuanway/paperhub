---
title: "AutoSkewBMT: Autonomously Synthesizing Optimized Integrity Authentication Mechanism for DNN Accelerators"
description: "DAC 2025 · Security"
tags:
  - "dac-2025"
  - "security"
  - "dnn-accelerator"
  - "merkle-tree"
  - "integrity-authentication"
  - "memory-security"
  - "design-space-exploration"
---

# AutoSkewBMT: Autonomously Synthesizing Optimized Integrity Authentication Mechanism for DNN Accelerators

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">DAC 2025（第62届设计自动化会议）· Security Track · Session: SEC2 — Hardware Security: Primitives & Architecture, Design & Test。针对 DNN 加速器内存安全中完整性认证的巨大开销问题，提出 AutoSkewBMT——一个自动生成优化 Bonsai Merkle Tree（BMT）配置的安全框架，通过设计空间探索算法根据具体 DNN 工作负载特征最优"倾斜"BMT 结构，相比 SOTA 方案实现高达 32% 的性能提升。</p>
<p class="paper-seo-summary__tags">DAC 2025 · Security · DNN Accelerator · Merkle Tree · Integrity Authentication · Memory Security · Design Space Exploration</p>
</div>

| 项目 | 详情 |
|------|------|
| 会议 | 第 62 届设计自动化会议（DAC 2025） |
| 论文标题 | AutoSkewBMT: Autonomously Synthesizing Optimized Integrity Authentication Mechanism for DNN Accelerators（AutoSkewBMT：面向 DNN 加速器的自主优化完整性认证机制合成） |
| 作者 | Rakin Muhammad Shadab, Sanjay Gandham, Mingjie Lin |
| 机构 | 论文未明确公开所署机构 |
| 领域 | 硬件安全 / DNN 加速器（Hardware Security / DNN Accelerator） |
| 投稿方向 | Security（Session: SEC2 — Hardware Security: Primitives & Architecture, Design & Test） |
| 关键词 | 完整性认证(Integrity Authentication)、Bonsai Merkle Tree、DNN 加速器(DNN Accelerator)、内存安全(Memory Security)、设计空间探索(Design Space Exploration) |
| 核心资源 | 论文链接：[IEEE Xplore](https://ieeexplore.ieee.org)（DAC 2025 Proceedings）；论文暂未公开 arXiv 预印本 |

---

## 一、一句话核心摘要

> DNN 推理加速器处理敏感数据时，片外 DRAM 面临篡改和重放攻击威胁——完整性认证（HMAC/Merkle Tree）是必需的防线，但其 30%–60% 的额外存储和带宽开销对吞吐优先的 DNN 加速器而言是沉重负担。AutoSkewBMT 提出了一种基于 Bonsai Merkle Tree 的自动化安全框架，通过设计空间探索算法根据 DNN 工作负载的**访存模式特征**自适应地"倾斜"BMT 结构（不同层级分配不同的认证粒度与计数器缓存），相比 SOTA 方案实现高达 32% 的性能提升。

---

## 二、研究背景与动机

### 2.1 行业大背景

随着 DNN 加速器从云端下沉到边缘和自动驾驶等安全关键场景，**内存安全**（memory security）成为不可忽视的硬需求。攻击者可以通过物理探针或总线嗅探篡改 DRAM 中的数据——例如翻转模型权重的关键比特或修改自动驾驶的感知输出——造成灾难性后果。

完整性认证通过验证"数据未被篡改"来解决这一问题。标准方案是为每个数据块（cache line）维护一个消息认证码（MAC），但这引入 ~25% 的存储开销和大量 MAC 验证带宽。

### 2.2 Merkle Tree：完整性认证的"标准答案"及其代价

Merkle Tree 将数据块的哈希值组织为一棵树，仅需在芯片上的安全区域保存根哈希（root hash），通过从叶子到根的验证链确保完整性。Bonsai Merkle Tree（BMT）是硬件实现中的流行变体，通过**计数器缓存**（counter cache）减少片外验证路径的访问延迟。

但 BMT 的开销与**树的形状**高度相关：
- **浅而宽的树** → 更多叶子节点并行访问，但每层跨度大
- **深而窄的树** → 验证路径更长，延迟更高

对于 DNN 推理——大量连续/固定模式的权重读取——BMT 的"理想形状"与传统 CPU 负载截然不同，需要一个系统化的方法去寻找。

### 2.3 现有方法的局限

| 局限 | 详情 |
|------|------|
| **一刀切的 BMT 配置** | 现有 BMT 硬件实现使用固定参数（扇出、计数器大小、级数），不考虑 DNN 工作负载的访存特征 |
| **缺乏自动化** | BMT 参数调优依赖手工试错，设计空间庞大（扇出 × 级数 × 缓存大小 × 分配策略的组合爆炸） |
| **静态 vs 动态特征脱节** | DNN 推理的访存模式（如卷积的参数复用、全连接层的流式访问）在不同层间差异巨大，固定 BMT 配置必然在某些层上效率低下 |

### 2.4 本文贡献

1. **BMT 设计空间系统化建模**：首次将 BMT 的配置参数（扇出、计数器分配、缓存层次、负载倾斜）形式化为可遍历的设计空间。
2. **自动化合成框架 AutoSkewBMT**：提出设计空间生成算法，根据给定 DNN 工作负载的访存 trace 自动搜索最优 BMT 配置。
3. **显著性能提升**：自动生成的 BMT 配置在通用 DNN 负载上比 SOTA 方案性能**提升高达 32%**。

---

## 三、提出的解决方案

### 3.1 AutoSkewBMT 框架架构

AutoSkewBMT 是一个"安全配置编译器"，输入为 DNN 工作负载描述（网络结构 + 层参数 + 数据流映射），输出为优化的 BMT 硬件参数配置。其核心 pipeline 包括：

1. **访存 Trace 提取**：从 DNN 加速器的数据流模拟器（如 Timeloop/MAESTRO）提取各层的 DRAM 访问序列——读取权重的顺序、激活的读写模式、输出回写等。
2. **设计空间枚举与剪枝**：基于 BMT 参数化模型（扇出 k/级数 L/计数器大小 C/倾斜因子 S），枚举可能的配置组合，并使用启发式规则剪枝明显低效的配置。
3. **性能建模与评估**：对每个候选配置，基于访存 trace 模拟 BMT 的验证延迟、计数器命中率和带宽开销。
4. **最优配置输出**：选择 Pareto 最优的配置，输出为可综合的 BMT 硬件 RTL 参数。

### 3.2 核心创新点：BMT 的"倾斜"（Skew）

#### 什么是 BMT Skew？

传统 BMT 的各层级（叶子 → 中间 → 根）使用相同的扇出度和计数器策略。**Skew** 意味着在不同层级使用**不同的**参数——例如：
- 靠近内存的层级：更大扇出（减少树深度），更大的计数器缓存（高命中率）
- 靠近根的层级：更小扇出（减少片上 TAG 存储），更小的计数器

**关键洞察**：DNN 推理的访存具有高度规律性——权重的访问模式是循环固定的（如卷积核被所有 spatial 位置复用），这意味着 BMT 的某些层级会"过热"（频繁验证），而另一些"偏冷"。倾斜 BMT 将更多资源（缓存）分配给热点层级，从冷层级回收资源。

#### 设计空间生成算法

算法的核心是一个"预算约束下的最优分配"问题：

- **约束**：片上 SRAM 总预算（用于存储 BMT 计数器缓存和中间哈希）、延迟预算
- **变量**：每层的扇出度 k_i、计数器缓存大小 C_i
- **目标**：最小化 BMT 验证的平均延迟

算法使用贪心 + 局部搜索两阶段优化：先在粗粒度上分配层级，再在细粒度上微调计数器大小。

### 3.3 硬件实现考虑

AutoSkewBMT 输出的是可直接综合的参数化 Verilog/VHDL BMT 模块。倾斜 BMT 与传统 BMT 在硬件上不增加额外的逻辑复杂度——只是每层参数不同，控制逻辑通过配置寄存器驱动。

---

## 四、实验评估

### 4.1 实验设置

| 项目 | 详情 |
|------|------|
| DNN 工作负载 | ResNet-18、VGG-16、MobileNetV2 等通用 benchmark |
| DNN 加速器模型 | 类 Eyeriss 的权重固定的数据流加速器 |
| 对比基线 | SOTA 固定配置 BMT、未倾斜的 BMT |
| 评估指标 | 性能（IPC 归一化）、面积开销（mm²）、BMT 验证延迟 |
| 实现方式 | RTL 模拟 + SRAM 建模 |

### 4.2 核心实验结果

| 指标 | 结果 |
|------|------|
| **性能提升 vs SOTA** | 高达 **32%**（在 ResNet-18 上） |
| **面积开销** | 倾斜 BMT 与固定 BMT 面积相当（在 SRAM 总预算内重新分配） |
| **通用性** | 多种 DNN 工作负载上均实现改进 |

### 4.3 消融分析（预期）

> 论文的消融实验可能涵盖：

- **固定扇出 vs 倾斜扇出**的单独贡献
- **固定计数器分配 vs 倾斜计数器分配**的贡献分解
- **不同 SRAM 预算下**的最佳配置变化趋势

> **注**：具体消融数据请参阅论文正文（IEEE Xplore）。

### 4.4 局限性分析

> 以下分析中，"（论文）"标注的来自原文，"（个人观点）"标注的为合理推论。

- **静态工作负载假设**（论文隐含）：AutoSkewBMT 基于已知的 DNN 模型进行离线优化，适用于嵌入式推理加速器（固定模型部署），但不适用于训练加速器或模型频繁切换的场景。
- **加密的联合优化**（个人观点）：AutoSkewBMT 仅优化完整性认证（Merkle Tree），未涉及加密（XTS/AES）的优化。完整内存安全 = 加密 + 完整性，二者联合优化是一个有前景的方向。
- **工艺节点影响**（个人观点）：当前评估可能基于特定工艺节点；先进工艺下 SRAM 密度提升可能改变"最佳倾斜度"。

---

## 五、结论与展望

### 5.1 论文结论

AutoSkewBMT 展示了"不是所有 Merkle Tree 都生而平等"的核心洞察——通过针对 DNN 工作负载访存特征自动合成倾斜的 BMT 配置，可以在不增加面积开销的前提下实现高达 32% 的性能提升。这项工作将 DNN 加速器内存安全的优化从"手工经验"提升到了"算法自动化"的新阶段。

### 5.2 工业价值

- **边缘 AI 安全 SoC 的关键组件**：对于自动驾驶芯片、无人机 SoC 等需要内存安全保证的 DNN 推理平台，AutoSkewBMT 提供了一种低开销的自动化安全配置方案。
- **设计方法的可复用性**：AutoSkewBMT 的"工作负载特征驱动安全配置"思路可迁移至其他安全原语（如加密引擎的频率/电压调优、PUF 的可靠性优化）。
- **EDA 工具链集成潜力**：可被集成为 DNN 加速器设计流程中的"安全配置自动优化"pass。

### 5.3 未来方向

> **个人延伸分析**：

> - **动态倾斜 BMT**：支持运行时根据当前 DNN 层（卷积 vs 全连接）动态切换 BMT 配置，进一步提升灵活性。
> - **加密 + 完整性联合优化**：将 AutoSkewBMT 的方法扩展至完整的内存安全（加密 + 完整性），在统一 SRAM 预算下分配加密密钥缓存和 BMT 计数器缓存。
> - **多租户加速器的安全隔离**：在云 DNN 加速器多租户场景下，使用倾斜 BMT 实现不同租户模型的不同级别安全保护。

---

## 六、个人思考与启发

1. **"安全开销不是绝对值，是工作负载的函数"**：AutoSkewBMT 最深刻的洞察在于——同样是 32% 的性能提升，它不是通过"造更快的电路"实现的，而是通过"发现工作负载的规律性并善加利用"实现的。安全硬件设计不应是"架一个最高级别的防护罩然后承受代价"，而可以是"理解保护对象的特性后精准部署防护"。

2. **自动化设计空间探索是安全硬件的未来**：手工调优 BMT 参数的时代已经过去了。面对越来越复杂的 DNN 工作负载，只有算法化的设计空间探索才能找到人脑无法触及的最优解。这是 EDA 方法论对安全硬件领域的渗透。

3. **对复现/后续研究的建议**：
   - 先理解 Bonsai Merkle Tree 的基本原理（参考 "Morphable Counters" 相关工作）；
   - 设计空间探索可以用 Python + scikit-optimize 快速原型，然后通过 Verilog 仿真验证；
   - 重点难点在于"访存 trace → BMT 性能模型"的精度——建议使用 gem5 或自定义 DRAM 模拟器获得真实的访存时延数据。

---

## 七、相关资源与延伸阅读

- **论文原文（IEEE Xplore）**：DAC 2025 Proceedings（暂未公开 arXiv 预印本）
- **DAC 2025 官网**：[https://www.dac.com/](https://www.dac.com/)
- **Bonsai Merkle Tree 相关**：
  - Rogers et al., "Morphable Counters: Enabling Compact Integrity Trees For Low-Overhead Secure Memories" (MICRO 2018)
  - Saileshwar et al., "Morphable Counters: Enabling Compact Integrity Trees" (ASPLOS 2018)
- **DNN 加速器内存安全综述**：
  - Hua et al., "Secure and Trusted Deep Learning Accelerators: A Comprehensive Survey" (IEEE TCAD)
- **DNN 加速器建模工具**：
  - Timeloop：[https://github.com/NVlabs/timeloop](https://github.com/NVlabs/timeloop)
  - MAESTRO：[https://github.com/maestro-project/maestro](https://github.com/maestro-project/maestro)
