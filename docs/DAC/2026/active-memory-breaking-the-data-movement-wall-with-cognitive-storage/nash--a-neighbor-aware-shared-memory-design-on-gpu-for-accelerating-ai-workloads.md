Nash: A Neighbor-Aware Shared Memory Design on GPU for Accelerating AI Workloads
Authors：
[Hanqing Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=44466995197740926571)，[Tiejun Li](https://63dac.conference-program.com/?post_type=page&p=15&uid=9453770871458706098)，[Sheng ma](https://63dac.conference-program.com/?post_type=page&p=15&uid=601243)，[Jianmin Zhang](https://63dac.conference-program.com/?post_type=page&p=15&uid=61240000798276450401)，[Hanzhi Xun](https://63dac.conference-program.com/?post_type=page&p=15&uid=86083165974470359731)，[Lizhou Wu](https://63dac.conference-program.com/?post_type=page&p=15&uid=2098325991236217763)

## 中文标题

Nash：一种面向 AI 工作负载加速的 GPU 邻居感知共享内存设计

## 英文摘要

Driven by the increasing dominance of AI workloads and the resulting pressure on in-core SRAM resources, shared memory plays a pivotal role as an intermediate data buffer in the GPU. We observe substantial data redundancy in the shared memory, where up to 60.2% of later memory requests fetch data that have already been loaded into the shared memory by preceding requests. Such shared memory redundancy remains largely underexplored, exacerbating the bandwidth demands of AI workloads on modern GPUs. We propose Nash, a lightweight mechanism that tracks the source address of data in the shared memory using a Source Location Table (SLT). Using this SLT, Nash detects and redirects redundant requests within or across neighboring SMs, reducing unnecessary global memory traffic with minimal hardware overhead. Experimental results suggest that Nash achieves up to 18.3% performance improvement, 9.8% energy savings, and 25.3% reduction in global memory traffic compared to a baseline GPU.

## 中文摘要

随着 AI 工作负载日益占据主导地位，以及由此产生的对核内 SRAM 资源的压力，共享内存作为 GPU 中的中间数据缓冲区发挥着关键作用。我们观察到共享内存中存在大量数据冗余：高达 60.2% 的后续内存请求所获取的数据，已经由先前的请求加载到共享内存中。这种共享内存冗余在很大程度上仍未得到充分研究，并加剧了现代 GPU 上 AI 工作负载的带宽需求。我们提出了 Nash，一种轻量级机制，它使用源位置表（SLT）跟踪共享内存中数据的源地址。利用该 SLT，Nash 能够检测并重定向相邻 SM 内部或跨相邻 SM 的冗余请求，从而以极小的硬件开销减少不必要的全局内存流量。实验结果表明，与基线 GPU 相比，Nash 实现了最高 18.3% 的性能提升、9.8% 的能耗节省以及 25.3% 的全局内存流量降低。

## 英文关键词

AI, GPU, Shared Memory

## 中文关键词

AI、GPU、共享内存
