Hierarchical Pareto-Prompted Optimization for Probabilistic DAG Scheduling on Real-Time Systems
Authors：
[Yili Guo](https://63dac.conference-program.com/?post_type=page&p=15&uid=92713559440480851621)，[Weijie Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=9544014308302856987)，[Xingchen Liu](https://63dac.conference-program.com/?post_type=page&p=15&uid=1992286392993685474)，[Zuoyan Qin](https://63dac.conference-program.com/?post_type=page&p=15&uid=3866835739223921831)，[Liangliang He](https://63dac.conference-program.com/?post_type=page&p=15&uid=44184084160675160371)，[Weichen Liu](https://63dac.conference-program.com/?post_type=page&p=15&uid=073143)，[Wanli Chang](https://63dac.conference-program.com/?post_type=page&p=15&uid=432143)

## 中文标题

面向实时系统概率 DAG 调度的分层 Pareto 提示优化

## 英文摘要

Real-time automotive workloads modeled as directed acyclic graphs (DAGs) with probabilistic execution times face severe latency bottlenecks, where shared tasks couple multiple sensor-to-actuator paths. Minimizing end-to-end latency under such variability requires navigating a complex joint space of task mappings and offsets. To address this, we propose a Pareto-prompted metaheuristic with hierarchical mapping-then-offset refinement, utilizing Pareto dominance to search for non-dominated schedules. Evaluated on production navigation-on-autopilot workloads running on NVIDIA Orin-N–based vehicles, our method satisfies all constraints and significantly outperforms an industrial static baseline, reducing mean latency by up to 12% and 99th-percentile latency by up to 15%.

## 中文摘要

以有向无环图（DAG）建模、执行时间具有概率分布的实时汽车负载面临严重的延迟瓶颈，其中共享任务耦合了多条从传感器到执行器的路径。在此类不确定性下最小化端到端延迟，需要在任务映射与偏移构成的复杂联合空间中求解。为此，我们提出一种 Pareto 提示的元启发式方法，采用先映射、后偏移的分层细化过程，利用 Pareto 支配关系搜索非支配调度方案。在基于 NVIDIA Orin-N 的车载平台上运行的实际量产自动驾驶导航负载上进行评估，本方法满足全部约束，并显著优于工业静态基线，平均延迟最多降低 12%，第 99 百分位延迟最多降低 15%。

## 英文关键词

Real-time systems, Probabilistic DAG scheduling, Multi-objective optimization

## 中文关键词

实时系统、概率 DAG 调度、多目标优化
