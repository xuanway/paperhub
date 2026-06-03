---
title: "A Novel Covert Timing Channel for Cloud FPGAs"
description: "DAC 2025 · Security"
tags:
  - "dac-2025"
  - "security"
  - "covert-channel"
  - "cloud-fpga"
  - "side-channel"
  - "axi-protocol"
---

# A Novel Covert Timing Channel for Cloud FPGAs

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">DAC 2025（第62届设计自动化会议）· Security Track · Session: SEC4 — Embedded and Cross-Layer Security。针对云 FPGA 多租户场景中的隐蔽数据泄露威胁，提出一种基于 AXI 协议握手信号的新型隐蔽时序信道（Covert Timing Channel），无需 FPGA 主动发出专用消息即可实现数据外传，BER 低至 0.01988%，并成功在 AWS EC2 上演示远程功耗分析攻击。</p>
<p class="paper-seo-summary__tags">DAC 2025 · Security · Covert Channel · Cloud FPGA · AXI Protocol · Side-Channel Attack</p>
</div>

| 项目 | 详情 |
|------|------|
| 会议 | 第 62 届设计自动化会议（DAC 2025） |
| 论文标题 | A Novel Covert Timing Channel for Cloud FPGAs（面向云 FPGA 的新型隐蔽时序信道） |
| 作者 | Brian Udugama, Darshana Jayasinghe, Hassaan Saadat, Aleksandar Ignjatović, Sri Parameswaran |
| 机构 | School of Computer Science and Engineering, UNSW Sydney（新南威尔士大学） |
| 领域 | 硬件安全 / 云安全（Hardware Security / Cloud Security） |
| 投稿方向 | Security（Session: SEC4 — Embedded and Cross-Layer Security） |
| 关键词 | 隐蔽时序信道(Covert Timing Channel)、云 FPGA(Cloud FPGA)、AXI 协议(AXI Protocol)、功耗分析攻击(Power Analysis Attack)、AWS EC2 |
| 核心资源 | 论文链接：[IEEE Xplore](https://doi.org/10.1109/DAC63849.2025.11133099)（DAC 2025 Proceedings）；论文暂未公开 arXiv 预印本 |

---

## 一、一句话核心摘要

> 云 FPGA 服务中，恶意租户可以利用共享硬件基础设施对同一物理设备上的良性用户实施旁路攻击，但如何将窃取的数据**隐秘地传出云平台**是一个核心挑战。本文提出了一种新型隐蔽时序信道（CTC），首次利用 AXI 协议握手信号的时序特性与互联网数据包间延迟（Inter-Packet Delay）编码信息，在不发送任何专用外传消息的前提下实现数据外泄，误码率低至 0.01988%。作者进一步将该 CTC 与远程功耗分析攻击结合，在 AWS EC2 F1 实例上完整演示了"窃取 → 编码 → 外传"的全链路攻击。

---

## 二、研究背景与动机

### 2.1 行业大背景

云 FPGA（如 AWS F1、阿里云 F3、Azure FPGA）允许用户将自定义硬件设计部署到云端，广泛应用于机器学习推理、基因测序、金融加速等场景。然而，**多租户共享同一物理 FPGA 芯片**的架构带来了严重的安全隐患：恶意租户可通过功耗侧信道、电磁辐射、温度传感器等手段窃取同芯片上其他用户的敏感信息。

但窃取数据只是攻击链的一环。更隐蔽的问题在于：**窃取的数据如何传送到攻击者手中？** 云服务提供商（CSP）通常会监控 FPGA 的所有对外通信，传统的网络隐蔽信道（如 DNS 隧道、ICMP 隐写）在 FPGA 场景下面临独特的实现障碍。本文正是瞄准这一"数据外传"环节展开研究。

### 2.2 现有方法回顾与不足

| 局限 | 详情 |
|------|------|
| **需要专用外传消息** | 现有 FPGA 隐蔽信道研究大多假设 FPGA 可以主动发起网络通信（如发送 UDP 包），但这在现代云 FPGA 安全监控下极易触发告警。 |
| **依赖共享 PDN 假设** | 功耗侧信道攻击常假设攻击者和受害者在同一电源配送网络（PDN）上，但云服务商可能通过物理隔离削弱此类攻击。 |
| **缺乏真实云平台验证** | 多数 FPGA 侧信道/隐蔽信道研究停留在板级实验，未在商用云平台（AWS、Azure）上进行端到端验证。 |

### 2.3 论文动机

本文的核心动机是回答一个问题：**一个恶意 FPGA 设计能否在不主动发送任何网络消息的情况下，将数据隐秘传输到云端外的攻击者？** 如果答案是肯定的，那么云 FPGA 的多租户安全模型就存在根本性缺陷。作者选择研究 AXI 协议——FPGA 与主机间通信的标准总线——因为它的时序行为是 FPGA 正常工作不可避免的"副产品"，难以被监控系统彻底封锁。

### 2.4 本文贡献

1. **新型 AXI 隐蔽时序信道设计**：首次提出利用 AXI 握手信号（VALID/READY）的时序特征编码信息，结合互联网数据包间延迟（Inter-Packet Delay）实现跨网络数据外传，无需 FPGA 主动发送任何专用消息。
2. **信道可靠性分析**：在不同网络条件和 AXI 事务负载下系统分析了 CTC 的误码率（BER），证明该信道在真实环境中可达 0.01988% 的 BER。
3. **端到端攻击演示**：将 CTC 与远程功耗分析攻击结合，在 AWS EC2 F1 实例上完成从数据窃取到外传的完整攻击链路，为云 FPGA 安全研究提供了重要的现实威胁模型。
4. **防御启示**：通过揭示 AXI 时序信道的可行性，为云服务商提供了具体的安全加固方向。

---

## 三、提出的解决方案

### 3.1 整体攻击模型

该攻击链路包含三个阶段：

1. **数据窃取阶段**：攻击者利用 FPGA 上的功耗侧信道（如远程功耗分析）从受害者租户处窃取敏感信息（如 AES 密钥、DNN 模型参数等）。
2. **AXI CTC 编码阶段**：将窃取的比特流通过控制 AXI 总线握手信号的时序特征（如 VALID 信号的有效→无效转换速率）编码为时序模式。
3. **互联网传输阶段**：主机端软件在正常接收 FPGA 数据时，数据包到达时间的间隔（Inter-Packet Delay）自然地携带了 AXI 时序特征，攻击者从互联网另一端通过观测数据包到达间隔即可解码信息。

### 3.2 核心技术原理：AXI 握手信号时序编码

AXI4 协议使用 VALID 和 READY 握手信号控制数据传输：

- **VALID**（Master→Slave）：发送方数据有效
- **READY**（Slave→Master）：接收方准备就绪
- 传输发生在 VALID && READY 同时为高的周期

**攻击核心思路**：恶意 FPGA 设计通过刻意调节 VALID 信号的拉高节奏来编码比特——例如，高频切换代表 '1'，低频切换代表 '0'。主机的 PCIe DMA 引擎在读取这些"节奏化"的数据时，产生的数据包间隔会自然地反映这一时序特征。由于这是正常的 AXI 传输行为（没有协议违规），防火墙和入侵检测系统极难区分。

### 3.3 关键设计挑战与解决

#### 挑战 1：网络抖动干扰

互联网的数据包到达间隔天然存在抖动（jitter），可能淹没 AXI 时序编码的信号。

- **解决**：作者设计了鲁棒的编码方案，通过引入校准序列和自适应阈值，在编码速率和误码率之间找到平衡。实测在跨区域 AWS 网络条件下仍能保持可接受的 BER。

#### 挑战 2：AXI 事务负载竞争

FPGA 的正常数据传输（如 DMA 读写）会与 CTC 编码产生时序竞争，可能破坏编码精度。

- **解决**：通过精心设计 AXI 事务调度策略，将 CTC 信号交错嵌入正常数据流中，使时序特征在统计意义上得以保留。

### 3.4 与现有工作的本质区别

不同于此前依赖专用外传消息或额外硬件资源的信道，本文的 AXI CTC 利用了 FPGA 云架构中**不可避免的通信路径**——FPGA 总要和主机通信，主机总要和互联网通信。攻击者只是"骑"在这条必经之路上调制时序信号，这使得防御异常困难：彻底封锁该信道意味着要牺牲 AXI 总线的正常功能。

---

## 四、实验评估

### 4.1 实验设置

| 项目 | 详情 |
|------|------|
| 实验平台 | AWS EC2 F1 实例（Xilinx Virtex UltraScale+ VU9P） |
| 目标 FPGA | 云 FPGA 多租户共享环境 |
| AXI 协议 | AXI4（Full） |
| 网络条件 | AWS 跨区域（多跳互联网） |
| 评估指标 | 误码率（BER）、传输速率、检测难度 |

### 4.2 核心实验结果

| 指标 | 结果 |
|------|------|
| **最低 BER** | **0.01988%** |
| 编码机制 | AXI VALID/READY 握手时序 + IPD 调制 |
| 攻击演示 | 成功在 AWS EC2 上实现远程功耗分析 → CTC 外传完整链路 |
| 检测逃逸 | 无专用外传消息，防火墙/DIDS 难以区分正常流量 |

### 4.3 BER 影响因素分析

> 作者系统分析了不同条件下的 BER 变化：

- **AXI 事务负载增加** → BER 上升（正常 DMA 流量与 CTC 信号竞争）
- **网络跳数增加** → BER 上升（累积抖动）
- **编码速率降低** → BER 下降（在速率与可靠性间存在 trade-off）

### 4.4 局限性分析

> 以下分析中，"（论文）"标注的来自原文，"（个人观点）"标注的为合理推论。

- **跨平台通用性需进一步验证**（个人观点）：当前实验基于 AWS EC2 F1（Xilinx VU9P），对于 Azure FPGA（Intel/Altera）或阿里云 F3 的适用性尚不明确——不同云平台的 PCIe 拓扑、网络架构和监控策略可能影响信道质量。
- **传输速率受限**（论文隐含）：基于时序的编码天然带宽极低（通常 bps 级别），仅适用于窃取密钥、模型指纹等小数据量信息，不适合大批量数据外泄。
- **防御技术正在跟进**（个人观点）：AWS 已在 FPGA 安全白皮书中提及 AXI 流量异常检测；随机化 DMA 调度可能是一个有效的缓解手段。

---

## 五、结论与展望

### 5.1 论文结论

本文证明了云 FPGA 中存在一种新的攻击面——利用 AXI 协议握手信号构建隐蔽时序信道，在不发送专用外传消息的情况下实现数据外泄。该信道 BER 低至 0.01988%，且已成功在 AWS EC2 真实环境中驱动远程功耗分析攻击。这一发现对云 FPGA 的多租户安全模型构成了实质性挑战。

### 5.2 工业价值

- **对云服务商的警示**：揭示了一个此前被忽视的数据外泄路径，推动 CSP 重新审视 FPGA 实例的网络监控策略和 AXI 流量审计机制。
- **攻击面的系统化认知**：将 AXI 时序信道问题纳入云 FPGA 安全威胁模型，有助于更全面地评估多租户共享 FPGA 的风险。
- **防御技术的催化剂**：为 AXI 流量随机化、时序混淆、延迟注入等防御手段提供了研究动机。

### 5.3 未来方向

> **论文作者提出的方向**（已在原文涉及）：
> - 探索更鲁棒的编码方案以在更高网络抖动下维持低 BER。

> **个人延伸分析**：
> - **跨 CSP 平台基准测试**：在 Azure、阿里云等不同云 FPGA 平台上一致性验证 CTC 的可行性和 BER 差异。
> - **主动防御设计**：在 FPGA Shell 中引入时序随机化模块——在 AXI 事务中注入随机延迟，使时序信道信噪比降至不可用水平，同时保证对正常应用性能影响可忽略。
> - **AI 辅助检测**：训练时序异常检测模型（如 LSTM Autoencoder）识别 AXI 流量的隐蔽调制模式。

---

## 六、个人思考与启发

1. **"正常即异常"的警醒**：这篇论文最令人不安的地方在于——攻击者并不需要做任何"异常"的事，只是在 AXI 协议完全合法的行为空间中调制信息。这对传统基于签名的安全检测方法提出了根本性挑战。防御思维的转变可能是从"检测恶意行为"到"检测罕见时序模式"。

2. **FPGA 安全研究的"最后一公里"**：此前的 FPGA 侧信道研究大多止步于"证明了可以窃取数据"，但本文把这最后一公里——"怎么把数据传出去"——补齐了，真正形成了完整的攻击闭环，这对于安全社区评估真实风险至关重要。

3. **对复现/后续研究的建议**：
   - 先熟悉 AWS F1 的开发流程和 Xilinx Shell（AWS FPGA Developer Kit），理解 AXI 接口在 Shell 中的封装方式；
   - 从简单的 AXI 主设备设计入手，观察 VALID/READY 信号的时序行为，逐步实验时序编码方案；
   - 复现时注意 AWS 的 AUP（可接受使用政策）——安全研究需在授权环境下进行。

---

## 七、相关资源与延伸阅读

- **论文原文（IEEE Xplore）**：[https://doi.org/10.1109/DAC63849.2025.11133099](https://doi.org/10.1109/DAC63849.2025.11133099)（DAC 2025 Proceedings）
- **DAC 2025 官网**：[https://www.dac.com/](https://www.dac.com/)
- **AWS FPGA 开发指南**：[https://github.com/aws/aws-fpga](https://github.com/aws/aws-fpga)
- **相关云 FPGA 安全研究**：
  - Tian & Szefer, "Temporal Thermal Covert Channels in Cloud FPGAs" (FPGA 2019)
  - Giechaskiel et al., "Cross-VM Covert- and Side-Channel Attacks in Cloud FPGAs" (ACM Computing Surveys, 2022)
  - Gnad et al., "Voltage-Based Covert Channels Using FPGAs" (ACM TODAES, 2021)
- **AXI 协议规范**：ARM IHI 0022 (AXI4 Specification)
- **作者机构**：UNSW Sydney, School of Computer Science and Engineering
