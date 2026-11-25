Reconfigurable 3D-VRRAM LUT-CiM with Greedy G-Shuffle Quantization for End-to-End 4-Bit ViTs in Edge Dense Prediction
Authors：
[Yi Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=0115851161869105479)，[Zijian Ye](https://63dac.conference-program.com/?post_type=page&p=15&uid=87232756898366890461)，[Zhaori Cong](https://63dac.conference-program.com/?post_type=page&p=15&uid=19074265382560794281)，[Shengzhe Yan](https://63dac.conference-program.com/?post_type=page&p=15&uid=1817089621015480789)，[Songqi Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=2107628920399826662)，[Ning Lin](https://63dac.conference-program.com/?post_type=page&p=15&uid=14119393813058012901)，[Jinshan Yue](https://63dac.conference-program.com/?post_type=page&p=15&uid=43444652076933285701)，[xiaojuan qi](https://63dac.conference-program.com/?post_type=page&p=15&uid=05655718575474240481)，[Zhongrui Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=93538193207214203841)，[Han Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=0699690152643758866)

## 中文标题

面向边缘稠密预测中端到端 4 比特 ViT 的可重构 3D-VRRAM LUT-CiM 与贪心 G-Shuffle 量化

## 英文摘要

The rise of embodied intelligence is driving the deployment of Vision Transformers (ViTs) for dense prediction (DP) tasks on resource-limited edge devices. Look-up-table (LUT)-based digital compute-in-memory (CiM) has emerged as a promising paradigm, delivering high accuracy with superior energy and area efficiency. However, practical ViT deployment on LUT‑CiM for edge DP faces dual hardware and software challenges: (1) LUT cost scales exponentially with bit-width, while NLP‑oriented quantization struggles to push convolution-heavy ViTs below 8 bits, especially in compact on‑chip CiM models; and (2) fixed LUT structures cannot accommodate ViTs’ heterogeneous static/dynamic workloads, while unstructured mixed‑precision weights strain memory density and utilization. To overcome these, we propose a software-hardware co-designed low-precision ViT accelerator. Software-wise, we propose Greedy G-shuffle, a lightweight, general quantization method, paired with a PCA‑based, channel‑wise weight assignment, tailored for lightweight ViTs in edge DP tasks. Hardware-wise, at the architectural level, we introduce a reconfigurable LUT-based CiM macro that accelerates both static and dynamic matrix operations with superior energy efficiency, complemented by a high-utilization pipeline-and tensor-parallel dataflow that serves heterogeneous ViT layers. At the circuit level, we employ high-density 1TnR VRRAM with flexible read paths and channel-wise hardware remapping to support mixed-precision INT4/2/1 weights, minimizing area overhead. We demonstrate the first fully 4-bit ViT with INT4 activations and structured INT4/2/1 weights on a reconfigurable 3D 1TnR VRRAM LUT-based CiM macro, achieving a 26.7% improvement in mIoU and a 30.1% reduction in RMSE on the ADE20K and NYUDv2 compared to vanilla round-to-nearest quantization, along with up to 8.9× area efficiency and 9.7× energy efficiency improvements over the state-of-the-art.

## 中文摘要

具身智能的兴起推动 Vision Transformer（ViT）在资源受限的边缘设备上部署，以完成稠密预测（DP）任务。基于查找表（LUT）的数字存内计算（CiM）已成为颇具前景的范式，能够在保持高精度的同时提供优异的能效与面积效率。然而，在边缘 DP 场景下将 ViT 实际部署于 LUT-CiM 面临硬件与软件的双重挑战：（1）LUT 成本随位宽呈指数增长，而面向 NLP 的量化方法难以将卷积密集的 ViT 压缩至 8 比特以下，在紧凑的片上 CiM 模型中尤为如此；（2）固定的 LUT 结构无法适应 ViT 静态与动态负载的异构性，而非结构化混合精度权重又会加剧存储密度与利用率的压力。为克服上述问题，我们提出一种软硬件协同设计的低精度 ViT 加速器。软件层面，我们提出 Greedy G-shuffle——一种轻量、通用的量化方法，并配合基于 PCA 的逐通道权重分配，针对边缘 DP 任务中的轻量级 ViT 量身定制。硬件层面，在架构级，我们引入可重构的 LUT 存内计算宏，以优异的能效同时加速静态与动态矩阵运算，并辅以高利用率的流水线与张量并行数据流，服务异构的 ViT 层。在电路级，我们采用高密度 1TnR VRRAM，配合灵活的读取路径与逐通道硬件重映射，以支持混合精度 INT4/2/1 权重，并将面积开销降至最低。我们基于可重构 3D 1TnR VRRAM LUT 存内计算宏，首次展示了采用 INT4 激活与结构化 INT4/2/1 权重的全 4 比特 ViT；与朴素的就近舍入量化相比，在 ADE20K 与 NYUDv2 上分别取得 26.7% 的 mIoU 提升与 30.1% 的 RMSE 下降，并且相较当前最优方案实现最高 8.9 倍的面积效率与 9.7 倍的能效提升。

## 英文关键词

Vision Transformers, Compute-in-memory, Quantization, Look-up table, 1TnR VRRAM, Edge AI accelerator, Dense prediction

## 中文关键词

Vision Transformer、存内计算、量化、查找表、1TnR VRRAM、边缘 AI 加速器、稠密预测
