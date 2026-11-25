IR-Drop Aware Global Placement with PDN Optimization and GPU-Accelerated Analysis for Mitigating Global and Local IR-Drop
Authors：
[Jai-Ming Lin](https://63dac.conference-program.com/?post_type=page&p=15&uid=381243)，[Pin-Yu Chen](https://63dac.conference-program.com/?post_type=page&p=15&uid=0873278154618921801)，[Zhao-Xian Huang](https://63dac.conference-program.com/?post_type=page&p=15&uid=3908595193519626159)，[Chen-Fa Tsai](https://63dac.conference-program.com/?post_type=page&p=15&uid=291243)，[De-Shiun Fu](https://63dac.conference-program.com/?post_type=page&p=15&uid=24252640386869674811)，[Shih-Cheng Huang](https://63dac.conference-program.com/?post_type=page&p=15&uid=6417459987248475744)

## 中文标题

结合 PDN 优化与 GPU 加速分析的 IR-Drop 感知全局布局以缓解全局与局部 IR-Drop

## 英文摘要

This paper presents an analytical global placement framework that concurrently integrates PDN optimization, effectively addressing both global and local IR-drop challenges. To enable accurate and efficient voltage drop estimation, we implement a fast, GPU-accelerated IR-drop analysis engine based on Modified Nodal Analysis (MNA). For PDN optimization, we introduce an iterative strategy that enhances power delivery robustness by inserting additional power delivery paths to reduce global IR-drop. To further address localized IR-drop issues, we propose a novel density control mechanism that constrains cell placement based on the maximum tolerable power load at each PDN node, as determined by IR-drop severity. Experimental results show that the proposed methodology significantly reduces IR-drop violations without incurring additional wirelength, runtime, or routability overhead compared to state-of-the-art IR-drop-aware placement techniques.

## 中文摘要

本文提出一个解析全局布局框架，同时集成 PDN 优化，有效应对全局与局部 IR-drop 的挑战。为实现准确而高效的电压降估计，我们实现了一个基于改进节点分析（MNA）的快速 GPU 加速 IR-drop 分析引擎。在 PDN 优化方面，我们引入一种迭代策略，通过插入额外的供电路径来降低全局 IR-drop，从而增强供电的鲁棒性。为进一步解决局部 IR-drop 问题，我们提出一种新颖的密度控制机制，依据 IR-drop 的严重程度确定每个 PDN 节点可容忍的最大功率负载，并据此约束单元布局。实验结果表明，与先进的 IR-drop 感知布局技术相比，所提方法显著减少了 IR-drop 违例，且未带来额外的线长、运行时间或可布线性开销。
