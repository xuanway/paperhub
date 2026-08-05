---
title: "DroidFuzz: Proprietary Driver Fuzzing for Embedded Android Devices"
description: "DAC 2025 · Systems"
tags:
  - "DAC2025"
  - "Systems"
---

# DroidFuzz: Proprietary Driver Fuzzing for Embedded Android Devices

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">SYS3: Embedded Software</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11132499">https://dl.acm.org/doi/10.1109/DAC63849.2025.11132499</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 安卓测试，模糊测试，嵌入式Linux，错误检测</p>
</div>

---

## 研究概要
本文提出DROIDFUZZ面向嵌入式安卓闭源厂商驱动模糊测试工具，设计HAL预探测、内核-用户关联载荷生成、跨层执行反馈三大核心模块，联合模糊HAL与内核驱动。在7款真实嵌入式设备实测，发现12个厂商确认全新漏洞，内核分支覆盖率相较Syzkaller平均提升17%。

## 背景和动机
1. 嵌入式安卓广泛用于车机、医疗、工控，厂商HAL驱动闭源，大量漏洞潜藏HAL层（如CVE-2021-0673），传统工具难以覆盖。
2. Syzkaller等内核模糊器仅能测试系统调用，无法触及用户态HAL接口，缺少内核与HAL联动测试能力。
3. 闭源HAL无接口文档，静态分析难以提取API与参数，无法构造有效跨层测试用例。
4. 内核、HAL分属不同地址空间，传统覆盖率反馈割裂，无法统一判定跨层交互的有效执行路径。
5. 漏洞多依赖HAL与内核协同状态触发，仅单独模糊其中一层很难复现深层缺陷。

## 相关工作
1. 内核模糊工具（Syzkaller、kAFL、HEALER）：仅面向Linux系统调用，不支持安卓HAL层接口测试，无法模拟硬件完整调用链路。
2. 安卓原生库模糊（Atlas、FuzzGen++）：针对应用层Native库，不涉及底层硬件驱动交互，缺少内核联动逻辑。
3. 驱动接口模糊Difuze：仅单独生成ioctl调用，无HAL完整调用上下文，测试载荷真实性不足。
4. 嵌入式系统模糊（Tardis、EmbSan）：面向通用嵌入式OS，未适配安卓HAL-Binder特殊通信架构。

## 本文解决方案
### 1 预测试HAL探测模块
通过lshal枚举HAL服务，Poke应用结合eBPF挂钩Binder IPC，无源码提取全部HAL接口、参数类型；依据调用频次分配接口采样权重，解决闭源接口无文档问题。
### 2 内核-用户关联载荷生成
构建HAL接口/系统调用加权关系图，基于依赖权重生成跨层调用序列；自动补全参数前置生成调用，定期衰减边权重避免局部搜索停滞，产出真实硬件交互用例。
### 3 跨边界统一执行反馈
内核侧采用kcov采集分支覆盖率；HAL侧通过eBPF捕获其发起的系统调用序列作为等效覆盖，融合两类数据形成统一状态反馈，指导变异生成新测试用例。
### 4 主从分布式模糊架构
主机端Daemon+模糊引擎负责用例生成与反馈分析；设备端Broker、HAL执行器、系统调用执行器负责本地执行，通过ADB完成跨设备通信。

## 实验分析
1. 实验环境：7款主流嵌入式安卓设备（小米、树莓派、商米等），对比Syzkaller、Difuze，每组重复10轮144小时模糊。
2. 漏洞挖掘：DROIDFUZZ共挖出12个未披露高危漏洞（5个HAL、7个内核），Syzkaller仅发现2个内核漏洞，全部厂商确认修复。
3. 代码覆盖：内核分支覆盖率相比Syzkaller平均提升17%；仅保留ioctl的DROIDFUZZ-D仍比Difuze覆盖率高34%。
4. 消融实验：移除关联载荷生成/跨层反馈后覆盖率明显下滑，证明两大模块为核心增益来源。
5. 工程落地：基于Rust/Go/C/Java实现完整工具链，适配aarch64/amd64多架构嵌入式固件。

## 研究启发
1. 安卓驱动漏洞挖掘必须打通HAL与内核两层，仅测试系统调用会丢失大量闭源厂商逻辑缺陷。
2. 无源码闭源组件可通过Binder IPC动态探测+eBPF捕获，高效提取全部对外接口，无需逆向二进制。
3. 测试用例不能随机生成，基于HAL与系统调用依赖关系图可大幅提升真实硬件交互场景占比。
4. 针对无覆盖率的闭源用户层代码，可将其系统调用序列等效为执行反馈，实现灰盒模糊闭环。
5. 车机、工控等安全关键嵌入式安卓设备，需要内核+HAL联合模糊方案才能完整覆盖攻击面。