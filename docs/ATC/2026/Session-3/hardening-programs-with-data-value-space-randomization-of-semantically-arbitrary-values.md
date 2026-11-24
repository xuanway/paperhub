# Hardening Programs with Data Value Space Randomization of Semantically Arbitrary Values

**中文标题**：基于语义任意值的数据值空间随机化的程序加固

**所属 Session**：[Session 3: Software Reliability and Bugs](index.md) · [ATC 2026](../index.md)

**作者**：Jaeyoon Kim (Sungkyunkwan University), Hajeong Lim (Sungkyunkwan University), Kyuwon Cho (Sungkyunkwan University), Hojoon Lee (Sungkyunkwan University)

## 英文摘要
With control-flow integrity now widely deployed, attackers increasingly corrupt non-control data, such as authentication flags and privilege levels, to steer execution along legitimate but unintended paths. Existing defenses such as Data-Flow Integrity counter these attacks but remain too expensive to deploy in practice. We present DVSR, a randomization defense that turns Semantically Arbitrary Values (SAVs) — values whose encoding can be remapped without altering program semantics — into per-execution secrets. Analogous to how ASLR randomizes memory layout, DVSR randomizes the constant values that security-critical branches test, denying the attacker knowledge of what to write. Data Value Space Analysis, DVSR’s whole-program value-flow analysis, conservatively and efficiently identifies a program’s SAVs and the constraints their randomization must preserve. DVSR extends the compiler-loader infrastructure to relocate SAV constants just as it relocates addresses, so every launch runs with per-execution secrets. DVSR thus serves as a distinct practical layer of defense with negligible overhead, composing with defenses already in deployment.

## 中文摘要
随着控制流完整性已得到广泛部署，攻击者越来越多地篡改非控制数据（例如认证标志和权限级别），以将执行引导至合法但非预期的路径。数据流完整性（Data-Flow Integrity）等现有防御能够对抗这类攻击，但开销过高，难以在实践中部署。我们提出 DVSR，一种随机化防御，它把语义任意值（Semantically Arbitrary Values，SAV）——即其编码可以在不改变程序语义的前提下重新映射的值——转换为每次执行独有的秘密。类比 ASLR 随机化内存布局的方式，DVSR 随机化安全关键分支所检测的常量值，从而使攻击者无从得知应当写入什么。数据值空间分析（Data Value Space Analysis）是 DVSR 的全程序值流分析，它以保守而高效的方式识别程序中的 SAV 以及随机化这些值时必须保持的约束。DVSR 扩展了编译器-加载器基础设施，使其像重定位地址一样重定位 SAV 常量，因此每次启动都以每次执行独有的秘密运行。由此，DVSR 成为一层独立的实用防御，开销可忽略，并能与已部署的防御组合使用。

## 英文关键词
data-only attacks, non-control data attacks, program hardening, randomization

## 中文关键词
仅数据攻击，非控制数据攻击，程序加固，随机化

[返回 Session 3](index.md) · [返回 ATC 2026](../index.md)
