# AL0017 · Bayes’ Power 中文教学课件

163 页独立 HTML 教学课件。已完成内容与交互验收。课件保持验收冻结版本。

## 阅读

打开 index.html。默认单页等比适应窗口，支持目录跳页、左右键翻页、全部页面、原尺寸滚动及全屏。全部页面模式会随手动滚动更新页码与网址。

1–13 页为主线；14–27 页为机制与实验补充；28–90 页为原图及全部子图；91–150 页为原文段落、公式和完整图注的分段放大；151–162 页为全部原 PDF 页；163 页为末页清单。目录.txt 与 revision_mapping.json 提供完整页码映射。

保留原有 103 页内容及原画布字号，新增 60 页原文放大，不以删减或缩字数代替分段解释。共 156 张原文截图，覆盖论文主文和附录全部 12 图、51 个空间子图；原文没有编号表。

## 原文、署名与许可

Samuel Müller, Noah Hollmann, Frank Hutter (2024). *Bayes’ Power for Explaining In-Context Learning Generalizations*. arXiv:2410.01565v1，2024-10-02。

- [原论文记录](https://arxiv.org/abs/2410.01565v1)
- [原论文 PDF](https://arxiv.org/pdf/2410.01565v1)，包内 source/paper.pdf 为 12 页原文。
- [Creative Commons Attribution 4.0 International（CC BY 4.0）](https://creativecommons.org/licenses/by/4.0/)。本课件中的原论文文字、截图和图表适用该许可。
- [作者对应实验代码](https://github.com/SamuelGabriel/BayesGeneralizations)，代码采用 Apache-2.0；本包未复制作者代码。

修改说明：新增中文教学解释、教学计算和研究建议；原论文页面经直接截图、裁切、放大和编排，未改写原图数值与曲线。页面新增目录、翻页、适应窗口、全屏和滚动同步。新增解释及标记的教学示意并非论文原始实验结果；原作者不为本课件背书。

## 使用边界

本文分析受控合成先验中的贝叶斯后验与 PFN 近似，不保证任意真实数据任务的准确率。DMD 指数字微镜器件；与可编程拉曼细菌分类相关内容属于待验证研究建议，准确率优先。课件不包含真实细菌实验结果，未复现论文训练或基准实验。

## 配套文件

- slides.json / slides_text.md：课件结构与文字。
- assets_manifest.json / zoom_assets_manifest.json：截图原文页码、裁切坐标与倍率。
- figure_coverage.json：全部图与子图的课件覆盖位置。
- source_manifest.json / rights_manifest.json：版本、来源、许可与修改说明。
- checksums.json：逐文件 SHA-256；index.html 的冻结哈希为 46531650dfa76bce2e1fc9c67657470946ecc2c0d3354225352409d503e6b269。

请保留 HTML 与 assets 相对目录结构。已完成全部163页内容审查、独立原文核查与交互复测。47个真实浏览器交互状态通过；三种显示方式的缩窗、窄窗和恢复均保持当前页，页内位置偏差在3个显示像素内。未测试系统级全屏；未复现论文实验。
