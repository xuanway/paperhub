A Levelized Load-Balanced and Structure-Adaptive GPU LU Factorization Method for Circuit Simulation
Authors：
[Yunfan Zuo](https://63dac.conference-program.com/?post_type=page&p=15&uid=1606588320386281826)，[Renjie Xia](https://63dac.conference-program.com/?post_type=page&p=15&uid=5244501270339128757)，[Yongtian Ren](https://63dac.conference-program.com/?post_type=page&p=15&uid=46981870402420472331)，[Jiajie Xu](https://63dac.conference-program.com/?post_type=page&p=15&uid=0838899781460608536)，[Chenpu Shi](https://63dac.conference-program.com/?post_type=page&p=15&uid=35364257464496451741)，[zhaohan wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=7223338003693622547)，[Hao Yan](https://63dac.conference-program.com/?post_type=page&p=15&uid=969143)，[Lixin Ge](https://63dac.conference-program.com/?post_type=page&p=15&uid=88796094378190374701)，[Longxing Shi](https://63dac.conference-program.com/?post_type=page&p=15&uid=079143)

## 中文标题

面向电路仿真的分级负载均衡与结构自适应 GPU LU 分解方法

## 英文摘要

As IC designs become more complex and chips exceed ten billion transistors, post-layout SPICE simulations often require solving large sparse linear systems, significantly reducing efficiency. Although GPU acceleration is promising, existing methods often suffer from poor load balancing and low resource utilization, limiting their effectiveness for ultra-large-scale circuit simulations. In this paper, we propose a levelized load-balanced and structure-adaptive LU factorization framework for GPU-based circuit simulation. Our method improves resource utilization and parallel efficiency by introducing computation-balanced dependency level partitioning, adaptive resource allocation, and a hybrid matrix indexing mechanism. These strategies aim to better utilize both GPU memory bandwidth and compute resources. We demonstrate significant acceleration over existing methods, achieving a 2.1× speedup compared to GLU3.0 and a 5.2× speedup over 16-thread PARDISO on circuit sparse matrices ranging from thousands to millions of dimensions. Additionally, our framework has been successfully integrated into the open-source SPICE simulator Ngspice, accelerating circuit simulations with promising results and showcasing its potential for large-scale IC design verification.

## 中文摘要

随着 IC 设计日益复杂、芯片晶体管数量突破百亿，版图后 SPICE 仿真往往需要求解大规模稀疏线性系统，效率显著降低。GPU 加速虽具前景，但现有方法常受制于负载不均衡与资源利用率偏低，限制了其在大规模电路仿真中的效果。本文提出一种面向 GPU 电路仿真的分级负载均衡、结构自适应 LU 分解框架。该方法通过引入计算均衡的依赖层级划分、自适应资源分配与混合矩阵索引机制，提高了资源利用率与并行效率。这些策略旨在更好地利用 GPU 的存储带宽与计算资源。我们在从数千维到数百万维的电路稀疏矩阵上相较现有方法取得显著加速：相比 GLU3.0 加速 2.1 倍，相比 16 线程 PARDISO 加速 5.2 倍。此外，该框架已成功集成到开源 SPICE 仿真器 Ngspice 中，加快了电路仿真并取得良好效果，展现了其在大规模 IC 设计验证中的潜力。
