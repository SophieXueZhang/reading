# 📚 Reading Comprehension Tool - Web版使用指南

## 🚀 快速启动

### 1. 安装依赖
```bash
pip install -r requirements.txt
```

### 2. 启动Web界面
```bash
streamlit run app.py
```

### 3. 访问应用
浏览器会自动打开，或手动访问：
- **本地**: http://localhost:8501
- **网络**: http://192.168.1.113:8501

## 🎯 功能介绍

### 🏠 主页面
- **统计卡片**: 显示12篇文章、8种题型、进度追踪
- **快速数据**: 你的阅读统计一目了然
- **学习亮点**: 展示核心学习内容

### 📖 阅读练习（核心功能）

#### 步骤1: 选择年级
点击对应的年级卡片：
- **Kindergarten (K)** - 简单句子，基础词汇
- **Grade 1** - 短篇故事
- **Grade 2** - 发展性故事
- **Grade 3** - 多角色故事
- **Grade 4** - 复杂叙述
- **Grade 5** - 抽象概念

#### 步骤2: 选择文章
每个年级有2篇精选文章：
- 故事类（Story）
- 科普类（Informational）

#### 步骤3: 阅读文章
- 文章显示在美观的卡片中
- 适当的行距和字体便于阅读
- 无干扰的阅读体验

#### 步骤4: 回答问题
- 每篇文章3-5个选择题
- 单选按钮交互，操作简单
- 显示题型标签（Main Idea, Inference等）
- 实时保存你的答案

#### 步骤5: 查看结果
- **正确答案**: 绿色背景 ✓
- **错误答案**: 红色背景 ✗
- **详细解释**: 每题都有解答说明
- **统计数据**:
  - 总题数
  - 正确数
  - 准确率百分比
  - 等级评价

### 📊 进度报告

查看你的学习历程：
- **总体统计**:
  - 阅读文章数
  - 回答问题数
  - 正确答案数
  - 总体准确率

- **分级进度**: 每个年级完成的文章数

- **最近会话**:
  - 文章标题
  - 准确率
  - 正误比例

- **进步趋势**: 智能分析你的提升情况

### ❓ 帮助页面

- 详细使用说明
- 题型解释
- 学习建议
- 成功技巧

## 🎨 界面亮点

### 视觉设计
- **渐变色卡片**: 现代化的紫色渐变主题
- **响应式布局**: 适配桌面、平板、手机
- **清晰的色彩编码**:
  - 蓝色: 主题色
  - 绿色: 正确答案
  - 红色: 错误答案
  - 紫色: 统计卡片

### 交互特性
- **即时反馈**: 无需等待，立即显示结果
- **自动保存**: 学习进度自动记录
- **流畅导航**: 侧边栏快速切换页面
- **友好提示**: 引导式操作说明

## 📝 使用示例

### 完整学习流程

1. **首次使用**:
   ```
   主页 → 了解功能 → 开始阅读
   ```

2. **选择内容**:
   ```
   选择年级 → Grade 1 → "Sam and the Lost Puppy"
   ```

3. **阅读答题**:
   ```
   仔细阅读文章 → 回答3个问题 → 提交答案
   ```

4. **查看结果**:
   ```
   准确率: 100% → 查看解析 → 继续练习
   ```

5. **追踪进度**:
   ```
   进度报告 → 查看统计 → 发现提升
   ```

## 🎓 学习建议

### 对于学生
- ✅ 每天练习15-20分钟
- ✅ 从自己年级或低一级开始
- ✅ 仔细阅读，不要着急
- ✅ 重读不理解的部分
- ✅ 查看错题解析，理解原因

### 对于家长/老师
- ✅ 陪同低年级学生使用
- ✅ 讨论答案和解析
- ✅ 关注进度趋势
- ✅ 鼓励坚持练习
- ✅ 庆祝每一次进步

## 📦 可用内容

### 全部12篇文章

**Kindergarten (K)**
- 🦆 The Little Red Hen (故事)
- 🌈 Colors in Nature (科普)

**Grade 1**
- 🐶 Sam and the Lost Puppy (故事)
- 🌱 How Plants Grow (科普)

**Grade 2**
- 🌻 The Friendship Garden (故事)
- 💧 The Water Cycle (科普)

**Grade 3**
- 📚 The Mystery of the Missing Books (故事)
- 🐝 Honeybees: Nature's Helpers (科普)

**Grade 4**
- ⏰ The Time Capsule Project (故事)
- 🌍 The Science of Earthquakes (科普)

**Grade 5**
- 🎯 The Art of Perseverance (故事)
- ⚡ The Revolutionary World of Renewable Energy (科普)

## 🔧 技术细节

### 技术栈
- **前端**: Streamlit (Python Web框架)
- **后端逻辑**: Python
- **数据存储**: JSON文件
- **界面**: 自定义CSS + Streamlit组件

### 文件结构
```
reading/
├── app.py                    # Streamlit Web应用 ⭐
├── main.py                   # 命令行版本
├── demo.py                   # 快速演示
├── requirements.txt          # 依赖列表
├── .env                      # 配置文件
├── src/
│   ├── reading_passages.py  # 文章数据库
│   ├── questions.py         # 题库
│   ├── evaluator.py         # 评分系统
│   ├── progress_tracker.py  # 进度追踪
│   └── difficulty_levels.py # 年级管理
└── data/
    └── user_progress.json   # 用户数据
```

## 🚀 高级功能

### 进度追踪算法
- 自动计算准确率趋势
- 识别薄弱题型
- 生成个性化建议

### 自适应难度
- 根据年级调整文章复杂度
- 词汇量范围控制
- 问题类型分级

## 💡 快捷键

在Streamlit界面中：
- `R` - 重新运行应用
- `C` - 清除缓存
- `?` - 显示快捷键帮助

## 🌐 访问方式

### 本地开发
```bash
streamlit run app.py
```
默认端口: 8501

### 自定义端口
```bash
streamlit run app.py --server.port 8080
```

### 网络访问
同一WiFi下的其他设备可以通过Network URL访问

## 📱 移动端体验

Streamlit响应式设计，完美支持：
- 📱 iPhone/Android手机
- 📱 iPad/平板电脑
- 💻 笔记本电脑
- 🖥️ 桌面显示器

## 🎉 开始使用

**现在就启动应用开始学习吧！**

```bash
cd /Users/pc/Documents/cursor/reading
streamlit run app.py
```

然后在浏览器中打开: **http://localhost:8501**

Happy Reading! 📖✨
