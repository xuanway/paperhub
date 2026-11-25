Stochastic Diffusion Prior: Knowledge Elicitation and Local Adaptation for Transistor Sizing
Authors：
[Wei Xing](https://63dac.conference-program.com/?post_type=page&p=15&uid=693843)，[Zhuohua Liu](https://63dac.conference-program.com/?post_type=page&p=15&uid=13428001996582328441)，[Weilun Xie](https://63dac.conference-program.com/?post_type=page&p=15&uid=48397764126252805501)，[Yuxuan Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=3039322232812589947)，[Yuan Yao](https://63dac.conference-program.com/?post_type=page&p=15&uid=378354340017359814)，[Yuanqi Hu](https://63dac.conference-program.com/?post_type=page&p=15&uid=82503196820783347371)

## 中文标题

随机扩散先验：面向晶体管尺寸设计的知识抽取与局部自适应

## 英文摘要

Automatic transistor sizing remains a significant challenge in modern analog and mixed-signal circuit design. While recent AI-driven methods show promise, they remain sample-inefficient, largely because they struggle to effectively incorporate expert knowledge and generalize across different designs. We propose Stochastic Diffusion Prior (SDP), a framework that systematically bridges this gap. SDP elicits domain expertise through an intuitive interface based on the established gm/ID methodology, formally integrating this knowledge into the optimization. Critically, SDP is not a static prior; it enables dynamic adaptation through a novel mutual information-guided diffusion process, allowing the prior to be refined and corrected by new simulation data. SDP can be integrated with virtually any optimization method, enhancing its sample efficiency and exploration capabilities. Experimental validation on practical analog circuits demonstrates SDP’s superiority over state-of-the-art approaches. When integrated with a simple Vanilla BO, SDP achieves up to 92.3× speedup (27.9× on average) while improving key performance metrics by up to 2.0× (1.5× on average). The approach maintains high effectiveness even with imperfect prior knowledge and successfully enables knowledge transfer between technology nodes, positioning it as a versatile and robust enhancement for circuit optimization.

## 中文摘要

自动晶体管尺寸设计仍是现代模拟与混合信号电路设计中的重大挑战。尽管近期 AI 驱动的方法展现出潜力，但其样本效率仍然较低，主要原因是难以有效融合专家知识并跨不同设计泛化。我们提出随机扩散先验（SDP），一个系统性地弥合这一差距的框架。SDP 通过基于成熟的 gm/ID 方法学的直观接口抽取领域专家知识，并将该知识形式化地融入优化过程。关键在于，SDP 并非静态先验；它通过一种新颖的互信息引导扩散过程实现动态自适应，使先验能够被新的仿真数据修正和完善。SDP 可与几乎任何优化方法集成，提升其样本效率与探索能力。在实际模拟电路上的实验验证表明，SDP 优于最先进的方法。当与简单的 Vanilla BO 集成时，SDP 实现最高 92.3 倍加速（平均 27.9 倍），同时将关键性能指标提升最高 2.0 倍（平均 1.5 倍）。该方法即使在先验知识不完美的情况下仍保持高效，并成功实现工艺节点间的知识迁移，使其成为电路优化中通用且鲁棒的增强手段。

## 英文关键词

Transistor Sizing, Bayesian Optimization, Knowledge Elicitation, Diffusion Models, Analog Circuit Design

## 中文关键词

晶体管尺寸设计、贝叶斯优化、知识抽取、扩散模型、模拟电路设计
