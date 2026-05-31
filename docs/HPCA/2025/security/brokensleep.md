---
title: "BrokenSleep: 远程处理器Idle状态电源时序攻击"
description: "HPCA 2025论文解读：BrokenSleep发现处理器Idle State（C-state）转换的电源消耗具有可测量的时序特征，可被远程攻击者利用来推断目标CPU的工作负载信息。"
tags: ["HPCA2025", "硬件安全", "侧信道攻击", "电源分析", "C-state", "远程攻击", "DGIST"]
---

# BrokenSleep: Remote Power Timing Attack Exploiting Processor Idle States

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">BrokenSleep 揭示了处理器 Idle State（C-state）深浅转换的时序特征可被网络时序测量推断，攻击者无需物理接触即可通过远程网络请求的响应时间，推断目标 CPU 的实时工作负载状态，从而实现跨虚拟机信息泄露。</p>
<p class="paper-seo-summary__tags">HPCA 2025 · 侧信道攻击 · C-state · 电源时序 · 远程攻击 · 云安全</p>
</div>

**作者**：Hyosang Kim, Ki-Dong Kang, Gyeongseo Park, Seungkyu Lee, Daehoon Kim  
**机构**：DGIST; Yonsei University  
**会议**：HPCA 2025, Las Vegas, NV, USA  

---

## 一句话总结

> 处理器 C-state（空闲节能状态）的退出延迟（C-state exit latency）会暴露为网络响应时间的抖动；BrokenSleep 将此抖动建模为侧信道，通过远程精密计时攻击推断云服务器上其他 VM 的秘密信息。

## 背景与动机

- **C-state 背景**：现代 CPU 在无工作负载时进入深度节能状态（C6/C7 可节省 90%+ 功耗），但从深 C-state 恢复需要 200μs ～ 1ms 的退出延迟
- **信息泄露路径**：攻击者 VM 周期性向目标 VM 发送网络探包，观察响应时间。若目标 VM 刚从 C-state 唤醒（被其他 VM 的负载影响），响应时间会有 200μs+ 的额外延迟
- **跨 VM 推断**：同一物理主机上，攻击者 VM 可通过观察目标 VM 的 C-state 退出时刻，推断目标 VM 的请求到达模式

## 方法详解

### 攻击模型

1. **探包发送**：攻击者 VM 以高频（1kHz）向目标 VM 发送 ICMP/TCP 探包
2. **时序测量**：精确记录每次探包的往返时延（RTT）
3. **C-state 推断**：RTT > 阈值（约 500μs）时，推断目标 VM 处于 C-state 并被本探包唤醒
4. **负载推断**：通过 C-state 进入频率推断目标 VM 的实时请求率和负载强度

### 密钥推断攻击

- 若目标 VM 运行密码学操作（如 RSA 解密），负载的规律性与密钥相关
- 攻击者通过 C-state 时序序列与密码学操作模式匹配，在实验中成功推断 1024-bit RSA 私钥的部分 bits

## 实验结果

| 攻击场景 | 推断准确率 | 条件 |
|---------|----------|------|
| C-state 进入检测 | 94.7% | 局域网，同主机 |
| 请求率推断（1～100 RPS） | 误差 < 5% | AWS EC2 同区域实例 |
| AES 密钥区分（128-bit） | 78% bits 正确 | 受控实验环境 |

## 核心亮点

1. 首个利用 C-state 退出延迟的远程侧信道攻击，无需物理访问
2. 可在真实云平台（AWS EC2）上实施，具有现实威胁性
3. 揭示了 CPU 节能机制与安全性之间的根本冲突

## 防御建议

- 禁用深度 C-state（C6/C7），代价是功耗显著增加
- 引入随机 C-state 退出延迟噪声（约 ±2ms）可有效降低攻击精度
- 操作系统级别的 C-state 调度策略与租户隔离结合
