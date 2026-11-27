HDDB: Efficient In-Storage SQL Database Search Using Hyperdimensional Computing on Ferroelectric NAND Flash
Authors：
[Quanling Zhao](https://63dac.conference-program.com/?post_type=page&p=15&uid=5206446888527865201)，[Yanru Chen](https://63dac.conference-program.com/?post_type=page&p=15&uid=5572618758601895021)，[Runyang Tian](https://63dac.conference-program.com/?post_type=page&p=15&uid=57248037345382668711)，[Sumukh Pinge](https://63dac.conference-program.com/?post_type=page&p=15&uid=820904522695200884)，[Weihong Xu](https://63dac.conference-program.com/?post_type=page&p=15&uid=01084335719793086831)，[Augusto Vega](https://63dac.conference-program.com/?post_type=page&p=15&uid=804143)，[Steven Holmes](https://63dac.conference-program.com/?post_type=page&p=15&uid=3909469412404121825)，[Saransh Gupta](https://63dac.conference-program.com/?post_type=page&p=15&uid=4121006736621562969)，[Tajana Rosing](https://63dac.conference-program.com/?post_type=page&p=15&uid=913243)

## 中文标题

HDDB：在铁电 NAND 闪存上利用超维计算的高效存内 SQL 数据库搜索

## 英文摘要

Hyperdimensional Computing (HDC) represents data as high dimensional distributed vectors manipulated through simple bitwise operations and similarity search, providing parallelism, low-precision hardware efficiency, and strong noise robustness. These properties suit SQL workloads dominated by predicate evaluation and scans, which require low latency and energy efficiency over large fact tables. HDC’s noise tolerance also aligns well with emerging ferroelectric NAND (FeNAND) memory, which offers ultra-high density and in-storage compute but suffers from high raw bit-error rates. We propose HDDB, a hardware-software co-design that combines HDC with FeNAND multi-level cells (MLC) for massively parallel, in-storage SQL predicate evaluation and analytics with minimal data movement. We introduce new HDC encodings for standard SQL tables and express predicate filtering and aggregation as highly efficient in-storage HDC operations. By leveraging HDC’s intrinsic redundancy, HDDB preserves correct predicate and decode results under substantial device noise, including up to 10% randomly corrupted TLC cells, without explicit error-correction overhead. Experiments on TPC-DS fact tables show that HDDB achieves up to 80.6× lower latency and 12,636× lower energy than conventional CPU/GPU SQL engines, suggesting it is a practical substrate for noise-robust, memory-centric database processing.

## 中文摘要

超维计算（HDC）将数据表示为高维分布式向量，通过简单的位运算与相似性搜索进行操作，具有并行性、低精度硬件效率和强噪声鲁棒性。这些特性适合以谓词求值与扫描为主的 SQL 工作负载，此类负载需要在大型事实表上实现低延迟与高能效。HDC 的噪声容忍性也与新兴的铁电 NAND（FeNAND）存储器高度契合，后者提供超高密度与存内计算能力，但原始误码率较高。我们提出 HDDB，这是一种软硬件协同设计，将 HDC 与 FeNAND 多值单元（MLC）相结合，以最少的数据移动实现大规模并行的存内 SQL 谓词求值与分析。我们为标准 SQL 表引入了新的 HDC 编码，并将谓词过滤与聚合表达为高效的存内 HDC 操作。借助 HDC 固有的冗余性，HDDB 在显著的器件噪声下——包括高达 10% 的 TLC 单元随机损坏——仍能保持正确的谓词与解码结果，而无需显式的纠错开销。在 TPC-DS 事实表上的实验表明，HDDB 相较传统 CPU/GPU SQL 引擎可实现最高 80.6 倍的延迟降低和 12,636 倍的能耗降低，表明它是噪声鲁棒、以内存为中心的数据库处理的一种实用基底。
