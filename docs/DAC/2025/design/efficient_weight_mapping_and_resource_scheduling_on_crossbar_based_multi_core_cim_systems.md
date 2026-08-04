---
title: "Efficient Weight Mapping and Resource Scheduling on Crossbar-based Multi-core CIM Systems"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# Efficient Weight Mapping and Resource Scheduling on Crossbar-based Multi-core CIM Systems


<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">DES2B: In-memory and Near-memory Computing Architectures, Applications and Systems</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://ieeexplore.ieee.org/document/11132743">https://ieeexplore.ieee.org/document/11132743</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong>存内计算，卷积神经网络，编译器，权重映射，资源调度 </p>
</div>


---

## 研究概要
本文面向eFlash多核交叉阵列CIM片上系统，设计配套编译层权重映射与资源调度方案。构建多层硬件抽象模型，提出进化式资源调度、ILP加权扩展权重映射。在Yolov5、ResNet等网络实测，整体延迟降低76%，硬件资源利用率提升30%，交叉阵列最高利用率达94.7%。

## 背景和动机
1. 冯诺依曼架构存在内存墙，交叉阵列CIM可原位并行MAC，但多核大规模CIM缺少自动化部署编译工具，需人工调参部署CNN。
2. 现有CIM编译多面向小核架构，权重拆分带来多核求和、量化误差；大核阵列下权重排布松散，阵列利用率极低。
3. 卷积滑动窗口计算存在层间算力瓶颈，传统顺序权重映射未区分各层计算负载差异，整体时延居高不下。
4. 多核CIM存在片上多级缓存、核间NoC通信开销，现有调度策略未统筹各级带宽与存储资源，数据搬移延迟严重。

## 相关工作
1. 小核CIM编译框架：依靠权重分块多核并行，但多核拼接引入额外运算与量化误差，不适合eFlash大核场景。
2. OMM重叠权重映射：仅简单复用输入减少补零，未结合整数规划优化阵列空间，无法针对卷积瓶颈层倾斜资源。
3. 线性顺序映射：按网络顺序存放权重，阵列空白区域多，资源浪费严重，无全局空间最优求解。
4. 基础CIM调度：仅静态分配硬件，未采用进化算法遍历数据流最优解，难以平衡多级缓存带宽瓶颈。

## 本文解决方案
### 1. 四层多核CIM硬件抽象模型
芯片-核心-MCU-交叉阵列分层架构，定义全局/核间/核内三级缓存，异步多核触发同步机制，统一编译建模底层硬件资源。
### 2. 进化式多级资源调度算法
基于剩余资源概率划分计算子图，进化迭代最小化总时延；分级分配L0/L1/L2缓存，优先就近分配存储削减跨核数据传输。
### 3. ILP加权扩展权重映射
以整数规划求解权重排布最小空白；融合类OMM重叠输入减少零填充；设计卷积滑动窗口奖励函数，向瓶颈层倾斜阵列资源。
### 4. 宏级权重复制并行策略
跨核复制权重提升多核并行度；单阵列对角复制权重，结合窗口数据复用降低补零开销，大幅提升阵列有效算力。

## 实验分析
1. 实验平台：自研4核eFlash CIM SoC，4MB全局缓存，1152×960交叉阵列；基准为线性调度、基础OMM映射，测试Yolov5/ResNet50/Unet等。
2. 资源收益：计算与存储资源利用率最高提升30%，芯片流水线数量显著减少，各级缓存负载均衡。
3. 阵列利用：ILP+加权扩展组合方案交叉阵列利用率最高94.7%，相比纯OMM提升12%以上。
4. 时延指标：单模型整体延迟平均下降76%，卷积瓶颈层MVM计算时延降低42%。
5. 消融对比：调度与映射二者缺一不可，仅单独优化一项性能提升幅度不足35%。

## 研究启发
1. 大核与小核CIM编译优化路线完全不同，小核侧重分块并行，大核需全局权重空间规划减少空白。
2. 卷积层滑动窗口迭代次数是核心瓶颈，映射算法必须加入分层加权机制，倾斜阵列资源给重负载层。
3. 多核CIM时延由多级缓存带宽共同决定，仅优化计算阵列无法治本，需进化搜索最优子图与缓存分配方案。
4. 权重复制是低成本提升并行度的手段，搭配输入重叠映射可大幅消除零填充带来的阵列资源浪费。
5. 面向非易失大阵列CIM需软硬件协同，硬件抽象层是自动化编译工具链的基础前置条件。