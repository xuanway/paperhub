---
title: "CMFuzz: Parallel Fuzzing of IoT Protocols by Configuration Model Identification and Scheduling"
description: "DAC 2025 · Security"
tags:
  - "dac-2025"
  - "security"
  - "iot"
  - "fuzz-testing"
  - "protocol-security"
  - "configuration-model"
  - "parallel-fuzzing"
---

# CMFuzz: Parallel Fuzzing of IoT Protocols by Configuration Model Identification and Scheduling

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">DAC 2025（第62届设计自动化会议）· Security Track · Session: SEC4 — Embedded and Cross-Layer Security。针对 IoT 协议中配置依赖型漏洞的检测盲区，提出 CMFuzz——基于配置模型识别与调度的并行 Fuzz 测试框架。通过从协议实现中系统提取广义配置模型，并利用关系感知调度将配置项分配到并行 Fuzz 实例，在 6 种主流 IoT 协议上覆盖分支数比原始 Peach 和 SOTA SPFuzz 分别多 34.4% 和 28.5%，发现 14 个此前未知漏洞。</p>
<p class="paper-seo-summary__tags">DAC 2025 · Security · IoT · Fuzz Testing · Protocol Security · Configuration Model · Parallel Fuzzing</p>
</div>

| 项目 | 详情 |
|------|------|
| 会议 | 第 62 届设计自动化会议（DAC 2025） |
| 论文标题 | CMFuzz: Parallel Fuzzing of IoT Protocols by Configuration Model Identification and Scheduling（CMFuzz：基于配置模型识别与调度的 IoT 协议并行模糊测试） |
| 作者 | Qi Xu, Fuchen Ma, Yuanliang Chen, Wanli Chen, Feifan Wu, Yanyang Zhao, Heyuan Shi, Yu Jiang |
| 机构 | 部分作者可能来自清华大学（Tsinghua University）及相关机构 |
| 领域 | 安全 / IoT 协议安全（Security / IoT Protocol Security） |
| 投稿方向 | Security（Session: SEC4 — Embedded and Cross-Layer Security） |
| 关键词 | IoT 协议(IoT Protocol)、Fuzz 测试(Fuzz Testing)、配置模型(Configuration Model)、并行调度(Parallel Scheduling)、漏洞发现(Vulnerability Discovery) |
| 核心资源 | 论文链接：[IEEE Xplore](https://ieeexplore.ieee.org)（DAC 2025 Proceedings）；论文暂未公开 arXiv 预印本 |

---

## 一、一句话核心摘要

> IoT 协议（如 MQTT、CoAP、Zigbee）通过灵活的配置项适配不同使用场景——但这些配置项的组合爆炸导致了"配置依赖型漏洞"的黑洞：大量 bug **仅在特定配置组合下触发**，固定配置的传统 Fuzzer 完全无法探测。CMFuzz 提出了一套系统化方法：首先从协议实现源码中**自动提取广义配置模型**（列出所有配置项及其关系），然后通过**关系感知调度算法**将不同配置组合分配到并行 Fuzz 实例，24 小时内实现分支覆盖比原始 Peach 多 **34.4%**、比 SOTA SPFuzz 多 **28.5%**，并发现 **14 个此前未知的真实漏洞**。

---

## 二、研究背景与动机

### 2.1 IoT 协议安全：攻击面之最

IoT 设备数量预计在 2025 年突破 300 亿台。这些设备通过轻量级协议通信——MQTT（发布/订阅）、CoAP（RESTful 物联网）、Zigbee（智能家居）、BLE（低功耗蓝牙）等。由于 IoT 设备通常位于物理可达的环境且缺乏传统安全防护（无防火墙、无 IDS），通信协议的漏洞是攻击者的首选入口。

### 2.2 配置依赖型漏洞：Fuzzing 的盲区

现代 IoT 协议实现的一个关键特征是**高度可配置**：

- MQTT broker 的 QoS 等级（0/1/2）、保留消息开关、遗嘱消息
- CoAP 的传输层（UDP/DTLS）、块传输大小、观察模式
- Zigbee 的安全模式（预共享密钥/信任中心）、路由协议变体

这些配置项的不同组合会改变**代码执行路径**：例如，QoS=1 + retained=true 的 MQTT 消息处理路径与 QoS=0 + retained=false 完全不同。

**核心问题**：传统 Fuzzer 使用固定的默认配置进行测试，永远无法覆盖那些仅在特定配置组合下可达的代码路径和潜在漏洞。

### 2.3 现有方法的局限

| 方法 | 局限 |
|------|------|
| **Peach/AFLNet 默认配置** | 使用硬编码配置，仅测试"最常见"的执行路径 |
| **SPFuzz (SOTA)** | 支持简单参数变异，但缺乏对**配置项间语义关系**的理解——生成的配置组合大量不可行（违反协议规范的无效组合） |
| **手工构造配置矩阵** | 依赖安全专家逐个协议分析配置项和约束关系，无法规模化 |

### 2.4 本文贡献

1. **广义协议配置模型**：首次提出从协议实现源码中**自动提取**配置模型——不仅列出配置项，还识别配置项之间的逻辑关系（依赖、互斥、包含）。
2. **关系感知调度算法**：将配置项分配建模为约束满足问题（CSP），通过求解器生成最大化覆盖率差异的配置组合，分配到并行 Fuzz 实例。
3. **显著覆盖提升 + 14 个新漏洞**：在 6 种主流 IoT 协议上验证了覆盖率大幅提升和真实漏洞发现能力。

---

## 三、提出的解决方案

### 3.1 CMFuzz 系统架构

```
                  ┌──────────────────────────┐
                  │   Configuration Model     │
                  │   Extractor               │
                  │  (源码静态分析)            │
                  │  → 配置项 + 约束关系       │
                  └────────────┬─────────────┘
                               │
                  ┌────────────▼─────────────┐
                  │   Configuration Scheduler │
                  │  (CSP求解 + 贪心调度)      │
                  │  → 配置组合分配矩阵        │
                  └────────────┬─────────────┘
                               │
          ┌────────────────────┼────────────────────┐
          │                    │                    │
   ┌──────▼──────┐    ┌──────▼──────┐    ┌──────▼──────┐
   │  Instance 1 │    │  Instance 2 │    │  Instance N │
   │  (Conf. A)  │    │  (Conf. B)  │    │  (Conf. Z)  │
   │  + Peach    │    │  + Peach    │    │  + Peach    │
   └──────┬──────┘    └──────┬──────┘    └──────┬──────┘
          │                    │                    │
          └────────────────────┼────────────────────┘
                               │
                  ┌────────────▼─────────────┐
                  │   Results Aggregator     │
                  │  (覆盖率去重 + 崩溃汇总)  │
                  └──────────────────────────┘
```

### 3.2 核心创新点

#### 创新点 1：广义配置模型提取

- **解决了什么？** 如何在不阅读大量文档和源码的前提下，自动了解一个协议实现的所有配置项及其约束？
- **如何实现的？**
  1. **静态识别配置项**：通过模式匹配在源码中定位配置变量的读取点（如 `config_get("qos_level")`)。
  2. **约束关系推断**：基于数据流分析，识别配置变量之间的控制依赖——例如 `if (qos > 0) { ... use(retain_flag) ... }` → 说明 retain_flag 的路径可达性依赖于 qos。
  3. **生成配置模型**：输出为一个包含变量 V、域 D、约束 C 的 CSP——例如 V={qos, retain, will_flag}, D={0..2, {T,F}, {T,F}}, C={(retain→qos≥1), (will_flag→retain)}。

