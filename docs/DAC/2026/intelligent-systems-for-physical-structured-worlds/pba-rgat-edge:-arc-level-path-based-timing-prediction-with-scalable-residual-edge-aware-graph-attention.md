PBA-rGAT-Edge: Arc-Level Path-Based Timing Prediction with Scalable Residual Edge-Aware Graph Attention
Authors：
[Fangjian Liu](https://63dac.conference-program.com/?post_type=page&p=15&uid=9106556163489397287)，[Chenyang Lv](https://63dac.conference-program.com/?post_type=page&p=15&uid=9307049518340631499)，[Chunyang Feng](https://63dac.conference-program.com/?post_type=page&p=15&uid=4551377893376210835)

## 中文标题

PBA-rGAT-Edge：基于可扩展残差边感知图注意力的弧级路径时序预测

## 英文摘要

Path-Based Analysis (PBA) provides accurate timing by evaluating real signal transitions along true paths, but its computational cost makes full-chip deployment impractical on modern large-scale designs. Graph-Based Analysis (GBA), while much faster, often suffers from pessimism due to worst-case propagation. To bridge this accuracy–efficiency gap, we propose PBA-rGAT-Edge, a scalable residual graph attention model that predicts arc-level delay and slew using edge-aware message passing. Unlike prior cell-centric formulations, PBA-rGAT-Edge operates on a pin-level timing graph and explicitly embeds both cell and interconnect arcs as edge features. A lightweight residual attention backbone, coupled with multi-level feature fusion and dual-task prediction, enables efficient training and accurate timing inference. On three benchmark test cases, the model achieved a 29× to 48× inference speedup compared to commercial STA analysis, while maintaining stable acceleration performance across diverse circuit structures, significantly enhancing timing analysis efficiency. The implementation will be open-sourced at github.com/PBA-rGAT-Edge .

## 中文摘要

基于路径的分析（PBA）沿真实路径评估实际信号跳变，从而给出精确的时序结果，但其计算开销使全芯片部署在现代大规模设计上难以实现。基于图的分析（GBA）虽然快得多，却常因最坏情况传播而过于悲观。为弥合精度与效率之间的这一差距，我们提出 PBA-rGAT-Edge，一个可扩展的残差图注意力模型，利用边感知消息传递来预测弧级延时与转换时间（slew）。与以往以单元为中心的建模方式不同，PBA-rGAT-Edge 在引脚级时序图上运行，并将单元弧与互连弧一并显式地嵌入为边特征。轻量级残差注意力主干网络，配合多级特征融合与双任务预测，实现了高效训练与精确的时序推断。在三个基准测试用例上，该模型相比商用 STA 分析取得 29× 至 48× 的推理加速，并在多样的电路结构上保持稳定的加速效果，显著提升了时序分析效率。实现将在 github.com/PBA-rGAT-Edge 开源。

## 英文关键词

STA, PBA, Graph Neural Networks (GNN)

## 中文关键词

STA、PBA、图神经网络（GNN）
