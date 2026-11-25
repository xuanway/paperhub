---
title: "Canopy: Property-Driven Learning for Congestion Control"
description: "EuroSys 2026 · Traffic Engineering, CDNs & Congestion Control · Chenxi Yang (UT Austin), Divyanshu Saxena (UT Austin), Rohit Dwivedula (UT Austi"
tags:
  - "EuroSys2026"
  - "Traffic Engineering, CDNs & Congestion Control"
---

# Canopy: Property-Driven Learning for Congestion Control

**中文标题：** Canopy：面向拥塞控制的属性驱动学习

**所属 Session：** [Session 7.2: Traffic Engineering, CDNs & Congestion Control](index.md) · [EuroSys 2026](../index.md)

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 EuroSys 2026，所属方向：Traffic Engineering, CDNs & Congestion Control。</p>
<p class="paper-seo-summary__tags">EuroSys 2026 · Traffic Engineering, CDNs & Congestion Control</p>
</div>

**作者**：Chenxi Yang (UT Austin), Divyanshu Saxena (UT Austin), Rohit Dwivedula (UT Austin), Kshiteej Mahajan (Google DeepMind), Swarat Chaudhuri (UT Austin), Aditya Akella (UT Austin)

**会议**：EuroSys 2026 · Edinburgh, United Kingdom

**官方资料：** [EuroSys 2026 官方议程](https://2026.eurosys.org/preliminary-program.html) · [ACM 论文 DOI](https://doi.org/10.1145/3767295.3769362)

## 英文摘要

Learning-based congestion controllers offer better adaptability compared to traditional heuristics. However, the unreliability of learning techniques can cause learning-based controllers to behave poorly, creating a need for formal guarantees. While methods for formally verifying learned congestion controllers exist, these methods offer binary feedback that cannot optimize the controller toward better behavior. We improve this state-of-the-art via Canopy, a new property-driven framework that integrates learning with formal reasoning in the learning loop. Canopy uses novel quantitative certification with an abstract interpreter to guide the training process, rewarding models, and evaluating robust and safe model performance on worst-case inputs. Our evaluation demonstrates that unlike state-of-the-art learned controllers, Canopy-trained controllers provide both adaptability and worst-case reliability across a range of network conditions.

## 中文摘要

与传统的启发式方法相比，基于学习的拥塞控制器具有更好的适应性。然而，学习技术的不确定性可能导致基于学习的控制器表现不佳，因此需要形式化保证。尽管已有形式化验证学习型拥塞控制器的方法，但这些方法只提供二值反馈，无法引导控制器优化到更好的行为。我们通过 Canopy 改进这一最先进水平：Canopy 是一个新的属性驱动框架，在学习循环中将学习与形式化推理相结合。Canopy 采用新颖的定量认证与抽象解释器来引导训练过程，对模型给予奖励，并在最坏情况输入下评估模型稳健且安全的性能。我们的评估表明，与最先进的习得控制器不同，经 Canopy 训练的控制器在一系列网络条件下同时具备适应性和最坏情况下的可靠性。

**英文关键词：** Congestion Control, Reinforcement Learning, Machine Learning for Systems, Abstract Interpretation, Formal Verification

**中文关键词：** 拥塞控制、强化学习、面向系统的机器学习、抽象解释、形式化验证

---

[返回 Session](index.md) · [EuroSys 2026 主页](../index.md)
