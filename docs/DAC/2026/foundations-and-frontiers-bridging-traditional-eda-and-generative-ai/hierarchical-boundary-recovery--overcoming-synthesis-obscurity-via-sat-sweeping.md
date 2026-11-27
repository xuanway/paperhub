Hierarchical Boundary Recovery: Overcoming Synthesis Obscurity via SAT Sweeping
Authors：
[Kuo-Wei Ho](https://63dac.conference-program.com/?post_type=page&p=15&uid=50123091500354126231)，[Jie-Hong Roland Jiang](https://63dac.conference-program.com/?post_type=page&p=15&uid=044143)，[Alan Mishchenko](https://63dac.conference-program.com/?post_type=page&p=15&uid=876243)，[Sean Weaver](https://63dac.conference-program.com/?post_type=page&p=15&uid=1386066542997075894)，[Yu-Wei Fan](https://63dac.conference-program.com/?post_type=page&p=15&uid=20900596902649071281)

## 中文标题

层次边界恢复：通过 SAT 扫描克服综合造成的模糊性

## 英文摘要

In the integrated circuit design flow, a high-level specification is synthesized into a gate-level netlist. However, this synthesis often results in the loss of the association between the high-level and gate-level designs. Maintaining signal correspondences between these two levels is crucial for preserving the design hierarchy, which in turn facilitates design debugging, engineering change orders (ECOs), cross-abstraction-level model training, and other synthesis and verification tasks. In this work, we present an automated approach for recovering the hierarchical boundaries of high-level components in gate-level netlists, even in cases where the synthesis process has completely removed the original boundary signals. The method is implemented as an open-source tool, and the experimental results demonstrate its robustness in recovering hierarchical boundaries. Our results may benefit various potential applications in synthesis and verification.

## 中文摘要

在集成电路设计流程中，高层规约被综合为门级网表。然而，这一综合过程常常导致高层设计与门级设计之间的关联丢失。保持两个层次之间的信号对应关系，对于维持设计层次结构至关重要，而这又有助于设计调试、工程变更单（ECO）、跨抽象层模型训练以及其他综合与验证任务。在本工作中，我们提出一种自动化方法，用于恢复门级网表中高层组件的层次边界，即使在综合过程已完全移除原始边界信号的情况下亦可适用。该方法已实现为开源工具，实验结果表明其在恢复层次边界方面具有稳健性。我们的结果可惠及综合与验证中的多种潜在应用。
