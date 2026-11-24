# IBTpoline: Flexible, Robust, and Intel IBT-compliant System Call Hooking

**中文标题**：IBTpoline：灵活、健壮且符合 Intel IBT 的系统调用挂钩

**所属 Session**：[Session 24: Kernel Interfaces and Service Reliability](index.md) · [ATC 2026](../index.md)

**作者**：Alexander J. Gaidis (Brown University), Ioulios Patmanidis (TU Delft), Isabelle Shapiro (Brown University), Georgios Portokalidis (IMDEA Software Institute), Alexios Voulimeneas (TU Delft), Vasileios P. Kemerlis (Brown University)

## 英文摘要
System call interposition underpins essential systems tooling, from tracers and sandboxes to compatibility layers. While binary rewriting-based approaches offer state-of-the-art performance by transforming syscall instructions into indirect branches that target a zero-page trampoline, this design is fundamentally incompatible with modern, hardware-assisted protection. Specifically, Intel IBT—an increasingly deployed hardware-based forward-edge CFI mechanism—requires all indirect branches to target valid endbr64 landing pads, causing existing zero-page trampolines to fault. Consequently, the fastest interposition mechanisms are currently broken on modern, IBT-enabled platforms. We present IBTpoline: a lightweight, high-performance syscall interposition framework that is IBT-compliant by construction. Rather than relying on a zero-page mapping, IBTpoline rewrites both the syscall and its preceding number-loading instruction, seamlessly redirecting execution to a localized, IBT-compliant trampoline stub. This eliminates the security risks of mapping page zero while flexibly supporting pre-syscall, post-syscall, and replacement hooks. Furthermore, IBTpoline introduces a hardware-backed lockdown mode, uniquely combining seccomp-bpf with Intel CET shadow stacks to guarantee that installed hooks cannot be bypassed, even by an attacker with arbitrary read/write capabilities. Evaluated on IBT-enabled hardware, IBTpoline incurs just 1.49% overhead on a worst-case microbenchmark (compared to 10.69% for state-of-the-art approaches) and sub-1.5% overhead across SQLite, Redis, and Nginx.

## 中文摘要
系统调用拦截是众多关键系统工具的基础，从跟踪器和沙箱到兼容层皆依赖于它。基于二进制重写的方法通过把系统调用指令转换为跳转到零页蹦床（zero-page trampoline）的间接分支，提供了当前最优的性能，但这一设计与现代硬件辅助保护机制从根本上不兼容。具体而言，Intel IBT——一种部署日益广泛的基于硬件的前向边 CFI 机制——要求所有间接分支都跳转到有效的 endbr64 着陆垫，从而使现有的零页蹦床触发故障。因此，当前最快的拦截机制在启用 IBT 的现代平台上已经失效。我们提出 IBTpoline：一个轻量级、高性能且在构造上即符合 IBT 的系统调用拦截框架。IBTpoline 不依赖零页映射，而是重写系统调用及其前面的编号加载指令，将执行无缝重定向到一个本地的、符合 IBT 的蹦床桩（trampoline stub）。这消除了映射零页的安全风险，同时灵活支持系统调用前、系统调用后以及替换式挂钩。此外，IBTpoline 引入了硬件支撑的锁定模式，独特地把 seccomp-bpf 与 Intel CET 影子栈结合起来，以保证已安装的挂钩无法被绕过，即使攻击者具备任意读/写能力。在启用 IBT 的硬件上评估，IBTpoline 在最坏情况微基准测试中仅带来 1.49% 的开销（现有最优方法为 10.69%），并在 SQLite、Redis 和 Nginx 上开销低于 1.5%。

## 英文关键词
system call interposition, Intel CET/IBT

## 中文关键词
系统调用拦截，Intel CET/IBT

[返回 Session 24](index.md) · [返回 ATC 2026](../index.md)
