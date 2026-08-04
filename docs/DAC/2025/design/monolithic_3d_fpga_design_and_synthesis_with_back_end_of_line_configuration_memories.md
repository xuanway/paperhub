---
title: "Monolithic 3D FPGA Design and Synthesis with Back-End-of-Line Configuration Memories"
description: "DAC 2025 · Design"
tags:
  - "DAC2025"
  - "Design"
---

# Monolithic 3D FPGA Design and Synthesis with Back-End-of-Line Configuration Memories


<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com">DES5: Emerging Device and Interconnect Technologies</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11132615">https://dl.acm.org/doi/10.1109/DAC63849.2025.11132615</a></p>
<p class="paper-seo-summary__meta"><strong>关键词:</strong> FPGA，单片三维集成，非晶氧化物半导体，可重构计算</p>
</div>


---

## 研究概要
本文提出基于BEOL氧化物半导体(AOS)的单片3D FPGA架构，采用W-In₂O₃(n)/SnO(p)晶体管实现配置存储与布线传输门。搭建适配M3D的COFFE与VTR评估流程，7nm工艺下相较传统CMOS FPGA，AT²乘积降低3.4倍，关键路径延迟下降27%，布线功耗减少26%，适配LLM、HDC等负载。

## 背景和动机
1. 传统2D CMOS FPGA配置SRAM占瓦片超50%面积、静态功耗高，交换/连接块布线开销巨大，与ASIC存在显著PPA差距。
2. 现有非易失存储型3D FPGA依赖高压编程电路，面积与可靠性受损，难以在后端金属层堆叠有源器件。
3. 常规晶体管无法在低温BEOL工艺制备，难以将配置存储、布线层堆叠在逻辑上方，走线RC延迟高。
4. 缺少适配单片3D堆叠FPGA的完整EDA建模与评估工具链，无法量化面积、时延、功耗综合收益。

## 相关工作
1. 传统平面CMOS FPGA：配置单元、布线全部位于底层FEOL，资源开销大，AT指标差。
2. RRAM/FeFET/NEM型3D FPGA：采用后端存储，但编程电压高，需额外升压电路，部分器件开关可靠性差。
3. 单片3D标准单元：仅实现通用逻辑堆叠，未针对FPGA可重构布线、配置存储做专用器件优化。
4. FPGA架构评估工具COFFE/VTR：原生仅支持2D平面架构，无M3D多层器件建模能力。

## 本文解决方案
### 1 双层BEOL AOS配置SRAM
采用双层堆叠IWO(n)、SnO(p)氧化物晶体管构建存储单元，低漏电、0.7V逻辑兼容编程电压，无需高压驱动，静态功耗相比硅SRAM降低60.1%。
### 2 BEOL AOS传输门布线阵列
在CL上层堆叠IWO传输门构成SB/CB交换块，缩短互连线RC；提升传输门供电电压消除电平恢复器，进一步降低布线功耗。
### 3 M3D适配EDA工具链
定制M3D-COFFE器件建模工具，耦合TCAD/SPICE/NeuroSim；改造VTR架构文件，支持多层堆叠瓦片面积、时延、功耗量化评估。
### 4 分电压供电策略
逻辑VDD=0.7V、配置存储0.8V、布线传输门1.2V，在小幅增加存储功耗前提下大幅削减布线动态能耗。

## 实验分析
1. 仿真平台：7nm ASAP7工艺，TCAD校准AOS紧凑模型，VTR覆盖FFT/CNN/GEMM/AES/GPT2等负载。
2. 瓦片面积：纯硅瓦片341.1μm²，仅替换AOS存储降至175.5μm²，全套M3D架构降至147.1μm²，降幅59%。
3. 时序功耗：关键路径延迟最高降低30%，交换/连接块功耗分别下降13.7%、26%；整体AT²几何均值降低77.1%。
4. 大模型场景：GPT-2部署相比商用Versal，面积缩减42.4%、时延降20.6%，AT²优化63.7%。
5. 路由特性：M3D架构长线利用率提升，布线拥塞均匀分散，热点缓解明显。

## 研究启发
1. BEOL兼容AOS晶体管是单片3D FPGA核心载体，可同时优化配置存储与布线两层硬件开销。
2. 分层堆叠将可重构资源移至逻辑上方，能大幅缩短互连线，从根源降低FPGA布线延迟与动态功耗。
3. 高低压分区供电可平衡存储静态功耗与布线动态能耗，避免电平恢复器带来额外时序损失。
4. 现有FPGA评估工具需针对3D堆叠扩展器件与层间寄生建模，才能精准量化架构收益。
5. 该方案显著缩小FPGA与ASIC的PPA差距，对LLM、高维计算等大规模并行负载适配性极强。