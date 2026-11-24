# Skip it, don’t speed it. Accelerating Graph Pattern Matching through Disjoint Intersection Bypassing

**中文标题**：跳过而非加速：通过不相交求交绕过加速图模式匹配

**官方议程标题**：Skip it, don't speed it. Accelerating Graph Pattern Matching through Disjoint Intersection Bypassing

**所属 Session**：[Session 11: Search, Recommender and Graph Systems](index.md) · [ATC 2026](../index.md)

**作者**：Haotian Ma (The Chinese University of Hong Kong, Shenzhen), Wei-Chung Hsu (The Chinese University of Hong Kong, Shenzhen), Yeh-Ching Chung (The Chinese University of Hong Kong, Shenzhen)

## 英文摘要
Set intersection dominates the inner loop of graph pattern matching (GPM). Practical engines repeatedly intersect sorted adjacency lists under irregular memory access and tight latency constraints, and many issued intersections produce no output. Our workload characterization shows that these disjoint intersections are common, especially under symmetry-breaking constraints. Prior work accelerates exact intersection kernels and prunes search states. Disjoint intersections nevertheless remain in the measured workload, leaving an opportunity to certify emptiness before exact execution. This paper presents GraphDIB, a Disjoint Intersection Bypassing mechanism for GPM. GraphDIB stores a cacheline-sized 512-bit signature per vertex neighborhood and tests two signatures with a single SIMD bitwise AND, where a zero result certifies disjointness and safely skips the exact intersection kernel. To maximize bypass coverage under this fixed metadata budget, GraphDIB learns a workload-specific projection from sampled disjoint intersections. We define false positive penalty to quantify how strongly pairs of vertices should map to different signature bits, use it to refine the projection iteratively, and extend the guard to symmetry-breaking constrained intersections through projection-aligned reordering. Across 16 workload instances, GraphDIB improves end-to-end performance by 1.56× geomean and up to 6.84× over the fastest evaluated baseline, while reducing executed intersections by 30.2% on average and preserving the original exact intersection kernel.

## 中文摘要
集合求交主导了图模式匹配（GPM）的内层循环。实用引擎在不规则内存访问和严苛延迟约束下反复对有序邻接表求交，而许多发出的求交并不产生输出。我们的负载刻画表明这类不相交求交十分常见，在对称性破除约束下尤为如此。已有工作加速了精确求交内核并剪枝搜索状态，但不相交求交在实测负载中依然存在，从而留下了在执行精确求交之前就证明结果为空的机会。本文提出 GraphDIB，一种面向 GPM 的不相交求交绕过机制。GraphDIB 为每个顶点邻域存储一个缓存行大小的 512 位签名，并用一次 SIMD 按位与同时测试两个签名，结果为零即可证明二者不相交，从而安全地跳过精确求交内核。为在固定元数据预算下最大化绕过覆盖率，GraphDIB 从采样得到的不相交求交中学习负载特定的投影。我们定义假阳性惩罚来量化顶点对应在多大程度上映射到不同的签名位，并用它迭代精化投影；同时通过投影对齐的重排序，将该守卫扩展到对称性破除约束下的求交。在 16 个负载实例上，GraphDIB 相比评测中最快的基线取得 1.56 倍的几何平均端到端性能提升，最高达 6.84 倍，同时平均减少 30.2% 的实际执行求交次数，并保留了原有的精确求交内核。

## 英文关键词
Graph Partitioning, Set Intersection, SIMD

## 中文关键词
图划分，集合求交，SIMD

[返回 Session 11](index.md) · [返回 ATC 2026](../index.md)
