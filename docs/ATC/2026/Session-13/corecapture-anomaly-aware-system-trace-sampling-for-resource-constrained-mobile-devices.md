# CoreCapture: Anomaly-Aware System Trace Sampling for Resource-Constrained Mobile Devices

**中文标题**：CoreCapture：面向资源受限移动设备的异常感知系统跟踪采样

**所属 Session**：[Session 13: Mobile, Edge and Embedded systems](index.md) · [ATC 2026](../index.md)

**作者**：Yongqian Sun (Nankai University), Xiaotian Wang (Nankai University), Yicheng Sui (Nankai University), Jintao Feng (Nankai University), Yue Zhang (Nankai University), Shenglin Zhang (Nankai University), Bowen Zheng (Huawei), Qiang Li (Huawei), Wei Liang (Huawei), Dan Pei (Tsinghua University)

## 英文摘要
Diagnosing performance anomalies on production mobile devices requires System Traces, which are whole-system runtime records spanning kernel, services, and applications. Yet each trace dump consumes over 100 MB, and the daily upload budget shared across all diagnostic components limits collection to a few dumps per day; anomalies occurring after the quota is exhausted are permanently lost. We present CoreCapture, an on-device system that compresses each dump by filtering out steady-state data while preserving anomaly-relevant diagnostic context. CoreCapture employs a dual-stream anomaly detector (DS-TraceNet) that separately models semantic and temporal features to identify anomalous traces, followed by a spatio-temporal retention mechanism (STA-ER) that expands each anomaly to a complete interaction-event window and prunes irrelevant threads. Evaluation on production traces shows that CoreCapture reduces per-dump volume by approximately 70% while preserving 95% event-level anomaly coverage. Deployed on production smartphones, it adds only 4–5% CPU and 13–15 MB memory overhead on device per alert-triggered dump. Our source code demo and two data cases are publicly available at https://github.com/linjiaxiaoyue/ CoreCapture.

## 中文摘要
在生产移动设备上诊断性能异常需要系统跟踪，即跨越内核、服务与应用的整系统运行时记录。然而每次跟踪转储占用超过 100 MB，而所有诊断组件共享的每日上传配额将采集限制为每天仅数次转储；配额耗尽后发生的异常会被永久丢失。我们提出 CoreCapture，一个端侧系统，通过过滤稳态数据同时保留与异常相关的诊断上下文来压缩每次转储。CoreCapture 采用双流异常检测器（DS-TraceNet），分别对语义特征与时间特征建模以识别异常跟踪，随后使用时序-空间保留机制（STA-ER）将每个异常扩展为完整的交互事件窗口并剪除无关线程。在生产跟踪数据上的评估表明，CoreCapture 将每次转储的数据量减少约 70%，同时保留 95% 的事件级异常覆盖率。在生产智能手机上部署后，每次由告警触发的转储在设备上仅增加 4–5% 的 CPU 和 13–15 MB 内存开销。我们的源代码演示与两个数据案例已公开在 https://github.com/linjiaxiaoyue/CoreCapture。

## 英文关键词
System Trace, Anomaly-Aware Sampling, Mobile Devices, On-Device Anomaly Detection, Performance Diagnosis

## 中文关键词
系统跟踪，异常感知采样，移动设备，端侧异常检测，性能诊断

## 代码与研究制品

- [code](https://github.com/linjiaxiaoyue/CoreCapture)

[返回 Session 13](index.md) · [返回 ATC 2026](../index.md)
