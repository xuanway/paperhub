EXRA: Efficient Execution of Data-Dominated Applications via ISA Extensions for Expandable Register Files
Authors：
[Heshan Dissanayake](https://63dac.conference-program.com/?post_type=page&p=15&uid=80293900172312253171)，[Darshana Jayasinghe](https://63dac.conference-program.com/?post_type=page&p=15&uid=7301517898559890424)，[Sri Parameswaran](https://63dac.conference-program.com/?post_type=page&p=15&uid=485743)

## 中文标题

EXRA：通过面向可扩展寄存器堆的 ISA 扩展高效执行数据密集型应用

## 英文摘要

Modern processor architectures employ a fixed, small register file, which is well-suited for most computations due to its simplicity, energy efficiency, and ease of implementation. However, data-intensive applications often suffer from limited register availability; simply enlarging the register file increases code size, pressures the instruction cache, complicates decoding, and raises power consumption. To address these challenges, we propose an extension to the legacy RISC-V Instruction Set Architecture (ISA) that supports an expandable register file. Our design partitions the register file into multiple logical banks, each mirroring the standard 32-register configuration, allowing operands and destination registers to reside in different banks concurrently. We introduce instruction extensions, overhead-reduction mechanisms, and exception-handling infrastructure to fully exploit the expanded register space on a scalar processor. The approach is implemented on the CVA6 CPU, a 6-stage RISC-V processor, and deployed on an FPGA with only 27% hardware overhead. Experimental results demonstrate substantial performance improvements: matrix multiplication achieves 60% speed-up with 17% energy reduction, convolutions improve by 48% with 22% energy reduction, and convolutional neural networks such as ResNet-50 achieve 83.5% speed-up with 45% energy reduction.

## 中文摘要

现代处理器架构采用固定的小容量寄存器堆，因其简单、高能效且易于实现，适用于大多数计算。然而，数据密集型应用常常受限于寄存器资源不足；单纯扩大寄存器堆会增加代码体积、对指令缓存造成压力、使译码复杂化并提高功耗。为应对这些挑战，我们提出对传统 RISC-V 指令集架构（ISA）的扩展，以支持可扩展的寄存器堆。我们的设计将寄存器堆划分为多个逻辑 bank，每个 bank 均镜像标准的 32 个寄存器配置，使操作数和目的寄存器可同时位于不同 bank 中。我们引入指令扩展、开销削减机制和异常处理基础设施，以在标量处理器上充分利用扩展后的寄存器空间。该方法在 6 级 RISC-V 处理器 CVA6 CPU 上实现，并仅以 27% 的硬件开销部署于 FPGA。实验结果表明性能显著提升：矩阵乘法加速 60% 且能耗降低 17%，卷积运算提升 48% 且能耗降低 22%，而 ResNet-50 等卷积神经网络则实现 83.5% 的加速与 45% 的能耗降低。
