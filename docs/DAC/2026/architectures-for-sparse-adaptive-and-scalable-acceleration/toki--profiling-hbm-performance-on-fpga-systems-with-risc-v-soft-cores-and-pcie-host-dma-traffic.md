Toki: Profiling HBM Performance on FPGA Systems with RISC-V Soft Cores and PCIe Host DMA Traffic
Authors：
[Andrea Galimberti](https://63dac.conference-program.com/?post_type=page&p=15&uid=3124202399727907231)，[Andrea Motta](https://63dac.conference-program.com/?post_type=page&p=15&uid=185630317282772734)，[Gianni Antichi](https://63dac.conference-program.com/?post_type=page&p=15&uid=4864792488974065777)，[Davide Zoni](https://63dac.conference-program.com/?post_type=page&p=15&uid=69373877675392773111)

## 中文标题

Toki：在配备 RISC-V 软核与 PCIe 主机 DMA 流量的 FPGA 系统上剖析 HBM 性能

## 英文摘要

Programmable RISC-V soft cores are becoming more widespread in data-center scenarios, making it crucial to design efficient systems that deploy them on FPGA chips with HBM memory. Toki, released as open source, is the first hardware-software framework that enables profiling the performance of HBM on FPGA accelerator cards by jointly considering (i) the execution of workloads on RISC-V soft cores instantiated on the FPGA and (ii) the injection of memory traffic from the host system via DMA over PCIe, providing insights that cannot be obtained with synthetic traffic generators alone. Extensive experiments target an AMD Alveo U55C card, deploying up to 60 RISC-V compute cores and stressing its HBM2 memory through real-world applications and microbenchmarks with user-defined access patterns. Results showcase how Toki can effectively profile the impact on HBM performance of the compute cores’ organization, the workload’s memory access patterns, data locality, contention over the memory controllers, and host traffic.

## 中文摘要

可编程 RISC-V 软核在数据中心场景中日益普及，因此设计将其部署在带有 HBM 的 FPGA 芯片上的高效系统至关重要。Toki 以开源形式发布，是首个硬件—软件框架，能够同时考虑 (i) 工作负载在 FPGA 上实例化的 RISC-V 软核上的执行，以及 (ii) 主机系统通过 PCIe 上的 DMA 注入的访存流量，从而对 FPGA 加速卡上 HBM 的性能进行剖析，提供仅靠合成流量生成器无法获得的洞见。大量实验以 AMD Alveo U55C 卡为目标，部署了多达 60 个 RISC-V 计算核，并通过真实应用和具有用户自定义访问模式的微基准对其 HBM2 内存施加压力。结果展示了 Toki 如何有效地剖析计算核的组织方式、工作负载的访存模式、数据局部性、存储控制器上的竞争以及主机流量对 HBM 性能的影响。

## 英文关键词

FPGA, HBM, RISC-V, Performance profiling, Memory systems, Soft cores, PCI Express, Direct memory access

## 中文关键词

FPGA、HBM、RISC-V、性能剖析、存储系统、软核、PCI Express、直接内存访问
