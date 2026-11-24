# DESAN: READ/WRITE-Aware Redundant Sanitizer Check Elimination

**中文标题**：DeSan：读写感知的冗余 Sanitizer 检查消除

**所属 Session**：[Session 18: Programming Languages and Compilers](index.md) · [ATC 2026](../index.md)

**作者**：Yunlong Xing (Michigan Technological University; George Mason University), Shiyu Sun (George Mason University), Kun Sun (George Mason University)

## 英文摘要
Sanitizers such as ASan, UBSan, and MSan are widely used to detect memory-related errors and undefined behavior. However, their high runtime overhead makes continuous use difficult in testing and production-like executions. A major source of this overhead is redundant sanitizer instrumentation: compiler-inserted checks often validate the same variable repeatedly along the same control-flow paths. Reducing sanitizer checks requires reasoning about the property each check validates and the program state on which it depends. We explore a conservative policy that eliminates only covered READ checks and retains WRITE checks and those whose semantics remain unresolved. This paper presents DeSan, an LLVM IR-level framework that reduces redundant sanitizer checks while preserving sanitizer semantics. DeSan identifies high-impact core checks and recovers the checked variable for each check through backward IR tracing. It then classifies checks as READ, WRITE, or UNKNOWN and builds per-variable check graphs to find covered READ checks. DeSan preserves all WRITE and UNKNOWN checks. When safe, it removes redundant READ checks along with their sanitizer-only IR slices, including shadow computation, comparisons, branches, and isolated report paths. We evaluate DeSan on SPEC CPU2006, SPEC CPU2017, and 20 open-source projects. Across 163 valid sanitizer configurations, core checks cover a median of 96.62% of inserted checks, and DeSan removes a median of 51.48% of all checks while preserving evaluated bug-detection capability. Compared with ASAN−−for ASan and SanRazor for UBSan, DeSan achieves competitive or stronger overhead reduction.

## 中文摘要
ASan、UBSan 和 MSan 等 sanitizer 被广泛用于检测内存相关错误和未定义行为。然而，它们高昂的运行时开销使得在测试和类生产执行中持续使用变得困难。这种开销的一个主要来源是冗余的 sanitizer 插桩：编译器插入的检查常常在同一条控制流路径上反复校验同一个变量。减少 sanitizer 检查需要推理每个检查所校验的性质以及它所依赖的程序状态。我们探索了一种保守策略，即只消除已被覆盖的 READ 检查，而保留 WRITE 检查以及语义尚未确定的检查。本文提出 DeSan，一个在 LLVM IR 层面减少冗余 sanitizer 检查、同时保持 sanitizer 语义的框架。DeSan 识别高影响的核心检查，并通过反向 IR 追踪恢复每个检查所校验的变量。随后它将检查分类为 READ、WRITE 或 UNKNOWN，并构建按变量划分的检查图以找出被覆盖的 READ 检查。DeSan 保留所有 WRITE 和 UNKNOWN 检查。在安全的情况下，它移除冗余的 READ 检查及其仅供 sanitizer 使用的 IR 切片，包括影子计算、比较、分支和孤立的报告路径。我们在 SPEC CPU2006、SPEC CPU2017 和 20 个开源项目上评估 DeSan。在 163 个有效的 sanitizer 配置中，核心检查中位数覆盖了 96.62% 的插入检查，并且 DeSan 在保持所评估的错误检测能力的同时，中位数消除了全部检查的 51.48%。与面向 ASan 的 ASAN−− 和面向 UBSan 的 SanRazor 相比，DeSan 实现了相当或更强的开销降低。

## 英文关键词
READ/WRITE Semantics, Sanitizer Checks, Redundancy Elimination.

## 中文关键词
读写语义，Sanitizer 检查，冗余消除

[返回 Session 18](index.md) · [返回 ATC 2026](../index.md)
