Probabilistic Memory Design for Efficient Trustworthy Edge Intelligence
Authors：
[Likai Pei](https://63dac.conference-program.com/?post_type=page&p=15&uid=59982486234722731381)，[Jiahao Zheng](https://63dac.conference-program.com/?post_type=page&p=15&uid=8205548638956137421)，[Xueji Zhao](https://63dac.conference-program.com/?post_type=page&p=15&uid=7996107774040102959)，[Emilie Ye](https://63dac.conference-program.com/?post_type=page&p=15&uid=78059075621814066631)，[Jianbo Liu](https://63dac.conference-program.com/?post_type=page&p=15&uid=4348761549937703807)，[Hanqing Tao](https://63dac.conference-program.com/?post_type=page&p=15&uid=2548628128501605017)，[Ming-Yen Lee](https://63dac.conference-program.com/?post_type=page&p=15&uid=1108956366232608711)，[Ruiyang Qin](https://63dac.conference-program.com/?post_type=page&p=15&uid=734843)，[Yiyu Shi](https://63dac.conference-program.com/?post_type=page&p=15&uid=092143)，[Shimeng Yu](https://63dac.conference-program.com/?post_type=page&p=15&uid=806243)，[X. Sharon Hu](https://63dac.conference-program.com/?post_type=page&p=15&uid=316243)，[Ningyuan Cao](https://63dac.conference-program.com/?post_type=page&p=15&uid=8143733196500498459)

## 中文标题

面向高效可信边缘智能的概率存储设计

## 英文摘要

Probabilistic computation plays an important role in trustworthy edge intelligence to quantify uncertainty, enhance robustness, reconstruct data and protect privacy, but its adoption is limited by the orders-of-magnitude data throughput gap between Gaussian random number generation (GRNG) and computation, as well as instruction overhead. This paper introduces probabilistic memory (p-MEM), a unified memory primitive that stores distribution parameters (e.g., mean and standard deviation) and samples directly at the native memory bandwidth where deterministic data becomes the zero-variance special case. Using a layout-validated p-MEM simulator, we comprehensively explore device choices, memory specifications, and technology nodes, showing that p-MEM can achieve > 1000 GSa/s/mm2 GRNG throughput (including memory arrays access). Integrated into CPU / GPU systems, p-MEM reduces instruction count by up to 2.19×/4.37×, sampling latency by 562×/3.45×, and energy by 295.5×/3.53× for Bayesian neural network workloads, providing a scalable hardware substrate for trustworthy probabilistic AI.

## 中文摘要

概率计算在可信边缘智能中发挥着量化不确定性、增强鲁棒性、重建数据与保护隐私等重要作用，但其应用受制于高斯随机数生成（GRNG）与计算之间数量级的数据吞吐差距以及指令开销。本文提出概率存储（p-MEM），一种统一的存储原语，可存储分布参数（如均值与标准差）并直接在原生存储带宽下完成采样，而确定性数据则成为零方差的特例。借助经版图验证的 p-MEM 仿真器，我们系统探索了器件选择、存储规格与工艺节点，表明 p-MEM 可实现 > 1000 GSa/s/mm2 的 GRNG 吞吐率（包含存储阵列访问）。将其集成到 CPU / GPU 系统中，对于贝叶斯神经网络负载，p-MEM 可将指令数分别减少最多 2.19 倍/4.37 倍，将采样延迟分别降低 562 倍/3.45 倍，将能耗分别降低 295.5 倍/3.53 倍，为可信概率 AI 提供了可扩展的硬件基础。
