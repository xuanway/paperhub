# XCG: Decoupling Control from Configuration to Improve Cgroup Scalability with Flat Mapping

**中文标题**：XCG：解耦控制与配置，以扁平映射提升 cgroup 可扩展性

**所属 Session**：[Session 17: Scheduling and Serverless](index.md) · [ATC 2026](../index.md)

**作者**：Ruofan Xiong (Xiamen University), Li Wang (KylinSoft), Zhihao Zhang (Tsinghua University), Xinbiao Gan (NUDT), Yiming Zhang (Shanghai Jiao Tong University)

## 英文摘要
Cgroup (control group) is the Linux kernel mechanism that underpins resource management for containers, a foundational building block of modern cloud systems. A cgroup combines a core, which maintains hierarchical configuration and process-controller mappings, with resource controllers, which enforce limits on the connected processes. This coupled design provides flexible resource management, but it serializes cgroup creation and process attachment through coarse-grained kernel synchronization, compromising scalability when launching many short-lived containers simultaneously. Existing pooling-based mitigations move cgroup creation off the startup path but do not remove the underlying cost: pools must be provisioned for bursts, can miss during spikes, and add management overhead. We observe that serverless platforms typically organize processes into per-container groups and enforce resource limitations at the granularity of individual containers, and thus there is no correlation between processes across different containers. Based on this observation, in this paper we present XCG, a novel extension to cgroup for improving its scalability. The basic idea of XCG is to decouple control (by the controllers) from configuration (by the core), allowing container startup to involve only the creation of controllers for predefined resource usage control, while avoiding the creation of the core. The removal of cgroup core enables flat process-controller mapping, i.e., directly attaching the processes to the controllers, which allows XCG to use fine-grained locks to protect cgroup operations thus effectively improving scalability. XCG further reduces controller setup cost through lazy release and on-demand initialization, and streamlines configuration by extending cgroupfs with an ioctl interface that batches creation and configuration into a single operation. We have implemented XCG on Linux kernel v6.7.2. Extensive evaluation shows that XCG significantly outperforms the original cgroup design when launching a large number of containers in parallel.

## 中文摘要
cgroup（控制组）是支撑容器资源管理的 Linux 内核机制，也是现代云系统的基础构件。一个 cgroup 由核心（core）与资源控制器（controller）组合而成：核心维护层次化配置和进程—控制器映射，控制器则对挂接的进程施加限制。这种耦合设计提供了灵活的资源管理，却通过粗粒度的内核同步把 cgroup 创建与进程挂接串行化，在同时启动大量短生命周期容器时损害了可扩展性。现有的基于池化的缓解方法把 cgroup 创建移出启动路径，但未消除底层开销：池必须按突发规模预配置，在尖峰时可能发生失效，还增加了管理开销。我们观察到，无服务器平台通常把进程组织为每容器一组，并以单个容器为粒度施加资源限制，因此不同容器之间的进程不存在关联。基于这一观察，本文提出 XCG，一种对 cgroup 的新颖扩展，用于提升其可扩展性。XCG 的基本思想是把（由控制器承担的）控制与（由核心承担的）配置解耦，使容器启动只涉及为预定义的资源用量控制创建控制器，而避免创建核心。去除 cgroup 核心可实现扁平的进程—控制器映射，即把进程直接挂接到控制器上，这使 XCG 能够用细粒度锁保护 cgroup 操作，从而有效提升可扩展性。XCG 进一步通过延迟释放和按需初始化降低控制器建立开销，并扩展 cgroupfs 增加 ioctl 接口，把创建与配置批处理为单次操作，从而简化配置。我们已在 Linux 内核 v6.7.2 上实现 XCG。大量评估表明，在并行启动大量容器时，XCG 显著优于原始 cgroup 设计。

## 英文关键词
control groups (cgroups), containers, serverless computing, scalability

## 中文关键词
控制组（cgroup），容器，无服务器计算，可扩展性

[返回 Session 17](index.md) · [返回 ATC 2026](../index.md)
