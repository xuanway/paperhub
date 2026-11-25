Stateful Embedded Fuzzing Using Peripheral-Accurate Systemc Virtual Prototypes
Authors：
[Chiara Ghinami](https://63dac.conference-program.com/?post_type=page&p=15&uid=61928645409917609931)，[Igor Tresolavy](https://63dac.conference-program.com/?post_type=page&p=15&uid=13016820648082557671)，[Luis Seibt](https://63dac.conference-program.com/?post_type=page&p=15&uid=92203427945367480561)，[Nils Bosbach](https://63dac.conference-program.com/?post_type=page&p=15&uid=33527748648327903901)，[Rainer Leupers](https://63dac.conference-program.com/?post_type=page&p=15&uid=94910766145728885281)

## 中文标题

基于外设精确 SystemC 虚拟原型的有状态嵌入式模糊测试

## 英文摘要

The increasing complexity of embedded software has made comprehensive manual testing impractical, motivating the use of automated techniques such as fuzzing. Coverage-guided fuzzers like AFL++ have shown strong results for conventional software but remain challenging to apply effectively in embedded contexts, where peripheral behaviors play critical roles. Existing approaches either use fast user-mode simulators, sacrificing peripheral realism, or rely on full-system simulators with manual instrumentation, limiting applicability to large-scale software. In this work, we present a novel framework that integrates AFL++ with a stateful SystemC-TLM virtual prototype to enable realistic fuzzing of embedded software. Fuzzer-generated inputs are injected directly into peripheral models, allowing peripherals to trigger natural side effects such as interrupts and FIFO updates. By integrating fuzzing with full-system simulation, our framework advances the effectiveness of pre-silicon testing for embedded systems. Results on embedded workloads show that our approach eliminates false positives while maintaining comparable code coverage and execution performance as state-of-the-art tools.

## 中文摘要

嵌入式软件复杂度的持续上升使全面的人工测试变得不切实际，从而推动了模糊测试等自动化技术的应用。AFL++ 等覆盖率引导的模糊测试器在传统软件上表现优异，但在外设行为起关键作用的嵌入式场景中仍难以有效应用。现有方法要么使用快速用户态模拟器而牺牲外设的真实性，要么依赖需人工插桩的全系统模拟器，从而限制了对大规模软件的适用性。本工作提出一种新颖框架，将 AFL++ 与有状态的 SystemC-TLM 虚拟原型相集成，以实现嵌入式软件的真实模糊测试。模糊测试器生成的输入被直接注入外设模型，使外设能够触发中断和 FIFO 更新等自然副作用。通过将模糊测试与全系统仿真相结合，我们的框架提升了嵌入式系统硅前测试的有效性。在嵌入式工作负载上的结果表明，我们的方法在保持与现有最优工具相当的代码覆盖率与执行性能的同时，消除了误报。

## 英文关键词

Fuzzing, SystemC, TLM, Virtual Prototyping, AFL++

## 中文关键词

模糊测试、SystemC、TLM、虚拟原型、AFL++
