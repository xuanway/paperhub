Circuitdiff: Bridging Netlist Knowledge with RTL Based on Graph Denoising Diffusion
Authors：
[Ning Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=0664891654584882089)，[Zichong Deng](https://63dac.conference-program.com/?post_type=page&p=15&uid=25929479764152932101)，[Bingkun Yao](https://63dac.conference-program.com/?post_type=page&p=15&uid=6337424854460121618)，[Jie Zhou](https://63dac.conference-program.com/?post_type=page&p=15&uid=38479733992353397501)，[Yuchen Hu](https://63dac.conference-program.com/?post_type=page&p=15&uid=4116076772303443402)，[Xi Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=675843)，[Zhe Jiang](https://63dac.conference-program.com/?post_type=page&p=15&uid=6168935507854231423)，[Nan Guan](https://63dac.conference-program.com/?post_type=page&p=15&uid=8605962012354093361)

## 中文标题

CircuitDiff：基于图去噪扩散的 RTL 与网表知识桥接

## 英文摘要

In Integrated circuit (IC) workflows, EDA tools provide accurate circuit metrics by simulating and analyzing physical characteristics, but their computational overhead makes them impractical for rapid design iterations. Thus, accurate and efficient circuit metric prediction at the register-transfer-level (RTL) stage has become a hot topic. However, current methods still struggle to efficiently bridge the gap between RTL and physical characteristics. We propose CircuitDiff , a generative pre-training framework designed to learn a unified representation space between RTL and netlist. This is achieved by encoding the RTL graph as a condition for training a netlist graph denoising diffusion model. During fine-tuning, learnable queries are used to incentivize knowledge from the pre-trained model via cross-attention mechanisms. Experimental results show that CircuitDiff achieves superior performance in the prediction of early-stage circuit metric compared to state-of-the-art models, supporting the "left-shift" paradigm while maintaining computational efficiency. Our code and data will be publicly available at https://github.com/CatIIIIIIII/CircuitDiff.

## 中文摘要

在集成电路（IC）设计流程中，EDA 工具通过仿真与分析物理特性来提供准确的电路指标，但其计算开销过大，难以支撑快速的设计迭代。因此，在寄存器传输级（RTL）阶段实现准确而高效的电路指标预测已成为研究热点。然而，现有方法仍难以在 RTL 与物理特性之间建立有效联系。我们提出 CircuitDiff，一个生成式预训练框架，旨在学习 RTL 与网表之间的统一表示空间。具体而言，我们将 RTL 图编码为条件，用于训练网表图去噪扩散模型。在微调阶段，通过交叉注意力机制利用可学习的查询向量激发预训练模型中的知识。实验结果表明，与当前最优模型相比，CircuitDiff 在早期电路指标预测上取得了更优的性能，在保持计算效率的同时支撑了“左移”（left-shift）范式。我们的代码与数据将公开于 https://github.com/CatIIIIIIII/CircuitDiff。

## 英文关键词

Circuit metrics; Graph neural network; Denoising diffusion

## 中文关键词

电路指标、图神经网络、去噪扩散
