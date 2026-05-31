---
title: "PuDHammer: 真实DRAM芯片中PuD读干扰效应实验分析"
description: "ISCA 2025论文解读：PuDHammer首次对真实DRAM芯片中Processing-using-DRAM（PuD）操作引起的读干扰效应进行系统实验分析。"
tags: ["ISCA2025", "Rowhammer", "PuDHammer", "DRAM实验", "读干扰", "ETH Zurich", "Onur Mutlu"]
---

# PuDHammer: Experimental Analysis of Read Disturbance Effects of Processing-using-DRAM in Real DRAM Chips

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">PuDHammer 揭示 PuD（Processing-using-DRAM）操作中行激活模式与标准读操作不同，会引发不同于传统 Rowhammer 的读干扰效应，并通过真实芯片实验量化其危害。</p>
<p class="paper-seo-summary__tags">ISCA 2025 · PuD · Rowhammer · DRAM读干扰 · ETH Zurich · Onur Mutlu</p>
</div>

**作者**：Ismail Emir Yuksel, Akash Sood, Ataberk Olgun, Oğuzhan Canpolat, Haocong Luo, Nisa Bostanci, Mohammad Sadrosadati, Giray Yaglikci, Onur Mutlu  
**机构**：ETH Zurich  
**会议**：ISCA 2025, Tokyo, Japan  
**Session**：Session 5A: RowHammer  

---

## 一句话总结

> PuD（存内计算）操作的激活模式与传统 DRAM 读不同，可引发新型读干扰；PuDHammer 系统量化这一效应，揭示 PuD 架构的安全隐患。

## 背景与动机

- **PuD 兴起**：Processing-using-DRAM（如 Compute DRAM）通过特殊激活序列在 DRAM 内执行逻辑运算
- **读干扰新形式**：PuD 的多行同时激活模式比传统 Rowhammer 更激进，可能导致更严重的位翻转
- **安全性未知**：现有 Rowhammer 分析基于标准读操作，PuD 场景下的安全性未经评估

## 主要贡献

1. **首次系统实验分析**：在商用 PuD 原型上测量不同激活模式下的位翻转率
2. **PuDHammer 攻击**：构造专门利用 PuD 操作触发的 Rowhammer 攻击向量
3. **跨芯片测量**：在多个供应商（Hynix、Samsung、Micron）的 DRAM 芯片上验证
4. **威胁模型**：分析恶意应用程序通过 PuD 指令发动 PuDHammer 的实际可行性

## 实验结果

- PuDHammer 在某些 DRAM 芯片上的位翻转率比标准 Rowhammer 高 **3-10×**
- TRH 门槛降低 **50%**（即更少激活次数即可触发位翻转）

## 关键词

PuD · Rowhammer · DRAM安全 · 存内计算安全 · ETH Zurich · ISCA 2025
