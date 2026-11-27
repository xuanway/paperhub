IGNITE: An Inquisitive and Graph-Aware Neural Circuit Simulator with Two-Stage Enhanced In-Context Learning
Authors：
[Jing Kou](https://63dac.conference-program.com/?post_type=page&p=15&uid=97878627384712641711)，[Jiayi Sun](https://63dac.conference-program.com/?post_type=page&p=15&uid=6211522247773540624)，[Yifei Lyu](https://63dac.conference-program.com/?post_type=page&p=15&uid=5238155946473556128)，[Liang Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=8520032144551964537)，[Yinpan Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=30247401892284257421)，[Yuxin Xie](https://63dac.conference-program.com/?post_type=page&p=15&uid=4016910572457195523)，[Yinbo Sun](https://63dac.conference-program.com/?post_type=page&p=15&uid=23829690451527850481)，[Wei Xing](https://63dac.conference-program.com/?post_type=page&p=15&uid=693843)，[Wang Kang](https://63dac.conference-program.com/?post_type=page&p=15&uid=6384140613079907404)

## 中文标题

IGNITE：一种具备两阶段增强上下文学习能力的探究式图感知神经电路仿真器

## 英文摘要

Neural circuit simulators promise fast alternatives to SPICE but remain impractical due to three fundamental limitations: per-circuit hyperparameter tuning, cold-start problems from lacking cross-task knowledge sharing, and prohibitive online retraining costs that negate computational advantages. We introduce IGNITE, a pretrained neural simulator that addresses these challenges through in-context learning. Built on a self-supervised topology encoder and Prior-data Fitted Network decoder, IGNITE adapts to new circuits via a single forward pass conditioned on a small context set, eliminating online training overhead. An information-theoretic active learning strategy enables intelligent sample selection, maximizing data efficiency. IGNITE transfers knowledge across topologies and technology nodes, achieving 𝑅2 > 0.9 with only 95 samples in average—a 15.8× improvement over SOTA. Integration with optimization frameworks yields 2−30× speedup for transistor sizing and more than 5× speedup for yield optimization, demonstrating practical viability for industrial analog circuit design.

## 中文摘要

神经电路仿真器有望成为 SPICE 的快速替代方案，但受制于三个根本性局限而难以实用：需逐电路调优超参数；缺乏跨任务知识共享而导致冷启动问题；在线重训练开销过高，抵消了其计算优势。我们提出 IGNITE，一个预训练的神经仿真器，通过上下文学习（in-context learning）应对上述挑战。IGNITE 建立在自监督拓扑编码器与先验数据拟合网络（PFN）解码器之上，只需以少量上下文样本为条件进行一次前向传播即可适配新电路，从而消除在线训练开销。一种基于信息论的主动学习策略可实现智能的样本选择，最大化数据效率。IGNITE 能够在不同拓扑与工艺节点之间迁移知识，平均仅需 95 个样本即可达到 R² > 0.9，相比 SOTA 提升 15.8×。与优化框架集成后，在晶体管尺寸设计上实现 2–30× 加速，在良率优化上实现超过 5× 的加速，证明了其在工业模拟电路设计中的实用可行性。

## 英文关键词

Neural Circuit Simulator, Prior-data Fitted Network, Yield Optimizaion, Transistor Sizing

## 中文关键词

神经电路仿真器、先验数据拟合网络、良率优化、晶体管尺寸设计
