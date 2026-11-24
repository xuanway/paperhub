# Unipool: Efficient Management of Pre-Provisioned Resources for Container Platforms

**中文标题**：Unipool：容器平台预配置资源的高效管理

**所属 Session**：[Session 17: Scheduling and Serverless](index.md) · [ATC 2026](../index.md)

**作者**：Hanfei Yu (Stevens Institute of Technology), Enrique Saurez (Microsoft Azure Research - Systems), Íñigo Goiri (Microsoft Azure Research - Systems), Hao Wang (Stevens Institute of Technology), Rodrigo Fonseca (Microsoft Azure Research - Systems)

## 英文摘要
Cloud platforms reduce deployment latency by pre-initializing resources, but fragmented resource management across cloud layers often leads to substantial over-provisioning and increased cost. Through production trace analysis and replay using state-of-the-practice resource management approaches, we show that independently managing resources at each layer results in a poor trade-off between resource waste and deployment latency. We present Unipool, the first unified platform that exposes the state of pre-provisioned resources across layers, enabling more accurate resource pool sizing and dynamic multiplexing. Guided by insights from production traces, Unipool leverages cloud-native workload patterns to safely consolidate and oversubscribe pre-provisioned resources, significantly reducing platform cost while preserving quality of service. We implement Unipool on Kubernetes and Kata Containers, and evaluate it using both a large-scale event-driven simulator and a testbed of 25 virtual machines. Across mixed Function-as-a-Service and Container-as-a-Service production traces, we reduce resource waste by 92% while lowering container deployment latency by 21% compared with state-of-the-art baselines.

## 中文摘要
云平台通过预先初始化资源来降低部署延迟，但跨云层的碎片化资源管理往往导致大量过度配置与成本上升。通过生产轨迹分析，并使用当前实践中的资源管理方法进行回放，我们表明在各层独立管理资源会在资源浪费与部署延迟之间形成糟糕的权衡。我们提出 Unipool，首个统一平台，它暴露跨层的预配置资源状态，从而实现更准确的资源池容量规划与动态复用。受生产轨迹洞察的引导，Unipool 利用云原生的工作负载模式，安全地整合与超售预配置资源，在保证服务质量的同时显著降低平台成本。我们在 Kubernetes 和 Kata Containers 上实现了 Unipool，并使用大规模事件驱动模拟器和由 25 台虚拟机组成的测试床进行评估。在混合的 FaaS 与 CaaS 生产轨迹上，与最先进的基线相比，我们将资源浪费降低 92%，同时把容器部署延迟降低 21%。

## 英文关键词
Cloud computing, container platforms, resource management

## 中文关键词
云计算，容器平台，资源管理

[返回 Session 17](index.md) · [返回 ATC 2026](../index.md)
