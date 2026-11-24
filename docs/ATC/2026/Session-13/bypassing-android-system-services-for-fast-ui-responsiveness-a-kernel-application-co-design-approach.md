# Bypassing Android System Services for Fast UI Responsiveness: A Kernel-Application Co-Design Approach

**中文标题**：绕过 Android 系统服务以实现快速 UI 响应：一种内核与应用协同设计方法

**所属 Session**：[Session 13: Mobile, Edge and Embedded systems](index.md) · [ATC 2026](../index.md)

**作者**：Zizhan Chen (Chongqing University), Renhai Chen (Huawei Technologies Co., Ltd), Zili Shao (The Chinese University of Hong Kong)

## 英文摘要
Android’s input and display paths rely heavily on user-space system services (InputFlinger, SurfaceFlinger), which introduce significant inter-process communication and scheduling overhead, leading to high latency and limited scalability. We present a method that bypasses these system services by splitting their functionality between the Linux kernel and individual application processes. In the kernel, a Screen Manager module directly dispatches input events and composites display buffers; within each process, dedicated memory segments and shared libraries allow unmodified apps to consume input and submit frames without involving any user-space service. This kernel-application co-design eliminates redundant IPC and context switches from the critical path. Our prototype on Android 14 reduces end-to-end input latency by 90.91% and display latency by 87.93%, while also lowering CPU and memory usage, and significantly improves scalability as the number of concurrent apps increases. All source code is publicly available.

## 中文摘要
Android 的输入与显示路径严重依赖用户态系统服务（InputFlinger、SurfaceFlinger），这会引入大量进程间通信与调度开销，导致高延迟和有限的可扩展性。我们提出一种方法，通过将上述系统服务的功能在 Linux 内核与各个应用进程之间拆分来绕过这些系统服务。在内核中，一个屏幕管理器模块直接派发输入事件并合成显示缓冲区；在每个进程内部，专用内存段与共享库使未经修改的应用即可消费输入并提交帧，而无需涉及任何用户态服务。这种内核与应用协同设计从关键路径上消除了冗余的 IPC 与上下文切换。我们在 Android 14 上的原型将端到端输入延迟降低 90.91%，将显示延迟降低 87.93%，同时还降低了 CPU 与内存占用，并随着并发应用数量增加显著提升了可扩展性。全部源代码已公开。

## 英文关键词
embedded software, mobile system, Android

## 中文关键词
嵌入式软件，移动系统，Android

[返回 Session 13](index.md) · [返回 ATC 2026](../index.md)
