Dropping Multiple Literals per SAT Call in IC3 Model Checking
Authors：
[Tianjun Bu](https://63dac.conference-program.com/?post_type=page&p=15&uid=0987379137023648854)，[Zhichao Lyu](https://63dac.conference-program.com/?post_type=page&p=15&uid=97224586481353910651)，[Qiusong Yang](https://63dac.conference-program.com/?post_type=page&p=15&uid=37877104431850784231)

## 中文标题

IC3 模型检测中每次 SAT 调用丢弃多个文字

## 英文摘要

IC3 is the state-of-the-art model checking algorithm where generalizing cubes by dropping literals one-by-one is the most computationally expensive step. We propose multi-literal drop strategies that eliminate two or more literals simultaneously. Successful 𝑛-drop saves 𝑛−1 SAT invocations. To mitigate performance losses from failures, we introduce deduction mechanisms that analyze counterexamples to generalization and identify non-droppable literals early. With these, failed multi-drop attempts are sometimes as useful as conventional single-drops. Additionally we analyze the diminishing returns of higher-order drops. Our implementation on ABC solves 28 unique and 16 more cases than vanilla ABC and implementation on rIC3 runs 6.0% faster.

## 中文摘要

IC3 是最先进的模型检测算法，其中通过逐一丢弃文字来泛化立方体是计算代价最高的步骤。我们提出多文字丢弃策略，可同时消除两个或更多文字。成功的 n-drop 可节省 n−1 次 SAT 调用。为缓解失败所带来的性能损失，我们引入推导机制，通过分析泛化反例提前识别不可丢弃的文字。借助这些机制，失败的多文字丢弃尝试有时与传统的单文字丢弃同样有用。此外，我们分析了更高阶丢弃的收益递减现象。我们在 ABC 上的实现相比原始 ABC 多求解 28 个独有案例和 16 个案例，在 rIC3 上的实现运行速度快 6.0%。

## 英文关键词

Formal verification, IC3, Model checking

## 中文关键词

形式验证、IC3、模型检测
