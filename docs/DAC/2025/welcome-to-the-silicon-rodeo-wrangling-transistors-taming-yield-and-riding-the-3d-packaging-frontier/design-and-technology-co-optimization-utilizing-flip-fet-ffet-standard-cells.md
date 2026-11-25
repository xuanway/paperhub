---
title: "Design and Technology Co-optimization Utilizing Flip-FET (FFET) Standard Cells"
description: "DAC 2025 · EDA"
tags:
  - "DAC2025"
  - "EDA"
---

# Design and Technology Co-optimization Utilizing Flip-FET (FFET) Standard Cells

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">EDA8: Design for Manufacturing and Reliability</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11132817">https://dl.acm.org/doi/10.1109/DAC63849.2025.11132817</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> 互补场效应晶体管，鳍式场效应晶体管，标准单元，设计技术协同优化，物理设计 </p>
</div>


---

## 研究概要
本文面向3nm以下FFET堆叠器件提出DTCO协同优化流程，设计多引脚分布标准单元生成器，布局阶段单元替换消除Tap单元，双层布线拥塞均衡。7nm ASAP工艺测试，FFET单元相较CFET面积缩减20%~25%，完整流程相比传统CFET流片面积降26%，布线DR违规大幅减少，总线长降低9%。

## 背景和动机
1. CFET垂直堆叠器件仅正面可用信号金属，背面布线需大量Tap通孔连接引脚，占用面积、增大延迟与布线拥塞。
2. FFET翻转堆叠结构可双面引出引脚，但缺少配套标准单元生成与顶层物理设计协同DTCO方案。
3. 现有CFET单元生成仅单一引脚排布，无法通过单元选型规避双面跨层网线，大量DS双面网线加剧资源紧缺。
4. 传统布局布线未区分前后金属层负载，单侧拥塞严重，M2/M3高层金属耗尽引发海量设计规则违例。
5. 缺乏面向FFET的三层协同流程：单元库生成、布局单元替换、双层网线均衡分配，难以释放背面布线增益。

## 相关工作
1. FinFET标准单元生成：仅单层金属架构，不支持双面BEOL与堆叠器件适配。
2. CFET单元合成工具CFET-fp：仅固定引脚位置，无法生成多排布单元，不可消除Tap单元开销。
3. 背面布线网划分方法：仅在网表阶段分割网线，无法利用单元引脚自由度，Tap数量难控制。
4. ECO背面修复方案：后置修改代价高，无法从布局源头减少跨层双面网线。
5. 堆叠器件DTCO研究：仅优化单元面积，未联动布局布线缓解双层布线拥塞。

## 本文解决方案
### 1 多类型FFET标准单元综合
基于OpenROAD晶体管布局，支持栅合并缩小单元；采用SMT求解内布线，生成四类引脚排布单元：全正面、全背面、均衡、交换均衡，仅FM/BM两层金属完成单元内部走线。
### 2 布局阶段无Tap单元替换算法
贪心策略优先处理高HPWL多引脚单元，遍历四类单元选型，最小化DS双面网线数量，从源头消除Tap通孔需求，不破坏原有布局密度。
### 3 双层布线拥塞均衡重分配
仅修改2引脚单元引脚侧，在不新增DS网线前提下，将局部拥塞区域网线分配至空闲金属层，平衡前后层布线资源占用。
### 4 完整FFET-DTCO协同流程
单元库生成→布局单元替换优化→双层网线均衡，接入商用DC/Innovus工具链，原生兼容7nm ASAP工艺规则。
### 5 多目标SMT单元内布线模型
依次最小金属总长、通孔数量、优先指定引脚层、均衡双面引脚数量，兼容EOL、MPL全套先进工艺规则。

## 实验分析
1. 实验环境：ASAP7nm工艺，AES/FPU/USB等开源基准，对比传统CFET流、单纯FFET无DTCO流、本文完整DTCO流。
2 单元层面：2.5T/3.5T FFET相较同轨CFET面积分别降25%、20%，单元内线长减少31%、13%，无需高层金属。
3 芯片面积：单纯FFET相比CFET缩减26%，本文DTCO流程维持面积优势。
4 布线指标：DS双面网线平均下降63%，DR违规数量相较普通FFET方案减少67%，总线长降低9%。
5 开销对比：传统CFET流程存在大量Tap单元，本文方案全程无需引入Tap通孔，布线资源压力显著缓解。

## 研究启发
1. FFET器件核心优势是双面引脚自由排布，DTCO必须打通单元库-布局-布线三层协同才能发挥背面布线价值。
2. 仅依靠网表分割无法根除Tap开销，多引脚样式单元替换是消除双面跨层网线的低成本手段。
3. 堆叠器件单元设计需优先支持栅合并、双面内部走线，彻底放弃M2/M3可大幅释放芯片布线资源。
4. 双层布线拥塞均衡应限制仅调整简单2引脚单元，避免新增DS网线抵消优化收益。
5. 先进堆叠工艺不能仅优化器件版图，单元库多样性与顶层物理设计联动是DTCO关键优化路径。
