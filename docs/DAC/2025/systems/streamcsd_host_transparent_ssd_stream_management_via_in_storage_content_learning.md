---
title: "StreamCSD: Host-Transparent SSD Stream Management via In-Storage Content Learning"
description: "DAC 2025 · Systems"
tags:
  - "DAC2025"
  - "Systems"
---

# StreamCSD: Host-Transparent SSD Stream Management via In-Storage Content Learning

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">SYS5: Embedded Memory and Storage Systems</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://ieeexplore.ieee.org/document/11133202">https://ieeexplore.ieee.org/document/11133202</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong>流管理，内容学习，计算存储驱动器，写放大 </p>
</div>

---

## 研究概要
本文提出StreamCSD面向计算型SSD实现无主机参与自主流管理。以压缩率/香农熵为数据特征，轻量化流式K-means完成内容聚类，搭配GC重映射、生命周期二级映射优化混合寿命页面。仿真与PCIe5硬件实测，多模态AI负载下写放大由1.7降至1.06，吞吐量最高提升74%，无需修改主机系统。

## 背景和动机
1. 传统块接口SSD无法区分不同生命周期页面，GC迁移大量有效页产生高写放大，硬件预留开销大，存在块接口损耗问题。
2. 现有多流方案（ZNS、PCStream、AutoStream等）均需修改应用/内核下发流标识，大规模存量块SSD难以部署。
3. 基于LBA时序聚类依赖历史IO轨迹，日志型数据库场景效果差，且占用SSD控制器大量算力内存。
4. 传统文本TF-IDF等内容聚类维度高、延迟大，不适合SSD写通路实时页面分类，缺少通用低开销内容特征。
5. 仅靠压缩率聚类存在同压缩率不同生命周期、多学习流超过物理流数量两类缺陷，缺少配套修正机制。

## 相关工作
1. 开放通道/ZNS SSD：暴露闪存底层，主机承担GC、块管理，系统改造成本极高，存量设备不兼容。
2. 主机辅助多流（PCStream/FStream）：依托程序上下文/文件类型下发流ID，必须修改驱动或业务代码。
3. LBA时序聚类AutoStream/MiDAS：依靠读写频率、更新间隔划分冷热，动态混合负载精度下滑，控制器开销高。
4. 传统内容聚类TF-IDF：高维向量计算，单页聚类毫秒级延迟，无法适配SSD实时写入流水线。
5. 人工标注多流ManualStream：性能最优，但依赖开发者手动区分数据，通用性极差。

## 本文解决方案
### 1 无主机透明内容学习整体架构
完全兼容标准NVMe块接口，SSD内部硬件加速器提取页面压缩率/熵特征，自主划分数据流，主机、应用零修改。
### 2 硬件轻量化特征提取单元
已有压缩器复用压缩率；无压缩器则部署极简香农熵加速器，仅占芯片1%面积，256字节采样即可达到98%熵精度。
### 3 无等待流式K-means聚类
页面实时分配流ID，批量后台更新聚类中心，写通路无阻塞，适配连续高速写入负载。
### 4 GC反馈页面重映射机制
统计页面GC迁移次数，设置双阈值区分普通/冷/冻结流，将超长寿命异常页隔离，降低同流寿命方差。
### 5 生命周期辅助二级流映射
统计各学习流平均页面寿命，将寿命相近学习流合并至有限物理流，解决学习流数量超限问题。

## 实验分析
1. 实验平台：FEM全系统仿真、PCIe 5.0 7.68TB硬件原型；负载包含Microbench、RocksDB、MySQL、SQLite与多模态生成AI数据集。基线为SingleStream、AutoStream、PCStream、MiDAS、ManualStream。
2. 写放大优化：通用负载写放大平均降低63.4%；生成AI多模态场景WAF从1.7降至1.06，GC页面迁移占比从38%降至4%。
3. 吞吐量提升：Microbench提升74%、RocksDB提升11%、MySQL提升25%、SQLite提升11%，仅小幅损耗写带宽。
4. 消融验证：GC重映射对混合冷热数据库可再降20%左右写放大；生命周期二级映射解决多流溢出场景性能衰减。
5. 硬件开销：流式K-means单页分配仅275ns，随机写带宽仅下降11.6%，熵加速器芯片面积可忽略。

## 研究启发
1. 依靠数据压缩率、熵作为通用内容特征，可实现完全不依赖主机的自主数据流划分，适配存量标准块SSD。
2. 存储内学习必须硬件轻量化，复用已有压缩单元或极简熵计算单元，才能避免写入延迟恶化。
3. 纯内容聚类存在寿命匹配缺陷，需要GC运行时反馈机制动态隔离冷热异常页面。
4. 物理流硬件数量有限，基于页面生命周期的合并策略可高效压缩流数量，不损失写放大优化效果。
5. 面向生成式AI图文音视频混合负载，基于内容特征的多流方案相比时序LBA聚类具备显著优势。