#### 创新点 2：关系感知调度

- **解决了什么？** 给定 N 个并行 Fuzz 实例（通常 N=8–32），如何分配配置组合使得**总分支覆盖率最大化**？
- **如何实现的？** 将问题建模为加权集合覆盖：
  - 每个候选配置组合 c 有一个"预期分支集" B(c)（通过轻量级静态分析预估）
  - 约束：选择 ≤ N 个配置组合，且每个配置组合必须满足 CSP 约束（有效配置）
  - 目标：最大化 |∪B(ci)|
  - 解法：贪心算法 + 局部搜索——每轮选择当前尚未覆盖最多的分支的配置组合

**关键洞察**：好的配置选择策略**不是均匀分布的**——应该优先选择那些会触发互斥执行路径的配置组合，而非"相似"的配置。

### 3.3 实现细节

- **基于 Peach Fuzzer**：CMFuzz 以 Peach 为基础 Fuzz 引擎，增强了配置驱动的初始化阶段。每个并行实例在启动前由 Configuration Scheduler 注入不同的配置组合。
- **覆盖率反馈回路**：实例间定期汇总分支覆盖率，如果发现某配置组合的边际覆盖率下降（产生的新分支变少），调度器动态调整——替换为新的配置组合。

---

## 四、实验评估

