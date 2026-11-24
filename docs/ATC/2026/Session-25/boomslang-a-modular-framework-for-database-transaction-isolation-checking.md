# Boomslang: A Modular Framework for Database Transaction Isolation Checking

**中文标题**：Boomslang：一个用于数据库事务隔离性检查的模块化框架

**所属 Session**：[Session 25: Formal Methods and Verification](index.md) · [ATC 2026](../index.md)

**作者**：Jian Zhang (Northeastern University), Shuai Mu (Stony Brook University), Cheng Tan (Northeastern University)

## 英文摘要
Checking whether database transactions adhere to isolation levels is a crucial yet challenging problem. Existing checkers are typically designed for a specific combination of isolation level, operation types, and workload assumptions. As a result, supporting a new application scenario often requires building a new checker from scratch. We present Boomslang, an extensible framework for checking the isolation of transactional database executions using only client-side traces, without requiring knowledge of database internals. Boomslang adopts a front-/back-end separation. As the front-end, it parses a database trace into an Abstract Semantic Graph, which is then lowered into a low-level intermediate representation (IR). The back-end converts this IR to a set of constraints for satisfiability modulo theories (SMT) solving. This design is enabled by a key abstraction in the IR, called superpositions, which represent heterogeneous forms of uncertainty—including unknown version orders, ambiguous read-from relationships, and physical deletions—as a single first-class IR object. Isolation levels, operation semantics, and database-specific behaviors are implemented as modules that generate this IR over a shared back-end. Our experiments show that with only a few hundred lines of code, the core logic of three prior checkers can be reimplemented as Boomslang modules. Using Boomslang, we also support eight isolation levels, from read committed to strict serializability, identify a new bug in TiDB, audit the metadata layer of the JuiceFS file system, check vendor-specific behavior in MariaDB, and confirm a theoretical result on the correctness of strict serializability.

## 中文摘要
检查数据库事务是否遵守隔离级别是一个至关重要却又极具挑战性的问题。现有检查器通常针对隔离级别、操作类型和工作负载假设的某一特定组合而设计。因此，支持新的应用场景往往需要从头构建一个新的检查器。我们提出 Boomslang，一个可扩展的框架，仅使用客户端轨迹来检查事务型数据库执行的隔离性，无需了解数据库内部实现。Boomslang 采用前端/后端分离的设计。作为前端，它把数据库轨迹解析为抽象语义图，随后将其降低为低层中间表示（IR）。后端把该 IR 转换为一组用于可满足性模理论（SMT）求解的约束。这一设计得益于 IR 中的一个关键抽象，称为叠加态（superpositions），它把异构形式的不确定性——包括未知的版本顺序、模糊的读取来源关系以及物理删除——表示为单一的一等 IR 对象。隔离级别、操作语义和数据库特定行为都被实现为模块，在共享的后端之上生成该 IR。我们的实验表明，仅用数百行代码即可把先前三个检查器的核心逻辑重新实现为 Boomslang 模块。使用 Boomslang，我们还支持从读已提交到严格可串行化的八种隔离级别，在 TiDB 中发现了一个新缺陷，审计了 JuiceFS 文件系统的元数据层，检查了 MariaDB 中的厂商特定行为，并证实了一个关于严格可串行化正确性的理论结果。

## 英文关键词
Transaction isolation, Database checking

## 中文关键词
事务隔离，数据库检查

[返回 Session 25](index.md) · [返回 ATC 2026](../index.md)
