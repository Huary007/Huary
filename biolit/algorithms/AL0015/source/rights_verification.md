# TabPFN-TS 版本与图表许可核验

核验日期：2026-11-04 UTC。范围：只读官方来源，保留本地源PDF，不作对外发布。

## 结论

1. 本地 `arxiv.pdf` 为 **arXiv:2501.02945v4，2026-01-26**，26页。封面侧边版本标记、标题及四名作者与官方版本页一致。主文许可为 **CC BY 4.0**。
2. 第19页表1注明表格转载自 **Aksu et al. (2024), GIFT-Eval**，并明确标注 CC BY 4.0。上游 arXiv:2410.10393 的 v1 与 v2 官方许可链接均已独立核验，均为 CC BY 4.0。
3. **TMLR 正式发表版本已存在**。TMLR 官方 Accepted papers 目录将本文列在 **July 2026**，链接至 OpenReview ID **KIkQj8VOUY**。不应再称“尚未正式发表”。
4. 可以将当前课件明确固定为 **基于 arXiv v4（2026-01-26）** 的解读，图号、页码、数值均保持该版；但不能称其为“TMLR最终版”或断言它与正式版完全相同。公开目录仅核实到发表月份，尚未核实具体日及正式PDF逐项差异。

## 本地文件身份

- 标题：From Tables to Time: Extending TabPFN-v2 to Time Series Forecasting
- 作者：Shi Bin Hoo, Samuel Müller, David Salinas, Frank Hutter
- 本地文件：原论文PDF（不随课件发布）
- 大小：15,114,298 bytes；页数：26
- SHA-256：`f5810a42f0f490980eb38508602d801eb407109fc53976e5a300357f67279837`
- 官方版本页：https://arxiv.org/abs/2501.02945v4
- 版本化PDF：https://arxiv.org/pdf/2501.02945v4
- 官方记录 v4 提交时间：2026-01-26 20:04:45 UTC。
- 此次用封面标记及元数据确认版本，未将本地文件与重新下载官方PDF做字节级一致性比对。

## 许可证据链与适用范围

- 主文官方版本页的“view license”链接直接指向 https://creativecommons.org/licenses/by/4.0/ 。
- 上游：Aksu, Taha; Woo, Gerald; Liu, Juncheng; Liu, Xu; Liu, Chenghao; Savarese, Silvio; Xiong, Caiming; Sahoo, Doyen. GIFT-Eval: A Benchmark For General Time Series Forecasting Model Evaluation (2024).
- 上游 v1：https://arxiv.org/abs/2410.10393v1 （2024-10-14）。
- 上游 v2：https://arxiv.org/abs/2410.10393v2 （2024-11-11）；非版本链接 https://arxiv.org/abs/2410.10393 本次解析至v2。
- 两个版本页的“view license”均指向同一个 CC BY 4.0 许可页。
- 本地PDF第19页表1 caption 自身明确给出 Aksu et al. (2024) 与 CC BY 4.0 来源说明。
- 许可允许复制、分发和改编（包括商业用途），前提包括恰当署名、链接许可、说明改动，不暗示作者背书，不附加妨碍许可权利的限制。许可不自动覆盖原始数据集、第三方商标、模型权重或代码的另行条款。此结论针对论文/表格素材，而非下载或重新分发所有底层数据集的授权。

## 正式版本与差异核验边界

- 官方发表目录：https://jmlr.org/tmlr/papers/
- 本文正式论坛：https://openreview.net/forum?id=KIkQj8VOUY
- 正式PDF：https://openreview.net/pdf?id=KIkQj8VOUY
- 官方BibTeX链接：https://jmlr.org/tmlr/papers/bib/KIkQj8VOUY.bib
- 官方目录显示本文同名、同四位作者，月份为 July 2026。
- **阻碍**：本次读取正式论坛和PDF时，OpenReview返回浏览器验证页面（Verifying your browser / Complete the check below），未获得正文；没有尝试完成验证或绕过访问限制。BibTeX读取器则报告不支持 text/x-bibtex 内容类型。因此尚不能核实具体发表日、最终PDF许可标记，亦不能确认其与v4的图表、数值、论述差异。
- 已能确认的差异仅是**版本/发表状态和时间**：v4为2026年1月预印本版本；官方TMLR目录为2026年7月发表。不能把 arXiv v4 的修订说明误当作 v4→TMLR 的修改清单。
- arXiv版本页对v4相对前版的说明包括加入协变量任务、额外消融、局限性章节并重写组织结构。该说明不证明最终版作了何种修改。

## 建议在课件中使用的署名

通用图表（按实际操作选择“原图/裁剪/重绘/译注”）：

> 来源：Hoo, Müller, Salinas & Hutter, From Tables to Time: Extending TabPFN-v2 to Time Series Forecasting, arXiv:2501.02945v4 (2026-01-26), Fig. X / p. X. CC BY 4.0. 本页含裁剪、中文译注或重绘（按实际修改注明）。原文：https://arxiv.org/abs/2501.02945v4；许可：https://creativecommons.org/licenses/by/4.0/。

表1：

> 来源：Aksu et al. (2024), GIFT-Eval, arXiv:2410.10393，CC BY 4.0；经 Hoo et al., arXiv:2501.02945v4, Table 1 / p.19 转载。本页含裁剪/译注/重排（按实际修改注明）。原始来源：https://arxiv.org/abs/2410.10393；许可：https://creativecommons.org/licenses/by/4.0/。

版本说明：

> 本课件图表、数值与页码统一依据 arXiv v4（2026-01-26）。论文后发表于 TMLR（2026年7月）；本课件未将正式版与v4视为逐项相同。

## 恢复轮复核（2026-11-04 UTC）

本轮重新打开两个版本化 arXiv 记录并点击各自许可链接，均仍指向CC BY 4.0；重新打开TMLR accepted papers目录，本文仍列为July 2026。保留上述正式PDF访问与版本差异未核实边界，未绕过浏览器验证。
