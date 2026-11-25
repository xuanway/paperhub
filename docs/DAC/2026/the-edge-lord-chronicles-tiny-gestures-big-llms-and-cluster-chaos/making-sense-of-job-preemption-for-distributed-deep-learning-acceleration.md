Making Sense of Job Preemption for Distributed Deep Learning Acceleration
Authors：
[Younghun Go](https://63dac.conference-program.com/?post_type=page&p=15&uid=4749620891683409952)，[Changyong Shin](https://63dac.conference-program.com/?post_type=page&p=15&uid=9631621852535759272)，[Minchul Kang](https://63dac.conference-program.com/?post_type=page&p=15&uid=0692137197084419431)，[Jaehyun Hwang](https://63dac.conference-program.com/?post_type=page&p=15&uid=89575562650905287641)，[Chuck Yoo](https://63dac.conference-program.com/?post_type=page&p=15&uid=95106983502369552471)，[Gyeongsik Yang](https://63dac.conference-program.com/?post_type=page&p=15&uid=9169105563718225763)

## 中文标题

面向分布式深度学习加速的作业抢占机制解析

## 英文摘要

Preemptive scheduling is gaining attention in GPU scheduling for distributed training because it reduces job completion times (JCT). However, our analysis of production traces reveals that, surprisingly, it can increase JCT in practice. We identify two key contributors to this inefficiency. First, preemptions become “futile” when a job is preempted right after being loaded, before it begins execution. We find this futile preemption wastes the load time and so inflates JCT ∼1.6×. Second, existing GPU schedulers run at fixed intervals (e.g., 360 s) rather than upon new job arrivals or when a job completes. So, new jobs must wait until the scheduler kicks in, which, we find, increases JCT ∼2.6×. To address the problems, we introduce Lazer, a novel job scheduler that predicts when to preempt jobs based on job-specific and cluster conditions. Lazer is designed to efficiently explore the scheduling space and adapt to diverse job and GPU cluster characteristics based on Bayesian optimization. Our extensive evaluation shows that Lazer significantly outperforms state-of-the-art schedulers—reducing JCT by 1.2×–233.3×, waiting time by 2×–11690×, and futile preemptions by 23×–67×.

## 中文摘要

抢占式调度在分布式训练的 GPU 调度中日益受到关注，因为它能缩短作业完成时间（JCT）。然而，我们对生产 trace 的分析揭示，令人意外的是，它在实践中反而可能增加 JCT。我们识别出造成这种低效的两个关键因素。第一，当作业在刚被加载之后、开始执行之前即被抢占时，抢占变得“无效”。我们发现这种无效抢占浪费了加载时间，从而使 JCT 膨胀约 1.6 倍。第二，现有 GPU 调度器以固定间隔（例如 360 秒）运行，而非在新作业到达或作业完成时运行。因此，新作业必须等待调度器触发，我们发现这使 JCT 增加约 2.6 倍。为解决这些问题，我们提出 Lazer，一种新颖的作业调度器，它基于作业特定条件与集群条件来预测何时抢占作业。Lazer 基于贝叶斯优化设计，能够高效探索调度空间并适应多样的作业与 GPU 集群特征。我们的大量评估表明，Lazer 显著优于最先进的调度器——将 JCT 降低 1.2 倍–233.3 倍、等待时间降低 2 倍–11690 倍、无效抢占减少 23 倍–67 倍。
