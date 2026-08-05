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
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">SEC4: Embedded and Cross-Layer Security</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11133162">https://dl.acm.org/doi/10.1109/DAC63849.2025.11133162</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 物联网协议，并行模糊测试，配置模型识别与调度</p>
</div>

---

## 研究概要
本文提出CMFUZZ并行物联网协议模糊测试框架，新增配置模型维度。自动提取各类配置并量化参数依赖关系，基于权重聚类分配并行实例。在MQTT、CoAP等6款IoT协议验证，相较Peach、SPFuzz分支覆盖率平均提升34.4%、28.5%，发现14个全新高危漏洞。

## 背景和动机
1. IoT协议存在大量可配置参数，仅默认配置模糊会遗漏仅特定参数下触发的内存崩溃、DoS类漏洞。
2. 现有协议模糊器仅构建数据、状态模型，缺少统一配置建模能力，无法系统性遍历多参数组合。
3. 并行模糊直接随机分配配置易出现参数冲突、初始化失败，冗余组合大幅降低路径探索效率。
4. 配置项存在协同、互斥依赖关系，现有并行调度未量化关联权重，资源分配不均衡。
5. IoT配置来源分为CLI、多格式配置文件，缺少通用自动化提取标准化方案。

## 相关工作
1. 单协议模糊工具（Peach、BooFuzz）：仅建模数据包与状态机，完全忽略系统配置维度。
2. 并行模糊框架（AFLNet、SPFuzz）：侧重种子同步、状态路径调度，不处理配置参数空间划分。
3. 序列导向模糊Bleem、日志引导Logos：优化报文生成逻辑，无配置感知并行分配机制。
4. 工业并行PAFL：基于负载均衡分配实例，未考虑配置间依赖冲突问题。
5. 现有IoT安全测试：聚焦报文漏洞，极少挖掘配置切换引发的隐藏执行路径缺陷。

## 本文解决方案
### 1 通用配置模型识别模块
解析CLI参数与ini/JSON/XML等多格式配置文件，标准化提取配置项，生成包含名称、类型、可变标记、典型取值的四元组统一模型。
### 2 配置关系权重量化机制
以程序启动分支覆盖率为指标，遍历参数两两组合，归一化交互权重构建加权关系图，协同参数权值更高。
### 3 关联感知聚类分配算法
按权重降序处理参数节点，采用分组适配评分公式聚类，强关联参数划入同一并行实例，隔离冲突配置。
### 4 隔离式并行模糊调度
各实例通过Linux网络命名空间隔离运行，仅在覆盖率停滞时动态变异配置取值，避免跨实例干扰。
### 5 基于Peach二次工程实现
复用原有报文/状态建模能力，新增配置解析、权重计算、分组调度三层扩展模块，适配主流IoT协议实现。

## 实验分析
1. 实验设置：6款主流IoT开源实现（Mosquitto、libcoap等），4并行实例，24小时5轮重复测试，指标为分支覆盖率、加速比、漏洞数。
2. 覆盖提升：对比原生Peach平均+34.4%分支覆盖，对比SPFuzz平均+28.5%，MQTT、DNS提升幅度超50%。
3. 执行加速：达到同等覆盖平均相较Peach提速3544倍、相较SPFuzz提速2746倍。
4. 漏洞挖掘：共发现14个未公开漏洞，包含空指针解引用、堆溢出、内存泄漏、超大分配等高危缺陷。
5. 案例验证：libco分块传输漏洞仅开启特定Q-Block配置触发，默认模式无法复现，证明配置建模必要性。

## 研究启发
1. IoT协议漏洞存在强配置依赖性，传统仅面向报文的模糊测试存在大量路径盲区，必须引入配置维度建模。
2. 并行模糊不能随机分配参数，量化参数依赖并聚类分组可大幅减少无效配置组合，提升探索效率。
3. 配置项交互强度可通过启动覆盖率快速量化，无需完整全量仿真，调度开销可控。
4. 现有成熟协议模糊器可模块化扩展配置调度层，无需重构报文生成核心逻辑。
5. 嵌入式资源受限IoT设备，配置切换引发内存缺陷危害极高，安全测试需覆盖全参数组合场景。

## 相关资源

- **Peach Fuzzer**：[https://gitlab.com/peachtech/peach-fuzzer-community](https://gitlab.com/peachtech/peach-fuzzer-community)
- **代表性 IoT 协议实现**：
  - Mosquitto (MQTT)：[https://github.com/eclipse/mosquitto](https://github.com/eclipse/mosquitto)
  - libcoap (CoAP)：[https://github.com/obgm/libcoap](https://github.com/obgm/libcoap)
- **协议 Fuzz 测试相关**：
  - AFLNet：[https://github.com/aflnet/aflnet](https://github.com/aflnet/aflnet)
  - BooFuzz：[https://github.com/jtpereyda/boofuzz](https://github.com/jtpereyda/boofuzz)
