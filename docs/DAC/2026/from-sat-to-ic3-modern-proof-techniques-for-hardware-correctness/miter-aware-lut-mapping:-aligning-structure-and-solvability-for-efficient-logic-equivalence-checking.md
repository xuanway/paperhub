Miter-Aware LUT Mapping: Aligning Structure and Solvability for Efficient Logic Equivalence Checking
Authors：
[Jiaying Zhu](https://63dac.conference-program.com/?post_type=page&p=15&uid=148477401016677462)，[Zhengyuan Shi](https://63dac.conference-program.com/?post_type=page&p=15&uid=383743)，[Mengxia Tao](https://63dac.conference-program.com/?post_type=page&p=15&uid=85380526002902085621)，[Kezhi Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=18853028312320476761)，[Min Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=18105896767626631281)，[Qiang Xu](https://63dac.conference-program.com/?post_type=page&p=15&uid=024143)

## 中文标题

感知 Miter 的 LUT 映射：对齐结构与可求解性以实现高效逻辑等价性检查

## 英文摘要

Logic Equivalence Checking (LEC), a fundamental hardware verification task, is often bottlenecked by synthesis-induced structural perturbations and XOR-dense regions that degrade SAT solver performance. We contend that the modeling of the miter is as critical as the SAT solver itself. To this end, we introduce a miter-aware mapping framework that strategically formulates the problem before solving. By constructing a LUT-based miter—instead of a traditional, flat netlist—our approach preserves critical structural correspondence between the two designs while making high-level logic relations explicit. Our framework uniquely integrates three techniques: equivalence-preserving mapping to structurally align the two circuits, Gaussian-guided XOR modeling to algebraically simplify dense arithmetic, and solver-oriented LUT selection to generate a representation optimized for efficient SAT reasoning. Evaluated on comprehensive datasets, our method achieves up to a 92.1% reduction across state-of-the-art SAT solvers. This demonstrates that a solver-aware modeling paradigm, which unifies structural mapping with SAT reasoning, can fundamentally enhance LEC efficiency.

## 中文摘要

逻辑等价性检查（LEC）是一项基础的硬件验证任务，但常常受制于综合引入的结构扰动以及 XOR 密集区域，二者都会削弱 SAT 求解器的性能。我们认为，miter 的建模与 SAT 求解器本身同等关键。为此，我们提出一个感知 miter 的映射框架，在求解之前对问题进行策略性建模。通过构建基于 LUT 的 miter（而非传统的扁平网表），我们的方法在两个设计之间保留了关键的结构对应关系，同时使高层逻辑关系显式化。该框架独特地集成了三项技术：保持等价性的映射，用于在结构上对齐两个电路；高斯引导的 XOR 建模，用于对密集算术进行代数化简；面向求解器的 LUT 选择，用于生成面向高效 SAT 推理的优化表示。在综合性数据集上的评测表明，我们的方法相对最先进的 SAT 求解器最高实现 92.1% 的缩减。这说明，将结构映射与 SAT 推理相统一的求解器感知建模范式能够从根本上提升 LEC 的效率。
