---
title: "RUPlace: Optimizing Routability via Unified Placement and Routing Formulation"
description: "DAC 2025 · EDA"
tags:
  - "DAC2025"
  - "EDA"
---

# RUPlace: Optimizing Routability via Unified Placement and Routing Formulation

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">EDA7: Physical Design and Verification</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://yibolin.com/publications/papers/PLACE_DAC2025_Chen.pdf">https://yibolin.com/publications/papers/PLACE_DAC2025_Chen.pdf</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 统一布局布线，可布线性优化，交替方向乘子法，凸单元膨胀 </p>
</div>


---

## 研究概要
本文提出RUPlace布线友好全局布局统一优化框架，构建布局-路由联合整数规划模型，基于ADMM双层优化搭配Wasserstein距离正则；设计模块化聚类凸单元膨胀与局部面积微调策略。在CircuitNet、Chipyard基准测试，相较OpenROAD横向拥塞降低4.74倍，运行速度提升3.67倍，布线线长优化7%。

## 背景和动机
1. 先进工艺电路规模激增，布线拥塞成为布局核心瓶颈，传统工具仅做单向布局后估算路由，割裂二者内在耦合关系。
2. 现有单元膨胀方案依赖人工启发式调参，缺少严谨凸优化理论支撑，拥塞缓解效果不稳定。
3. 统计/ML拥塞预测将路由视作黑盒，无法显式建模布线流量与网格容量约束，指导精度有限。
4. 传统力导向布局仅简单加权线长，不能真实反映全局路由溢出带来的拥塞损失。
5. KL散度等分布度量在无重叠网格下失效，难以精准约束单元移动带来流量分布突变。

## 相关工作
1. 启发式单元膨胀布局(Xplace、NTUPlace4)：基于拥塞图放大单元，无凸优化建模，泛化性差。
2 DREAMPlace系列深度学习布局：GPU加速但仅采用RUDY简易拥塞预估，未联合路由完整数学模型。
3. 统计拥塞预测工具：概率模型速度快，但无法刻画完整布线流约束，优化导向弱。
4. ML路由预测(RouteNet)：数据驱动黑盒模型，缺少布局-路由耦合数学表达。
5. 独立全局路由工具：仅完成布线分配，无法反向迭代优化单元位置。

## 本文解决方案
### 1 布局-路由统一整数规划UCP模型
同时最小布线总长与网格容量溢出拥塞，以引脚流量守恒方程耦合布局坐标与路由流量变量，完整建立双向优化目标。
### 2 ADMM双层迭代优化框架
外层解析布局更新单元坐标；内层求解全局路由得到流量场；引入Wasserstein距离做流量分布正则，解决KL散度失效问题，梯度下降求解子问题。
### 3 超图模块化分层聚类
基于电路逻辑层次与超图模块度合并高互联单元簇，为全局膨胀提供分组依据，避免零散单元缩放。
### 4 凸优化全局单元膨胀
以簇内布线总长为目标、网格路由容量为约束构造凸规划，求解最优膨胀系数，统一放大高拥塞模块释放布线空间。
### 5 Gcell粒度局部面积迭代微调
区分簇内、跨网路由需求动态增减单元尺寸，迭代至全局拥塞低于阈值，精细消除局部残留溢出。

## 实验分析
1. 测试环境：14nm工艺，CircuitNet/Chipyard七组工业基准，对比OpenROAD、Xplace2.0、DREAMPlace4.1。
2. 拥塞指标：几何均值横向拥塞降4.74倍、纵向降3.47倍，绝大多数设计全局拥塞控制在1%以内。
3. 线长与效率：相对OpenROAD布线总长优化7倍，运行提速3.67倍；对比Xplace/DREAMPlace线长小幅增加，但拥塞优势显著。
4. 可视化对比：同VORTEX_S设计，RUPlace拥塞区域数量、峰值溢出远少于三款基线工具。
5. 适配场景：NVDLA、GEMMINI等大规模加速器、RISC-V处理器均能稳定大幅缓解布线溢出。

## 研究启发
1. 布局与路由不可拆分，统一联合数学模型可从根源消除迭代优化信息断层。
2. Wasser距离适配网格流量分布约束，相比KL散能有效处理单元大幅移动后的流量偏移。
3. 单元膨胀不能简单全局统一缩放，结合超图聚类+凸优化可精准匹配模块拥塞程度。
4. 双层ADMM分解高维耦合联合问题，将布局、路由拆分为可高效求解的独立子问题。
5. 布局评估不能只看线长，拥塞是决定后端可绕性的核心指标，适度线长换取极低溢出具备工程价值。