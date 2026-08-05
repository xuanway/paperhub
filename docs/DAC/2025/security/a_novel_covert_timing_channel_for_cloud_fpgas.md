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
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">SEC4: Embedded and Cross-Layer Security</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11133099">https://dl.acm.org/doi/10.1109/DAC63849.2025.11133099</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 隐蔽定时信道，云FPGA，AXI协议，远程功耗分析攻击</p>
</div>

---


## 研究概要
本文提出面向云FPGA的新型隐蔽时序信道，分两阶段窃取加密功耗数据。第一阶段篡改AXI握手时序实现FPGA向vCPU隐传；第二阶段操纵UDP包间隔跨云外传。搭载LDPC最小和解码降低误码，AWS F1实测最低BER仅0.01988，可完成远程功耗分析窃取AES密钥。

## 背景和动机
1. 云FPGA（AWS EC2 F1）采用厂商封装AXI外壳隔离用户逻辑，缺少跨设备隐蔽数据泄露路径的完整安全研究。
2. 现有FPGA隐蔽信道多局限芯片内/同主机，无法实现云端到外网计算机长距离数据窃取。
3. 已有FPGA-CPU侧信道攻击需共享内存、专用缓存篡改，在商用云FPGA环境难以落地，隐蔽性差。
4. 远程功耗分析（RPA）依赖现场物理探针，云环境无硬件接入条件，缺少纯软件+逻辑实现的功耗轨迹窃取方案。
5. 时序信道易受vCPU负载、网络噪声干扰，现有纠错机制开销高、解码精度不足。

## 相关工作
1. 片内FPGA隐蔽信道：线串扰、供电电压调制，仅单芯片内部通信，无法跨vCPU、跨公网传输。
2 FPGA-CPU缓存侧信道攻击：依赖内存共享、缓存预置，云AXI外壳限制访问，易被检测。
3. 网络时序隐蔽信道：仅面向通用网卡，未适配云FPGA与vCPU联动场景。
4. 跨FPGA供电泄露信道：依靠多板卡共电源，攻击部署门槛高。
5. 简单重复码纠错时序信道：噪声下误码率高，无法适配云CPU波动带来的时序扰动。

## 本文解决方案
### 1 两段式端到端隐蔽时序信道架构
阶段一（FPGA→vCPU）：篡改AXI R通道VALID握手信号时钟延迟，0无延迟、δ周期延迟代表1；阶段二（vCPU→外网攻击者）操纵UDP数据包间隔调制隐蔽比特，攻击者仅监听流量即可解调。
### 2 轻量LDPC最小和解码算法
设计专用校验矩阵，迭代最小和译码，仅简单算术运算，兼顾隐蔽性与纠错能力，相比传统重复码大幅降低BER。
### 3 块同步传输机制
每2000数据块插入100ms长间隔作为同步标记，解决UDP丢包、时序漂移导致的解调错位，缺失样本零填充补齐。
### 4 低开销恶意软硬件套件
恶意IP伪装通用第三方加速核，仅占用少量FPGA逻辑，vCPU侧恶意库不修改主业务，云DRC检测难以识别。
### 5 完整RPA攻击链路适配
搭配PPWM片上功耗传感器采集AES功耗轨迹，经隐蔽信道外传后，攻击者端执行CPA分析恢复加密密钥。

## 实验分析
1. 实验平台：AWS EC2 F1实例（XCVU9P FPGA+Xeon vCPU），125MHz FPGA时钟，目标128位AES加密电路。
2. 误码性能：δ=100时整体最低BER=0.01988；vCPU利用率越高时序噪声越大，BER显著上升；LDPC相比重复码最高提升739%纠错效果。
3. 密钥窃取效果：原始轨迹需17100条恢复密钥；经AXI阶段需18600（+9%），完整两阶段需21300（+24%）。
4. δ参数消融：δ从1提升至2时BER断崖下降，δ越大信号区分度越高，但传输带宽小幅降低。
5. 实用性验证：恶意IP通过厂商DRC检测，无显式外发报文，云监控难以捕获隐蔽传输行为。

## 研究启发
1. 云FPGA的AXI握手时序存在原生安全漏洞，无需显式对外报文即可构建跨层隐蔽泄露通道。
2. 仅芯片内部侧信道不足以评估云FPGA安全，必须考虑FPGA-vCPU-公网完整端到端泄露链路。
3. 时序信道噪声来自CPU调度、网络抖动，轻量级LDPC迭代译码是低开销降噪最优方案。
4. 第三方IP引入存在重大安全风险，厂商DRC仅校验功能，无法识别时序类恶意隐蔽逻辑。
5. 云端加密硬件防护不能仅防范物理探针，需新增AXI时序、网络包间隔两类隐蔽信道检测机制。

