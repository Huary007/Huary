# AL0014 · ifBO 中文教学课件

**已完成独立原文核查、258页浏览器实际渲染及逐页验收的发布版（2026-11-04）。**

论文：Herilalaina Rakotoarison, Steven Adriaensen, Neeratyoy Mallik, Samir Garibov, Eddie/Edward Bergman, Frank Hutter. In-Context Freeze-Thaw Bayesian Optimization for Hyperparameter Optimization. ICML 2024, PMLR 235:41982–42008.

- 正式记录：https://proceedings.mlr.press/v235/rakotoarison24a.html
- 正式PDF：https://raw.githubusercontent.com/mlresearch/v235/main/assets/rakotoarison24a/rakotoarison24a.pdf
- 论文实验代码：https://github.com/automl/ifBO/tree/icml-2024
- 复用依据：https://proceedings.mlr.press/pmlr-license-agreement.html
- 许可：https://creativecommons.org/licenses/by/4.0/

## 使用

保留assets与index.html的相对位置，用浏览器打开index.html。左右方向键、PageUp/PageDown或底部按钮翻页，F切换放映/阅读。打印按钮供浏览器导出PDF。所有文字可编辑，来源图像为原始PDF的高分辨率区域截图。

当前258页（保留原198页，另增60页分段阅读）。包括17幅图、133个子面板、6张表、2项算法、4个编号公式及7组未编号公式，附录A–F全覆盖。整图总览用于保留版面和共享图例，随后逐子图放大。PDF页码始终指原文物理页1–27，不是出版页41982–42008。

## 原文范围与版本

课件固定使用PMLR正式27页PDF。PMLR元数据extras为空，没有单列补充文件，附录A–F在该PDF内。OpenReview独立附件未另行取得。arXiv记录为2404.16795v3，2024-08-12修订，未将该版本图表混入正式稿。代码分支README指定论文模型版本0.0.1，本项目未执行训练或复现实验。

## 科学边界

- 附录B称16个PD1任务，图15实际仅15子图。因此逐任务图为35+15+24=74；不补造缺图。
- 原文未说明阴影的置信水平，课件不把阴影称作95%置信区间。
- Taskset无界log-loss先按初始损失中位数模拟的上界裁剪，NaN也处理为上界。这是评估条件。
- 正文§5.3与附录D.3对random-horizon变体固定阈值描述不一致，课件保留两段证据。
- 表1中无HP版本在部分PD1条件下优于完整FT-PFN，Taskset部分MSE并列，均保留。
- 教学手算、Transformer展开与设备/微生物研究设想明确标记，不属于论文实测。

## 图像与权利

截图从**最终PDF页面渲染**后裁剪，不能用底层嵌入图片替代，因为逐任务图的旧图例被正式PDF覆盖层修正。截图处理只包括区域裁剪、等比展示、表1原表头与数据组的原像素纵向拼接，不修改曲线或数值。

全部17图/6表图注已查，未发现第三方转载/单独许可标注。依据PMLR CC BY 4.0出版协议复用，并在每页提供原始论文及许可链接。中文教学解释不代表原作者认可。本版已完成独立原文核查与逐页渲染验收；未重新执行论文实验。

## 审核文件

- slides.json / slides_text.md：逐页内容。
- assets_manifest.json：源页、裁剪坐标、像素尺寸与处理方法。
- source/display_inventory.json：独立来源清单，133子图逐项解释。
- source/per_task_panels.json：74个逐任务图的完整标题、坐标与趋势。
- source/evidence_notes.md：证据边界和原文问题。
- display_coverage.csv：185个图表/公式/附录证据单元与课件页码。
- coverage_manifest.json：固定验收脚本所需逐页来源映射。
- rights_manifest.json / source_manifest.json：许可及版本依据。

## 发布说明

本包包含258页HTML课件、HTML直接引用的253个本地PNG资产，以及逐页内容、来源、覆盖与许可文档。原始PDF、临时审核材料、审核截图和依赖内部中间稿的制作脚本不随包发布。

论文及所复用原图依据 PMLR 出版协议采用 CC BY 4.0：https://creativecommons.org/licenses/by/4.0/ 。原文作者与链接见上。处理包括从最终PDF页面裁剪、放大、部分表格原像素拼接，以及新增中文解释和教学示例；未改动原图曲线或数据。新增内容不代表论文作者认可。

资产以最终HTML实际引用为准；制作清单可能记录未随包分发的中间资产。无需联网即可打开 index.html 阅读课件；外部原文与许可链接需要网络。SHA256SUMS.json 列出包内所有其他文件的校验值。
