---
title: "IntraFuzz: Coverage-Guided Intra-Enclave Fuzzing for Intel SGX Applications"
description: "DAC 2025 · Security"
tags:
  - "dac-2025"
  - "security"
  - "intel-sgx"
  - "fuzz-testing"
  - "tee"
  - "vulnerability-discovery"
---

# IntraFuzz: Coverage-Guided Intra-Enclave Fuzzing for Intel SGX Applications

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">SEC2: Hardware Security: Primitives & Architecture, Design & Test</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11132848">https://dl.acm.org/doi/10.1109/DAC63849.2025.11132848</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 飞地内模糊测试，SGX安全，覆盖率引导，漏洞检测 </p>
</div>

---

## 研究概要
本文提出IntraFuzz，首款完全在硬件SGX飞地内执行的覆盖率导向模糊测试框架。基于LibOS解决飞地多进程、监控隔离难题，设计共享内存通信与AEX异常捕获机制。在21款真实SGX程序实测，复现全部已知漏洞并新增6个未披露内存缺陷，平均代码覆盖率相较基线提升2.9%。

## 背景和动机
1. 现有SGX模糊工具仅在模拟器或宿主侧测试ECALL/OCALL边界，无法进入硬件飞地内部挖掘应用层内存漏洞，模拟环境缺失远程认证等硬件特性。
2. SGX硬件隔离机制阻断外部调试监控，传统插桩、崩溃捕获手段失效，难以收集飞地内执行路径与崩溃栈信息。
3. 飞地内存容量受限、跨边界ECALL/OCALL通信开销巨大，多进程并行模糊难以落地，测试效率低下。
4. 大量移植至SGX的C/C++程序存在溢出、野指针等内存缺陷，模拟器测试无法复现硬件专属漏洞，安全验证存在盲区。
5. 现有工具无法区分飞地边界漏洞与内部业务代码漏洞，难以定位可信计算核心安全隐患。

## 相关工作
1. 边界模糊工具(SGXFuzz、EnclaveFuzz、FuzzSGX)：仅面向宿主与飞地交互接口，运行于模拟环境，不进入飞地内部，遗漏内部代码漏洞。
2. SEnFuzzer：程序跑在硬件飞地，但模糊引擎在外部，仅采集接口信息，无内部路径覆盖追踪。
3. 符号执行TEERex/COIN/SymGx：依赖静态分析，难以生成海量变异输入，无法覆盖深层执行路径。
4. 飞地运行时监测工具(SgxMonitor)：仅做运行态溯源，不具备自动输入生成与漏洞挖掘能力。
5. 通用模糊器(Honggfuzz)：原生不兼容SGX隔离、AEX异步退出机制，无法直接用于飞地内测试。

## 本文解决方案
### 1 飞地内置LibOS支撑层
基于Occlum改造库操作系统，提供加密文件系统、进程调度，绕过SGX fork限制，使用spawn创建并行测试进程，支持256GB EPC大内存场景。
### 2 飞地内共享内存多进程管理
2048字节共享内存块划分执行状态、信号、栈回溯三区，父子工作组绑定内存索引，低开销同步运行时信息，解决飞地进程隔离通信难题。
### 3 AEX异常捕获与信号跳板
注册自定义信号处理函数，崩溃触发异步飞地退出时自动保存栈、PC、内存映射至共享内存，分析器解析后下发恢复信号继续迭代测试。
### 4 自适应栈崩溃去重机制
结合信号类型、指令页内偏移、指令字节、调用栈哈希四元组唯一标识崩溃，过滤重复崩溃样本，精准识别全新漏洞。
### 5 飞地内覆盖率导向变异引擎
改造Honggfuzz内核，全部种子存储于飞地加密文件系统，仅在可信域完成输入变异、路径采集，不依赖宿主侧监控。

## 实验分析
1. 实验平台：Xeon铂金8444H服务器，256GB飞地页缓存，21款开源SGX应用，单程序模糊时长24小时。
2. 漏洞挖掘：总计发现9个可验证漏洞，其中6个是模拟器工具无法检测的飞地内部溢出、越界、双重释放缺陷。
3. 代码覆盖：平均覆盖率17.7%，对比EnclaveFuzz的14.8%提升2.9%，加密、聚类等业务代码覆盖提升显著。
4. 对比基准：SGXFuzz、EnclaveFuzz仅能发现接口类漏洞，无法识别纯飞地业务内存错误；IntraFuzz支持远程认证硬件场景漏洞检测。
5. 性能：多进程共享内存通信大幅降低ECALL交互频次，单轮模糊耗时相较外部工具降低41%。

## 研究启发
1. SGX安全验证不能仅测试宿主-飞地接口，必须在真实硬件飞地内部开展全代码模糊，模拟器存在大量漏洞盲区。
2. SGX硬件隔离带来监控、进程两大核心障碍，配套LibOS与飞地原生共享内存是落地内部模糊的关键。
3. AEX异步退出机制是崩溃捕获核心难点，需基于信号跳板设计栈信息持久化方案才能完成漏洞溯源。
4. 区分边界漏洞与飞地业务漏洞对可信软件审计至关重要，内部模糊可直接保护密钥、加密核心逻辑。
5. 覆盖率引导模糊可适配各类SGX加密、机器学习、钱包应用，是TEE软件硅前/上线前自动化安全验证有效手段。

---

## 相关资源

- [Intel SGX SDK](https://github.com/intel/linux-sgx) 
