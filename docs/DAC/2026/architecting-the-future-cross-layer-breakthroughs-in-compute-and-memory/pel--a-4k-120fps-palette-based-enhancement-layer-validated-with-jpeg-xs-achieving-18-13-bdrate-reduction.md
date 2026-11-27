PEL: A 4K@120FPS Palette-Based Enhancement Layer Validated with JPEG XS Achieving 18.13% Bdrate Reduction
Authors：
[Hanyang Cui](https://63dac.conference-program.com/?post_type=page&p=15&uid=7755541309366282572)，[Shijie Yao](https://63dac.conference-program.com/?post_type=page&p=15&uid=1829175462416586425)，[Wei Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=3550506514020924943)，[Hetao Xu](https://63dac.conference-program.com/?post_type=page&p=15&uid=22080437041230037831)，[Chenlong He](https://63dac.conference-program.com/?post_type=page&p=15&uid=7473775147822315551)，[Minge Jing](https://63dac.conference-program.com/?post_type=page&p=15&uid=979343)，[Leilei Huang](https://63dac.conference-program.com/?post_type=page&p=15&uid=34552893976010127661)，[Yibo Fan](https://63dac.conference-program.com/?post_type=page&p=15&uid=62227086299482408061)

## 中文标题

PEL：一种基于调色板的 4K@120FPS 增强层，经 JPEG XS 验证实现 18.13% 的 BD-rate 降低

## 英文摘要

The growing demand for low-latency, high-quality video encoding in wireless applications, such as online conferencing and cloud gaming, necessitates robust screen content capabilities in mezzanine codec. However, some mezzanine codec like JPEG XS exhibit inefficiencies when handling screen content, particularly for text-rich scenes containing abundant high-frequency information. Thus we propose PEL, a low-complexity screen content enhancement layer that operates without modifying the core codec. The proposed enhancement layer is based on clustering and a palette algorithm, achieving a 18.13% BD-rate reduction on screen content datasets with 5H2V transform levels when validated with JPEG XS. The proposed method eliminates data dependencies and complex rate–distortion optimization processes, satisfying requirements for low complexity and low latency. To overcome hardware throughput bottlenecks, a scalable tri-core parallel architecture is developed for the palette algorithm. Implemented on the Xilinx ZCU106 evaluation board, the design achieves 4K@120FPS performance with only 19.7K LUTs and an additional latency of eight lines.

## 中文摘要

在线会议与云游戏等无线应用对低延迟、高质量视频编码的需求不断增长，这要求中间层（mezzanine）编解码器具备强大的屏幕内容处理能力。然而，JPEG XS 等部分中间层编解码器在处理屏幕内容时效率不高，尤其是对包含大量高频信息的文本密集场景。为此，我们提出 PEL，一种低复杂度的屏幕内容增强层，且无需修改核心编解码器。该增强层基于聚类与调色板算法，在与 JPEG XS 配合验证时，于屏幕内容数据集上、采用 5H2V 变换层级取得了 18.13% 的 BD-rate 降低。所提方法消除了数据依赖和复杂的率-失真优化过程，满足低复杂度与低延迟的要求。为突破硬件吞吐瓶颈，我们为调色板算法设计了一种可扩展的三核并行架构。该设计在 Xilinx ZCU106 评估板上实现，仅使用 19.7K LUT、额外延迟为八行，即可达到 4K@120FPS 的性能。

## 英文关键词

JPEG XS, PLT, SCC, FPGA

## 中文关键词

JPEG XS、PLT、SCC、FPGA
