RISC-Q: A Generator for Real-Time Quantum Control System-on-Chips Compatible with RISC-V
Authors：
[Junyi Liu](https://63dac.conference-program.com/?post_type=page&p=15&uid=2748395297401317262)，[Yi Lee](https://63dac.conference-program.com/?post_type=page&p=15&uid=77395460508328629811)，[Haowei Deng](https://63dac.conference-program.com/?post_type=page&p=15&uid=90903437086397818081)，[Connor Clayton](https://63dac.conference-program.com/?post_type=page&p=15&uid=0048337804367920641)，[Gengzhi Yang](https://63dac.conference-program.com/?post_type=page&p=15&uid=5850903728429397674)，[Xiaodi Wu](https://63dac.conference-program.com/?post_type=page&p=15&uid=50654323429854228031)

## 中文标题

RISC-Q：兼容 RISC-V 的实时量子控制系统级芯片生成器

## 英文摘要

Quantum computing imposes stringent requirements for the precise control of large-scale qubit systems, including, for example, microsecond-latency feedback and nanosecond-precision timing of gigahertz signals—demands that far exceed the capabilities of conventional real-time systems. The rapidly evolving and highly diverse nature of quantum control necessitates the development of specialized hardware accelerators. While a few custom real-time systems have been developed to meet the tight timing constraints of specific quantum platforms, they face major challenges in scaling and adapting to increasingly complex control demands—largely due to fragmented toolchains and limited support for design automation. To address these limitations, we present RISC-Q—an open-source flexible generator for Quantum Control System-on-Chip (QCSoC) designs, featuring a programming interface compatible with the RISC-V ecosystem. Developed using SpinalHDL, RISC-Q enables efficient automation of highly parameterized and modular QCSoC architectures, supporting agile and iterative development to meet the evolving demands of quantum control. We demonstrate that RISC-Q can replicate the performance of existing QCSoCs with significantly reduced development effort, facilitating efficient exploration of the hardware–software co-design space for rapid prototyping and customization.

## 中文摘要

量子计算对大规模量子比特系统的精确控制提出了严苛要求，例如微秒级延迟反馈以及千兆赫兹信号的纳秒级精度时序——这些需求远超传统实时系统的能力。量子控制技术快速演进且高度多样，亟需开发专用硬件加速器。尽管已有若干定制实时系统能够满足特定量子平台的严格时序约束，但它们在扩展以及适配日益复杂的控制需求方面仍面临重大挑战，其主要原因在于工具链碎片化、对设计自动化的支持有限。为应对这些局限，我们提出 RISC-Q——一个面向量子控制系统级芯片（QCSoC）设计的开源灵活生成器，并提供与 RISC-V 生态兼容的编程接口。RISC-Q 基于 SpinalHDL 开发，能够高效自动生成高度参数化、模块化的 QCSoC 架构，支持敏捷迭代式开发，以满足量子控制不断演进的需求。我们证明 RISC-Q 能够以显著降低的开发工作量复现现有 QCSoC 的性能，从而有助于高效探索软硬件协同设计空间，实现快速原型验证与定制化。
