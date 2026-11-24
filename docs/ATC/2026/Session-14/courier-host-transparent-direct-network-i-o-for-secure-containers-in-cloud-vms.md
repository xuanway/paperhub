# Courier: Host-Transparent Direct Network I/O for Secure Containers in Cloud VMs

**中文标题**：Courier：面向云虚拟机中安全容器的宿主透明直接网络 I/O

**所属 Session**：[Session 14: Networking I](index.md) · [ATC 2026](../index.md)

**作者**：Hang Huang (Huazhong University of Science and Technology), Zhucan Ye (Huazhong University of Science and Technology), Zhiheng Tao (Ant Group), Hui Lu (The University of Texas at Arlington), Wenlong Hou (Ant Group), Wei Guo (Alibaba Group), Quan Xu (Alibaba Group), Jiang Liu (Alibaba Group), Jiangshan Lai (Ant Group), Jia Rao (The University of Texas at Arlington), Zhuo Huang (Huazhong University of Science and Technology), Song Wu (Huazhong University of Science and Technology), Chen Yu (Huazhong University of Science and Technology), Hai Jin (Huazhong University of Science and Technology)

## 英文摘要
Secure containers strengthen isolation by encapsulating conventional OS-level containers within lightweight virtual machines (microVMs), and have been widely adopted to execute untrusted, multi-tenant workloads in modern cloud platforms. In practice, these platforms are increasingly deployed atop cloud virtual machines to exploit cloud elasticity and cost efficiency, which places secure containers within a nested virtualization stack. Although prior work has significantly advanced nested CPU and memory virtualization, network I/O remains a critical bottleneck. Existing para-virtualized networking solutions incur substantial overhead due to repeated cross-layer mediation, while hardware-assisted device passthrough depends on IOMMU virtualization support that is often unavailable in public clouds. This paper presents Courier, a direct network I/O architecture that enables passthrough-like, high-performance networking for secure containers in cloud environments. Courier rethinks nested network virtualization by introducing an in-guest shadow IOMMU to enable secure device passthrough with a shorter network stack and zero-copy data transfer, without requiring host involvement. In addition, Courier incorporates several data-plane techniques, including direct-kick notifications, used-ring passthrough, and efficient interrupt handling, to further improve packet processing efficiency. We implement Courier in a production system and evaluated it using both microbenchmarks and real-world applications. The results show that Courier significantly improves both throughput and tail latency, consistently outperforming state-of-the-art virtio-net and vhost-net by up to 9.36x and 96.7%, respectively, while achieving near-native performance under realistic workloads.

## 中文摘要
安全容器通过将传统 OS 级容器封装在轻量级虚拟机（microVM）内来强化隔离，已被现代云平台广泛采用以运行不可信的多租户工作负载。在实践中，这些平台越来越多地部署在云虚拟机之上，以利用云的弹性与成本效率，这使安全容器处于嵌套虚拟化栈之中。尽管已有工作在嵌套 CPU 与内存虚拟化方面取得了显著进展，网络 I/O 仍是关键瓶颈。现有的半虚拟化网络方案因反复的跨层中介而带来大量开销，而硬件辅助的设备直通依赖于公共云中往往不可用的 IOMMU 虚拟化支持。本文提出 Courier，一种直接网络 I/O 架构，在云环境中为安全容器提供类直通的高性能网络。Courier 重新思考嵌套网络虚拟化，引入客户机内影子 IOMMU，从而以更短的网络栈和零拷贝数据传输实现安全的设备直通，且无需宿主参与。此外，Courier 还结合了多项数据面技术，包括直接通知、已用环直通和高效中断处理，以进一步提升包处理效率。我们在生产系统中实现了 Courier，并用微基准测试和真实应用对其进行了评估。结果表明，Courier 显著改善吞吐与尾延迟，分别以最高 9.36 倍和 96.7% 的优势持续优于最先进的 virtio-net 与 vhost-net，同时在真实工作负载下达到接近原生的性能。

## 英文关键词
Secure containers, Network, I/O virtualization

## 中文关键词
安全容器，网络，I/O 虚拟化

[返回 Session 14](index.md) · [返回 ATC 2026](../index.md)