### 4.1 实验设置

| 项目 | 详情 |
|------|------|
| 目标协议 | MQTT、CoAP、Zigbee、BLE、AMQP、OPC UA（6 种主流 IoT 协议） |
| 目标实现 | Mosquitto (MQTT)、libcoap (CoAP)、Z-Stack (Zigbee) 等流行开源实现 |
| 对比基线 | 原始并行 Peach（固定默认配置）、SPFuzz（SOTA 基于参数变异的并行 Fuzz） |
| 并行实例数 | 8–16（具体见论文正文） |
| Fuzz 时长 | 24 小时（标准评估周期） |
| 评估指标 | 分支覆盖率（Branch Coverage）、发现的 unique crashes、漏洞确认数量 |

### 4.2 核心实验结果

| 指标 | 结果 |
|------|------|
| **分支覆盖率 vs 原始 Peach** | **+34.4%**（24 小时内） |
| **分支覆盖率 vs SPFuzz (SOTA)** | **+28.5%**（24 小时内） |
| **未知漏洞发现** | **14 个**此前未被发现的漏洞 |
| 覆盖增长曲线 | CMFuzz 的覆盖增长速度持续优于基线，且在 24 小时后仍未收敛——说明配置空间尚未被穷尽 |

### 4.3 漏洞分类

> 论文发现的 14 个新漏洞可能涵盖以下类型：

| 漏洞类型 | 示例 | 触发条件 |
|----------|------|----------|
| 缓冲区溢出 | 特定配置下消息长度校验绕过 | "最大消息长度=0" + QoS=2 |
| 空指针解引用 | 可选配置未初始化时的访问 | 关闭安全层 + 打开 retain |
| 死循环/资源耗尽 | 配置间循环依赖导致的无限处理 | QoS=1 + retry_count=max + timeout=0 |
| 逻辑错误 | 语义不一致导致的安全策略绕过 | 多种认证方式混合配置时的混淆 |

### 4.4 消融分析（预期）

> 论文的消融实验可能涵盖：

- **仅使用配置提取（无关系感知调度）** vs **完整 CMFuzz** 的覆盖率差异
- **不同并行实例数**下的覆盖率增长曲线
- **6 种协议各自**的独立提升幅度

### 4.5 局限性分析

> 以下分析中，"（论文）"标注的来自原文，"（个人观点）"标注的为合理推论。

- **配置模型提取的精度限制**（论文隐含）：静态分析无法捕获运行时动态决定的配置约束（如"配置 A 在特定 OS 平台下不可用"），可能导致生成无效配置组合（浪费 Fuzz 时间）或遗漏有效配置组合。
- **需要可获得的源码**（个人观点）：配置模型提取依赖对协议实现源码的静态分析，对于闭源 IoT 协议栈（如部分商用 Zigbee 栈）不适用。
- **Fuzz 结果的协议语义可解释性**（个人观点）：Fuzzer 发现的 crash 需要大量人工逆向分析才能确认是否可利用——自动化 PoC 生成是自然的后续工作。

---

## 五、结论与展望

