# fRAC: Remote Accelerator Calls on Hostless FPGAs

**中文标题**：fRAC：无宿主 FPGA 上的远程加速器调用

**所属 Session**：[Session 15: Remote Memory and RDMA](index.md) · [ATC 2026](../index.md)

**作者**：Ziyi Yang (KAUST), Krishnan B. Iyer (KAUST), Yixi Chen (KAUST), Ran Shu (Microsoft Research), Zsolt István (TU Darmstadt), Marco Canini (KAUST), Suhaib Fahmy (KAUST)

## 英文摘要
Hardware accelerators are essential for meeting microsecond-scale demands in distributed applications, but invoking them over the network remains bottlenecked by host software. Host-mediated paths (RPC, RDMA) still rely on the CPU to reassemble requests and launch accelerators, which dominates end-to-end latency, while packet-level offload on SmartNICs lacks any notion of a complete request. We introduce the Remote Accelerator Call (RAC) paradigm, in which transport ingestion, request reassembly, dispatch, and accelerator invocation are handled entirely in hardware. We build fRAC, a hostless prototype that implements this network-to-accelerator interface as a lightweight shim on an FPGA hosting multiple virtualized accelerators, reconfigurable at runtime in a few milliseconds. Serverless functions backed by fine-grained accelerators are a natural fit, since host-mediated invocation overhead can match or exceed their short execution times. fRAC achieves under 7.8 𝜇s end-to-end latency while sustaining application throughput of up to 90 Gbps. Compared to highly optimized DPDK-based CPU and DPU baselines, it achieves at least 80% lower latency under saturation, while consuming 85% less power.

## 中文摘要
硬件加速器对于满足分布式应用中微秒级的需求至关重要，但通过网络调用它们仍受制于宿主软件。宿主中介的路径（RPC、RDMA）仍依赖 CPU 来重组请求并启动加速器，这主导了端到端延迟；而 SmartNIC 上的包级卸载则缺乏完整请求的概念。我们提出远程加速器调用（RAC）范式，其中传输层收包、请求重组、派发和加速器调用完全在硬件中完成。我们构建了 fRAC，一个无宿主原型，在承载多个虚拟化加速器的 FPGA 上以轻量级垫片实现这一网络到加速器的接口，并可在运行时于数毫秒内重配置。由细粒度加速器支持的无服务器函数是天然的适配对象，因为宿主中介的调用开销可以与其短暂执行时间相当甚至更高。fRAC 实现低于 7.8 微秒的端到端延迟，同时维持高达 90 Gbps 的应用吞吐。与高度优化的基于 DPDK 的 CPU 和 DPU 基线相比，它在饱和状态下延迟至少低 80%，同时功耗低 85%。

## 英文关键词
Field programmable gate arrays, hardware acceleration, serverless computing, in-network computing, remote procedure call.

## 中文关键词
现场可编程门阵列，硬件加速，无服务器计算，网内计算，远程过程调用

[返回 Session 15](index.md) · [返回 ATC 2026](../index.md)
