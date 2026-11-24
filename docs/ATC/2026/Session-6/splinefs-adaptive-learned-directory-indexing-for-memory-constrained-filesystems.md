# SplineFS: Adaptive Learned Directory Indexing for Memory-Constrained Filesystems

**中文标题**：SplineFS：面向内存受限文件系统的自适应学习式目录索引

**所属 Session**：[Session 6: Storage and File Systems](index.md) · [ATC 2026](../index.md)

**作者**：Jianqiang Zeng (Peking University), Shaocong Sun (Peking University), Chengying Huan (Nanjing University), Peng Wang (Huazhong University of Science and Technology), Ke Zhou (Huazhong University of Science and Technology), Yingwei Luo (Peking University), Xiaolin Wang (Peking University), Zhenlin Wang (Michigan Technological University), Diyu Zhou (Peking University), Yingdi Shan (Tsinghua University), Jie Zhang (Peking University)

## 英文摘要
Local filesystems manage increasingly large namespaces under limited directory-index cache. When this working set no longer fits, namespace walks suffer repeated dcache misses and directory-index probes before reaching file data. A learned index can reduce this overhead by replacing explicit routing metadata with a compact model that maps a lookup key to a small candidate range. However, applying learned indexing to filesystem directories is non-trivial: mutations change the key-to-record mapping and can force model maintenance, while parent-scoped lookup fragments the namespace into small keysets that duplicate models and leave little search to save. We observe that namespace mutations cluster in space and operation order, so large, stable subtrees are the right unit of learned indexing. We present SplineFS, a filesystem that promotes a quiet subtree into one shared learned index, amortizing the model across its directories while avoiding frequent retraining. An append-only delta absorbs occasional mutations, and sustained churn triggers demotion to the conventional layout, so SplineFS does no harm where locality is absent. Implemented in ext4, SplineFS reduces directory metadata by up to 19.7× and improves cold-scan throughput by up to 3.6× on real namespaces, and speeds real application stages by up to 2.1×.

## 中文摘要
本地文件系统在有限的目录索引缓存下管理着日益庞大的命名空间。当这一工作集不再能被容纳时，命名空间遍历在到达文件数据之前就会遭遇反复的 dcache 缺失和目录索引探测。学习式索引可以通过用一个紧凑模型把查找键映射到一小段候选范围来替代显式路由元数据，从而降低这一开销。然而，将学习式索引应用于文件系统目录并非易事：变更会改变键到记录的映射，可能迫使模型进行维护；而父目录作用域内的查找会把命名空间切碎成许多小键集，导致模型重复并且可节省的搜索空间很小。我们观察到命名空间的变更在空间和操作顺序上呈聚集分布，因此大型稳定子树才是学习式索引的合适单位。我们提出 SplineFS，一个把安静的子树提升为一个共享学习式索引的文件系统，它在这些目录之间摊销模型开销，同时避免频繁重训练。一个只追加的增量吸收偶发的变更，而持续的改动则会触发降级回传统布局，因此 SplineFS 在缺乏局部性的场景下不会造成损害。SplineFS 在 ext4 中实现，在真实命名空间上将目录元数据最多减少 19.7×，将冷扫描吞吐最多提升 3.6×，并将真实应用的阶段速度最多提升 2.1×。

## 英文关键词
File systems, directory index, learned index, namespace locality

## 中文关键词
文件系统，目录索引，学习式索引，命名空间局部性

[返回 Session 6](index.md) · [返回 ATC 2026](../index.md)
