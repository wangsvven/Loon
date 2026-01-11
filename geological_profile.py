#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
地质剖面图生成脚本
根据输入的地质层信息生成地质剖面简图，支持中文标注
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib import rcParams
import platform


def configure_chinese_font():
    """配置中文字体支持"""
    system = platform.system()
    
    if system == 'Windows':
        rcParams['font.sans-serif'] = ['SimSun', 'SimHei', 'Microsoft YaHei']
    elif system == 'Darwin':
        rcParams['font.sans-serif'] = ['Songti SC', 'STSong', 'Heiti SC', 'PingFang SC']
    else:
        rcParams['font.sans-serif'] = ['Noto Sans CJK SC', 'WenQuanYi Micro Hei', 'Droid Sans Fallback']
    
    rcParams['axes.unicode_minus'] = False


class GeologicalLayer:
    """地质层数据类"""
    
    def __init__(self, depth_start, depth_end, rock_type, description, color=None):
        """
        初始化地质层
        
        参数:
            depth_start: 起始深度(m)
            depth_end: 结束深度(m)
            rock_type: 岩石类型
            description: 特征描述
            color: 显示颜色(可选)
        """
        self.depth_start = depth_start
        self.depth_end = depth_end
        self.rock_type = rock_type
        self.description = description
        self.color = color
        self.thickness = depth_end - depth_start
    
    def __repr__(self):
        return f"GeologicalLayer({self.depth_start}-{self.depth_end}m, {self.rock_type})"


class GeologicalProfile:
    """地质剖面图生成器"""
    
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
    
    def __init__(self, title="地质剖面图"):
        """
        初始化地质剖面图生成器
        
        参数:
            title: 图表标题
        """
        self.title = title
        self.layers = []
        configure_chinese_font()
    
    def add_layer(self, depth_start, depth_end, rock_type, description, color=None):
        """
        添加地质层
        
        参数:
            depth_start: 起始深度(m)
            depth_end: 结束深度(m)
            rock_type: 岩石类型
            description: 特征描述
            color: 显示颜色(可选)
        """
        if color is None:
            color = self.DEFAULT_COLORS[len(self.layers) % len(self.DEFAULT_COLORS)]
        
        layer = GeologicalLayer(depth_start, depth_end, rock_type, description, color)
        self.layers.append(layer)
        return layer
    
    def generate_profile(self, output_file="geological_profile.png", figsize=(12, 10), dpi=150):
        """
        生成地质剖面图
        
        参数:
            output_file: 输出文件名
            figsize: 图表尺寸
            dpi: 图像分辨率
        """
        if not self.layers:
            print("警告：没有添加任何地质层数据")
            return
        
        self.layers.sort(key=lambda x: x.depth_start)
        
        max_depth = max(layer.depth_end for layer in self.layers)
        
        fig, ax = plt.subplots(figsize=figsize, dpi=dpi)
        
        profile_width = 4
        profile_x = 2
        
        for layer in self.layers:
            y_position = -layer.depth_start
            height = -(layer.depth_end - layer.depth_start)
            
            rect = patches.Rectangle(
                (profile_x, y_position),
                profile_width,
                height,
                linewidth=2,
                edgecolor='black',
                facecolor=layer.color,
                alpha=0.7
            )
            ax.add_patch(rect)
            
            ax.plot([profile_x - 0.3, profile_x], 
                   [-layer.depth_start, -layer.depth_start], 
                   'k-', linewidth=1.5)
            ax.plot([profile_x - 0.3, profile_x], 
                   [-layer.depth_end, -layer.depth_end], 
                   'k-', linewidth=1.5)
            
            ax.text(profile_x - 0.5, -layer.depth_start, 
                   f'{layer.depth_start:.1f}m', 
                   ha='right', va='center', fontsize=10, fontweight='bold')
            ax.text(profile_x - 0.5, -layer.depth_end, 
                   f'{layer.depth_end:.1f}m', 
                   ha='right', va='center', fontsize=10, fontweight='bold')
            
            layer_center = -(layer.depth_start + layer.depth_end) / 2
            label_x = profile_x + profile_width + 0.5
            
            ax.text(label_x, layer_center, 
                   f'{layer.rock_type}', 
                   ha='left', va='center', fontsize=11, fontweight='bold',
                   bbox=dict(boxstyle='round,pad=0.5', facecolor='white', alpha=0.8))
            
            if layer.description:
                desc_lines = self._wrap_text(layer.description, 30)
                desc_y = layer_center - 0.15
                for i, line in enumerate(desc_lines):
                    ax.text(label_x, desc_y - i * 0.15, 
                           line, 
                           ha='left', va='top', fontsize=9, 
                           style='italic', color='#333333')
        
        ax.plot([profile_x - 0.3, profile_x - 0.3], 
               [0, -max_depth], 
               'k-', linewidth=2)
        
        ax.set_xlim(0, 10)
        ax.set_ylim(-max_depth - 0.5, 0.5)
        ax.set_aspect('equal')
        
        ax.set_title(self.title, fontsize=16, fontweight='bold', pad=20)
        ax.set_ylabel('深度 (m)', fontsize=12, fontweight='bold')
        
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['bottom'].set_visible(False)
        ax.spines['left'].set_visible(False)
        ax.set_xticks([])
        ax.set_yticks([])
        
        ax.axhline(y=0, color='brown', linestyle='--', linewidth=1.5, alpha=0.5)
        ax.text(profile_x - 0.5, 0.2, '地表', ha='right', va='bottom', 
               fontsize=11, fontweight='bold', color='brown')
        
        plt.tight_layout()
        plt.savefig(output_file, bbox_inches='tight', dpi=dpi)
        print(f"地质剖面图已生成: {output_file}")
        plt.close()
    
    def _wrap_text(self, text, max_length):
        """文本自动换行"""
        if len(text) <= max_length:
            return [text]
        
        lines = []
        current_line = ""
        
        for char in text:
            if len(current_line) >= max_length and char in ['，', '。', '、', ' ', ',', '.']:
                lines.append(current_line + char)
                current_line = ""
            else:
                current_line += char
        
        if current_line:
            lines.append(current_line)
        
        return lines


