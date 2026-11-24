# Lean: Saving OSS Network Cost by Application-Infrastructure Coordination

**中文标题**：Lean：通过应用与基础设施协同降低 OSS 网络成本

**所属 Session**：[Session 14: Networking I](index.md) · [ATC 2026](../index.md)

**作者**：Qiankun Yue (Alibaba Cloud), Kun Qian (Alibaba Cloud), Jiashi Lu (Alibaba Cloud), Xue Li (Alibaba Group), Qingchao Luo (Alibaba Cloud), Weibin Yan (Alibaba Cloud), Zhihong Li (Alibaba Cloud), Jianyao Sun (Alibaba Cloud), Junping Liang (Alibaba Cloud), Yuyao Chen (Alibaba Cloud), Liefeng Rong (Alibaba Cloud), Jing Zhang (Alibaba Cloud), Ensheng Xu (Alibaba Cloud), Boyu Ying (Alibaba Cloud), Fanghu Zheng (Alibaba Cloud), Guangren Chai (Alibaba Cloud), Erci Xu (Alibaba Cloud), Yuanchao Su (Alibaba Cloud), Dennis Cai (Alibaba Cloud)

## 英文摘要
Network is the single largest line item in a hyperscale Object Storage Service (OSS), consuming roughly 40% of an annual infrastructure bill measured in hundreds of millions of dollars. Two tiers dominate: the access network, where client traffic is locked into expensive in-region EdgePoPs despite 2–5× cheaper off-region bandwidth being widely available; and the intra-region network, where 3AZ replication amplifies every write into massive cross-AZ traffic that accounts for a substantial share of the network bill. We present Lean, a dedicated system that breaks through this barrier via application-infrastructure co-design, using SRv6 as a single unifying primitive to enable three capabilities: lightweight ingress units deployable at any EdgePoP, arbitrary traffic steering, and physical isolation of OSS traffic. In production for 4 years serving 𝑂(1𝐵) objects and 𝑂(10𝐾) enterprise customers, Lean has cut the OSS network bill by 55.6%, saving hundreds of millions of dollars annually.

## 中文摘要
网络是超大规模对象存储服务（OSS）中最大的一项单项支出，约占年度基础设施账单的 40%，而该账单以数亿美元计。其中两层网络占主导：一是接入网络，客户流量被锁定在昂贵的区域内 EdgePoP，尽管便宜 2–5 倍的区域外带宽广泛可用；二是区域内网络，3AZ 复制将每次写入放大为大量跨 AZ 流量，在网络账单中占相当大的比重。我们提出 Lean，一个专门系统，通过应用与基础设施协同设计突破这一障碍，使用 SRv6 作为单一统一的原语来实现三项能力：可部署于任意 EdgePoP 的轻量级入口单元、任意流量调度，以及 OSS 流量的物理隔离。Lean 已在生产环境运行 4 年，服务 O(1B) 个对象和 O(10K) 家企业客户，将 OSS 网络账单削减 55.6%，每年节省数亿美元。

## 英文关键词
Object Storage Service, Network Cost Reduction, Application-Infrastructure Coordination

## 中文关键词
对象存储服务，网络成本降低，应用与基础设施协同

[返回 Session 14](index.md) · [返回 ATC 2026](../index.md)
