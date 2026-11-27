Hestia: Hyperthread-Level Scheduling for Cloud Microservices with Interference-Aware Attention
Authors：
[Dingyu Yang](https://63dac.conference-program.com/?post_type=page&p=15&uid=0594360326778181906)，[Fanyong Kong](https://63dac.conference-program.com/?post_type=page&p=15&uid=6003400577898932799)，[Jie Dai](https://63dac.conference-program.com/?post_type=page&p=15&uid=24378679097197018501)，[Shiyou Qian](https://63dac.conference-program.com/?post_type=page&p=15&uid=90467613409896005511)，[Shuangwei Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=6414648393632291963)，[Jian Cao](https://63dac.conference-program.com/?post_type=page&p=15&uid=70802945398566787851)，[Guangtao Xue](https://63dac.conference-program.com/?post_type=page&p=15&uid=6021168681999282789)，[Gang Chen](https://63dac.conference-program.com/?post_type=page&p=15&uid=77036473254873004831)

## 中文标题

Hestia：基于干扰感知注意力的云微服务超线程级调度

## 英文摘要

Modern cloud servers routinely co-locate multiple latency-sensitive microservice instances to improve resource efficiency. However, the diversity of microservice behaviors, coupled with mutual performance interference under simultaneous multithreading (SMT), makes large-scale placement increasingly complex. Existing interference aware schedulers and isolation techniques rely on coarse core-level profiling or static resource partitioning, leaving asymmetric hyperthread-level heterogeneity and SMT contention dynamics largely unmodeled. We present Hestia, a hyperthread-level, interference-aware scheduling framework powered by self-attention. Through an extensive analysis of production traces encompassing 32,408 instances across 3,132 servers, we identify two dominant contention patterns—sharing-core (SC) and sharing-socket (SS)-and reveal strong asymmetry in their impact. Guided by these insights, Hestia incorporates (1) a self-attention-based CPU usage predictor that models SC/SS contention and hardware heterogeneity, and (2) an interference scoring model that estimates pairwise contention risks to guide scheduling decisions. We evaluate Hestia through large-scale simulation and a real production deployment. Hestia reduces the 95th-percentile service latency by up to 80%, lowers overall CPU consumption by 2.3% under the same workload, and surpasses five state-of-the-art schedulers by up to 30.65% across diverse contention scenarios.

## 中文摘要

现代云服务器通常共置多个时延敏感的微服务实例以提升资源效率。然而，微服务行为的多样性，加之同时多线程（SMT）下的相互性能干扰，使大规模放置日益复杂。现有干扰感知调度器与隔离技术依赖粗粒度的核级画像或静态资源划分，未能对非对称的超线程级异构性以及 SMT 争用动态进行建模。我们提出 Hestia，一个由自注意力驱动的、超线程级干扰感知调度框架。通过对涵盖 3,132 台服务器上 32,408 个实例的生产环境跟踪数据进行广泛分析，我们识别出两种主要的争用模式——共享核（SC）与共享插槽（SS）——并揭示出二者在影响上的强烈非对称性。基于这些洞察，Hestia 包含：(1) 基于自注意力的 CPU 使用率预测器，对 SC/SS 争用与硬件异构性建模；(2) 干扰评分模型，估计成对争用风险以指导调度决策。我们通过大规模仿真与真实生产部署评估 Hestia。Hestia 将 95 分位服务时延最多降低 80%，在相同负载下将整体 CPU 消耗降低 2.3%，并在多种争用场景中最多超越五个最先进调度器 30.65%。

## 英文关键词

Microservices, Inference Scheduling, Cloud computing

## 中文关键词

微服务、推理调度、云计算
