TopGQ: Fast GNN Post-Training Quantization Leveraging Topology Information
Authors：
[Dain Kwon](https://63dac.conference-program.com/?post_type=page&p=15&uid=0069865126040260105)，[Kanghyun Choi](https://63dac.conference-program.com/?post_type=page&p=15&uid=47552787106430827131)，[Hyeyoon Lee](https://63dac.conference-program.com/?post_type=page&p=15&uid=44642103000894836211)，[Sunjong Park](https://63dac.conference-program.com/?post_type=page&p=15&uid=0066776247563070914)，[Seoyong Lee](https://63dac.conference-program.com/?post_type=page&p=15&uid=38870975199218663381)，[Sukjin Kim](https://63dac.conference-program.com/?post_type=page&p=15&uid=4510689400118074205)，[Jinho Lee](https://63dac.conference-program.com/?post_type=page&p=15&uid=808643)

## 中文标题

TopGQ：利用拓扑信息的快速 GNN 训练后量化

## 英文摘要

Existing GNN quantization methods suffer from considerable quantization overhead, which severely limits their practical usage in real-world scenarios. To this end, we present TopGQ, an accurate post-training GNN quantization framework, alleviating redundant quantization overhead. We propose dual-axis scale absorption, which enables activation quantization along both the outer and inner dimensions by merging one into the adjacency matrix. On top of that, we introduce TopPIN, a proxy for nodes’ local structure, and use it to group nodes with similar topology during quantization. Experimental results show that TopGQ reduces quantization time by an order of magnitude while preserving accuracy. The code is available at https://github.com/meowrowan/TopGQ.

## 中文摘要

现有 GNN 量化方法存在较大的量化开销，严重限制了其在真实场景中的实际应用。为此，我们提出 TopGQ，一个精确的训练后 GNN 量化框架，可缓解冗余的量化开销。我们提出双轴缩放吸收，通过将一侧合并进邻接矩阵，使激活量化可沿外部和内部两个维度进行。在此基础上，我们引入 TopPIN——一种节点局部结构的代理指标，并用它在量化过程中对拓扑相似的节点进行分组。实验结果表明，TopGQ 在保持精度的同时将量化时间降低了一个数量级。代码已开源于 https://github.com/meowrowan/TopGQ。

## 英文关键词

Graph Neural Network, Post-Training Quantization, Inference Acceleration, Edge Device, Graph Topology

## 中文关键词

图神经网络、训练后量化、推理加速、边缘设备、图拓扑
