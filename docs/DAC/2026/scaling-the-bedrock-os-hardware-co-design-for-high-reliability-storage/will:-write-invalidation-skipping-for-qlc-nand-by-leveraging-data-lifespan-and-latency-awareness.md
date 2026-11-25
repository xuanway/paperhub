WILL: Write Invalidation Skipping for QLC NAND by Leveraging Data Lifespan and Latency Awareness
Authors：
[Beichen Ning](https://63dac.conference-program.com/?post_type=page&p=15&uid=84370365443740428511)，[Yina Lv](https://63dac.conference-program.com/?post_type=page&p=15&uid=01023773994143462201)，[Tianyu Ren](https://63dac.conference-program.com/?post_type=page&p=15&uid=61625621441718601271)，[Bin Gao](https://63dac.conference-program.com/?post_type=page&p=15&uid=647475770233978714)，[Xiangyu Yao](https://63dac.conference-program.com/?post_type=page&p=15&uid=1023163900232962845)，[Jie Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=3031408747147996539)，[Qiao Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=6393363691648557937)，[Chun Jason Xue](https://63dac.conference-program.com/?post_type=page&p=15&uid=0429261838049077539)

## 中文标题

WILL：利用数据生命周期与延迟感知的 QLC NAND 写失效跳过

## 英文摘要

3D QLC NAND flash suffers from a slow two-step programming process. The problem is exacerbated by write invalidation on wordlines, which occurs when pages are updated between the two steps, wasting programming effort and degrading performance. While prior work offers partial mitigation, it fails to fundamentally address the root cause: the misalignment of page invalidation time within a wordline. In this paper, we propose WILL, a proactive page mapping scheme that enables write invalidation skipping for QLC NAND flash. The basic idea is to group pages with similar invalidation time into the same wordline and turn partially-invalid wordlines into fully-valid or fully invalid ones, thereby skipping the programming on fully-invalid wordlines. To achieve this, WILL first predicts page invalidation time and then organizes pages accordingly to maximize the opportunities of writing invalidation skipping. Finally, WILL schedules short-lifespan data to wordlines requiring high-latency fine-step programming to increase the probability of skipping high programming latencies for further programming performance enhancement. In addition, read parallelism is maintained by identifying and excluding read-hot data from this mapping. Experimental results show that WILL reduces programming execution time by 10.0% compared with the state-of-the-art, along with skipping an additional 5.03% of fully-invalid wordlines and lowering the partially-invalid ratio by 15.9% on average, at a minimal read performance cost of 2.59%.

## 中文摘要

3D QLC NAND 闪存受制于缓慢的两步编程过程。字线上的写失效会进一步加剧该问题：当页在两步之间被更新时，已投入的编程被浪费且性能下降。尽管已有工作提供了部分缓解，但未能从根本上解决根因，即字线内页失效时间的不一致。本文提出 WILL，一种主动式页映射方案，为 QLC NAND 闪存实现写失效跳过。其基本思想是将失效时间相近的页归入同一字线，把部分失效字线转化为全有效或全失效字线，从而跳过对全失效字线的编程。为此，WILL 首先预测页失效时间，然后据此组织页，以最大化写失效跳过的机会。最后，WILL 将短生命周期数据调度到需要高延迟细步编程的字线，以提高跳过高编程延迟的概率，进一步提升编程性能。此外，通过识别读热点数据并将其排除在该映射之外来保持读并行性。实验结果表明，与现有最优工作相比，WILL 将编程执行时间降低 10.0%，额外跳过 5.03% 的全失效字线，并将部分失效比例平均降低 15.9%，而读性能代价仅为 2.59%。

## 英文关键词

QLC NAND Flash Memory, Two-Step Programming, Invalid Programming, Latency

## 中文关键词

QLC NAND 闪存、两步编程、无效编程、延迟
