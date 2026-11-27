Chiplanner: Physically-Aware and Timing-Driven Design Planner for 2.5D Multi-Chiplet Systems
Authors：
[Zixuan Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=61217393877035728101)，[Kanglin Tian](https://63dac.conference-program.com/?post_type=page&p=15&uid=800611592560663361)，[Fan Hu](https://63dac.conference-program.com/?post_type=page&p=15&uid=87403547304950747711)，[Zirui Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=8667739248084651279)，[Xinyue Wu](https://63dac.conference-program.com/?post_type=page&p=15&uid=7900322410667800701)，[hengyuan zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=10547608578691552031)，[Shixin Chen](https://63dac.conference-program.com/?post_type=page&p=15&uid=3601825552448404171)，[Jianwang Zhai](https://63dac.conference-program.com/?post_type=page&p=15&uid=36525870277041148421)，[Xinfei Guo](https://63dac.conference-program.com/?post_type=page&p=15&uid=046843)，[Kang Zhao](https://63dac.conference-program.com/?post_type=page&p=15&uid=31063505926127256031)

## 中文标题

ChiPlanner：面向 2.5D 多芯粒系统的物理感知与时序驱动设计规划器

## 英文摘要

While chiplet-based 2.5D integration offers scalable high-performance computing with reduced manufacturing cost, it also poses significant challenges in design closure. Achieving timing closure in chiplet-based systems is difficult and frequently demands repeated engineering change orders (ECOs) and architectural-level iterations. To overcome these challenges, we propose ChiPlanner, a holistic early-stage design planner that integrates chiplet partitioning and physical planning. ChiPlanner first employs approximate placement to estimate post-chiplet-placement timing in advance of partitioning, which provides guidance for partitioning and helps reduce timing gaps. It further models inter-chiplet delay and incorporates a parallel net-weighting strategy in timing-driven physical planning to optimize overall system performance. Moreover, Bayesian optimization is leveraged to systematically explore the trade-off between chiplet manufacturing cost and system timing. Experimental results demonstrate that incorporating ChiPlanner’s early-stage planning enables downstream chiplet design tools to achieve notably superior optimization outcomes, delivering average improvements of 42.4% in total negative slack (TNS) and 16.8% in worst negative slack (WNS). These results confirm that accurate early-stage planning provides a far better initialization for chiplet design and significantly reduces the burden on later ECOs.

## 中文摘要

基于芯粒的 2.5D 集成在提供可扩展的高性能计算并降低制造成本的同时，也给设计收敛带来了重大挑战。在基于芯粒的系统中实现时序收敛十分困难，往往需要反复进行工程变更指令（ECO）和架构级迭代。为克服这些挑战，我们提出 ChiPlanner，这是一个融合芯粒划分与物理规划的整体早期设计规划器。ChiPlanner 首先采用近似布局，在划分之前预先估计芯粒放置后的时序，从而为划分提供指导并有助于缩小时序差距。它进一步对芯粒间延迟建模，并在时序驱动的物理规划中引入并行网络加权策略，以优化系统整体性能。此外，它利用贝叶斯优化系统性地探索芯粒制造成本与系统时序之间的权衡。实验结果表明，纳入 ChiPlanner 的早期规划可使下游芯粒设计工具取得显著更优的优化效果，在总负松弛（TNS）上平均改善 42.4%，在最差负松弛（WNS）上改善 16.8%。这些结果证实，准确的早期规划为芯粒设计提供了远更好的初始化，并显著减轻了后续 ECO 的负担。

## 英文关键词

Chiplet, 2.5D Integration, Design Planning, Physically-Aware

## 中文关键词

芯粒、2.5D 集成、设计规划、物理感知
