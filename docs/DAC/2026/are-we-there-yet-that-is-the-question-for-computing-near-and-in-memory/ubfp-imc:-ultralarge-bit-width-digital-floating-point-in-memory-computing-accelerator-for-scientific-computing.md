UBFP-IMC: Ultralarge Bit-Width Digital Floating-Point In-Memory Computing Accelerator for Scientific Computing
Authors：
[Yongjian Xu](https://63dac.conference-program.com/?post_type=page&p=15&uid=5905087024900570874)，[Biwei Liu](https://63dac.conference-program.com/?post_type=page&p=15&uid=09080097775594587441)，[Tianbo Ming](https://63dac.conference-program.com/?post_type=page&p=15&uid=2677317273855868033)，[Zhenyu Wu](https://63dac.conference-program.com/?post_type=page&p=15&uid=1512783668843847927)，[Yuanxi Peng](https://63dac.conference-program.com/?post_type=page&p=15&uid=06730002849449596751)

## 中文标题

UBFP-IMC：面向科学计算的超大字宽数字浮点存内计算加速器

## 英文摘要

Scientific computing represents a class of computation-intensive workloads, creating a critical demand for in-memory computing(IMC) architectures. Although IMC has demonstrated strong performance in low-precision applications, extending it to FP64 or higher precision required by scientific computing poses significant challenges: analog IMC(AIMC) is intrinsically limited to 4-bit fixed-point precision, while digital IMC(DIMC) suffers from area and performance overheads caused by large-bit-width mantissa processing and complex exponent-alignment operations. In this paper, we propose an ultralarge bit-width IMC architecture supporting FP64 and can be extended to higher precision. The design incorporates two-step carry-save adders(TSCSA) to efficiently implement Booth mantissa multiplication, along with an exponent difference generator and FIFO-based adder tree to perform alignment and accumulation. In 28nm technology, we implemented UBFP-IMC with 168 MAC units. When executing FP64 scientific computations, it achieves 4.30× to 8.53× improvement in energy efficiency(EEF) compared to existing high-performance GPUs and AIMCs. On the basis of maintaining low accumulation latency with 27× reduction over prior work, our area benefit increases with the increase of mantissa bit-width, indicating that UBFP-IMC has excellent scalability. Application level evaluation has demonstrated the potential of our work in accelerating scientific computing. To best of our knowledge, our work is the first ultralarge bit-width digital floating-point in-memory computing accelerator designed for scientific computing.

## 中文摘要

科学计算是一类计算密集型负载，对存内计算（IMC）架构提出了迫切需求。尽管 IMC 在低精度应用中已展现出强劲性能，但将其扩展到科学计算所需的 FP64 乃至更高精度仍面临重大挑战：模拟 IMC（AIMC）本质上受限于 4 位定点精度，而数字 IMC（DIMC）则因大位宽尾数处理和复杂的指数对齐操作而存在面积与性能开销。本文提出一种支持 FP64 并可扩展至更高精度的超大字宽 IMC 架构。该设计采用两步进位保存加法器（TSCSA）高效实现 Booth 尾数乘法，并结合指数差生成器与基于 FIFO 的加法树完成对齐与累加。我们采用 28nm 工艺实现了包含 168 个 MAC 单元的 UBFP-IMC。在执行 FP64 科学计算时，相较现有高性能 GPU 与 AIMC，其能效（EEF）提升 4.30× 至 8.53×。在保持低累加延迟（相较先前工作降低 27×）的基础上，我们的面积优势随尾数位宽的增加而增大，表明 UBFP-IMC 具有优异的可扩展性。应用级评测展示了本工作在加速科学计算方面的潜力。据我们所知，本工作是首个面向科学计算设计的超大字宽数字浮点存内计算加速器。

## 英文关键词

SRAM, DIMC, Scientific Computing

## 中文关键词

SRAM、DIMC、科学计算
