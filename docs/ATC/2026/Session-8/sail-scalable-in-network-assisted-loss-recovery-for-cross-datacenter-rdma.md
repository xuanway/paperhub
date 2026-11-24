# SAIL: Scalable In-Network-Assisted Loss Recovery for Cross-Datacenter RDMA

**中文标题**：SAIL：面向跨数据中心 RDMA 的可扩展网内辅助丢包恢复

**所属 Session**：[Session 8: Data Center Networking](index.md) · [ATC 2026](../index.md)

**作者**：Xiao Li (Tsinghua University), Haoyuan Yu (Tsinghua University), Yuan Yang (Tsinghua University), Mingwei Xu (Tsinghua University)

## 英文摘要
Cross-datacenter transmission is critical to many emerging Internet applications, and RDMA is a promising technology. To enable efficient cross-datacenter RDMA, loss recovery is essential due to lossy long-haul links. Most existing approaches face a scalability challenge: limited resources cannot accommodate loss recovery for networks with longer links, higher bandwidth, and more concurrent flows. We present SAIL, a scalable in-network-assisted loss-recovery mechanism for cross-datacenter RDMA. SAIL decomposes selective repeat (SR) into loss detection, out-of-order packet buffering, and retransmission, which are deployed solely on DCI switches and end-host software, respecting resource constraints while coordinating to achieve provably effective SR. We propose a suite of techniques to ensure SAIL’s effectiveness and scalability, including loss detection through an aggregated macro-flow and metadata piggybacking, out-of-order packet reception via dummy packet injection, and precise data repair and completion validation with minimal CPU overhead. We implement a SAIL prototype using a Tofino 1 programmable switch and a user-level software agent. Extensive experiments and simulations validate SAIL’s effectiveness across a wide range of network environments. Notably, SAIL achieves 13% to 8.8× higher goodput than the state-ofthe-art approaches at a 1% loss rate.

## 中文摘要
跨数据中心传输对许多新兴互联网应用至关重要，而 RDMA 是一项有前景的技术。为高效实现跨数据中心 RDMA，由于长距离链路存在丢包，丢包恢复必不可少。现有大多数方法面临可扩展性挑战：有限的资源无法满足链路更长、带宽更高、并发流更多的网络的丢包恢复需求。我们提出 SAIL，一种面向跨数据中心 RDMA 的可扩展网内辅助丢包恢复机制。SAIL 将选择重传（SR）分解为丢包检测、乱序报文缓存和重传，这些功能仅部署在 DCI 交换机和端主机软件上，在遵守资源约束的同时协同实现可证明有效的 SR。我们提出一系列技术以确保 SAIL 的有效性与可扩展性，包括通过聚合宏流进行丢包检测并捎带元数据、通过注入哑报文实现乱序报文接收，以及以最小 CPU 开销完成精确的数据修复与完成校验。我们使用 Tofino 1 可编程交换机和用户态软件代理实现了 SAIL 原型。大量实验与仿真验证了 SAIL 在广泛网络环境中的有效性。值得注意的是，在 1% 丢包率下，SAIL 相较现有最优方法取得 13% 至 8.8× 更高的有效吞吐。

## 英文关键词
RDMA, Cross-datacenter networks, Loss recovery

## 中文关键词
RDMA，跨数据中心网络，丢包恢复

[返回 Session 8](index.md) · [返回 ATC 2026](../index.md)
