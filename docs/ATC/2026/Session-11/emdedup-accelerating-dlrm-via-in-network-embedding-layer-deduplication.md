# EMDedup: Accelerating DLRM via In-Network EMbedding Layer Deduplication

**中文标题**：EMDedup：通过网内嵌入层去重加速 DLRM

**所属 Session**：[Session 11: Search, Recommender and Graph Systems](index.md) · [ATC 2026](../index.md)

**作者**：Wenjie Li (SKLP, Institute of Computing Technology, Chinese Academy of Sciences; Zhengzhou University), Ke Liu (SKLP, Institute of Computing Technology, Chinese Academy of Sciences), Zhao Zhang (SKLP, Institute of Computing Technology, Chinese Academy of Sciences), Ning Liu (Huawei), Hui Yuan (Huawei), Zixuan Guan (Huawei), Xiaolong Zheng (Huawei), Xu Zhang (SKLP, Institute of Computing Technology, Chinese Academy of Sciences), Kefan Liu (SKLP, Institute of Computing Technology, Chinese Academy of Sciences), Guanghui Zhang (Shandong University), Yungang Bao (ICT, CAS), Mingyu Chen (SKLP, Institute of Computing Technology, Chinese Academy of Sciences), Chenxi Wang (SKLP, Institute of Computing Technology, CAS; University of Chinese Academy of Sciences)

## 英文摘要
DLRM systems are highly dependent on the efficiency of the embedding layer, which becomes increasingly critical as it scales trillions of parameters, causing the model’s memory footprint to exceed the HBM capacity of a single GPU node. Consequently, DLRM is scaled out by sharding the embedding layer across multiple nodes for distributed inference and training, shifting the bottleneck to all-to-all communication over fast interconnects such as RDMA and CXL. Prior works addressed the challenge with fine-grained hybrid parallelism that uses DP for caching hot embeddings. However, for TB-scale DLRM with multi-hot sparse features, caching proves neither cost-effective nor efficient to address the communication bottleneck. Our insight shows that 1) deduplication achieves comparable communication volume reduction to caching under large global batch sizes, without persistent embedding replication, and 2) as DLRMs scale out across many nodes, there is a non-trivial fraction of cross-node duplicated sparse feature requests, which can be identified by in-network deduplication. Motivated, we propose EMDedup, a host-network co-designed system accelerating distributed DLRM training and inference, which offloads request deduplication and multicast to programmable switches, while also incorporating existing in-network gradient aggregation to further improve DLRM training. Its customized endhost communication backend enables in-network functions to operate transparently with existing DLRM frameworks and embedding parallelisms. Real testbed results show that EMDedup reduces communication and embedding overhead, achieving average speedups of 1.74x and 1.94x in training and inference runtime over PyTorch DLRM systems, while our large-scale simulations also have similar results.

## 中文摘要
DLRM 系统高度依赖嵌入层的效率，随着其参数规模增长到数万亿，嵌入层愈发关键，导致模型的内存占用超过单个 GPU 节点的 HBM 容量。因此，DLRM 通过将嵌入层分片到多个节点上来横向扩展以进行分布式推理与训练，瓶颈随之转移到 RDMA 和 CXL 等高速互连上的全对全通信。已有工作采用细粒度混合并行（使用 DP 缓存热嵌入）来应对这一挑战。然而，对于具有多热稀疏特征的 TB 级 DLRM，缓存既不具备成本效益，也无法高效地解决通信瓶颈。我们的洞见表明：1）在大全局批大小下，去重可以达到与缓存相当的通信量削减效果，且无需持久复制嵌入；2）当 DLRM 横向扩展到众多节点时，存在不可忽略比例的跨节点重复稀疏特征请求，这些请求可以通过网内去重识别。基于此，我们提出 EMDedup，一个主机-网络协同设计的系统，用于加速分布式 DLRM 训练与推理，它将请求去重与多播卸载到可编程交换机，同时结合已有的网内梯度聚合以进一步改进 DLRM 训练。其定制的端主机通信后端使网内功能能够透明地与现有 DLRM 框架和嵌入并行方式协同工作。真实测试床结果表明，EMDedup 降低了通信与嵌入开销，相比 PyTorch DLRM 系统在训练和推理运行时分别取得平均 1.74 倍和 1.94 倍的加速，我们的大规模仿真也得到类似结果。

## 英文关键词
Deep learning recommendation models, In-network computing, Deduplication

## 中文关键词
深度学习推荐模型，网内计算，去重

[返回 Session 11](index.md) · [返回 ATC 2026](../index.md)
