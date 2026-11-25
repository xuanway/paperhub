ARC-SRAM: A Memory Subarray with Local Addressing and Reduced Access Energy
Authors：
[Ismail Bourhaeil](https://63dac.conference-program.com/?post_type=page&p=15&uid=31640633534715634671)，[Geerten Verweij](https://63dac.conference-program.com/?post_type=page&p=15&uid=63714004393521983631)，[Mahmood Naderan-Tahan](https://63dac.conference-program.com/?post_type=page&p=15&uid=6235183571049925985)，[Dawit Abdi](https://63dac.conference-program.com/?post_type=page&p=15&uid=1757139280809878501)，[Prashant Dubey](https://63dac.conference-program.com/?post_type=page&p=15&uid=3124630074581118511)，[Dwaipayan Biswas](https://63dac.conference-program.com/?post_type=page&p=15&uid=9647550395981553073)，[Georgi Gaydadjiev](https://63dac.conference-program.com/?post_type=page&p=15&uid=13542634686066396511)，[Francky Catthoor](https://63dac.conference-program.com/?post_type=page&p=15&uid=08933251173624129561)，[Said Hamdioui](https://63dac.conference-program.com/?post_type=page&p=15&uid=825143)

## 中文标题

ARC-SRAM：一种具有局部寻址与低访问能耗的存储器子阵列

## 英文摘要

Conventional SRAMs are designed for random access, resulting in significant energy waste under regular access patterns common in image processing, computer vision, deep learning, and dense linear algebra to name a few. We propose an energy-efficient ARC-SRAM subarray architecture that integrates three synergetic energy reduction schemes: (1) Address decoding energy reduction by relocating the address generation to the memory periphery; (2) Read energy reduction by reducing wordline activity to one pulse per row and minimizing precharge activity to suppress half-selection energy; (3) Write energy reduction by reusing the bitline charge across consecutive rows, and by minimizing wordline activation. We implement a 64KB instance of our ARC-SRAM using imec’s advanced gate all around nanosheet 1.4nm (A14) process design kit. At the cell-array level, the design achieves a 63–76% energy reduction for reads and 68–72% for writes in loop-nest dominated applications, with only 4% area overhead.

## 中文摘要

传统 SRAM 面向随机访问而设计，在图像处理、计算机视觉、深度学习与稠密线性代数等常见的规律性访问模式下会造成显著的能耗浪费。我们提出一种高能效的 ARC-SRAM 子阵列架构，融合三种协同的降耗方案：（1）通过将地址生成迁移至存储外围电路来降低地址译码能耗；（2）通过将字线活动减少为每行一个脉冲，并将预充活动降至最低以抑制半选能耗，从而降低读取能耗；（3）通过跨连续行复用位线电荷并最小化字线激活来降低写入能耗。我们采用 imec 先进环栅纳米片 1.4nm（A14）工艺设计套件实现了 64KB 的 ARC-SRAM 实例。在单元阵列层面，该设计在以循环嵌套为主的应用中实现读取能耗降低 63–76%、写入能耗降低 68–72%，而面积开销仅为 4%。
