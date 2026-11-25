SDM: A Variation-Tolerant Soft Decision Machine with In-Memory Sigmoid Computation
Authors：
[Bo Wen](https://63dac.conference-program.com/?post_type=page&p=15&uid=2629840666255037142)，[Zhicheng XU](https://63dac.conference-program.com/?post_type=page&p=15&uid=22464063206661235411)，[Pengyu Ren](https://63dac.conference-program.com/?post_type=page&p=15&uid=5921598584400398338)，[Guoyun Gao](https://63dac.conference-program.com/?post_type=page&p=15&uid=5660538928913216871)，[X. Sharon Hu](https://63dac.conference-program.com/?post_type=page&p=15&uid=316243)，[Can Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=036843)

## 中文标题

SDM：一种具有存内 Sigmoid 计算的抗工艺偏差软判决机

## 英文摘要

Edge deployment of interpretable models like Decision Trees (DTs) and Random Forests (RFs) is hindered by the von Neumann bottleneck in conventional digital hardware and hard, sequential decision boundaries catastrophically amplify device variations in analog in-memory computing hardware with emerging devices. We propose a hardware-algorithm co-design, the Soft Decision Machine (SDM), that overcomes these challenges. Algorithmically, SDM introduces a training scheme that transforms a globally-learned multivariate model into a hardware-friendly univariate form for parallel inference. At the hardware level, we design a compact 1-FeFET analog Content-Addressable Memory cell, where SDM natively computes the required sigmoid function and the subsequent in-memory aggregation of these probabilities. This approach significantly improved variation tolerance because the ‘soft’ sigmoidal computation avoids the sharp error around the hard boundaries, and a ‘collective’ decision across all parallel rules is inherently resilient to minor probabilistic errors. Consequently, under 40 mV device variation, SDM maintains 93.2% accuracy on MNIST (0.54% drop), while DT and RF degrade by 43.86% and 16.06%, respectively. This co-design enables robust, efficient, and interpretable computing for edge intelligence.

## 中文摘要

决策树（DT）与随机森林（RF）等可解释模型在边缘端的部署受到两方面制约：传统数字硬件中的冯·诺依曼瓶颈，以及模拟存内计算硬件中新兴器件上硬性、串行的判决边界会灾难性地放大大器件偏差。我们提出一种软硬件协同设计——软判决机（SDM），以克服这些挑战。在算法层面，SDM 引入一种训练方案，将全局学习的多变量模型转换为适合硬件实现的单变量形式，以支持并行推理。在硬件层面，我们设计了一种紧凑的 1-FeFET 模拟内容可寻址存储器单元，SDM 在其中原生计算所需的 sigmoid 函数，并完成这些概率的存内聚合。该方法显著提升了抗偏差能力，因为“软”的 sigmoid 计算避免了硬边界附近的剧烈误差，而跨所有并行规则的“集体”判决天然能够抵御微小的概率误差。因此，在 40 mV 器件偏差下，SDM 在 MNIST 上仍保持 93.2% 的准确率（仅下降 0.54%），而 DT 与 RF 分别退化 43.86% 与 16.06%。该协同设计为边缘智能提供了鲁棒、高效且可解释的计算。

## 英文关键词

In-memory computing, non-volatile memory, interpretable machine learning, FeFET, analog content-addressable memory (aCAM)

## 中文关键词

存内计算、非易失存储器、可解释机器学习、FeFET、模拟内容可寻址存储器（aCAM）
