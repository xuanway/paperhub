A Differentiable Approach to Task Graph Partitioning: A Case Study in RTL Simulation
Authors：
[Aditya Das Sarma](https://63dac.conference-program.com/?post_type=page&p=15&uid=7726790463313317363)，[Wan Luan Lee](https://63dac.conference-program.com/?post_type=page&p=15&uid=31529313222750401561)，[Shui Jiang](https://63dac.conference-program.com/?post_type=page&p=15&uid=3606913904265855708)，[Boyang Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=4879327568261776543)，[Tsung-Wei Huang](https://63dac.conference-program.com/?post_type=page&p=15&uid=026843)

## 中文标题

任务图划分的可微方法：以 RTL 仿真为案例研究

## 英文摘要

Graph partitioning is essential for many EDA applications that leverage task graph parallelism for faster execution. For instance, RTL simulators partition an input RTL design into dependent tasks and schedule them across threads. However, existing partitioners are largely limited to general-purpose heuristics that overlook real threading costs, resulting in suboptimal performance. Consequently, we introduce DiffPart, a differentiable task graph partitioning framework that automatically learns high-quality partitions under real operating conditions. Applied to RTL simulation, DiffPart improves state-of-the-art Verilator’s partitioning quality, delivering up to 1.22–55.25× faster simulation runtime across diverse designs.

## 中文摘要

图划分对于许多利用任务图并行来加速执行的 EDA 应用至关重要。例如，RTL 仿真器将输入的 RTL 设计划分为相互依赖的任务，并在多个线程间调度它们。然而，现有划分器大多局限于通用的启发式方法，忽略了真实的线程开销，导致性能次优。因此，我们提出 DiffPart，一个可微的任务图划分框架，它能够在真实运行条件下自动学习高质量的划分。应用于 RTL 仿真时，DiffPart 提升了最先进的 Verilator 的划分质量，在多种设计上实现高达 1.22–55.25× 的仿真运行加速。
