---
title: "ZenLeak: Practical Last-Level Cache Side-Channel Attacks on AMD Zen Processors"
description: "DAC 2025 · Security"
tags:
  - "dac-2025"
  - "security"
  - "amd-zen"
  - "llc"
  - "cache-side-channel"
  - "reverse-engineering"
---

# ZenLeak: Practical Last-Level Cache Side-Channel Attacks on AMD Zen Processors

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">SEC3: Hardware Security: Attack & Defense</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://yinqian.org/papers/dac25b.pdf">https://yinqian.org/papers/dac25b.pdf</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 侧信道攻击，非包容缓存，缓存寻址反向工程，驱逐集构建，AMD Zen处理器 </p>
</div>

---

## 研究概要
本文提出ZenLeak，面向AMD Zen系列非包容性缓存的跨核LLC缓存侧信道攻击。逆向L2/L3切片与索引哈希函数，设计适配AMD的驱逐集构造算法，利用信号触发私有缓存驱逐，提出Prime+Signal+Probe攻击。在Ryzen 9 5900X攻破OpenSSL AES-T表，多轮投票密钥恢复准确率达100%。

## 背景和动机
1. Intel/ARM非包容性缓存已有目录类缓存攻击，但AMD Zen采用分片影子标签目录，现有攻击完全失效，其LLC安全性长期存疑。
2 AMD缓存寻址哈希未公开，缺乏成熟逆向手段，无法构造有效缓存驱逐集，跨核无法驱逐受害者私有L2缓存，传统Prime+Probe不适用。
3 现有驱逐集生成算法适配Intel架构，在AMD上产生大量假阳性/假阴性，无法精准锁定同LLS集合地址。
4 缺乏能跨核、无共享内存依赖的AMD缓存攻击方案，AES查表等密码实现存在未被证实的硬件泄露风险。
5 软件缓存防护通用性差，硬件随机/分区方案商用普及率低，亟需验证AMD缓存真实漏洞风险。

## 相关工作
1 包容性缓存Prime+Probe：仅适用于Intel inclusive架构，无法迁移至AMD非包容性设计。
2 Intel/ARM非包容目录攻击：依托共享扩展目录冲突，AMD分片影子标签无全局共享目录，攻击失效。
3 缓存寻址逆向：Intel依赖PMU事件，AMD无对应硬件计数；现有AMD逆向耗时数十小时，效率极低。
4 驱逐集构造：Intel方案利用L2/L3切片分离特性，AMD同L2地址必映射同一LLC切片，产生误判。
5 Flush+Spec等攻击：要求攻击者与受害者共享内存，攻击门槛远高于无共享的Prime类方案。

## 本文解决方案
### 1 优化AMD缓存寻址逆向算法
加入预热分核刷新流程，消除时序区分不足问题；通过地址比特翻转统计矩阵，逆向L3切片、L2索引、L3索引三套XOR哈希函数，逆向时长由23小时缩短至30分钟。
### 2 双层过滤驱逐集生成算法
先筛选同L2集合地址作为占用集，再二次过滤得到L3驱逐集，规避AMD架构假阳性缺陷；支持4KB/1GB大页两种内存粒度。
### 3 信号驱动私有缓存驱逐机制
利用进程信号触发上下文切换，仅清空L2私有缓存、数据留存LLC，解决跨核无法驱逐受害者私有缓存核心难题。
### 4 Prime+Signal+Probe攻击流程
1. 填充目标LLC集合；2. 发送信号清空受害者L2；3. 遍历驱逐集测访问时延，根据缺失频率判断受害者查表行为。
### 5 多数投票密钥恢复策略
多次采集缓存缺失模板，投票筛选高置信字节，消除单次测量噪声，实现AES完整密钥还原。

## 实验分析
1 实验平台：AMD Ryzen 9 5900X（Zen3），测试4KB、1GB两种内存大页，目标OpenSSL AES-T表。
2 驱逐集成功率：1GB大页7轮累积成功率98%，4KB页面8轮达78%，构造稳定性良好。
3 攻击精度：4KB页面仅需16轮投票即可100%恢复单密钥字节；1GB直接选驱逐集需22轮，算法构造需30轮。
4 硬件机理验证：信号仅驱逐L2、LLC数据保留，时延曲线证实可区分受害者查表痕迹。
5 漏洞披露：成果已同步AMD PSIRT厂商，官方确认该架构安全隐患真实存在。

## 研究启发
1 AMD非包容性分片影子目录并非安全屏障，依靠信号驱逐私有缓存可绕过目录隔离实现LLC侧信道窃取。
2 不同厂商缓存寻址、目录硬件差异巨大，Intel缓存攻击方案无法直接移植，必须定制逆向与驱逐集算法。
3 进程信号上下文切换是AMD独有泄露辅助通路，系统侧缓存防护需管控跨进程信号调度风险。
4 大页内存能大幅简化驱逐集构造、提升攻击精度，高安全密码程序应规避大页优化。
5 仅依赖软件缓存脱敏难以完全抵御架构级硬件泄露，处理器厂商需部署缓存随机化等硬件防护。