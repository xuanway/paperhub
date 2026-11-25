Scalable Reliability Assessment of DNNs Through Simultaneous Fault Injection
Authors：
[Rafael Billig Tonetto](https://63dac.conference-program.com/?post_type=page&p=15&uid=72762482345633991521)，[Marcello Traiola](https://63dac.conference-program.com/?post_type=page&p=15&uid=0684442223299161376)，[Fernando Fernandes dos Santos](https://63dac.conference-program.com/?post_type=page&p=15&uid=0607566198598525177)，[Angeliki Kritikakou](https://63dac.conference-program.com/?post_type=page&p=15&uid=4089149177379253384)

## 中文标题

通过同时故障注入实现 DNN 的可扩展可靠性评估

## 英文摘要

Deep Neural Networks (DNNs) are increasingly deployed in safety-critical applications, where resilience to transient faults is essential. Traditional fault injection methods struggle to scale to large models, while most acceleration techniques depend on specific hardware or architectures. Simultaneous fault injection—injecting multiple faults in a single run—has shown promise, but its applicability to DNNs remains unexplored. In this work, we show that simultaneous faults in DNNs can interact due to their dense connectivity, creating artificial masking effects that lead to false negatives and compromise reliability assessment. To address this, we propose a method to mitigate fault interactions during simultaneous injection, ensuring accurate results. We further accelerate the process by pruning non-critical inputs from the batch, achieving additional speedup. To our knowledge, this is the first approach enabling accurate and efficient simultaneous fault injection in DNNs across abstraction levels. We evaluate nearly 42 million injections at both software (SW) and RTL, achieving very low false negatives (down to 0%, avg. 0.2%) and speedups of 3.82× (RTL) and 5.29× (SW).

## 中文摘要

深度神经网络（DNN）越来越多地部署于安全关键应用中，其抵御瞬态故障的能力至关重要。传统故障注入方法难以扩展到大型模型，而多数加速技术依赖特定的硬件或架构。同时故障注入——在单次运行中注入多个故障——已展现出潜力，但其对 DNN 的适用性尚未被探索。在本工作中，我们表明 DNN 中的同时故障会因其稠密连接而相互作用，产生人为的掩蔽效应，从而导致假阴性并损害可靠性评估。为此，我们提出一种在同时注入过程中缓解故障相互作用的方法，确保结果准确。我们进一步通过从批中剪除非关键输入来加速该过程，获得额外加速。据我们所知，这是首个能够在多个抽象层次上对 DNN 实现准确且高效同时故障注入的方法。我们在软件（SW）与 RTL 两个层面评估了近 4200 万次注入，实现极低的假阴性（最低至 0%，平均 0.2%）以及 3.82×（RTL）和 5.29×（SW）的加速。
