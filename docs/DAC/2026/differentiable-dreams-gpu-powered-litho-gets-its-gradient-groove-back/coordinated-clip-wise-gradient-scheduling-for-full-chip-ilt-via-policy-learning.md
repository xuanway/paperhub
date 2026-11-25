Coordinated Clip-Wise Gradient Scheduling for Full-Chip ILT via Policy Learning
Authors：
[Ziyang Yu](https://63dac.conference-program.com/?post_type=page&p=15&uid=45839454402838021661)，[Shuo Yin](https://63dac.conference-program.com/?post_type=page&p=15&uid=36544653970437952731)，[Su Zheng](https://63dac.conference-program.com/?post_type=page&p=15&uid=80843625085351335261)，[Xiaoxiao Liang](https://63dac.conference-program.com/?post_type=page&p=15&uid=1443267453033559885)，[Yuzhe Ma](https://63dac.conference-program.com/?post_type=page&p=15&uid=645743)，[Bei Yu](https://63dac.conference-program.com/?post_type=page&p=15&uid=991243)

## 中文标题

基于策略学习的全芯片 ILT 片段级协同梯度调度

## 英文摘要

Full-chip inverse lithography technology (ILT) is critical for semiconductor manufacturing but remains difficult to maintain global solution integrity. While gradient fusion flow mitigates mask stitching artifacts, it suffers from a uniform, unweighted update policy. We identify heterogeneous smoothness and inter-clip coupling as key factors that create conflicts between local clip convergence and global integrity. We propose a coordinated clip-wise gradient scheduling framework trained via policy learning to resolve these conflicts. The method constructs a full-chip state by combining per-clip static geometric descriptors and dynamic optimization signals, and aggregates them with a graph neural network to encode inter-clip relations. From this state, a scheduler generates continuous, correlated gradient weights learned with flow-matching policy gradients, capturing cross-clip dependencies. On industry-scale layouts, our framework outperforms state-of-the-art full-chip ILT baselines.

## 中文摘要

全芯片反向光刻技术（ILT）对半导体制造至关重要，但难以维持全局解的一致性。梯度融合流程虽能缓解掩模拼接伪影，却受制于均匀、无加权的更新策略。我们指出，异构的平滑性与片段间耦合是造成局部片段收敛与全局一致性之间冲突的关键因素。我们提出一个通过策略学习训练的片段级协同梯度调度框架来化解这些冲突。该方法通过结合每个片段的静态几何描述符与动态优化信号来构建全芯片状态，并用图神经网络对其进行聚合以编码片段间关系。基于该状态，调度器生成连续且相互关联的梯度权重，这些权重通过流匹配策略梯度学习得到，从而捕捉跨片段依赖关系。在工业规模版图上，我们的框架优于最先进的全芯片 ILT 基线方法。
