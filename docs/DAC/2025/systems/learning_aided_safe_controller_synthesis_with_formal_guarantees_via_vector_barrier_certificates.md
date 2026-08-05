---
title: "Learning-Aided Safe Controller Synthesis with Formal Guarantees via Vector Barrier Certificates"
description: "DAC 2025 · Systems"
tags:
  - "DAC2025"
  - "Systems"
---

# Learning-Aided Safe Controller Synthesis with Formal Guarantees via Vector Barrier Certificates

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">SYS1: Autonomous Systems (Automotive, Robotics, Drones)</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11132490">https://dl.acm.org/doi/10.1109/DAC63849.2025.11132490</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong>控制器综合，安全验证，向量屏障证书，强化学习，平方和 </p>
</div>

---

## 研究概要
本文提出LASAC-VBC方法，融合强化学习、PAC近似与向量障碍证书(VBC)，面向安全关键非线性系统合成带形式化保障控制器。采用Skip多项式网络学习原始约束下VBC，搭配增量SOS后置验证，无需松弛约束丢失可行解。10组基准测试表明，相较SOSTOOLS单障碍证书，验证更快且高维系统可成功求解。

## 背景和动机
1. 深度学习控制器仿真性能优秀，但缺少严格形式安全证明，难以用于自动驾驶、工业控制等安全关键场景。
2. 传统标量障碍证书表达能力有限，向量障碍证书可拓展可验证系统范围，但原生约束非凸。
3. 现有VBC求解为恢复凸性强制松弛析取条件，缩小可行解域，大量合法证书无法被求出。
4. 已有方案需人工指定本质非负矩阵A，无通用自动构造手段，落地门槛高。
5. 现有工作分开控制器合成与VBC验证，缺少从学习控制到形式化校验的端到端一体化流程。

## 相关工作
1. 标量障碍证书(SOS/SOSTOOLS)：基于平方和规划求解单一障碍函数，对复杂、高维非线性系统验证极易失败。
2. 向量障碍证书基础理论：提出多函数联合安全判定，但求解时强制放宽VBC2约束，丢失可行解，矩阵A手动配置。
3. 强化学习控制：DDPG等可生成连续域神经网络控制器，但无配套形式安全验证链路。
4. PAC场景优化：用于无限约束近似求解，仅用于控制拟合，未结合障碍证书安全验证。
5. 神经网络障碍学习：仅对标量BC设计网络，不支持向量多证书联合学习。

## 本文解决方案
### 1 强化学习+PAC多项式控制器生成
采用DDPG训练安全导向深度控制器，设计距离惩罚奖励；基于PAC场景优化采样无限约束，拟合低阶多项式控制器，便于后续形式验证。
### 2 Skip多项式向量BC学习网络
设计残差跳跃多项式网络批量学习多障碍函数与非负矩阵A；构造三合一损失函数，同步满足VBC1/VBC2/VBC3全部原始约束，无需松弛。
### 3 增量SOS后置验证框架
分层转化三类VBC条件为半定规划：初始/李导数约束批量SOS优化，不安全集析取约束迭代极小值判定，严格证明学习得到的B满足安全充要条件。
### 4 端到端LASAC-VBC完整流水线
先学习可拟合多项式控制器，再训练向量障碍证书候选，最后SDP形式校验，输出具备数学安全保证的控制策略。

## 实验分析
1. 测试环境：AMD双路CPU+RTX A6000，10组标准非线性控制基准，维度覆盖2~12阶。
2. 可求解性：LASAC-VBC全部10例均可生成有效VBC；传统SOSTOOLS无法验证7/9/12维3个高维案例。
3. 验证效率：同维度可解案例中，VBC验证耗时远低于标量BC，所用多项式阶数更低。
4. 表达能力：多低阶向量BC组合，等效甚至优于高阶单一标量障碍函数，降低SDP计算开销。
5. 消融对比：移除Skip网络或原始约束损失后，VBC训练极易不收敛，验证成功率大幅下降。

## 研究启发
1. 学习算法与形式化验证可深度协同，RL负责生成高性能控制策略，向量障碍证书提供严格安全数学证明。
2. 向量障碍证书不能简单松弛非凸约束，采用神经网络原始约束预筛选，可保留全部可行解空间。
3. Skip多项式网络适配障碍函数结构，相比纯平方网络表达更强，便于后续SOS校验。
4. 低阶多向量证书优于高阶单证书，能显著降低半定规划求解复杂度，提升高维系统验证能力。
5. 端到端流水线打通学习控制与形式安全证明，可落地工业安全关键非线性控制系统设计。