# AL0006 TabDPT 中文教学课件

这套133页中文课件介绍 TabDPT 的真实表格预训练、上下文检索、主要实验和附录，并讨论向微生物拉曼表格预测迁移时的验证边界。打开 `index.html` 即可离线阅读，不需要联网、安装依赖或构建。

本版用途说明更新于2026-11-04。用户确认本课原文截图可公开复用，仅用于非商业教育交流。代码、模型和数据仍分别适用各自原有条款。完整说明见 [RIGHTS.md](RIGHTS.md)。

## 阅读方式

- 解压ZIP后打开 `index.html`。截图、样式与交互脚本已内嵌，不需下载单独的图片文件。
- 左右方向键或 PageUp/PageDown 翻页；O 打开目录；F 切换全屏。
- 第2页是可点击的章节目录。链接 `index.html#slide-45` 可定位到第45页，也支持 `?slide=45`。
- `?all=1` 显示全部课件页，便于连续阅读或打印。
- 逻辑画布为1600×900，按窗口大小等比例显示。

## 内容与使用边界

课件覆盖正文、图表子图、公式、算法与附录A–G。表B.1的123个数据集分为17页展示；会议版Checklist的16项问题、回答与理由分为17页展示。HTML内嵌88个截图资产，其中87个用于课件页面，另一个是完整表1的参考裁图。

文中的手算数字是教学构造，不是新实验。未训练模型、未运行基准、未使用微生物实验数据。DMD指数字微镜器件；课件讨论的是由测量结果形成的预测表，不是控制光路。

## 论文版本和截图来源

论文为 *TabDPT: Scaling Tabular Foundation Models on Real Data*，NeurIPS 2025，DOI：10.52202/085713-5748。课件采用PDF中的10位作者名单，第3页说明文献元数据差异。

- [正式论文页面](https://proceedings.neurips.cc/paper_files/paper/2025/hash/fc0e3f908a2116ba529ad0a1530a3675-Abstract-Conference.html)
- [正式论文PDF](https://proceedings.neurips.cc/paper_files/paper/2025/file/fc0e3f908a2116ba529ad0a1530a3675-Paper-Conference.pdf)，31页。
- [arXiv v3](https://arxiv.org/pdf/2410.18164v3)，2026-01-17，24页。科学图表、公式、伪代码与相关原文截图来自此版本。
- [作者托管会议稿](https://www.cs.toronto.edu/~mvolkovs/NeurIPS2025_TabDPT.pdf)，31页，PDF元数据日期为2025-10-24。Checklist截图来自该文件的第15–21页。

这两份截图来源的页码不能混用。每张截图的实际源PDF页码与版本记录在 `manifest.json`、`coverage.csv` 和逐页索引中。第35页的TabArena声明注明2026-01-14，是后续修订补充，不是2025原始实验，也不是当前排行榜信息。完整论文PDF未放入本发布包，请使用以上原始来源链接。

## 代码版本

代码对照固定在以下提交，不将后续软件结果当作论文表1的结果：

- [TabDPT训练代码](https://github.com/layer6ai-labs/TabDPT-training/tree/af0340c5cdebe2ceb6b94c09d6f9564ee80b89df)，提交 `af0340c5cdebe2ceb6b94c09d6f9564ee80b89df`。
- [TabDPT推理代码](https://github.com/layer6ai-labs/TabDPT-inference/tree/bd03b004cd66fb45f77539036fdd9c187c3f5493)，提交 `bd03b004cd66fb45f77539036fdd9c187c3f5493`。

训练代码采用Toronto-Dominion研究用途许可；推理代码采用Apache-2.0。许可链接见 `manifest.json` 和 [RIGHTS.md](RIGHTS.md)。本包不附带代码仓库、模型权重或数据集。

## 文件说明

- `index.html`：可独立打开的完整课件。
- `slides.json`：与HTML一致的133页讲解文本和页面结构。
- `manifest.json`：论文和代码版本、截图来源页码、裁切范围及图片SHA-256。
- `coverage.csv`：内容条目与课件页面、截图来源的对应关系。
- `page_index.md`、`page_index.json`：逐页标题、章节与来源索引。
- `revision_mapping.csv`、`revision_mapping.json`：原130页到本版133页的对应关系和内容变动说明。
- `RIGHTS.md`：用途、归属与各类材料的权利边界。
- `checksums.sha256`：除自身以外全部发布文件的SHA-256校验值。

元数据中的 `assets/*.png` 是内嵌图片的标识，不是缺失文件的下载地址。单独图片和论文全文均不需要放在HTML旁边。

## 版本变化与校验

本版保留原130页顺序，新增第2页目录及第29、30页指标原文证据；第28页补充式(2)是缩放律的说明；第126页明确DMD含义。第116、125、132页的用途和证据边界表述与本发布版一致。

本版 `index.html` 的SHA-256为：

`9b578dbb36aa7a7c2f743943ec7f96947f5dda84454373f774b8cb1870f6ea92`

可在解压目录运行 `sha256sum -c checksums.sha256` 检查文件完整性。此校验验证文件内容是否改变，不是对论文科学结论或第三方权利的独立保证。
