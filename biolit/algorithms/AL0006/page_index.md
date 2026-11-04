# 逐页内容与来源索引

本索引对应133页公开交流版。页码均为课件页码；每项末尾的源PDF页码对应注明的版本。点击课件标题可在离线HTML中打开该页。

## 课程起点

- 001 [TabDPT：从真实表格学习预测规则](index.html#slide-1)｜图2b｜arXiv v3（2026-01-17） p.5

## 完整目录

- 002 [课程目录：章节与页码](index.html#slide-2)｜作者与机构｜arXiv v3（2026-01-17） p.1

## 文献身份

- 003 [文献归属以PDF中的完整作者名单为据](index.html#slide-3)｜作者与机构｜arXiv v3（2026-01-17） p.1

## 课程路线

- 004 [三个动作构成同一条预测流程](index.html#slide-4)｜图2a｜arXiv v3（2026-01-17） p.5

## 证据边界

- 005 [论文版本和当前软件需要分开](index.html#slide-5)｜表1上半：TFM与no val.｜arXiv v3（2026-01-17） p.7

## 原理

- 006 [ICL把训练样本放进输入](index.html#slide-6)｜图2b｜arXiv v3（2026-01-17） p.5
- 007 [一行对应一个 token](index.html#slide-7)｜图2b｜arXiv v3（2026-01-17） p.5
- 008 [固定输入宽度把不同表送入同一模型](index.html#slide-8)｜表C.1｜arXiv v3（2026-01-17） p.18
- 009 [图2a：一次批训练包含不同表](index.html#slide-9)｜图2a｜arXiv v3（2026-01-17） p.5
- 010 [图2b：标签只加进上下文行](index.html#slide-10)｜图2b｜arXiv v3（2026-01-17） p.5
- 011 [式1把输入、算子和输出写在一起](index.html#slide-11)｜式1｜arXiv v3（2026-01-17） p.5
- 012 [注意力限制阻断查询标签泄漏](index.html#slide-12)｜图2b｜arXiv v3（2026-01-17） p.5
- 013 [一个二维嵌入计算例](index.html#slide-13)｜式1｜arXiv v3（2026-01-17） p.5
- 014 [自监督任务来自被拿走的一列](index.html#slide-14)｜图2a｜arXiv v3（2026-01-17） p.5
- 015 [分类和回归目标用不同变换](index.html#slide-15)｜代码块1 第21–27行｜arXiv v3（2026-01-17） p.19
- 016 [把一列连续值变成三分类](index.html#slide-16)｜代码块1 第28–33行｜arXiv v3（2026-01-17） p.19
- 017 [列子采样改变同一目标的条件信息](index.html#slide-17)｜代码块1 第14–19行｜arXiv v3（2026-01-17） p.19
- 018 [检索用相似样本控制上下文长度](index.html#slide-18)｜图2a｜arXiv v3（2026-01-17） p.5
- 019 [检索计算例：距离只来自可用特征](index.html#slide-19)｜算法1｜arXiv v3（2026-01-17） p.4
- 020 [算法1：前向预测之后才更新权重](index.html#slide-20)｜算法1｜arXiv v3（2026-01-17） p.4
- 021 [训练和推理共享局部上下文](index.html#slide-21)｜图4a｜arXiv v3（2026-01-17） p.8
- 022 [超过10类时按位编码类别](index.html#slide-22)｜表C.1｜arXiv v3（2026-01-17） p.18
- 023 [集成平均削弱列顺序和类别编号影响](index.html#slide-23)｜图2b｜arXiv v3（2026-01-17） p.5

## 实验设置

- 024 [训练数据和测试数据来自不同集合](index.html#slide-24)｜图B.1a｜arXiv v3（2026-01-17） p.18
- 025 [评估的范围比“所有表格”窄](index.html#slide-25)｜图B.1a｜arXiv v3（2026-01-17） p.18
- 026 [基线有不同的调参和数据预算](index.html#slide-26)｜表1上半：TFM与no val.｜arXiv v3（2026-01-17） p.7

## 指标教学

- 027 [四个指标回答不同问题](index.html#slide-27)｜表1上半：TFM与no val.｜arXiv v3（2026-01-17） p.7
- 028 [R²和交叉熵的手算例](index.html#slide-28)｜式2｜arXiv v3（2026-01-17） p.9
- 029 [指标补充：原文怎样报告R²](index.html#slide-29)｜表1上半：TFM与no val.｜arXiv v3（2026-01-17） p.7
- 030 [指标补充：交叉熵不等于缩放律](index.html#slide-30)｜第4.5节：交叉熵、1−ρ与缩放图损失｜arXiv v3（2026-01-17） p.9

## 主结果

- 031 [表1：分类差异主要体现在准确率](index.html#slide-31)｜表1上半：TFM与no val.｜arXiv v3（2026-01-17） p.7
- 032 [表1：回归点估计略高但区间重叠](index.html#slide-32)｜表1上半：TFM与no val.｜arXiv v3（2026-01-17） p.7
- 033 [表1：不给验证集时应换一行比较](index.html#slide-33)｜表1上半：TFM与no val.｜arXiv v3（2026-01-17） p.7
- 034 [表1：树和深度基线也有强项](index.html#slide-34)｜表1下半：深度与树基线｜arXiv v3（2026-01-17） p.7

## 后续arXiv v3补充

- 035 [后续修订补充：2026-01-14的TabArena声明](index.html#slide-35)｜引言中注明日期的TabArena结果｜arXiv v3（2026-01-17） p.2

## 主结果

- 036 [图3a：每个格子是成对胜率](index.html#slide-36)｜图3a｜arXiv v3（2026-01-17） p.8

## 指标教学

- 037 [胜率忽略了胜负的幅度](index.html#slide-37)｜图3a｜arXiv v3（2026-01-17） p.8

## 速度与代价

- 038 [图3b：越靠左上，部署预算越划算](index.html#slide-38)｜图3b｜arXiv v3（2026-01-17） p.8
- 039 [固定模型在线推理时，树模型可更快](index.html#slide-39)｜图3b｜arXiv v3（2026-01-17） p.8

## 组件消融

- 040 [图4a：四种删减都会损伤表现](index.html#slide-40)｜图4a｜arXiv v3（2026-01-17） p.8
- 041 [图4b：没有SSL时真实表会过拟合](index.html#slide-41)｜图4b｜arXiv v3（2026-01-17） p.8
- 042 [真实数据优势有明确的对照范围](index.html#slide-42)｜图4b｜arXiv v3（2026-01-17） p.8

## 缩放规律

- 043 [图1：模型和数据两个维度共同扩展](index.html#slide-43)｜图1｜arXiv v3（2026-01-17） p.1
- 044 [式2中每个参数都有职责](index.html#slide-44)｜式2｜arXiv v3（2026-01-17） p.9
- 045 [扩大一倍只缩小对应的那一项](index.html#slide-45)｜式2｜arXiv v3（2026-01-17） p.9
- 046 [为何数据规模按单元格计数](index.html#slide-46)｜图B.1a｜arXiv v3（2026-01-17） p.18

## 少样本学习

- 047 [表2：每类10个标签，仍有未标注行](index.html#slide-47)｜表2｜arXiv v3（2026-01-17） p.9
- 048 [表2：平均提升0.80个百分点](index.html#slide-48)｜表2｜arXiv v3（2026-01-17） p.9
- 049 [表2：dna上的负结果不能藏起来](index.html#slide-49)｜表2｜arXiv v3（2026-01-17） p.9

## 附录A 失败尝试

- 050 [附录A：复杂预处理没有普遍收益](index.html#slide-50)｜附录A：预处理负结果｜arXiv v3（2026-01-17） p.15
- 051 [附录A：缺失标记没有带来预期收益](index.html#slide-51)｜附录A：缺失值编码负结果｜arXiv v3（2026-01-17） p.15
- 052 [附录A：更复杂标签表示也会失败](index.html#slide-52)｜附录A：标签嵌入负结果｜arXiv v3（2026-01-17） p.15
- 053 [附录A：逐单元格表示增加显存需求](index.html#slide-53)｜附录A：逐单元格编码｜arXiv v3（2026-01-17） p.15

## 附录B 训练数据

- 054 [图B.1a：训练表大小跨度很大](index.html#slide-54)｜图B.1a｜arXiv v3（2026-01-17） p.18
- 055 [图B.1b：123张表的领域组成](index.html#slide-55)｜图B.1b｜arXiv v3（2026-01-17） p.18

## 附录B 数据清单

- 056 [表B.1：训练表逐项核对 1](index.html#slide-56)｜表B.1，ID 24–389｜arXiv v3（2026-01-17） p.15
- 057 [表B.1：训练表逐项核对 2](index.html#slide-57)｜表B.1，ID 396–821｜arXiv v3（2026-01-17） p.15
- 058 [表B.1：训练表逐项核对 3](index.html#slide-58)｜表B.1，ID 843–1018｜arXiv v3（2026-01-17） p.16
- 059 [表B.1：训练表逐项核对 4](index.html#slide-59)｜表B.1，ID 1036–1118｜arXiv v3（2026-01-17） p.16
- 060 [表B.1：训练表逐项核对 5](index.html#slide-60)｜表B.1，ID 1120–1459｜arXiv v3（2026-01-17） p.16
- 061 [表B.1：训练表逐项核对 6](index.html#slide-61)｜表B.1，ID 1466–1493｜arXiv v3（2026-01-17） p.16
- 062 [表B.1：训练表逐项核对 7](index.html#slide-62)｜表B.1，ID 1503–3277｜arXiv v3（2026-01-17） p.16
- 063 [表B.1：训练表逐项核对 8](index.html#slide-63)｜表B.1，ID 4135–40679｜arXiv v3（2026-01-17） p.16
- 064 [表B.1：训练表逐项核对 9](index.html#slide-64)｜表B.1，ID 40680–41143｜arXiv v3（2026-01-17） p.16
- 065 [表B.1：训练表逐项核对 10](index.html#slide-65)｜表B.1，ID 41144–41161｜arXiv v3（2026-01-17） p.16
- 066 [表B.1：训练表逐项核对 11](index.html#slide-66)｜表B.1，ID 41162–41169｜arXiv v3（2026-01-17） p.16
- 067 [表B.1：训练表逐项核对 12](index.html#slide-67)｜表B.1，ID 41434–41980｜arXiv v3（2026-01-17） p.16
- 068 [表B.1：训练表逐项核对 13](index.html#slide-68)｜表B.1，ID 42563–42732｜arXiv v3（2026-01-17） p.17
- 069 [表B.1：训练表逐项核对 14](index.html#slide-69)｜表B.1，ID 42734–44061｜arXiv v3（2026-01-17） p.17
- 070 [表B.1：训练表逐项核对 15](index.html#slide-70)｜表B.1，ID 44063–44137｜arXiv v3（2026-01-17） p.17
- 071 [表B.1：训练表逐项核对 16](index.html#slide-71)｜表B.1，ID 44145–45041｜arXiv v3（2026-01-17） p.17
- 072 [表B.1：训练表逐项核对 17](index.html#slide-72)｜表B.1，ID 45043–45047｜arXiv v3（2026-01-17） p.17

## 附录B 污染排查

- 073 [附录B.1：污染排查用多种指纹](index.html#slide-73)｜附录B.1：污染排查｜arXiv v3（2026-01-17） p.17

## 附录C 架构

- 074 [表C.1：论文主干的固定参数](index.html#slide-74)｜表C.1｜arXiv v3（2026-01-17） p.18
- 075 [表C.2：七种模型尺寸逐项列出](index.html#slide-75)｜表C.2｜arXiv v3（2026-01-17） p.19

## 附录C 预处理

- 076 [附录C：两阶段标准化与缺失填补](index.html#slide-76)｜附录C.1：预处理｜arXiv v3（2026-01-17） p.17
- 077 [附录C：标准化后补零等价于均值填补](index.html#slide-77)｜附录C.1：缺失值处理｜arXiv v3（2026-01-17） p.18

## 计算例

- 078 [标准化回归的还原计算](index.html#slide-78)｜式1｜arXiv v3（2026-01-17） p.5

## 附录C 训练

- 079 [附录C：优化设置决定复现配方](index.html#slide-79)｜附录C.1：优化设置｜arXiv v3（2026-01-17） p.18

## 附录D 算法逐段

- 080 [代码块1：创建训练任务数据对象](index.html#slide-80)｜代码块1 第1–7行｜arXiv v3（2026-01-17） p.19
- 081 [代码块1：预处理后保存近邻索引](index.html#slide-81)｜代码块1 第8–12行｜arXiv v3（2026-01-17） p.19
- 082 [代码块1：随机选择并重排特征](index.html#slide-82)｜代码块1 第14–19行｜arXiv v3（2026-01-17） p.19
- 083 [代码块1：先判断是否保留连续目标](index.html#slide-83)｜代码块1 第21–27行｜arXiv v3（2026-01-17） p.19
- 084 [代码块1：用随机边界生成类别](index.html#slide-84)｜代码块1 第28–33行｜arXiv v3（2026-01-17） p.19
- 085 [代码块1：低基数目标与随机取表](index.html#slide-85)｜代码块1 第34–43行｜arXiv v3（2026-01-17） p.19
- 086 [代码块1：随机选种子行和目标列](index.html#slide-86)｜代码块1 第44–50行｜arXiv v3（2026-01-17） p.20
- 087 [代码块1：遮蔽目标后提取近邻任务](index.html#slide-87)｜代码块1 第52–56行｜arXiv v3（2026-01-17） p.20
- 088 [代码块1：最后输出一个训练任务](index.html#slide-88)｜代码块1 第58–64行｜arXiv v3（2026-01-17） p.20
- 089 [代码块2：建立模型和训练循环](index.html#slide-89)｜代码块2 第1–7行｜arXiv v3（2026-01-17） p.20
- 090 [代码块2：上下文标签可见，查询标签遮蔽](index.html#slide-90)｜代码块2 第8–12行｜arXiv v3（2026-01-17） p.20
- 091 [代码块2：任务损失和反向传播](index.html#slide-91)｜代码块2 第14–21行｜arXiv v3（2026-01-17） p.20

## 附录E 排名

- 092 [图E.1a：Elo把多次胜负汇成评分](index.html#slide-92)｜图E.1a｜arXiv v3（2026-01-17） p.21
- 093 [图E.1b：Glicko2的误差条含评级不确定性](index.html#slide-93)｜图E.1b｜arXiv v3（2026-01-17） p.21

## 附录F 分层结果

- 094 [图F.1a：分类按行数分桶](index.html#slide-94)｜图F.1a｜arXiv v3（2026-01-17） p.22
- 095 [图F.1b：回归也受任务组成影响](index.html#slide-95)｜图F.1b｜arXiv v3（2026-01-17） p.22
- 096 [图F.2a：高维分类仍需输入压缩](index.html#slide-96)｜图F.2a｜arXiv v3（2026-01-17） p.22
- 097 [图F.2b：宽表回归出现明显弱点](index.html#slide-97)｜图F.2b｜arXiv v3（2026-01-17） p.22
- 098 [图F.3a：类别特征比例改变分类任务](index.html#slide-98)｜图F.3a｜arXiv v3（2026-01-17） p.22
- 099 [图F.3b：类别比例与回归难度一起变化](index.html#slide-99)｜图F.3b｜arXiv v3（2026-01-17） p.22

## 附录G 统计比较

- 100 [图G.1：AUC的临界差异图](index.html#slide-100)｜图G.1｜arXiv v3（2026-01-17） p.24
- 101 [图G.2：准确率排序更有针对性](index.html#slide-101)｜图G.2｜arXiv v3（2026-01-17） p.24
- 102 [图G.3：相关系数也不能替代R²](index.html#slide-102)｜图G.3｜arXiv v3（2026-01-17） p.24
- 103 [图G.4：回归误差的排名结构](index.html#slide-103)｜图G.4｜arXiv v3（2026-01-17） p.24

## 会议版Checklist

- 104 [Checklist 1：主张必须与证据范围一致](index.html#slide-104)｜Checklist 1 Claims｜作者会议稿（2025-10-24） p.15
- 105 [Checklist 2：局限应当明确讨论](index.html#slide-105)｜Checklist 2 Limitations｜作者会议稿（2025-10-24） p.15
- 106 [Checklist 3：没有待证明的理论定理](index.html#slide-106)｜Checklist 3 Theory：问题与回答｜作者会议稿（2025-10-24） p.15
- 107 [Checklist 3续：NA的理由来自原文](index.html#slide-107)｜Checklist 3 Theory：理由（续页）｜作者会议稿（2025-10-24） p.16
- 108 [Checklist 4：方法与实验支持复现](index.html#slide-108)｜Checklist 4 Reproducibility｜作者会议稿（2025-10-24） p.16
- 109 [Checklist 5：开放代码、权重与数据](index.html#slide-109)｜Checklist 5 Open data and code｜作者会议稿（2025-10-24） p.17
- 110 [Checklist 6：训练与测试细节](index.html#slide-110)｜Checklist 6 Experimental details｜作者会议稿（2025-10-24） p.17
- 111 [Checklist 7：误差条与统计信息](index.html#slide-111)｜Checklist 7 Statistical significance｜作者会议稿（2025-10-24） p.17
- 112 [Checklist 8：完整计算时间没有记录](index.html#slide-112)｜Checklist 8 Compute resources｜作者会议稿（2025-10-24） p.18
- 113 [Checklist 9：伦理准则合规声明](index.html#slide-113)｜Checklist 9 Ethics｜作者会议稿（2025-10-24） p.18
- 114 [Checklist 10：广泛社会影响回答NA](index.html#slide-114)｜Checklist 10 Broader impacts｜作者会议稿（2025-10-24） p.18
- 115 [Checklist 11：高风险发布防护回答NA](index.html#slide-115)｜Checklist 11 Safeguards｜作者会议稿（2025-10-24） p.19
- 116 [Checklist 12：既有资产许可与归属](index.html#slide-116)｜Checklist 12 Existing asset licenses｜作者会议稿（2025-10-24） p.19
- 117 [Checklist 13：新资产的文档](index.html#slide-117)｜Checklist 13 New assets｜作者会议稿（2025-10-24） p.20
- 118 [Checklist 14：没有众包或人类受试者](index.html#slide-118)｜Checklist 14 Human subjects｜作者会议稿（2025-10-24） p.20
- 119 [Checklist 15：IRB回答NA](index.html#slide-119)｜Checklist 15 IRB｜作者会议稿（2025-10-24） p.20
- 120 [Checklist 16：核心方法没有使用LLM](index.html#slide-120)｜Checklist 16 LLM usage｜作者会议稿（2025-10-24） p.21

## 官方代码核验

- 121 [官方训练代码已经与论文配置分叉](index.html#slide-121)｜表C.1｜arXiv v3（2026-01-17） p.18
- 122 [检索前是否遮蔽目标列须复核](index.html#slide-122)｜代码块1 第52–56行｜arXiv v3（2026-01-17） p.20
- 123 [预处理参数也需锁到具体版本](index.html#slide-123)｜图2b｜arXiv v3（2026-01-17） p.5
- 124 [复现实验需要固定权重与汇总方式](index.html#slide-124)｜表1上半：TFM与no val.｜arXiv v3（2026-01-17） p.7

## 许可与来源

- 125 [软件许可与论文截图许可分开核对](index.html#slide-125)｜图2b｜arXiv v3（2026-01-17） p.5

## 与研究的关系

- 126 [微生物拉曼数据可先整理成预测表](index.html#slide-126)｜图2b｜arXiv v3（2026-01-17） p.5
- 127 [DMD压缩测量和表格预测是两层问题](index.html#slide-127)｜表C.1｜arXiv v3（2026-01-17） p.18
- 128 [一个分组验证计算例](index.html#slide-128)｜图B.1a｜arXiv v3（2026-01-17） p.18
- 129 [建议同时比较小样本与跨批次表现](index.html#slide-129)｜表2｜arXiv v3（2026-01-17） p.9
- 130 [伪标签和域偏移需要单独检查](index.html#slide-130)｜图4b｜arXiv v3（2026-01-17） p.8

## 限制与使用条件

- 131 [原始论文承认的能力边界](index.html#slide-131)｜第5节：限制与未来工作｜arXiv v3（2026-01-17） p.10

## 证据收束

- 132 [本课的证据和没有做的事](index.html#slide-132)｜图1｜arXiv v3（2026-01-17） p.1

## 50字内总结

- 133 [带走三点](index.html#slide-133)｜图2b｜arXiv v3（2026-01-17） p.5

