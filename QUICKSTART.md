# 快速开始指南

## 如何运行完整交互式体验

由于这是一个交互式命令行工具，你需要在终端中直接运行：

```bash
cd /Users/pc/Documents/cursor/reading
python main.py
```

## 操作流程

### 主菜单选项

运行后你会看到：

```
============================================================
                 Reading Comprehension Tool
============================================================

Main Menu:
1. Start Reading Practice  # 开始阅读练习
2. View Progress Report    # 查看进度报告
3. Help & Instructions     # 帮助说明
4. Exit                    # 退出
```

### 完整体验流程

**步骤1：选择年级**
```
Select Grade Level:
K - Kindergarten (幼儿园)
1 - Grade 1 (一年级)
2 - Grade 2 (二年级)
3 - Grade 3 (三年级)
4 - Grade 4 (四年级)
5 - Grade 5 (五年级)
```

**步骤2：选择文章**
每个年级有2篇文章：
- 故事类（Story）
- 科普类（Informational）

**步骤3：阅读文章**
系统会展示完整的阅读材料，你可以慢慢阅读。

**步骤4：回答问题**
每篇文章有3-5个选择题，题型包括：
- Main Idea (主旨大意)
- Supporting Details (细节题)
- Inference (推理题)
- Vocabulary (词汇题)
- Character Traits (人物性格)
- Sequence (顺序题)
- Cause and Effect (因果关系)

**步骤5：即时反馈**
每答完一题，立即显示：
- ✓ 正确 / ✗ 错误
- 详细解释
- 正确答案

**步骤6：查看总结**
完成所有题目后，显示：
- 总题数和正确数
- 准确率百分比
- 各题型表现
- 改进建议

## 可用的阅读材料

### Kindergarten (K年级)
1. **The Little Red Hen** (故事) - 小红母鸡的故事
2. **Colors in Nature** (科普) - 自然界的颜色

### Grade 1 (1年级)
1. **Sam and the Lost Puppy** (故事) - Sam和走失的小狗
2. **How Plants Grow** (科普) - 植物如何生长

### Grade 2 (2年级)
1. **The Friendship Garden** (故事) - 友谊花园
2. **The Water Cycle** (科普) - 水循环

### Grade 3 (3年级)
1. **The Mystery of the Missing Books** (故事) - 丢失书籍之谜
2. **Honeybees: Nature's Helpers** (科普) - 蜜蜂：自然的帮手

### Grade 4 (4年级)
1. **The Time Capsule Project** (故事) - 时间胶囊项目
2. **The Science of Earthquakes** (科普) - 地震科学

### Grade 5 (5年级)
1. **The Art of Perseverance** (故事) - 坚持的艺术
2. **The Revolutionary World of Renewable Energy** (科普) - 可再生能源的革命性世界

## 进度追踪功能

选择菜单选项2可以查看：
- 总共阅读的文章数
- 回答的总题数
- 总体准确率
- 各年级完成情况
- 最近的阅读记录
- 进步趋势分析

## 示例交互流程

```
> 1  (选择开始练习)
> 1  (选择Grade 1)
> 1  (选择第一篇文章 "Sam and the Lost Puppy")
[阅读文章内容...]
> Enter (继续到问题环节)

Question 1: What is the main idea of this story?
A. Sam found a lost puppy and helped find its owner
B. Sam got a new puppy
C. Sam walked home from school
D. A girl lost her puppy

> A  (你的答案)

✓ Excellent! That's correct!
Explanation: The story is about Sam finding...

[继续回答剩余问题...]

Session Summary:
Total Questions: 3
Correct Answers: 3
Accuracy: 100.0%

Performance Level: Excellent work!
```

## 快速演示版本

如果你想先快速预览所有功能而不交互，可以运行：

```bash
python demo.py
```

这会自动展示：
- 年级难度系统
- 所有可用文章
- 示例文章和问题
- 评分系统演示

## 数据存储

你的学习进度会自动保存在：
```
data/user_progress.json
```

可以随时查看历史记录和进步情况。

## 教育价值

这个工具设计用于：
- ✓ 提高阅读理解能力
- ✓ 扩展词汇量
- ✓ 培养批判性思维
- ✓ 鼓励独立阅读
- ✓ 提供结构化练习
- ✓ 追踪学习进度

---

**现在打开你的终端，运行 `python main.py` 开始体验吧！**
