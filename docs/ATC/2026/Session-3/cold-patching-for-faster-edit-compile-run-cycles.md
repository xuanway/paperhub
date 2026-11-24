# Cold-Patching for Faster Edit-Compile-Run Cycles

**中文标题**：冷补丁：加速编辑-编译-运行循环

**所属 Session**：[Session 3: Software Reliability and Bugs](index.md) · [ATC 2026](../index.md)

**作者**：Matthew Sotoudeh (Stanford University)

## 英文摘要
Programmers rely on fast edit-compile-run cycles when debugging code, exploring unfamiliar codebases, and trying out new ideas. Fiddle is a new tool for cold-patching small changes onto large compiled software systems. When repeatedly editing a small number of compilation units, Fiddle is faster than linkers, uses less memory, and does not require saving intermediate compilation artifacts. Fiddle is simpler and more reliable than hot-patching because it does not need to deal with global state migration or non-quiescent functions. Fiddle is designed for developers repeatedly fiddling with a handful of functions in a large codebase; it cannot patch changes to the types of global non-static objects, it cannot patch binaries compiled with LTO, and its speed relies on repeatedly editing the same set of compilation units. We end by describing a suite of tools enabled by the Fiddle cold-patching primitive that make it easier to rapidly prototype modifications to compiled system software.

## 中文摘要
程序员在调试代码、探索陌生代码库以及尝试新想法时，都依赖快速的编辑-编译-运行循环。Fiddle 是一款新工具，可将小的改动以冷补丁（cold-patching）的方式打到大体积的已编译软件系统上。当反复修改少量编译单元时，Fiddle 比链接器更快、占用内存更少，并且无需保存中间编译产物。Fiddle 比热补丁（hot-patching）更简单、更可靠，因为它无需处理全局状态迁移或非静止（non-quiescent）函数。Fiddle 面向的是在大型代码库中反复摆弄少数几个函数的开发者；它无法为全局非静态对象类型的变化打补丁，无法为使用 LTO 编译的二进制文件打补丁，而且其速度依赖于反复修改同一组编译单元。最后，我们描述了一套由 Fiddle 冷补丁原语所支持的工具，这些工具使快速原型化对已编译系统软件的修改变得更加容易。

## 英文关键词
Cold Patching, Incremental Compilation, Edit-Compile-Run Cycle

## 中文关键词
冷补丁，增量编译，编辑-编译-运行循环

[返回 Session 3](index.md) · [返回 ATC 2026](../index.md)
