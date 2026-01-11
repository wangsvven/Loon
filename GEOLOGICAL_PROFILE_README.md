# 地质剖面图生成工具

这个Python脚本用于根据输入的地质层信息生成地质剖面简图，支持中文标注。

## 功能特点

- ✅ 支持多层地质结构可视化
- ✅ 自动配置中文字体（宋体/黑体等）
- ✅ 为每个地层分配不同颜色
- ✅ 深度标尺自动生成
- ✅ 支持岩石类型和特征描述标注
- ✅ 输出高清PNG图片

## 依赖安装

### 1. 安装Python依赖

```bash
pip install matplotlib
```

或者在系统包管理环境中：

```bash
pip install matplotlib --break-system-packages
```

### 2. 安装中文字体（Linux系统）

```bash
sudo apt-get update
sudo apt-get install fonts-noto-cjk fonts-wqy-zenhei
fc-cache -f -v
```

### 3. 清除matplotlib字体缓存（如果中文显示不正常）

```bash
rm -rf ~/.cache/matplotlib
```

## 使用方法

### 方式一：运行示例脚本

直接运行脚本会生成两个示例地质剖面图：

```bash
python3 geological_profile.py
```

生成的文件：
- `geological_profile.png` - 基于用户提供的测试数据
- `custom_geological_profile.png` - 多层地质结构示例

### 方式二：在代码中使用

```python
from geological_profile import GeologicalProfile

# 创建地质剖面图对象
profile = GeologicalProfile(title="某工程地质勘探剖面")

# 添加地质层
profile.add_layer(
    depth_start=0.0,
    depth_end=0.6,
    rock_type="粉质黏土",
    description="表层为植物层",
    color="#D2B48C"  # 可选：自定义颜色
)

profile.add_layer(
    depth_start=0.6,
    depth_end=2.0,
    rock_type="灰岩",
    description="粘土矿物，薄-中厚层状，节理裂隙较发育，岩体破碎，呈碎块状（中风化）"
)

# 生成图片
profile.generate_profile(
    output_file="my_profile.png",
    figsize=(12, 10),
    dpi=150
)
```

## API文档

### GeologicalProfile 类

#### 初始化

```python
GeologicalProfile(title="地质剖面图")
```

**参数：**
- `title` (str): 图表标题

#### 方法：add_layer()

```python
add_layer(depth_start, depth_end, rock_type, description, color=None)
```

**参数：**
- `depth_start` (float): 起始深度（米）
- `depth_end` (float): 结束深度（米）
- `rock_type` (str): 岩石类型
- `description` (str): 特征描述
- `color` (str, 可选): 十六进制颜色代码，例如 "#D2B48C"

#### 方法：generate_profile()

```python
generate_profile(output_file="geological_profile.png", figsize=(12, 10), dpi=150)
```

**参数：**
- `output_file` (str): 输出文件路径
- `figsize` (tuple): 图表尺寸（宽，高）
- `dpi` (int): 图像分辨率

## 示例数据

脚本包含的测试数据：

### 示例1：简单两层结构

```
0.0-0.6m  粉质黏土：表层为植物层
0.6-2.0m  灰岩：粘土矿物，薄-中厚层状，节理裂隙较发育，岩体破碎，呈碎块状（中风化）
```

### 示例2：复杂多层结构

```
0.0-1.2m   杂填土：松散，含建筑垃圾
1.2-3.5m   粉质粘土：可塑，稍湿
3.5-6.8m   细砂：饱和，密实
6.8-10.0m  强风化花岗岩：节理发育，岩芯破碎
```

## 自定义颜色方案

脚本提供了默认的8种地质层颜色：

```python
DEFAULT_COLORS = [
    '#D2B48C',  # 棕褐色
    '#A9A9A9',  # 深灰色
    '#8B7355',  # 棕色
    '#B8860B',  # 暗金黄色
    '#778899',  # 灰石色
    '#696969',  # 暗灰色
    '#CD853F',  # 秘鲁色
    '#808000',  # 橄榄色
]
```

如果需要自定义颜色，可以在调用 `add_layer()` 时指定 `color` 参数。

## 字体配置

脚本会根据操作系统自动选择合适的中文字体：

- **Windows**: SimSun（宋体）, SimHei（黑体）, Microsoft YaHei（微软雅黑）
- **macOS**: Songti SC, STSong, Heiti SC, PingFang SC
- **Linux**: Noto Sans CJK SC, WenQuanYi Micro Hei, Droid Sans Fallback

## 输出效果

生成的地质剖面图包含：

1. **深度标尺**：左侧显示每层的起止深度
2. **地层块体**：不同颜色的矩形表示不同地层
3. **岩石类型**：右侧醒目标注
4. **特征描述**：详细的地质特征说明
5. **地表标线**：顶部虚线标记地表位置

## 注意事项

1. 深度单位统一使用米（m）
2. 地层深度从上到下递增
3. 脚本会自动按深度排序地层
4. 描述文本支持自动换行（超过30个字符）
5. 如果不指定颜色，脚本会自动循环使用默认颜色方案

## 故障排除

### 问题1：中文显示为方块

**解决方案：**
```bash
# 安装中文字体
sudo apt-get install fonts-noto-cjk
# 清除matplotlib缓存
rm -rf ~/.cache/matplotlib
```

### 问题2：ModuleNotFoundError: No module named 'matplotlib'

**解决方案：**
```bash
pip install matplotlib
```

### 问题3：图片无法保存

**解决方案：**
- 检查输出路径是否有写入权限
- 确保磁盘空间充足
- 检查文件名是否合法

## 技术细节

- **绘图库**：Matplotlib 3.x
- **Python版本**：3.6+
- **图像格式**：PNG（默认），也支持其他格式（如JPG, PDF, SVG）
- **默认DPI**：150（适合打印和屏幕显示）

## 扩展建议

可以根据需要扩展脚本功能：

1. 支持读取CSV/Excel文件批量导入地层数据
2. 添加地下水位线标记
3. 添加钻孔编号和坐标信息
4. 支持导出PDF报告
5. 添加标准图例
6. 支持多个钻孔横向对比

## 许可证

本脚本仅供学习和研究使用。

## 版本历史

- v1.0 (2025-01-11): 初始版本
  - 支持基本地质剖面图绘制
  - 中文字体自动配置
  - 可自定义颜色和图表参数
