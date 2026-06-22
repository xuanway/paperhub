---
title: "On Bit-level Reverse Engineering of Vehicular CAN Bus"
description: "DAC 2025 · Security"
tags:
  - "dac-2025"
  - "security"
  - "can-bus"
  - "automotive-security"
  - "reverse-engineering"
  - "tesla"
---

# On Bit-level Reverse Engineering of Vehicular CAN Bus

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">DAC 2025（第62届设计自动化会议）· Security Track · Session: SEC4。针对车载 CAN 总线逆向工程中比特级信号映射的巨大搜索空间挑战，提出首个系统性比特级 CAN 逆向框架，在 Tesla Model 3 上成功识别 43 种车辆控制动作的比特级信号映射，并可部署于 Raspberry Pi 实现轻量级车载安全监控。</p>
<p class="paper-seo-summary__tags">DAC 2025 · Security · CAN Bus · Automotive Security · Reverse Engineering · Tesla · Bit-level</p>
</div>

| 项目 | 详情 |
|------|------|
| 会议 | 第 62 届设计自动化会议（DAC 2025） |
| 论文标题 | On Bit-level Reverse Engineering of Vehicular CAN Bus（车载 CAN 总线的比特级逆向工程） |
| 作者 | Yunlang Cai, Hanxue Shi, Xiaohang Wang, Haoting Shen, Li Lu, Kui Ren |
| 机构 | Zhejiang University（浙江大学） |
| 领域 | 汽车安全 / 嵌入式安全（Automotive Security / Embedded Security） |
| 投稿方向 | Security（Session: SEC4） |
| 关键词 | CAN 总线(CAN Bus)、逆向工程(Reverse Engineering)、汽车安全(Automotive Security)、比特级(Bit-level)、Tesla |
| 核心资源 | [IEEE Xplore](https://ieeexplore.ieee.org/document/11132421/) · 扩展版发表于 IEEE Trans. Computers (2026) |

---

## 一、一句话核心摘要

> CAN 总线是现代汽车的神经中枢——但它缺乏认证/加密，攻击者一旦入侵即可注入恶意帧。防御的前提是**知道每个 CAN ID 和载荷比特对应什么物理控制动作**——但这需要逆向工程，而现有方法只能做到字节级（哪些字节和转向有关），无法精确到比特级（哪个比特控制左转灯）。本文提出首个系统性**比特级 CAN 逆向框架**，通过 Fuzzing 驱动自动化信号映射，在 Tesla Model 3、Leapmotor C10/C11 上实现精准比特级解析，其中 Tesla Model 3 成功识别了 43 种车辆控制动作。

---

## 二、核心方法

### 2.1 比特级逆向的搜索空间挑战

- 典型 CAN 帧：11 位 ID × 8 字节载荷 = 64 个载荷比特
- 每个比特可能独立控制一个功能，也可能与其他比特联合编码（如温度用 8-bit 整数）
- 暴力枚举不可行

### 2.2 方案：Fuzzing 驱动的比特级信号映射

1. **CAN 帧注入**：通过 OBD-II 接口发送不同 ID/载荷组合的 CAN 帧
2. **物理响应观测**：摄像头/传感器捕捉车辆物理响应（灯亮/窗动/锁门等）
3. **相关性分析**：将比特翻转与物理动作变化进行统计关联
4. **比特级映射输出**：输出"ID 0x123, Byte 2, Bit 3 = 左转向灯控制"

### 2.3 实验结果

| 指标 | Tesla Model 3 | Leapmotor C10/C11 |
|------|:----------:|:--------------:|
| 识别动作数 | **43** | 多平台验证 |
| 分辨率 | 比特级 | 比特级 |
| 部署平台 | Raspberry Pi | Raspberry Pi |

---

## 三、总结

该工作将 CAN 逆向工程从"字节级猜测"推进到"比特级精确映射"，为车载入侵检测系统（IDS）提供了精准的信号语义基础。Raspberry Pi 级别的轻量部署意味着该框架可实际集成到车载安全网关中。

**相关资源**：[IEEE Xplore](https://ieeexplore.ieee.org/document/11132421/) · 扩展版：IEEE Trans. Computers (2026)
