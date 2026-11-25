Vten: Tensor-Centric Verification Framework for Domain-Specific Accelerators
Authors：
[Chanmin Baek](https://63dac.conference-program.com/?post_type=page&p=15&uid=06113581210676948011)，[Keehyuk Lee](https://63dac.conference-program.com/?post_type=page&p=15&uid=1369894230720428116)，[Mincheol Cha](https://63dac.conference-program.com/?post_type=page&p=15&uid=3596184369124065481)，[Somi Hong](https://63dac.conference-program.com/?post_type=page&p=15&uid=72623130431747435861)，[Xuan Truong Nguyen](https://63dac.conference-program.com/?post_type=page&p=15&uid=53254707789065279161)，[Hyuk-Jae Lee](https://63dac.conference-program.com/?post_type=page&p=15&uid=957143)

## 中文标题

vTen：面向领域专用加速器的以张量为中心的验证框架

## 英文摘要

The semantic gap between tensor-centric software models and signal-level hardware testbenches creates significant productivity bottlenecks in verifying Domain-Specific Accelerators (DSAs). Existing frameworks like Cocotb suffer from prohibitive synchronization overheads due to fine-grained interactions. To address this, we propose vTen, a data-centric framework that strictly decouples verification intent from execution mechanics. By leveraging a declarative DSL and kernel-granular batching, vTen minimizes host-simulator interaction frequency. Evaluation on a production-scale 3D U-Net accelerator demonstrates that vTen achieves a 2× performance improvement in simulation latency and a 60.3% reduction in code complexity compared to Cocotb.

## 中文摘要

以张量为中心的软件模型与信号级硬件测试平台之间的语义鸿沟，在验证领域专用加速器（DSA）时造成了严重的生产力瓶颈。Cocotb 等现有框架因细粒度交互而承受难以承受的同步开销。为此，我们提出 vTen，这是一个以数据为中心的框架，将验证意图与执行机制严格解耦。通过采用声明式 DSL 与内核粒度的批处理，vTen 将主机与仿真器之间的交互频率降至最低。在生产规模的 3D U-Net 加速器上的评测表明，与 Cocotb 相比，vTen 在仿真时延上取得 2 倍的性能提升，并将代码复杂度降低 60.3%。
