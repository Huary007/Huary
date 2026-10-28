# BL0028｜活菌的早期检测与分类：时序相干成像与深度学习

**完整教学稿 108 页，原始已验收版本保持不动。此处只是无损文件容器分卷，不是删减版。**

本项目 AI 独立审阅与主审阅均已通过。教学内容不因单次传输大小限制而删页、缩小图文、重采样或改成页面截图堆叠。原 PDF 的文字、原图像素尺寸与图像像素摘要、缩放及每页大小均保持不变。分卷使用未用资源清理与无损流压缩，并有 PDF 内容流浮点数值规范化；独立核查发现极小平移差异，最大 0.00006103515625 pt。没有原图重采样或图像降质，全部页面在原验收分辨率 96 dpi 下逐像素完全相同。**不声称分卷绘制操作或内容流字节完全未变**；如需原始精确字节，请使用下述 original_pdf/ 恢复块。

## 教学 PDF：依次打开所有分卷

| 分卷 | 原完整稿页码 | 页数 | bytes | SHA-256 |
|---|---:|---:|---:|---|
| [第 1 卷](render/deck-pages-001-036.pdf) | 1–36 | 36 | 6,125,727 | `b148a7f336e2fbfbd0949ac89da1bdb7557b3ead01572675f7eb02028f62d20d` |
| [第 2 卷](render/deck-pages-037-072.pdf) | 37–72 | 36 | 4,957,894 | `88f098bb29e64fe40170fdd65b7b209a508d7709a6729b233424a1c42a456ea3` |
| [第 3 卷](render/deck-pages-073-108.pdf) | 73–108 | 36 | 10,955,696 | `56fc98434d1eed27714e8cb8f6149abd137d14b526a6c3440eed6075c1ba0b98` |

原完整稿页码不重置，连续覆盖 **1–108**，无遗漏、无重叠。卷内第 n 页对应“原起始页 + n − 1”。完整逐页映射见 [分卷验证报告](verification/pdf-parts-equivalence.json)。

原完整教学 PDF：**20,693,570 bytes，108 页**；SHA-256：`9c0503ae6f7ca08734b8c5c7bcf025d98f54f5f04d84775e0b340b1426142153`。分卷是新的 PDF 容器，不声称其文件 SHA 等于原完整稿。

如需单个逻辑完整 PDF，可安装 PyMuPDF 后，在此目录运行：

```sh
python3 merge_pdf_parts.py merged-teaching.pdf
```

该脚本核验每卷 SHA 和页码顺序；合并结果已对全部 108 页像素验证。**重新合并只保证完整页内容，不恢复原 PDF 文件字节或 SHA。**

如需恢复**字节完全相同的原完整 PDF**，本包同时提供 [二进制分块与说明](original_pdf/README.md)。下载 `original_pdf/` 的所有文件后，在当前目录运行：

```sh
python3 original_pdf/reassemble_pdf.py original-teaching.pdf
```

该脚本只需 Python 标准库，逐块与最终文件均验证 SHA-256，并拒绝覆盖已有文件。所有块均小于 11 MiB；已经实际恢复并比对原 SHA。它们不是上面可读 PDF 分卷的替代品，不能单独作为 PDF 打开。

## HTML：下载整个目录后离线打开

1. 下载此目录的**全部文件与 assets/**，保持相对目录结构。
2. 使用浏览器打开 [deck.html](deck.html)。GitHub 的文件预览页不是幻灯片播放器。
3. 不需要联网或服务端。不要只单独下载 HTML；否则缺少相邻图片资产。

原内嵌图片仅按原字节移到 assets/，没有重新编码。所有页面结构、CSS 尺寸、原图、解释与顺序保持不变。外置 HTML 使用原来的 **WeasyPrint 70.0** 实际打印后，全部 108 页与已验收 PNG 逐像素相同；这不是 Chromium 渲染或浏览器 DOM 溢出审计。

可用 Python 标准库恢复**字节完全相同的原自包含 HTML**：

```sh
python3 restore_html.py original-self-contained.html
```

原 HTML：34,538,586 bytes；SHA-256：`96c991190a252241b4e07bb1ba1b13d01b6b74b3a1443780d608eec300517887`。脚本会核验 HTML、每张图片与重建结果，拒绝覆盖已有文件。

## 来源、署名与证据

- [原论文 PDF（17 页）](sources/Wang2020-main.pdf) · [原补充材料 PDF（11 页）](sources/Wang2020-supplement.pdf)：原字节副本。
- [图表与证据映射](inventory.csv) · [来源版本清单](source_manifest.json)。
- [署名与许可](ATTRIBUTION.md) · [逐资产权利记录](rights.json)。
- [AI 审阅摘要](qa-summary.json) · [HTML 图片原字节清单](html-assets.json)。
- [HTML 全页等价报告](verification/html-render-equivalence.json) · [重建脚本实测](verification/reconstruction-tests.json) · [文件 SHA-256](SHA256SUMS)。

保留论文未解释的三处差异：总菌落 965 与分种合计 955；E. coli 80% 恢复时间约 8 h 与 Discussion 的 8.8 h；正文式 (5) 参数无法直接复得 Table S2 的有效像素值。教学算例不冒充原始实验结果。

AI 核查不等同于人类科学评审、法律审核、论文作者认可或实验复现。内容修改需要重新渲染和审阅；本次仅作无损文件组织。
