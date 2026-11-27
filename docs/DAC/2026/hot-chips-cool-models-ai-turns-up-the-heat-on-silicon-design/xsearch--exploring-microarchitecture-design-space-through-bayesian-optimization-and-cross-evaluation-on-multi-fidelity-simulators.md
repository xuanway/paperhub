Xsearch: Exploring Microarchitecture Design Space Through Bayesian Optimization and Cross Evaluation on Multi-Fidelity Simulators
Authors：
[Honghua Zhu](https://63dac.conference-program.com/?post_type=page&p=15&uid=35734733330447133931)，[Chunjie Luo](https://63dac.conference-program.com/?post_type=page&p=15&uid=273528229903980219)，[Xinke Zhao](https://63dac.conference-program.com/?post_type=page&p=15&uid=2251640570464063882)，[Jianfeng Zhan](https://63dac.conference-program.com/?post_type=page&p=15&uid=1764585439355782292)

## 中文标题

XSearch：基于贝叶斯优化与多保真度仿真器交叉评估的微架构设计空间探索

## 英文摘要

Design space exploration for microarchitecture parameters is a critical aspect of processor design, requiring a balance between evaluation cost and accuracy. New designs can be evaluated using either coarse-grained simulation (high efficiency, low accuracy) or fine-grained simulation (low efficiency, high accuracy). To address this efficiency-accuracy tradeoff, we propose XSearch, which employs multi-fidelity Bayesian optimization by cross-evaluating across simulators with varying fidelity levels. This approach leverages the efficiency of low-fidelity simulations to explore more design points while ensuring accuracy through calibration using high-fidelity simulation data. XSearch has been successfully applied to explore the design space of the large-scale open-source high-performance processor core XiangShan.

## 中文摘要

微架构参数的设计空间探索是处理器设计中的关键环节，需要在评估成本与精度之间取得平衡。新设计既可采用粗粒度仿真（效率高、精度低）评估，也可采用细粒度仿真（效率低、精度高）评估。为应对这一效率与精度之间的权衡，我们提出 XSearch，它通过在不同保真度层级的仿真器之间进行交叉评估来实施多保真度贝叶斯优化。该方法利用低保真度仿真的高效性探索更多设计点，同时通过高保真度仿真数据校准来保证精度。XSearch 已成功应用于大规模开源高性能处理器核“香山”（XiangShan）的设计空间探索。
