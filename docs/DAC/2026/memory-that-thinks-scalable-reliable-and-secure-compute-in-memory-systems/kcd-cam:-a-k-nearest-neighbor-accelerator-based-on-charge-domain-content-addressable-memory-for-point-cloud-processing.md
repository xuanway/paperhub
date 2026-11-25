KCD-CAM: A K-Nearest-Neighbor Accelerator Based on Charge-Domain Content-Addressable-Memory for Point Cloud Processing
Authors：
[Tong Hu](https://63dac.conference-program.com/?post_type=page&p=15&uid=5493654357975381669)，[Jiancong Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=7850206274924480873)，[Yingjie Yu](https://63dac.conference-program.com/?post_type=page&p=15&uid=11422021337699019251)，[Zhiwei Zhou](https://63dac.conference-program.com/?post_type=page&p=15&uid=9918726170358410803)，[Jia Chen](https://63dac.conference-program.com/?post_type=page&p=15&uid=09783556249522139631)，[Yi Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=2462582682263448031)，[Xiangshui Miao](https://63dac.conference-program.com/?post_type=page&p=15&uid=490210146683911856)

## 中文标题

KCD-CAM：一种基于电荷域内容寻址存储器的点云处理 K 近邻加速器

## 英文摘要

Three-dimensional (3D) point cloud models have been widely employed in modern 3D perception tasks such as robotics, autonomous driving, and virtual reality. The k-nearest-neighbor (KNN) search serves as a cornerstone operation for point cloud models, providing the essential mechanism for defining and exploiting local spatial relationships within unstructured data. However, the massive scale of point cloud data and the high computational complexity of Euclidean distance-based top-k searches in KNN impose substantial computational overhead. Conventional edge computing platforms struggle to achieve realtime and high efficiency of point cloud processing. In this work, we propose KCD-CAM, a KNN accelerator using ReRAM-based charge-domain content-addressable memory (CAM) for efficient point cloud processing. The proposed KCD-CAM employs a 4T2R CAM cell capable of performing in-situ range search, effectively replacing complex Euclidean distance calculations with massively parallel operations. In addition, corner-clipped (CC) iterative top-k search scheme and dual-granularity voxel hashing (DG-VH) are employed to enhance accuracy and parallelism. Performance benchmarks in real-world datasets demonstrate that KCD-CAM achieves 279.79× higher speed and 3282× greater energy efficiency than GPU implementations. Compared to the SOTA KNN accelerators, our KCD-CAM also achieved 8.51× and 4.76× improvements in speed and energy efficiency, respectively.

## 中文摘要

三维（3D）点云模型已广泛应用于机器人、自动驾驶与虚拟现实等现代 3D 感知任务。k 近邻（KNN）搜索是点云模型的基础操作，为在非结构化数据中定义与利用局部空间关系提供了关键机制。然而，点云数据的庞大规模以及 KNN 中基于欧氏距离的 top-k 搜索的高计算复杂度带来了沉重的计算开销。传统边缘计算平台难以兼顾点云处理的实时性与高能效。本文提出 KCD-CAM，一种采用基于 ReRAM 的电荷域内容寻址存储器（CAM）的 KNN 加速器，用于高效点云处理。所提 KCD-CAM 采用可原地执行范围搜索的 4T2R CAM 单元，以大规模并行操作有效替代复杂的欧氏距离计算。此外，采用角点裁剪（CC）迭代 top-k 搜索方案与双粒度体素哈希（DG-VH）以提升精度与并行度。在真实数据集上的性能基准测试表明，KCD-CAM 相较 GPU 实现取得 279.79 倍的加速与 3282 倍的能效提升；与当前最优 KNN 加速器相比，KCD-CAM 在速度与能效上分别提升 8.51 倍与 4.76 倍。

## 英文关键词

Point cloud, K-nearest-neighbor search, Content-addressable-memory, Compute-in-memory

## 中文关键词

点云、k 近邻搜索、内容寻址存储器、存内计算
