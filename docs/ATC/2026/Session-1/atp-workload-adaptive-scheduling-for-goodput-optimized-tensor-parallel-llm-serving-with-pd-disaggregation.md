# ATP: Workload-Adaptive Scheduling for Goodput-Optimized Tensor-Parallel LLM Serving with PD Disaggregation

**中文标题**：ATP：面向 PD 分离的有效吞吐优化张量并行 LLM 服务的负载自适应调度

**所属 Session**：[Session 1: LLM Inference I](index.md) · [ATC 2026](../index.md)

**作者**：Yinhe Chen (University of Science and Technology of China), Dongqi Tian (University of Science and Technology of China), Youhui Bai (University of Science and Technology of China), Chaoyi Ruan (National University of Singapore), Jiaan Zhu (University of Science and Technology of China), Long Zhao (Anhui University; Institute of Artificial Intelligence, Hefei Comprehensive National Science Center), Qinghe Wang (University of Science and Technology of China; Institute of Artificial Intelligence, Hefei Comprehensive National Science Center), Cheng Li (University of Science and Technology of China; Institute of Artificial Intelligence, Hefei Comprehensive National Science Center)

## 英文摘要
Online LLM serving must satisfy two latency SLOs: time-to-first-token (TTFT) for responsiveness and time-between-tokens (TBT) for smooth generation. To improve resource utilization under these targets, serving systems optimize goodput, the request completion rate that satisfies both SLOs. However, modern interactive, agentic, and long-document workloads are highly skewed and time-varying, making static tensor-parallel (TP) configurations and fixed GPU splits between prefill and decoding (PD) inefficient. We present ATP, a scheduling-layer system for goodput-optimized, PD-disaggregated LLM serving. It organizes GPUs into serving instances with different fixed TP degrees, each able to serve either prefill or decoding. Over these instances, ATP formulates request-level TP selection and pool-level PD allocation as one scheduling problem and addresses it at two timescales. Its fast path routes each request’s prefill and decoding to the TP instances that best fit each stage. Its slow path adapts the PD split by changing instance roles when workload composition changes. Implemented atop vLLM, ATP achieves, on average, 2.27× the sustainable goodput of LoongServe, 2.07× that of DistServe, and 1.82× that of an enhanced static baseline on real-world Mooncake traces, with mean scheduling latency below 310 𝜇s.

## 中文摘要
在线 LLM 服务必须满足两个延迟 SLO：用于保证响应性的首令牌时延（TTFT）和用于保证生成平滑的令牌间时延（TBT）。为在这些目标下提升资源利用率，服务系统以有效吞吐（goodput）为优化目标，即同时满足这两个 SLO 的请求完成速率。然而，现代交互式、智能体式与长文档负载高度偏斜且随时间变化，使得静态的张量并行（TP）配置以及预填充与解码（PD）之间固定的 GPU 划分变得低效。我们提出 ATP，一个面向有效吞吐优化的 PD 分离式 LLM 服务的调度层系统。它将 GPU 组织为具有不同固定 TP 度的服务实例，每个实例既能服务预填充也能服务解码。在这些实例之上，ATP 将请求级的 TP 选择与池级的 PD 分配建模为同一个调度问题，并在两个时间尺度上求解。其快路径将每个请求的预填充与解码路由到最适合各自阶段的 TP 实例，其慢路径则在负载构成发生变化时通过改变实例角色来调整 PD 划分。ATP 实现在 vLLM 之上，在真实的 Mooncake 轨迹上，其可持续有效吞吐平均达到 LoongServe 的 2.27 倍、DistServe 的 2.07 倍，以及一个增强的静态基线的 1.82 倍，平均调度延迟低于 310 微秒。

## 英文关键词
LLM Serving, PD Disaggregation, Tensor Parallelism

## 中文关键词
LLM 服务，PD 分离，张量并行

[返回 Session 1](index.md) · [返回 ATC 2026](../index.md)
