# Fuzz Testing on IPC Based OS Services with Resource State Awareness

**中文标题**：面向基于 IPC 的操作系统服务的资源状态感知模糊测试

**所属 Session**：[Session 24: Kernel Interfaces and Service Reliability](index.md) · [ATC 2026](../index.md)

**作者**：Yuheng Shen (Tsinghua University), Yifei Chu (Tsinghua University), Fan Ding (Central South University), Jianzhong Liu (Tsinghua University), Qiang Zhang (Jiangxi University of Finance and Economics), Heyuan Shi (Central South University), Yu Jiang (Tsinghua University)

## 英文摘要
Modern operating systems increasingly implement core functionality in IPC based OS services. Existing syscall and IPC fuzzers model producer-consumer dependencies to generate structured inputs and reach service handlers. However, handler reachability is insufficient when resources persist across requests, clients, and threads. Without tracking accepted resources, fuzzers may miss bugs requiring multiple requests. In this paper, we present RAIF, a fuzzer for IPC based OS services. RAIF organizes fuzzing around service-side resource dependencies rather than isolated IPC messages. It first generates workloads that connect resource creation, operations, and update APIs around the same service resources. It then dispatches test cases across clients, so related resources are exposed to the service in a compact request order. Finally, RAIF collects resource dependency information after IPC unmarshalling and uses it to guide subsequent fuzzing. Evaluation shows that RAIF identified 23 bugs on OpenHarmony, Android, and D-Bus. On the three Android services, it improved branch coverage by 25.8% and triggered 3.5× more resource state transitions than baselines.

## 中文摘要
现代操作系统越来越多地把核心功能实现在基于 IPC 的操作系统服务中。现有的系统调用模糊测试器和 IPC 模糊测试器通过建模生产者—消费者依赖来生成结构化输入并到达服务处理函数。然而，当资源在请求、客户端和线程之间持续存在时，仅能到达处理函数是不够的。如果不跟踪已被接受的资源，模糊测试器就可能错过需要多个请求才能触发的缺陷。在本文中，我们提出 RAIF，一个面向基于 IPC 的操作系统服务的模糊测试器。RAIF 围绕服务端的资源依赖而非孤立的 IPC 消息来组织模糊测试。它首先生成将同一服务资源上的资源创建、操作和更新 API 串联起来的工作负载。然后它在多个客户端之间分派测试用例，使相关资源以紧凑的请求顺序暴露给服务。最后，RAIF 在 IPC 反序列化之后收集资源依赖信息，并用其指导后续的模糊测试。评估表明，RAIF 在 OpenHarmony、Android 和 D-Bus 上发现了 23 个缺陷。在三个 Android 服务上，它把分支覆盖率提高了 25.8%，并触发了比基线多 3.5× 的资源状态转换。

## 英文关键词
Operating System Security, Fuzz Testing, Bug Detection

## 中文关键词
操作系统安全，模糊测试，缺陷检测

[返回 Session 24](index.md) · [返回 ATC 2026](../index.md)
