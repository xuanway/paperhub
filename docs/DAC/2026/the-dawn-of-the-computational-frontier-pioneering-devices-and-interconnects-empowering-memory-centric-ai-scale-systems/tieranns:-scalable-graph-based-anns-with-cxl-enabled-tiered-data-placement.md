TierANNS: Scalable Graph-Based ANNS with CXL-Enabled Tiered Data Placement
Authors：
[Ying Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=9973642579201045128)，[Chao Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=04993692006417441231)，[Xiaowei Chen](https://63dac.conference-program.com/?post_type=page&p=15&uid=36461621502894497151)，[Tianyu Wang](https://63dac.conference-program.com/?post_type=page&p=15&uid=4102639928273142851)，[Chenlin Ma](https://63dac.conference-program.com/?post_type=page&p=15&uid=4213970674159892189)，[Zhaoyan Shen](https://63dac.conference-program.com/?post_type=page&p=15&uid=010443)，[Jiaxian Chen](https://63dac.conference-program.com/?post_type=page&p=15&uid=37582528852818661511)，[Kecheng Huang](https://63dac.conference-program.com/?post_type=page&p=15&uid=9023677625232671802)

## 中文标题

TierANNS：基于 CXL 分层数据放置的可扩展图式 ANNS

## 英文摘要

Performing Approximate Nearest Neighbor Search (ANNS) on large-scale vector datasets is essential for AI applications. Graph-based ANNS demonstrates superior performance and accuracy, positioning itself as a leading approach within the ANNS landscape. However, its inherent reliance on random data access mandates a memory-centric deployment strategy, which, in turn, poses significant scalability challenges. Recent advancements in Compute eXpress Link (CXL) technologies, known for their high-bandwidth memory extension capabilities, offer a critical opportunity to enhance the scalability of graph-based ANNS. Nonetheless, the implications of the CXL-extended memory architecture when applied to graph-based ANNS remain largely unexplored. In this paper, we present a CXL-Oriented Graph-based ANNS (COGA) system to achieve scalable, high-speed ANNS for extensive datasets. Our key observation is that the search pipeline can be enhanced through a CXL-tailored priority queue that maximizes CXL bandwidth utilization while bridging the latency gap. Furthermore, we propose a tiered data layout and placement strategy that leverages queue hints to facilitate speculative access to index data. Evaluation results show that our system achieves a speedup of 2.8-4.5× compared to existing CXL-based approaches.

## 中文摘要

在大规模向量数据集上执行近似最近邻搜索（ANNS）对人工智能应用至关重要。基于图的 ANNS 在性能与精度上表现优异，已成为 ANNS 领域的主流方法。然而，其对随机数据访问的固有依赖要求采用以内存为中心的部署策略，这又带来严峻的可扩展性挑战。近来以高带宽内存扩展能力著称的 Compute eXpress Link（CXL）技术的进展，为提升图式 ANNS 的可扩展性提供了关键契机。但将 CXL 扩展内存架构应用于图式 ANNS 究竟会带来何种影响，目前仍鲜有探索。本文提出面向 CXL 的图式 ANNS 系统 COGA，以面向大规模数据集实现可扩展的高速 ANNS。我们的关键观察是：可为 CXL 定制优先队列以增强搜索流水线，在最大化 CXL 带宽利用率的同时弥合延迟差距。此外，我们提出分层数据布局与放置策略，利用队列提示实现对索引数据的推测性访问。评估结果显示，本系统相比现有基于 CXL 的方法取得 2.8 至 4.5 倍的加速。

## 英文关键词

Compute Express Link, Approximate Nearest Neighbor Search, Hierarchical Navigable Small World

## 中文关键词

Compute Express Link、近似最近邻搜索、分层可导航小世界
