---
title: "Protean: A Programmable Spectre Defense"
description: "HPCA 2026 · Hardware Security and Side-Channel Defenses"
tags:
  - "HPCA2026"
  - "Hardware Security and Side-Channel Defenses"
---

# Protean: A Programmable Spectre Defense

<div class="paper-seo-summary">
<p class="paper-seo-summary__desc">该论文收录于 HPCA 2026，所属 Track: Hardware Security and Side-Channel Defenses。</p>
<p class="paper-seo-summary__tags">HPCA 2026 · Hardware Security and Side-Channel Defenses</p>
</div>

**论文链接**：
**作者**：Nicholas Mosier Stanford University , Hamed Nemati KTH Royal Institute of Technology , John C. Mitchell Stanford University , Caroline Trippel Stanford University
**会议**：HPCA 2026

---

## 中文标题

Protean：一种可编程的 Spectre 防御方案

## 英文摘要

We present the PROTEAN Spectre defense—the first to be altogether comprehensive, covering all side-channels and speculation; programmer-transparent, requiring no source modifications; and programmable, tailoring its hardware protections to software’s security needs. Several Spectre defenses offer the first two features, but protect a hardware-defined subset of architectural state from transiently leaking. Meanwhile, many Spectre-vulnerable programs process secrets in ways that such rigid protections cannot both performantly and fully secure. PROTEAN overcomes this limitation through: (1) ProtISA, an ISA extension that allows software to tell hardware which architectural registers and memory bytes require protection from transiently leaking at each program point; (2) ProtCC, a compiler that automatically infers and programs ProtISA protections for vulnerable code with minimal user input; and (3) ProtDelay and ProtTrack, two alternative hardware mechanisms that performantly enforce software-defined ProtISA protections. By flexibly tailoring a hardware Spectre defense to a program’s data protection needs, PROTEAN significantly reduces the overhead of fully securing vulnerable programs. With ProtDelay/ProtTrack, it averages 0.27x/0.18x and 0.42x/0.34x of the runtime overhead of the best secure baseline for programs with and without mixed security needs, respectively, at lower/comparable hardware complexity.

## 中文摘要

我们提出 PROTEAN Spectre 防御，它首个同时做到全面覆盖所有侧信道与推测执行、对程序员透明（无需修改源码）以及可编程（按软件的安全需求定制硬件保护）。已有若干 Spectre 防御具备前两个特性，但只保护由硬件定义的架构状态子集不被瞬态泄漏。与此同时，许多易受 Spectre 攻击的程序处理机密数据的方式，使这种刚性保护无法兼顾性能与完全安全。PROTEAN 通过三点克服该局限：(1) ProtISA，一种 ISA 扩展，允许软件在每个程序点告知硬件哪些架构寄存器与内存字节需要防止瞬态泄漏；(2) ProtCC，一个编译器，在极少用户输入下自动推断并为易受攻击的代码生成 ProtISA 保护；(3) ProtDelay 与 ProtTrack，两种可高效执行软件定义保护的替代硬件机制。通过将硬件 Spectre 防御灵活地定制到程序的数据保护需求，PROTEAN 显著降低了完全保护易受攻击程序的运行时开销。在 ProtDelay/ProtTrack 下，对于有混合安全需求与无混合安全需求的程序，其运行时开销分别为最佳安全基线的 0.27 倍/0.18 倍和 0.42 倍/0.34 倍，且硬件复杂度更低或相当。
