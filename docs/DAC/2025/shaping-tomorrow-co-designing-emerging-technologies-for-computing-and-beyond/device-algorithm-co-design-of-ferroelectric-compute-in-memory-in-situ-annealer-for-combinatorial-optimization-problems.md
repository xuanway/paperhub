---
title: "Device-Algorithm Co-Design of Ferroelectric Compute-in-Memory In-Situ Annealer for Combinatorial Optimization Problems"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# Device-Algorithm Co-Design of Ferroelectric Compute-in-Memory In-Situ Annealer for Combinatorial Optimization Problems


<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">DES5: Emerging Device and Interconnect Technologies</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://arxiv.org/abs/2504.21280">https://arxiv.org/abs/2504.21280</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong>组合优化问题，存内计算退火器，增量E变换，双栅铁电场效应晶体管，器件-算法协同设计 </p>
</div>

---

## 研究概要
本文提出基于双栅铁电晶体管(DG FeFET)的存内退火器，软硬件协同设计增量E变换算法，将Ising能量计算复杂度从O(n²)降至O(n)，舍弃指数退火运算。依托背栅可调特性实现片上原位退火，3000节点Max-Cut测试能耗、时延分别降低1716×、8.15倍，求解成功率达98%。

## 背景和动机
1. 组合优化问题可映射Ising模型，传统CiM退火器每轮迭代需O(n²)复杂度VMV矩阵运算，硬件开销巨大。
2. 模拟退火流程依赖e^(-ΔE/T)指数运算，数字电路实现面积、能耗成本极高，制约大规模求解。
3. 常规单栅FeFET无法同步映射权重、自旋与退火温度三类输入，难以一体化完成能量与退火因子计算。
4. 现有退火架构需频繁启动ADC阵列，迭代开销随图节点规模线性暴涨，收敛速度慢、求解成功率偏低。

## 相关工作
1. 数字ASIC退火器：纯数字实现Ising求解，指数电路与大规模矩阵运算带来极高时延能耗，难以扩展。
2. 动态系统Ising机：依靠硬件固有动力学收敛，耦合参数轻微偏移即失效，鲁棒性差。
3. 传统FeFET CiM退火器：单栅器件仅支持三输入乘法，能量计算仍为O(n²)，独立模块计算指数，迭代ADC开销大。
4. ReRAM类优化求解器：存储与计算分离，无法将退火温度嵌入模拟阵列，无法实现原位一体化退火。

## 本文解决方案
### 1. 增量E（E_inc）变换算法
通过自旋翻转差分化简ΔE表达式，将二次VMV运算降为O(n)线性运算；分式函数近似指数退火因子，彻底消除指数硬件电路。
### 2. DG FeFET存内交叉阵列
双栅器件天然实现四输入乘运算，前栅/漏输入自旋向量、背栅映射退火温度，铁电阈值存储耦合权重，单阵列完成E_inc一体化模拟计算。
### 3. 背栅调控原位退火流程
将退火温度映射为背栅模拟电压，随迭代动态调节器件阈值；仅更新翻转自旋对应阵列列，大幅减少ADC读取次数。
### 4. 分层迭代调度逻辑
单次迭代生成新自旋向量，拆分σ_r、σ_c输入阵列，根据E_inc直接判定是否接受新解，仅自旋更新部分走数字通路。

## 实验分析
1. 仿真环境：22nm DG FeFET工艺，以Max-Cut为基准，对比CiM-FPGA、CiM-ASIC两类主流退火架构。
2. 能耗性能：800~3000节点场景能耗降幅401~1716倍，迭代能耗增长远慢于对比方案。
3. 时延指标：求解耗时降低7.98~8.15倍，仅激活更新对应列，削减大量ADC采样延迟。
4. 求解精度：同等迭代次数下本文成功率98%，基线方案仅50%，大规模图收敛优势显著。
5. 可扩展性：支持3000节点超大组合优化问题，优于现有多数Ising求解器规模上限。

## 研究启发
1. Ising求解瓶颈是二次VMV运算，通过自旋差分的增量变换可线性化计算，从算法层降低硬件负载。
2. 双栅FeFET多输入模拟特性是实现能量+退火因子一体化计算的关键，避免数字指数模块开销。
3. 退火温度无需数字电路计算，映射至器件背栅模拟电压可实现片上原位模拟退火。
4. 仅激活翻转自旋对应阵列列，能大幅削减ADC等外设迭代开销，规模越大收益越明显。
5. 器件-算法协同设计可同时兼顾计算复杂度、模拟一体化、收敛效率三重优化，优于单纯硬件或算法改进。