# SubSan: Efficient Memory Error Detection via Subtraction Checks

**中文标题**：SubSan：通过减法检查实现的高效内存错误检测

**所属 Session**：[Session 3: Software Reliability and Bugs](index.md) · [ATC 2026](../index.md)

**作者**：Jeonghwan Kang (Pusan National University), Kyounghwan Kim (Pusan National University), Donghyun Kwon (Pusan National University)

## 英文摘要
Memory sanitizers are widely used to find memory errors in C/C++ programs, and their runtime efficiency determines how much testing fits within a fixed time budget. Hardware-assisted AddressSanitizer (HWASan) checks object identity by binding tagged pointers to objects and keeps pointer tagging practical with hardware features such as Arm Top-Byte Ignore (TBI) and Intel Linear Address Masking (LAM). However, HWASan nearly doubles native execution time. A major cause is the granule-level semantics of its metadata. Since each metadata entry stores only the memory tag for one granule, a tag check confirms only that a tagged pointer may access that granule, forcing per-granule checks for multi-granule accesses. In this paper, we present SubSan, a tag-based sanitizer that extends per-granule metadata with the upper bound of the object. The tag checks object identity, while the upper bound checks object extent and enables check reduction over multi-granule accesses. This extension makes each check more demanding because a straightforward check must evaluate two conditions and consume two metadata fields. SubSan keeps the checking logic lightweight with a subtraction check, which checks object identity and object extent with one unsigned subtraction followed by one zero test. We implement SubSan for Arm TBI and Intel LAM. On SPEC CPU2017, SubSan lowers the runtime overhead of HWASan by 30.4 and 130.9 percentage points on Arm and Intel, respectively, and improves fuzzing throughput over HWASan by 59.9% in AFL++.

## 中文摘要
内存 sanitizer 被广泛用于发现 C/C++ 程序中的内存错误，其运行时效率决定了在固定时间预算内可以完成多少测试。硬件辅助的 AddressSanitizer（HWASan）通过将带标签指针绑定到对象来检查对象身份，并借助 Arm Top-Byte Ignore（TBI）和 Intel Linear Address Masking（LAM）等硬件特性使指针打标签保持实用。然而，HWASan 几乎使原生执行时间翻倍。一个主要原因是其元数据的粒度级语义。由于每个元数据条目只存储一个粒度的内存标签，一次标签检查只能确认某个带标签指针可以访问该粒度，从而对跨多个粒度的访问不得不逐粒度检查。本文提出 SubSan，一种基于标签的 sanitizer，它在逐粒度元数据的基础上扩展了对象上界。标签负责检查对象身份，而上界负责检查对象范围，并使得跨多粒度访问的检查可以被削减。这一扩展使每次检查的要求更高，因为直白的检查必须评估两个条件并读取两个元数据字段。SubSan 通过减法检查使检查逻辑保持轻量：用一次无符号减法加一次零值测试同时检查对象身份与对象范围。我们为 Arm TBI 和 Intel LAM 实现了 SubSan。在 SPEC CPU2017 上，SubSan 在 Arm 和 Intel 上分别将 HWASan 的运行时开销降低 30.4 和 130.9 个百分点，并在 AFL++ 中将模糊测试吞吐较 HWASan 提升 59.9%。

## 英文关键词
Sanitizers, Memory Safety

## 中文关键词
Sanitizer，内存安全

[返回 Session 3](index.md) · [返回 ATC 2026](../index.md)
