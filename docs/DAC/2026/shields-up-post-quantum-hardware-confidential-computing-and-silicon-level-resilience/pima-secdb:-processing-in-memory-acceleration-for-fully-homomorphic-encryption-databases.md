PIMA-SecDB: Processing-in-Memory Acceleration for Fully Homomorphic Encryption Databases
Authors：
[Lin Ding](https://63dac.conference-program.com/?post_type=page&p=15&uid=5848357759372200095)，[Pengao He](https://63dac.conference-program.com/?post_type=page&p=15&uid=05195458602253555431)，[Jiliang Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=711343)

## 中文标题

PIMA-SecDB：面向全同态加密数据库的存内计算加速架构

## 英文摘要

Databases utilizing fully homomorphic encryption (FHE) are the leading approach to preserving privacy for outsourced data. However, each query necessitates a full scan of all encrypted entries, imposing severe limitations on data access and processing efficiency. To address this bottleneck, we propose PIMA-SecDB, a processing-in-memory (PIM) architecture for FHE-based databases designed through rigorous hardware-software co-design. PIMA-SecDB features a three-tier hierarchical structure: the DIMM-level aggregation module, the x8 chip level with in-memory functional units, and the bank group level for data storage—enabling high intra-module bandwidth and parallelism for efficient in-situ processing. Moreover, we have developed a set of data management mechanisms to adapt to the parallel computing capabilities of PIMA-SecDB and a quantitative approach for selecting PIM-compatible encryption parameters to reduce computational load and data footprint. The experiment shows that PIMA-SecDB offers performance enhancements from 2.14 to 7.89× compared to existing FHE accelerators.

## 中文摘要

采用全同态加密（FHE）的数据库是保护外包数据隐私的主流方案。然而，每次查询都需要对所有加密条目进行全扫描，严重限制了数据访问与处理效率。为突破这一瓶颈，我们提出 PIMA-SecDB——一种面向 FHE 数据库的存内计算（PIM）架构，其设计经过严格的软硬件协同优化。PIMA-SecDB 采用三层层次化结构：DIMM 级聚合模块、集成存内功能单元的 x8 芯片级，以及用于数据存储的 bank group 级，从而在模块内部实现高带宽与高并行度，以支持高效的原地处理。此外，我们还开发了一套数据管理机制以适配 PIMA-SecDB 的并行计算能力，并提出一种定量方法来选择与 PIM 兼容的加密参数，以降低计算负载与数据占用。实验表明，与现有 FHE 加速器相比，PIMA-SecDB 的性能提升达 2.14 至 7.89 倍。

## 英文关键词

Fully Homomorphic Encryption (FHE), Processing-in-memory (PIM), Encrypted Database, FHE Acceleration, Privacy-preserving Computation

## 中文关键词

全同态加密（FHE）、存内计算（PIM）、加密数据库、FHE 加速、隐私保护计算
