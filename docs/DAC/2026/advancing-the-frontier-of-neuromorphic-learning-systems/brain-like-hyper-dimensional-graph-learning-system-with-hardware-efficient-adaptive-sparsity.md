Brain-Like Hyper-Dimensional Graph Learning System with Hardware-Efficient Adaptive Sparsity
Authors：
[Haomin Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=102725310443845334)，[Fangxin Liu](https://63dac.conference-program.com/?post_type=page&p=15&uid=318143)，[Zongwu Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=073443)，[Shiyuan Huang](https://63dac.conference-program.com/?post_type=page&p=15&uid=24687864021255189051)，[Ning Yang](https://63dac.conference-program.com/?post_type=page&p=15&uid=97857849623460577211)，[Chenyang Guan](https://63dac.conference-program.com/?post_type=page&p=15&uid=55869298845145161621)，[Tao Yang](https://63dac.conference-program.com/?post_type=page&p=15&uid=32490420365188384971)，[Xinran Liang](https://63dac.conference-program.com/?post_type=page&p=15&uid=1829945754236905675)，[Haibing Guan](https://63dac.conference-program.com/?post_type=page&p=15&uid=828243)

## 中文标题

具备硬件高效自适应稀疏性的类脑超维图学习系统

## 英文摘要

Graph neural networks (GNNs) are crucial for numerous applications, yet their excessive computational demands often lead to suboptimal performance. Hyper-Dimensional Computing (HDC) is a brain-inspired learning approach for efficient and robust learning. HDC-based Graph Learning (HDGL) shows significantly improved computational efficiency and accuracy by learning graph representations in a high-dimensional space. Despite these advantages, general-purpose computing platforms such as CPUs and GPUs are insufficient for efficiently handling HDGL tasks. In this paper we propose an accelerator called HDGAS through algorithm and hardware co-design for HDGL. Based on the insight that not all node features in a graph are equally important, we propose to jointly optimize a lightweight filter with the HDGL model to dynamically identify and eliminate less significant node features during runtime. Moreover, we design a specialized system architecture for end-to-end HDGL acceleration, harnessing the proposed dynamic sparsification technique in tandem with the inherent SpMM operations within HDGL. Extensive experiments demonstrate that HDGAS achieves 6.76× (69.31×) speedup and 7.58× (80.12×) energy efficiency improvements over GNN accelerators (GPU).

## 中文摘要

图神经网络（GNN）对众多应用至关重要，但其过高的计算需求往往导致性能欠佳。超维计算（HDC）是一种受大脑启发的学习方式，可实现高效且鲁棒的学习。基于 HDC 的图学习（HDGL）通过在高维空间中学习图表示，显著提升了计算效率与精度。尽管具有这些优势，CPU 和 GPU 等通用计算平台仍不足以高效处理 HDGL 任务。本文通过算法与硬件协同设计，提出一种名为 HDGAS 的 HDGL 加速器。基于图中并非所有节点特征都同等重要这一洞察，我们提出将轻量滤波器与 HDGL 模型联合优化，以在运行时动态识别并剔除不太重要的节点特征。此外，我们设计了一种专用系统架构以实现端到端 HDGL 加速，将所提出的动态稀疏化技术与 HDGL 固有的 SpMM 操作协同利用。大量实验表明，HDGAS 相较 GNN 加速器（GPU）分别实现 6.76 倍（69.31 倍）的加速和 7.58 倍（80.12 倍）的能效提升。