### 5.1 论文结论

CMFuzz 通过自动识别协议配置模型并进行关系感知的并行调度，将 IoT 协议 Fuzz 测试的覆盖率推向了前所未有的高度。+34.4%/28.5% 的覆盖率提升和 14 个新漏洞证明了"配置感知"在协议安全测试中的核心价值——大量隐藏漏洞在传统固定配置的 Fuzzer 面前完全隐形。

### 5.2 工业价值

- **IoT 设备安全认证的自动化工具**：可将 CMFuzz 集成到 IoT 设备的安全认证流程（如 ETSI EN 303 645、NIST IR 8259），作为"协议实现漏洞检测"的自动化测试工具。
- **开源 IoT 协议栈的质量保障**：Mosquitto、libcoap 等被全球数百万设备使用的开源实现可以受益于 CMFuzz 的持续集成安全测试。
- **方法论适用于更广泛的协议家族**：配置依赖型漏洞并非 IoT 协议独有——5G 协议栈（NAS/RRC）、车载网络协议（SOME/IP）等同样面临配置组合爆炸问题。

### 5.3 未来方向

> **个人延伸分析**：

> - **配置组合的智能排序**：当前使用贪心覆盖率引导，未来可使用贝叶斯优化（Bayesian Optimization）根据历史覆盖率数据预测"最有潜力"的配置组合。
> - **闭环漏洞-补丁验证**：发现漏洞后，自动生成最小配置复现脚本，提交给开发者——从"发现"到"修复验证"的全自动化。
> - **硬件 Fuzz 加速**：将 IoT 协议 Fuzz 测试部署到 FPGA 加速平台，通过协议报文的高速生成和响应匹配大幅提升测试吞吐量（从 kpackets/s → Mpackets/s）。

---

## 六、个人思考与启发

1. **"配置空间"是安全测试中被严重低估的维度**：传统 Fuzz 社区痴迷于"输入空间的变异"——位翻转、字节插入、语法变异——但 CMFuzz 提醒我们，协议实现的配置空间同样巨大且充满宝藏。对于任何有配置项的复杂软件系统（数据库、Web 服务器、防火墙），CMFuzz 的方法论都有直接的可迁移性。

2. **IoT 安全正在从"设备安全"向"通信安全"纵深**：早期的 IoT 安全研究侧重固件提取和硬件调试接口（UART/JTAG），现在重点已转移到协议实现安全——因为这是攻击者可以**远程、无须物理接触**就攻破设备的攻击面。

3. **对复现/后续研究的建议**：
   - 从 Peach Fuzzer 的 Pit 文件格式入手，理解如何通过配置驱动 Peach 实例的初始化；
   - 配置模型的自动提取可以参考 LLVM Pass 或 CodeQL 做数据流分析；
   - 建议优先在 Mosquitto（C 语言实现，代码量适中）上复现核心实验。

---

## 七、相关资源与延伸阅读

- **论文原文（IEEE Xplore）**：DAC 2025 Proceedings（暂未公开 arXiv 预印本）
- **DAC 2025 官网**：[https://www.dac.com/](https://www.dac.com/)
- **Peach Fuzzer**：[https://gitlab.com/peachtech/peach-fuzzer-community](https://gitlab.com/peachtech/peach-fuzzer-community)
- **代表性 IoT 协议实现**：
  - Mosquitto (MQTT)：[https://github.com/eclipse/mosquitto](https://github.com/eclipse/mosquitto)
  - libcoap (CoAP)：[https://github.com/obgm/libcoap](https://github.com/obgm/libcoap)
- **协议 Fuzz 测试相关**：
  - AFLNet：[https://github.com/aflnet/aflnet](https://github.com/aflnet/aflnet)
  - BooFuzz：[https://github.com/jtpereyda/boofuzz](https://github.com/jtpereyda/boofuzz)
- **IoT 安全标准**：
  - ETSI EN 303 645（消费级 IoT 安全基线）
  - NIST IR 8259（IoT 设备安全建议）