def create_sample_profile():
    """创建示例地质剖面图"""
    profile = GeologicalProfile(title="地质剖面图示例")
    
    profile.add_layer(
        depth_start=0.0,
        depth_end=0.6,
        rock_type="粉质黏土",
        description="表层为植物层",
        color="#D2B48C"
    )
    
    profile.add_layer(
        depth_start=0.6,
        depth_end=2.0,
        rock_type="灰岩",
        description="粘土矿物，薄-中厚层状，节理裂隙较发育，岩体破碎，呈碎块状（中风化）",
        color="#A9A9A9"
    )
    
    profile.generate_profile(output_file="geological_profile.png")


def main():
    """主函数"""
    print("=" * 60)
    print("地质剖面图生成工具")
    print("=" * 60)
    
    create_sample_profile()
    
    print("\n自定义示例：")
    custom_profile = GeologicalProfile(title="某工程地质勘探剖面")
    
    custom_profile.add_layer(0.0, 1.2, "杂填土", "松散，含建筑垃圾")
    custom_profile.add_layer(1.2, 3.5, "粉质粘土", "可塑，稍湿")
    custom_profile.add_layer(3.5, 6.8, "细砂", "饱和，密实")
    custom_profile.add_layer(6.8, 10.0, "强风化花岗岩", "节理发育，岩芯破碎")
    
    custom_profile.generate_profile(output_file="custom_geological_profile.png")
    
    print("\n完成！已生成以下文件：")
    print("1. geological_profile.png - 基于提供的测试数据")
    print("2. custom_geological_profile.png - 自定义多层示例")


if __name__ == "__main__":
    main()
