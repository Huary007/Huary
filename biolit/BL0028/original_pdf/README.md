# BL0028 原完整教学 PDF 的精确二进制备份

这些 `.part-*` 文件**不是可单独阅读的 PDF**。它们用于恢复原完整教学 PDF（108 页，20,693,570 bytes），而不是替代旁边的连续页可读分卷。

保持本目录所有文件在一起，运行（只需 Python 标准库）：

```sh
python3 reassemble_pdf.py original-teaching.pdf
```

脚本逐块验证 bytes、顺序与 SHA-256，重建后验证完整文件 SHA-256，拒绝覆盖现有文件。已实际执行并确认恢复结果与已验收原 PDF 字节完全一致。

原完整 PDF SHA-256：`9c0503ae6f7ca08734b8c5c7bcf025d98f54f5f04d84775e0b340b1426142153`。

来源、署名、许可与教学改动说明见上级 ATTRIBUTION.md、rights.json 和 source_manifest.json。二进制分块没有改变原完整 PDF 的任何字节。
