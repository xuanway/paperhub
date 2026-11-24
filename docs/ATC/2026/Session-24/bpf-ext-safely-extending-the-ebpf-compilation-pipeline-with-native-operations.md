# BPF-Ext: Safely Extending the eBPF Compilation Pipeline with Native Operations

**中文标题**：BPF-Ext：以原生操作安全地扩展 eBPF 编译流水线

**所属 Session**：[Session 24: Kernel Interfaces and Service Reliability](index.md) · [ATC 2026](../index.md)

**作者**：Yusheng Zheng (UC Santa Cruz), Zhengjie Ji (Virginia Tech), Weichen Tao (Telecom Paris), Hao Sun (ETH Zurich), Wei Zhang (University of Connecticut), Dan Williams (Virginia Tech), Andi Quinn (University of California Santa Cruz)

## 英文摘要
eBPF safely extends OS kernels in production by verifying bytecode before execution, and many of its uses are performance critical. However, its design favors safety over speed: the instruction set is designed to be verifiable, and the kernel just-in-time compiler (JIT) stays simple to remain trustworthy, translating one opcode at a time. As a result, eBPF takes up to twice as long to run as native code, and the clearest losses come from hardware idioms, operations that CPUs execute as a single instruction but eBPF lacks. Current approaches like optimizing the bytecode cannot emit these instructions, and adding them to the eBPF instruction set requires changing the compiler, the verifier, and the JIT for each architecture. Optimizing in the JIT instead enlarges the trusted computing base (TCB). We present BPF-Ext, an extension interface that lets kernel modules introduce new operations, such as native instructions, without further kernel patches or verifier changes. Our key insight is that a new operation can be verified through an equivalent vanilla eBPF form, while the CPU runs its native code. The verifier checks the eBPF form but never sees the native code, so the code that generates it is the only code each operation adds to the TCB. We prove in Lean 4 that it matches its eBPF form. Using BPF-Ext, we build Kinsn, seven hardware-idiom operations such as rotate and conditional select. On x86-64 and ARM64, Kinsn speeds up microbenchmarks by 24% and 22% and production applications by up to 12%. The same interface also supports replacing whole programs with native code, speeding up Cilium by 19% at the cost of a larger TCB.

## 中文摘要
eBPF 通过在执行前验证字节码而在生产环境中安全地扩展操作系统内核，其许多用途都对性能至关重要。然而，它的设计偏向安全而非速度：指令集以可验证为目标设计，内核即时编译器（JIT）为保持可信而保持简单，一次只翻译一个操作码。因此，eBPF 的运行时间最高可达原生代码的两倍，而最明显的性能损失来自硬件惯用操作，即 CPU 能以单条指令执行、但 eBPF 并不具备的操作。当前诸如优化字节码的方法无法生成这些指令，而将它们加入 eBPF 指令集则需要针对每种架构同时修改编译器、验证器和 JIT。改为在 JIT 中优化则会扩大可信计算基（TCB）。我们提出 BPF-Ext，一种扩展接口，使内核模块能够引入新的操作（例如原生指令），而无需额外的内核补丁或验证器改动。我们的关键洞察是：新操作可以通过一个等价的普通 eBPF 形式来验证，而由 CPU 执行其原生代码。验证器只检查 eBPF 形式，从不接触原生代码，因此生成原生代码的那部分代码就是每个操作加入 TCB 的唯一代码。我们在 Lean 4 中证明了它与对应的 eBPF 形式等价。使用 BPF-Ext，我们构建了 Kinsn，包含 rotate、conditional select 等七种硬件惯用操作。在 x86-64 和 ARM64 上，Kinsn 使微基准测试分别加速 24% 和 22%，使生产应用最高加速 12%。同一接口还支持用原生代码替换整个程序，以更大的 TCB 为代价使 Cilium 加速 19%。

## 英文关键词
eBPF, JIT compilation, kernel extensions, instruction set extension, verified compilation, proof-carrying code

## 中文关键词
eBPF，JIT 编译，内核扩展，指令集扩展，经过验证的编译，携带证明的代码

[返回 Session 24](index.md) · [返回 ATC 2026](../index.md)
