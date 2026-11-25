---
title: "Identifying System-on-Chip Security Assets with Structure-Based Analysis"
description: "DAC 2025 · Security"
tags:
  - "dac-2025"
  - "security"
  - "soc"
  - "security-assets"
  - "graph-neural-network"
  - "rtl-analysis"
  - "automation"
---

# Identifying System-on-Chip Security Assets with Structure-Based Analysis

<div class="paper-seo-summary">
<p class="paper-seo-summary__meta"><strong>会议:</strong> DAC 2025</p> 
<p class="paper-seo-summary__meta"><strong>专题:</strong> <a href="https://62dac.conference-program.com/">SEC2: Hardware Security: Primitives & Architecture, Design & Test</a></p> 
<p class="paper-seo-summary__meta"><strong>论文链接:</strong> <a href="https://dl.acm.org/doi/10.1109/DAC63849.2025.11133104">https://dl.acm.org/doi/10.1109/DAC63849.2025.11133104</a></p> 
<p class="paper-seo-summary__meta"><strong>关键词:</strong> SoC安全资产，结构分析，超流图，深度神经网络 </p>
</div>

---

## 研究概要
本文提出基于超流图HFG与DNN的SoC安全资产自动识别框架，解析RTL生成数据流/控制流图，提取20维结构特征向量，采用全连接DNN分类密钥、配置等安全资产。在OpenTitan、OpenPiton两款SoC验证，多类资产分类精度最高99%，二分类区分安全/非安全信号准确率94%，大幅减少人工审查工作量。

## 背景和动机
1. 现代SoC集成多来源IP，密钥、寄存器等安全资产分散，人工逐行审查RTL耗时，易遗漏受保护关键信号，引发硬件漏洞。
2. 现有资产识别工具依赖厂商预先标注主资产或关键词匹配，无标注IP会遗漏次级安全信号，泛化能力差。
3. 关键词检索受厂商命名规范限制，不同团队命名差异大，无法识别无特征命名的安全控制、存储信号。
4. 图神经网络跨SoC迁移性差，不同模块图结构差异大，训练后识别效果不稳定。
5. 硅前RTL阶段缺少自动化工具，无法在设计早期定位需加固的安全资产，流片后修复成本极高。

## 相关工作
1. 信息流追踪类工具：基于超流图人工分析OpenTitan资产，无自动分类能力，全流程依赖工程师手动梳理。
2. 主资产遍历方案：需预先给定核心密钥等主资产，仅能追踪关联次级资产，未标注资产完全漏检。
3. CWE漏洞扫描工具：仅针对特定硬件弱点开发专用算法，无法通用识别各类安全资产。
4. 关键词检索识别：依靠信号名称匹配安全关键词，适配单一设计，跨IP、跨芯片失效。
5. GNN硬件分析：图迁移缺陷明显，不同SoC拓扑差异大，推理开销高，不适合大规模RTL解析。

## 本文解决方案
### 1 RTL超流图(HFG)自动构建
使用Verific解析Verilog/SystemVerilog生成AST，遍历if/case条件、赋值语句，实线表示直接数据流、虚线表示控制流；自底向上遍历层级模块补齐跨信号连接，完整刻画信号交互关系。
### 2 双层邻域20维特征向量化
统计目标节点4类一阶邻域（条件前驱/直接前驱/条件后继/直接后继）；聚合四类邻域平均特征，拼接一阶统计与邻域均值构成20维结构签名向量，刻画信号拓扑模式。
### 3 轻量化全连接DNN分类器
四层FC网络搭配BN、ReLU、Dropout，交叉熵损失训练；仅需少量标注样本即可区分REGWEN、影子寄存器、密钥等多类安全资产，规避GNN迁移缺陷。
### 4 无预先标注识别流程
无需厂商提供主资产列表，仅少量各类资产标注样本，依靠拓扑结构特征识别；兼容不同IP命名规范，突破关键词局限。
### 5 批量RTL解析流水线
支持多模块批量解析、HFG可视化输出，一键导出分类结果，适配大规模SoC RTL工程。

## 实验分析
1. 实验平台：TITAN V显卡，OpenTitan(332模块)、OpenPiton(128模块)两款开源SoC，10折交叉验证。
2. 识别精度：OpenTitan四类细分资产分类99%；混入普通信号后多分类92%、安全/非安全二分类94%；OpenPiton对应精度93%/86%/88%。
3. 运行效率：OpenTitan近24万行RTL完整解析仅13.6秒，远快人工逐文件审查。
4. 特征有效性：模型首层权重分布均匀，20维向量全部参与分类，不存在无效冗余维度。
5. 泛化表现：两款架构差异巨大的SoC均保持高识别精度，不受IP命名、层级结构变化干扰。

## 研究启发
1. 安全资产核心区分特征是数据流、控制流拓扑结构，而非信号命名，基于图结构识别可摆脱关键词依赖。
2. 硬件安全分析不宜选用GNN，不同SoC图拓扑差异大，轻量化全连接DNN泛化与效率更优。
3. 双层邻域特征可捕获深层关联，仅一阶邻居不足以区分结构相似的安全/普通信号。
4. 硅前RTL阶段自动化资产识别能提前锁定保护对象，降低流片后漏洞修复成本。
5. 仅少量标注样本即可完成训练，无需完整资产清单，适配第三方黑盒IP安全审计场景。
