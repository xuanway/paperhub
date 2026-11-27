Freezone: An On-Device Out-of-Order Writes Reordering Scheme for Consumer Zoned Storage
Authors：
[Dingcui Yu](https://63dac.conference-program.com/?post_type=page&p=15&uid=6275613175492510145)，[Mengyang MA](https://63dac.conference-program.com/?post_type=page&p=15&uid=09506168951746339071)，[Tianyu REN](https://63dac.conference-program.com/?post_type=page&p=15&uid=61625621441718601271)，[Hongyu Zhu](https://63dac.conference-program.com/?post_type=page&p=15&uid=68044221732406707441)，[Xinghui Duan](https://63dac.conference-program.com/?post_type=page&p=15&uid=48020052544485262541)，[Yina Lv](https://63dac.conference-program.com/?post_type=page&p=15&uid=01023773994143462201)，[Lei Qiao](https://63dac.conference-program.com/?post_type=page&p=15&uid=0726272830970326449)，[Liang Shi](https://63dac.conference-program.com/?post_type=page&p=15&uid=324143)

## 中文标题

FreeZone：面向消费级分区存储的盘内乱序写重排方案

## 英文摘要

The zone interface has emerged as a promising standard in consumer devices to support high random read performance, as its design reduces read amplification and enables efficient read parallelism. However, to support the underlying zone interface, the kernel’s I/O subsystem must enforce strictly sequential writes per zone by logically ordering requests, which results in reduced write parallelism at the kernel level. Although prior work mitigates this by offloading the request reordering process to the on-device write buffer, the limited buffer size in consumer devices cannot accommodate the growing volume of requests that require reordering. This paper proposes FreeZone, an on-device writes reordering solution that extends the write buffer size by using the high-performance SLC flash region of storage. FreeZone allows the kernel to submit I/O requests freely, improving parallel write performance. Evaluation demonstrates that FreeZone achieves up to a 2.3× IOPS improvement compared with existing zoned storage architectures.

## 中文摘要

分区（zone）接口已成为消费级设备中一种有前景的标准，用于支持高随机读性能，因为其设计降低了读放大并实现了高效的读并行。然而，为支撑底层分区接口，内核 I/O 子系统必须通过对请求进行逻辑排序，强制每个分区内严格顺序写，这导致内核层面的写并行度下降。尽管已有工作通过将请求重排过程卸载到盘内写缓冲区来缓解这一问题，但消费级设备中有限的缓冲区容量无法容纳日益增长的待重排请求量。本文提出 FreeZone，一种盘内写重排方案，利用存储中高性能的 SLC 闪存区域来扩展写缓冲区容量。FreeZone 允许内核自由提交 I/O 请求，从而提升并行写性能。评估表明，与现有分区存储架构相比，FreeZone 实现了最高 2.3 倍的 IOPS 提升。

## 英文关键词

zoned storage, hierarchical storage management, operating system

## 中文关键词

分区存储、分层存储管理、操作系统
