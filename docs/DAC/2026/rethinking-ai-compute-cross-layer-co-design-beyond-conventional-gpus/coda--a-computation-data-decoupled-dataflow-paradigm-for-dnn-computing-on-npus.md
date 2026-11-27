CODA: A Computation-Data Decoupled Dataflow Paradigm for DNN Computing on NPUs
Authors：
[Xiuping Cui](https://63dac.conference-program.com/?post_type=page&p=15&uid=494343)，[Chengrui Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=09819359021208836511)，[Zihao Zheng](https://63dac.conference-program.com/?post_type=page&p=15&uid=5160323734301538912)，[Xiang Chen](https://63dac.conference-program.com/?post_type=page&p=15&uid=114843)，[Yun (Eric) Liang](https://63dac.conference-program.com/?post_type=page&p=15&uid=124143)

## 中文标题

CODA：一种面向 NPU 上 DNN 计算的计算-数据解耦数据流范式

## 英文摘要

Deep neural networks (DNNs) on Neural Processing Units (NPUs) require carefully optimized operator mappings to achieve high performance, yet the mapping space grows rapidly with increasingly complex on-chip memory hierarchies. Existing dataflow models rely on a computation–data coupled paradigm that forces all tensors to share identical storage structures and data transfer paths, severely limiting the expressible mapping space. We present CODA, a computation–data decoupled dataflow paradigm that enables tensor-wise independent modeling of on-chip storage and movement. CODA introduces the non-uniform loop space to jointly represent computation and per-tensor data mappings, together with an analytical performance model and a simulated-annealing–based optimizer. Across single-operator and fused-operator workloads, CODA achieves 1.10×–1.11× and 1.14×–1.85× speedup over state-of-the-art methods.

## 中文摘要

在神经处理单元（NPU）上，深度神经网络（DNN）需要经过精心优化的算子映射才能获得高性能，而随着片上存储层次结构日益复杂，映射空间迅速膨胀。现有数据流模型依赖计算与数据相耦合的范式，迫使所有张量共享相同的存储结构和数据传输路径，严重限制了可表达的映射空间。本文提出 CODA，一种计算与数据解耦的数据流范式，支持对片上存储与数据搬移进行逐张量的独立建模。CODA 引入非均匀循环空间来统一表示计算映射与各张量的数据映射，并配以解析性能模型和基于模拟退火的优化器。在单算子与融合算子负载上，CODA 相较当前最优方法分别取得 1.10×–1.11×和 1.14×–1.85×的加速。
