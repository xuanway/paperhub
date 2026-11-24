# Breaking Host-Wide Blocking: Boundary-Closure SCSI Error Handling

**中文标题**：打破主机级阻塞：边界闭合的 SCSI 错误处理

**所属 Session**：[Session 23: Storage and OS Policies](index.md) · [ATC 2026](../index.md)

**作者**：Dongdong Hao (Xiamen University), Ye Xu (LeapIO Inc.), Jiazheng Zhang (LeapIO Inc.), Xiaoyang Wang (LeapIO Inc.), Shuo Wang (LeapIO Inc.), Jiwu Shu (Xiamen University, Tsinghua University)

## 英文摘要
Linux SCSI Error Handling (EH) in modern storage systems frequently causes excessive host-wide blocking and prolonged fault-resolution duration. Our observations reveal that recovery durations range from tens of seconds to minutes, stalling healthy devices across the entire host even when faults remain localized, which conflicts with the bounded response-time requirements of modern applications. To mitigate these limitations, we propose a boundary-closure SCSI error handling (BC-EH) mechanism, which infers the minimal necessary recovery boundary from SCSI topology, forward progress loss (FPL) evidence, and driver capability constraints, and then confines blocking, validation, and recovery actions to that boundary. In contrast to existing Linux SCSI EH, BC-EH decouples fault-boundary inference from recovery execution, preventing unnecessary recovery escalation beyond the inferred fault boundary. We implement BC-EH in Linux kernel 6.18 and evaluate it across multiple SCSI drivers and storage backends. Experimental results demonstrate that BC-EH achieves up to a 9.9× reduction in fault-resolution duration and shortens Kafka JBOD error handling activity windows by 3.7×, while showing no statistically significant steady-state performance bias (0.04% signed mean difference).

## 中文摘要
现代存储系统中的 Linux SCSI 错误处理（EH）经常造成过度的主机级阻塞与过长的故障解决时间。我们的观察显示，恢复时长从数十秒到数分钟不等，即使故障仍局限于局部，也会使整个主机上的健康设备停顿，这与现代应用有界响应时间的要求相冲突。为缓解这些局限，我们提出边界闭合的 SCSI 错误处理（BC-EH）机制，它从 SCSI 拓扑、前向进展丢失（FPL）证据与驱动能力约束中推断出最小必要的恢复边界，随后把阻塞、校验与恢复动作限制在该边界之内。与现有 Linux SCSI EH 相比，BC-EH 将故障边界推断与恢复执行解耦，避免恢复不必要地升级到推断出的故障边界之外。我们在 Linux 内核 6.18 中实现 BC-EH，并在多种 SCSI 驱动与存储后端上进行了评估。实验结果表明，BC-EH 将故障解决时长最多缩短 9.9×，将 Kafka JBOD 错误处理活动窗口缩短 3.7×，同时未表现出统计上显著的稳态性能偏差（有符号平均差异 0.04%）。

## 英文关键词
SCSI error handling, boundary closure, forward progress loss, Linux kernel

## 中文关键词
SCSI 错误处理，边界闭合，前向进展丢失，Linux 内核

[返回 Session 23](index.md) · [返回 ATC 2026](../index.md)
