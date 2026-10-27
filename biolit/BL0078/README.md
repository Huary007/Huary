# BL0078 · 等温微量热法无菌检测：热流阈值与验证边界

**中文教学课件：49页；2026-10-27完成独立AI审查、主AI逐页验收及发布门槛校验。不是人工审查或临床、法规认证。**

## 阅读与下载

- [中文课件 PDF（49页）](render/deck.pdf)
- [自包含 HTML 课件](deck.html)：下载后本地打开，证据图片与样式已嵌入；本仓库未声称提供在线演示站点。
- [论文正式发表版原文 PDF（9页）](BL0078_source.pdf)
- [官方补充材料 PDF（4页，Online Resources 1–4）](BL0078_supplement.pdf)
- [逐图逐表覆盖清单](inventory.csv) · [关键数值与教学算例](consistency_manifest.json)
- [来源清单](source_manifest.json) · [版权与署名记录](rights.json)
- [AI验收与限制摘要](QA_SUMMARY.json) · [SHA-256 校验文件](SHA256SUMS)

## 论文

Sioen I, Coenye T. **Evaluation of a Novel Isothermal Microcalorimetry-Based Sterility Test.** *Journal of Pharmaceutical Innovation* **22**, 107 (2027). [DOI: 10.1007/s12247-026-10986-0](https://doi.org/10.1007/s12247-026-10986-0) · [出版者页面](https://link.springer.com/article/10.1007/s12247-026-10986-0)。**首次在线发表：2026-08-24；卷期年份：2027。** 两个日期分别记录，不把2027卷期年份当作首次发表时间。

课件覆盖原文3幅图及全部子图、3张表，以及唯一官方补充PDF的全部4项资源；解释代谢热、热电转换和基线扣除、热功率与热量、严格大于1 μW的报阳阈值、技术与生物学重复、TTD、RSD、低接种量随机性、对照与未检出结果。热电转换、概率与数值演算标注为教学模型或假设算例，不是厂家披露参数或新增实测数据。

## 结论与使用边界

- 这是**概念验证**，不能直接推出真实产品基质验证、常规放行替代资格或监管认可。
- 表2的阳性比例不是已确证的灵敏度/特异度；每水平48个、合计96个生物学结果，与技术重复的分母分开。
- **更早报阳不等于可以更早判阴性无菌放行。** 结果保留观察窗和未检出，不能把未检出当成零小时或证明不存在微生物。
- 保留并标明源文疑点：低水平统计说明与Fig.2检验并存；OR3中两组RSD均值与范围不相容；C. sporogenes高水平5/6缺少对应缺失配对脚注；技术TTD如何合成为生物学TTD未充分交代。不臆造修正、原始热谱或分析代码。
- 本材料用于文献学习，不替代原始论文、专业判断或设备使用说明；不是微生物实验操作指南。

## 验收范围

独立AI检查主文9页、补充4页、全部49个实际渲染课件页及21项覆盖清单；修订后重开变动页并验证未变页哈希。主AI随后逐页查看最终49页，复核原理、演算和证据。机械发布门槛通过，未解决的课件审查发现为零；源文本身的不确定性仍保留。

最终PDF由 **WeasyPrint 70.0** 对HTML实际打印渲染；未声称完成Chromium浏览器DOM或交互检查。已验收HTML/PDF和两份原文PDF按原字节发布，未重新渲染。公开元数据记录完成状态，不包含内部草稿、私人工作记录或厂家背景PDF。原文截图已嵌入HTML，完整原始页面可在随附原文与补充PDF中核对。

## 署名、许可与改动

原文及原图表：**© The Author(s) 2026，Sioen I、Coenye T**；依据 [Creative Commons Attribution 4.0 International（CC BY 4.0）](https://creativecommons.org/licenses/by/4.0/) 再分发。文章特定许可证据位于原文PDF第8页Open Access声明及[出版者版权段](https://link.springer.com/article/10.1007/s12247-026-10986-0#rightslink)。补充材料由该文章官方链接提供；结合文章特定许可与[出版者2026年标准CC BY协议](https://cms-resources.apps.public.k8s.springernature.io/springer-cms/rest/v1/content/27848838/data/v1)对Article包含补充信息的定义确认范围。标准协议是范围解释依据，不被冒充为该文已签署合同；全部主文与补充页面未发现单独第三方排除声明。逐项记录见 [rights.json](rights.json)。

原文与补充PDF不作修改；课件证据图仅作裁剪、放大，完整图、坐标、图例与表注通过总览和放大页保留，新增中文讲解及明确标识的教学算例。厂家托管的Vendur会议材料仅作为测量物理背景引文，未复制其PDF、图像或性能数据。文章、图表与产品标识不意味着作者、出版者或厂家为本课件背书；不主张独立商标许可，也不授予原权利人未授予的权利。

方法来源：Kassis T, Agarwal V, He Y, Patel D, Brueckner AM. *Scientific Agent Skills: A Library of Procedural Knowledge for Research Agents* (2026). [doi:10.48550/arXiv.2609.00065](https://doi.org/10.48550/arXiv.2609.00065)。这是工作流来源，不是微生物检测实验证据。
