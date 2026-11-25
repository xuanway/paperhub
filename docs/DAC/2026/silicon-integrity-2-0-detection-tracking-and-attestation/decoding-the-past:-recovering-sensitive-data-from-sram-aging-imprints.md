Decoding the Past: Recovering Sensitive Data from SRAM Aging Imprints
Authors：
[Zakia Tamanna Tisha](https://63dac.conference-program.com/?post_type=page&p=15&uid=35707616312443412041)，[Gaines Odom](https://63dac.conference-program.com/?post_type=page&p=15&uid=2815385603017856513)，[Biswajit Ray](https://63dac.conference-program.com/?post_type=page&p=15&uid=46804876453265542051)，[Ujjwal Guin](https://63dac.conference-program.com/?post_type=page&p=15&uid=643143)

## 中文标题

解读过往：从 SRAM 老化印记中恢复敏感数据

## 英文摘要

Long-term data remanence in SRAMs can pose serious security risks when ICs containing sensitive information are discarded at the end of their operational life. Sensitive information can fall into unauthorized hands if these discarded ICs are not sanitized properly. Traditionally, security experts from industry, academia, and government have addressed data remanence primarily with DRAM and flash memories. Unfortunately, SRAMs have been largely overlooked in this field due to very short data retention periods. Hovanes et al. [8] demonstrated that SRAMs are vulnerable to data remanence attacks, retrieving static data such as firmware and keys. Their method exploits aging-induced imprints on power-up states, enabling partial recovery by comparing aged states with the originals. Although effective, this method requires maintaining records of all initial power-up states. In this paper, we have proposed a data recovery approach without needing access to any prior information. Our proposed approach also exploits the phenomenon of data imprinting in SRAMs, but instead of using the actual initial power-up states, we use controlled aging to reconstruct these initial states. This allows us to partially recover SRAM data by analyzing the differences between the reconstructed power-up states and those with the aging imprint. Our experimental findings are based on individual SRAM chips storing a binary image. We demonstrated near-complete data recovery after 12 hours of controlled aging at 100◦C using only 32 copies.

## 中文摘要

当承载敏感信息的 IC 在寿命终结时被废弃，SRAM 中的长期数据残留会构成严重的安全风险。若这些被废弃的 IC 未得到妥善擦除，敏感信息便可能落入未授权者之手。长期以来，来自产业界、学术界与政府的安全专家主要针对 DRAM 与闪存处理数据残留问题。遗憾的是，由于数据保持时间极短，SRAM 在该领域基本被忽视。Hovanes 等人 [8] 已证明 SRAM 易受数据残留攻击，可恢复固件与密钥等静态数据。其方法利用老化在上电状态上留下的印记，通过比较老化后状态与原始状态实现部分恢复。该方法虽有效，却需要保存所有初始上电状态的记录。本文提出一种无需访问任何先验信息的数据恢复方法。我们所提方法同样利用 SRAM 中的数据印记现象，但不使用真实的初始上电状态，而是通过受控老化来重建这些初始状态。由此，我们可借助分析重建的上电状态与带有老化印记的上电状态之间的差异，对 SRAM 数据实现部分恢复。我们的实验发现基于存储二值图像的单个 SRAM 芯片。我们证明，在 100°C 下进行 12 小时受控老化、且仅使用 32 份副本，即可实现接近完全的数据恢复。

## 英文关键词

data remanence, data recovery, SRAM power-up state, process variation, aging

## 中文关键词

数据残留、数据恢复、SRAM 上电状态、工艺偏差、老化
