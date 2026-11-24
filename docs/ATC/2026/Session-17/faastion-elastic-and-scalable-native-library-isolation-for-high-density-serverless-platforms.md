# Faastion: Elastic and Scalable Native Library Isolation for High-Density Serverless Platforms

**中文标题**：Faastion：面向高密度无服务器平台的弹性可扩展原生库隔离

**所属 Session**：[Session 17: Scheduling and Serverless](index.md) · [ATC 2026](../index.md)

**作者**：Miguel Lourenço (INESC-ID, Instituto Superior Técnico, University of Lisbon), Rahul Kondlapudi (Purdue University), Serhii Ivanenko (INESC-ID, Instituto Superior Técnico, University of Lisbon), Rodrigo Cidra (INESC-ID, Instituto Superior Técnico, University of Lisbon), Pedro Fonseca (Purdue University), Rodrigo Bruno (INESC-ID, Instituto Superior Técnico, University of Lisbon)

## 英文摘要
Serverless platforms increasingly co-locate concurrent function invocations to maximize elasticity and density. This co-location is supported by either software or hardware isolation techniques. While software isolation provided by existing sandboxes is flexible and lightweight, it does not uphold its security guarantees across native code. Conversely, hardware-based approaches, such as PKU-based sandboxing, enforce stronger boundaries for native code but are constrained by the limited number of available protection domains. We propose Faastion, a serverless runtime that combines Language Based Isolation (LBI) with a novel PKU domain multiplexing architecture for highly concurrent serverless environments. Faastion maintains the high concurrency, low latency, and low memory footprint of LBI while isolating native libraries. Compared to OpenWhisk, which enforces process-based isolation, Faastion exhibits a 47% lower memory footprint and eliminates cold starts, reducing 99th percentile end-to-end request latency by 6.9× in a real-world trace execution. Furthermore, Faastion efficiently secures native libraries and prevents performance interference, increasing throughput by up to 3.7× compared to alternative co-location-aware runtimes like Knative and Hydra.

## 中文摘要
无服务器平台越来越多地共置并发函数调用，以最大化弹性和部署密度。这种共置由软件或硬件隔离技术支撑。现有沙箱提供的软件隔离灵活且轻量，但无法在原生代码上维持其安全保证。相反，基于硬件的方法（如基于 PKU 的沙箱）为原生代码施加了更强的边界，却受限于可用的保护域数量有限。我们提出 Faastion，一个将基于语言的隔离（LBI）与面向高并发无服务器环境的新型 PKU 域复用架构相结合的无服务器运行时。Faastion 在隔离原生库的同时，保持了 LBI 的高并发、低延迟与低内存占用。与采用基于进程隔离的 OpenWhisk 相比，Faastion 的内存占用低 47%，并消除了冷启动，在真实负载轨迹执行中把 99 分位端到端请求延迟降低 6.9×。此外，Faastion 高效地保护了原生库并防止了性能干扰，与 Knative、Hydra 等具备共置感知能力的替代运行时相比，吞吐最高提升 3.7×。

## 英文关键词
Serverless, MPK, Language-based Isolation

## 中文关键词
无服务器，MPK，基于语言的隔离

[返回 Session 17](index.md) · [返回 ATC 2026](../index.md)
