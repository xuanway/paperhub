---
title: "HoBBy: Hardening Unbalanced Branches against Control Flow Attacks on Intel SGX and AMD SEV"
description: "DAC 2025 · Security"
tags:
  - "dac-2025"
  - "security"
  - "control-flow-attack"
  - "intel-sgx"
  - "amd-sev"
  - "tee"
  - "compiler-security"
---

# HoBBy: Hardening Unbalanced Branches against Control Flow Attacks on Intel SGX and AMD SEV

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">SEC4: Embedded and Cross-Layer Security</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11132915">https://dl.acm.org/doi/10.1109/DAC63849.2025.11132915</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 秘密依赖分支，控制流攻击，指令级加固，可信执行环境 </p>
</div>

---

## 研究概要
本文基于LLVM提出编译器加固工具HoBBy，面向SGX/AMD SEV可信区，在指令层平衡密钥相关分支。设计单步污点分析定位不平衡代码，配套指令/数据影子、齿化、螺旋技术统一两路指令、访存、PC特征。密码库运行开销仅2.8%，二进制膨胀0.6%，可将三类前沿控制流攻击成功率降至随机猜测水平。

## 背景和动机
1. SGX、SEV等TEE无法抵御微架构控制流侧信道，攻击者借单步中断、缓存/预取器通道窃取密钥分支走向，威胁RSA、ECDSA密码程序。
2. 现有源码级分支平衡仅保证总时长，编译引入指令、PC、访存差异仍可被Nemisis、AfterImage等新型攻击绕过。
3. 现有防护只单一平衡指令数量，未统一指令类型、数据缓存行、加载PC地址，无法应对精细化单步攻击。
4. 缺少一体化编译器方案，无法自动化识别所有密钥依赖分支并多层次抹平执行痕迹，人工常量编程成本极高。
5. 多数加固方案性能/二进制膨胀过大，难以商用密码库、图像处理程序落地部署。

## 相关工作
1. 源码级分支均衡：仅对齐代码总行数，忽略编译后指令、PC偏移漏洞，易被单步类攻击突破。
2. 页面级混淆SGX-Shield：粒度粗，无法消除单条指令带来的微架构差异。
3. Obelix等指令均衡工具：仅保证单步时延一致，未处理加载/存储PC对预取器、TLB的持久泄露。
4. 硬件辅助防护（AEX-Notify）：依赖CPU微码更新，无法通用SGX/SEV设备。
5. 专用攻击防御：仅针对缓存/分支预测单一泄露源，无法覆盖调度器、预取器多类通道。

## 本文解决方案
### 1 密钥分支单步污点分析流水线
基于DFSan污点标记密钥数据，BFS提取分支公共后继，DFS遍历分支全路径；插桩单步指令采集寄存器、访存、PC信息，离线判定指令数量/类型/访存/PC四类不平衡漏洞。
### 2 指令影子平衡法
构造影子寄存器映射，向分支短路径插入同类型冗余影子指令，两路指令计数、操作码完全一致，不改变原始程序语义。
### 3 数据影子访存均衡
影子加载/存储复用原内存地址，保证两路访问完全相同缓存行与页，消除TLB、缓存侧信道差异。
### 4 指令齿化对齐PC
32B指令块交替排布在64B对齐内存，两路原始与影子指令共享I-cache行与内存页，屏蔽页面类攻击。
### 5 指令螺旋统一访存PC
分支两路load/store合并至统一公共基本块，通过cmov动态选择操作数，所有访存指令固定PC，抵御AfterImage预取器攻击。

## 实验分析
1. 实验对象：MbedTLS、WolfSSL密码库、Libjpeg图像库，LLVM后端实现x86-64加固。
2. 安全效果：Cache、SQUIP、AfterImage三类攻击成功率由99.75%/92.77%/98.89%降至50%随机水平；所有不平衡指令完全消除。
3. 性能开销：密码库整体运行平均开销2.8%，Libjpeg图像处理因大量分支开销19.3%；二进制体积仅增加0.6%。
4. 场景对比：原生源码平衡的密码库仍存在数十条不平衡指令，经HoBBy加固后无任何泄露点。
5. 通用性：同时适配Intel SGX与AMD SEV两套可信执行环境，无需硬件修改。

## 研究启发
1. 分支侧信道防护不能停留在源码层，必须在编译指令粒度统一指令、访存、PC全部执行特征。
2. 单一维度均衡不足以抵御多类微架构攻击，需同时抹平指令、缓存、预取器、TLB多泄露通道。
3. 编译器自动化加固相比人工常量编程、硬件补丁，通用性与部署成本优势显著。
4. 固定访存PC是抵御预取器类新型攻击关键手段，普通指令均衡无法解决持久硬件状态泄露。
5. 轻量化影子冗余设计可将性能、二进制膨胀控制在极低范围，适配嵌入式、TEE商用密码场景。


### 相关资源

- **Intel SGX SDK**：[https://github.com/intel/linux-sgx](https://github.com/intel/linux-sgx)
- **AMD SEV**：[https://developer.amd.com/sev/](https://developer.amd.com/sev/)
- **LLVM**：[https://llvm.org/](https://llvm.org/)
- **常量时间编程指南**：[https://github.com/veorq/cryptocoding](https://github.com/veorq/cryptocoding)
