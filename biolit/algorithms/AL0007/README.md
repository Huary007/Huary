# AL0007 · TabICL 中文教学课件

论文：Jingang Qu, David Holzmüller, Gaël Varoquaux, Marine Le Morvan. **TabICL: A Tabular Foundation Model for In-Context Learning on Large Data.** ICML 2025, PMLR 267:50817–50847.

- 正式论文：https://proceedings.mlr.press/v267/qu25d.html
- 官方PDF：https://raw.githubusercontent.com/mlresearch/v267/main/assets/qu25d/qu25d.pdf
- 作者代码：https://github.com/soda-inria/tabicl

## 阅读

解压完整文件夹后，用浏览器打开 `index.html`。保留 `assets` 文件夹与 HTML 的相对位置。

- 页面底部可上一页、下一页、输入页码或切换放映/阅读模式。
- 键盘左右方向键、PageUp/PageDown、空格切换页面。
- Home/End跳至首尾，F切换放映模式。
- 本稿172页。HTML文字可编辑，原文证据为PNG截图。

## 范围

本课件仅讲2025年原始TabICL分类模型，不混入后续TabICLv2。以31页PMLR正式PDF为准，附录A–I已包含其中。PMLR页面未列独立补充文件，OpenReview的独立附件未取得。

内容包括28幅图、2张表和全部子图。图C.2和C.3共128个二维任务例子按原位置分区放大。表F.1的15个数据集、7个模型和3项指标全部保留。另提供排名图的整幅放大视图。

论文中各分析的样本分母不完全一致，课件逐图保留原值并说明差额未解释。附录D的频率文字与RoPE公式存在10000/100000差异，课件按主文及公式讲解，并明确指出原文差异。

## 证据与复用

论文截图版权属于原作者。依据PMLR出版协议，按[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)复用。原始出版协议：https://proceedings.mlr.press/pmlr-license-agreement.html 。

截图处理包括区域裁剪、等比放大、长表的表头/数据区及跨栏、跨页文字证据的原像素分区拼接。图表数值未修改。每页列出PDF页码、图表/公式编号和处理方式，并提供PMLR原文及许可链接。本课件的中文解释、教学手算和研究设想不代表原作者的认可。

- `slides.json`：可编辑的逐页内容。
- `slides_text.md`：逐页文字阅读稿。
- `assets_manifest.json`：截图页码及裁剪坐标。
- `coverage_manifest.json`、`display_coverage.csv`：图表和子图的课件页码对应。
- `source_inventory.json`：正式来源、PDF校验值、许可和原文口径问题。

教学案例中的数字明确标为假设，不属于论文实测。设备及微生物检测部分是待验证研究设计，论文没有报告这些应用的实验结果。
