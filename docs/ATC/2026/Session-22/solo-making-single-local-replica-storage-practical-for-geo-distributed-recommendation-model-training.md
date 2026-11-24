# SOLO: Making Single-Local-Replica Storage Practical for Geo-Distributed Recommendation Model Training

**中文标题**：SOLO：使单本地副本存储在地理分布式推荐模型训练中切实可行

**所属 Session**：[Session 22: Large-scale AI](index.md) · [ATC 2026](../index.md)

**作者**：Tao Li (University of Science and Technology of China), Long Deng (University of Science and Technology of China), Xinyuan Li (ByteDance China), Xukun Chen (ByteDance China), Zheyu Lin (ByteDance China), Shibo Chen (ByteDance China), Shiru Ren (ByteDance China), Jingwei Xu (ByteDance China), Wei Zhang (ByteDance China), Jianhui Lu (ByteDance China), Yong Tian (ByteDance China), Bin Zhang (ByteDance China), Wei Feng (ByteDance China), Yang Guo (ByteDance China), Hang Cheng (ByteDance China), Jixi Shan (ByteDance China), Jun Song (ByteDance China), Wenzhe Zhu (University of Science and Technology of China), Yongkun Li (University of Science and Technology of China), Yinlong Xu (University of Science and Technology of China)

## 英文摘要
Large-scale deep learning recommendation model (DLRM) training commonly spans geo-distributed datacenters. Modern DLRMs consume increasingly rich training samples, pushing data footprints toward exabyte scale. At this scale, maintaining local storage redundancy substantially amplifies the footprint. Under strict datacenter power envelopes, this storage infrastructure directly competes with GPU deployment limits. We observe that datasets are already globally replicated for job scheduling, creating an opportunity to replace local multi-replica redundancy with single-local-replica storage backed by remote repair. However, eliminating local redundancy sacrifices read-time availability and reduces the read-serving capacity necessary to keep GPUs fully utilized. We present SOLO, a data orchestration system co-designed with DLRM training workloads to make single-local-replica storage practical. First, it leverages predictable data consumption orders to proactively check and repair upcoming files, preserving read-time local availability. Second, it exploits structured and skewed access patterns together with cross-job preprocessing similarity to achieve workload-aware data placement and compact intermediate reuse, preserving high-throughput data reads. We have deployed SOLO across multiple datacenters in ByteDance’s production infrastructure, serving thousands of daily jobs. SOLO reduces per-GPU storage cost by 45%–55%, saves tens of exabytes of storage and tens of megawatts of power capacity, consumes less than 1% of inter-datacenter bandwidth, and improves GPU SM activity by 1.35×–2.41× on I/O-bound jobs.

## 中文摘要
大规模深度学习推荐模型（DLRM）训练通常跨地理分布的数据中心进行。现代 DLRM 使用日益丰富的训练样本，使数据规模向 EB 级推进。在这一规模下，维持本地存储冗余会显著放大占用空间。在严格的数据中心功耗上限下，这类存储基础设施直接与 GPU 部署上限竞争。我们观察到，数据集已为作业调度而在全局进行了复制，这为用远程修复支撑的单本地副本存储取代本地多副本冗余创造了机会。然而，消除本地冗余会牺牲读时可用性，并降低维持 GPU 充分利用所需的读服务能力。我们提出 SOLO，一个与 DLRM 训练负载协同设计的数据编排系统，使单本地副本存储切实可行。首先，它利用可预测的数据消费顺序，主动检查并修复即将被读取的文件，从而保持读时的本地可用性。其次，它利用结构化且倾斜的访问模式以及跨作业的预处理相似性，实现负载感知的数据放置与紧凑的中间结果复用，从而保持高吞吐的数据读取。我们已在字节跳动生产基础设施的多个数据中心部署 SOLO，服务数千个日常作业。SOLO 将每 GPU 存储成本降低 45%–55%，节省数十 EB 存储与数十兆瓦电力容量，消耗的跨数据中心带宽不到 1%，并在 I/O 受限作业上把 GPU SM 活跃度提升 1.35×–2.41×。

## 英文关键词
Recommendation Model Training, Geo-Distributed Storage, Single Replica

## 中文关键词
推荐模型训练，地理分布式存储，单副本

[返回 Session 22](index.md) · [返回 ATC 2026](../index.md)
