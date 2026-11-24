# ESROS2: Application Sandboxes for Secure ROS2

**中文标题**：ESROS2：面向安全 ROS2 的应用沙箱

**所属 Session**：[Session 13: Mobile, Edge and Embedded systems](index.md) · [ATC 2026](../index.md)

**作者**：Dev Tejas Gandhi (Indian Institute of Science Bangalore), Vinod Ganapathy (Indian Institute of Science Bangalore)

## 英文摘要
ROS2 is a popular middleware for several robotics platforms. It allows rapid prototyping of distributed robotics applications via a convenient publish/subscribe-based abstraction for application communication. Secure ROS2 (SROS2) is a set of patches to ROS2 that provides several basic security primitives to secure application communication, such as encrypted communication and limiting applications to only publish/subscribe to topics that are declared in a manifest. Unfortunately, SROS2 is limited in its ability to confine application communication. Applications can freely communicate with each other by bypassing the SROS2 API and directly making system calls via the underlying operating system. This paper introduces ESROS2, which provides application sandboxing in SROS2. ESROS2 confines applications by limiting the set of system calls that they can issue at runtime. When an application issues a system call, ESROS2 determines whether the context in which the system call was issued is safe, and only then permits the system call to be issued. We describe the design of ESROS2 and its implementation using extended Berkeley Packet Filters (eBPF) and commodity intra-process memory isolation hardware (Intel MPK). We show that ESROS2 works on off-the-shelf application binaries, and effectively enforces application sandboxing while only imposing a modest performance overhead.

## 中文摘要
ROS2 是多种机器人平台上广泛使用的中间件。它通过便捷的、基于发布/订阅的应用通信抽象，支持分布式机器人应用的快速原型开发。Secure ROS2（SROS2）是 ROS2 的一组补丁，提供若干基础安全原语以保护应用通信，例如加密通信，以及将应用限制为只能发布/订阅清单中声明的主题。遗憾的是，SROS2 在限制应用通信方面的能力有限。应用可以绕过 SROS2 API，直接通过底层操作系统发起系统调用来自由地相互通信。本文提出 ESROS2，它在 SROS2 中提供应用沙箱。ESROS2 通过限制应用在运行时可以发起的系统调用集合来约束应用。当应用发起系统调用时，ESROS2 判断该系统调用发起时所处的上下文是否安全，只有安全时才允许发起该系统调用。我们描述了 ESROS2 的设计及其使用扩展 Berkeley 包过滤器（eBPF）与商用进程内内存隔离硬件（Intel MPK）的实现。我们表明 ESROS2 可在现成的应用二进制上工作，并在仅带来适度性能开销的情况下有效实施应用沙箱。

## 英文关键词
ROS2, application sandboxing, extended Berkeley packet filters, intra-process isolation

## 中文关键词
ROS2，应用沙箱，扩展 Berkeley 包过滤器，进程内隔离

[返回 Session 13](index.md) · [返回 ATC 2026](../index.md)
