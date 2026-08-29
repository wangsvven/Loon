#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
地质剖面图生成示例
展示如何使用 geological_profile 模块创建自定义地质剖面图
"""

from geological_profile import GeologicalProfile


def example_1_simple_profile():
    """示例1：简单的两层地质结构"""
    print("\n示例1: 生成简单两层地质剖面图...")
    
    profile = GeologicalProfile(title="某建筑工地地质勘探剖面")
    
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
    
    profile.generate_profile("example_1_simple.png")
    print("✓ 已生成: example_1_simple.png")


def example_2_multi_layer_profile():
    """示例2：复杂的多层地质结构"""
    print("\n示例2: 生成复杂多层地质剖面图...")
    
    profile = GeologicalProfile(title="深基坑工程地质勘探剖面")
    
    profile.add_layer(0.0, 1.2, "杂填土", "松散，含建筑垃圾，少量砖块碎片")
    profile.add_layer(1.2, 3.5, "粉质粘土", "可塑，稍湿，含少量铁锰质结核")
    profile.add_layer(3.5, 6.8, "细砂", "饱和，密实，灰色，局部夹薄层粘土")
    profile.add_layer(6.8, 10.0, "强风化花岗岩", "节理发育，岩芯破碎，呈块状")
    
    profile.generate_profile("example_2_multi_layer.png", figsize=(14, 12))
    print("✓ 已生成: example_2_multi_layer.png")


def example_3_detailed_profile():
    """示例3：详细的工程地质剖面"""
    print("\n示例3: 生成详细工程地质剖面图...")
    
    profile = GeologicalProfile(title="地铁隧道工程地质剖面")
    
    layers_data = [
        (0.0, 0.8, "人工填土", "杂色，松散，含大量建筑垃圾", "#CD853F"),
        (0.8, 2.5, "粉质粘土", "黄褐色，可塑，含少量铁锰质结核", "#D2B48C"),
        (2.5, 4.2, "淤泥质粘土", "灰黑色，流塑，含有机质，有腐臭味", "#696969"),
        (4.2, 7.8, "粉砂", "灰色，饱和，中密，局部夹薄层粘土", "#B8860B"),
        (7.8, 11.5, "中粗砂", "灰白色，饱和，密实，含砾石", "#A9A9A9"),
        (11.5, 15.0, "强风化泥岩", "灰黄色，节理裂隙发育，岩体破碎", "#8B7355"),
        (15.0, 20.0, "中风化泥岩", "灰色，岩质较硬，节理裂隙较发育", "#778899"),
    ]
    
    for depth_start, depth_end, rock_type, description, color in layers_data:
        profile.add_layer(depth_start, depth_end, rock_type, description, color)
    
    profile.generate_profile("example_3_detailed.png", figsize=(14, 16), dpi=200)
    print("✓ 已生成: example_3_detailed.png")


def example_4_custom_colors():
    """示例4：自定义颜色方案"""
    print("\n示例4: 使用自定义颜色方案...")
    
    profile = GeologicalProfile(title="海底隧道工程地质剖面")
    
    custom_colors = {
        "海底淤泥": "#2C3E50",
        "软塑粘土": "#34495E",
        "海相沉积砂层": "#5D6D7E",
        "风化基岩": "#7B7D7D",
        "完整基岩": "#95A5A6"
    }
    
    profile.add_layer(0.0, 3.0, "海底淤泥", "灰黑色，含有机质丰富，塑性高", custom_colors["海底淤泥"])
    profile.add_layer(3.0, 6.5, "软塑粘土", "深灰色，软塑，含贝壳碎片", custom_colors["软塑粘土"])
    profile.add_layer(6.5, 12.0, "海相沉积砂层", "灰色，中密-密实，含砾石", custom_colors["海相沉积砂层"])
    profile.add_layer(12.0, 18.0, "风化基岩", "灰白色，节理发育，岩体较破碎", custom_colors["风化基岩"])
    profile.add_layer(18.0, 25.0, "完整基岩", "灰色，坚硬，完整性好", custom_colors["完整基岩"])
    
    profile.generate_profile("example_4_custom_colors.png", figsize=(14, 14))
    print("✓ 已生成: example_4_custom_colors.png")


def example_5_thin_layers():
    """示例5：薄互层地质结构"""
    print("\n示例5: 生成薄互层地质剖面图...")
    
    profile = GeologicalProfile(title="沉积岩薄互层剖面")
    
    profile.add_layer(0.0, 0.5, "表土层", "腐殖质土，含植物根系")
    profile.add_layer(0.5, 1.0, "粘土层", "黄褐色，可塑")
    profile.add_layer(1.0, 1.3, "粉砂层", "灰色，湿润")
    profile.add_layer(1.3, 1.8, "粘土层", "灰色，软塑")
    profile.add_layer(1.8, 2.2, "细砂层", "黄灰色，稍密")
    profile.add_layer(2.2, 2.5, "粘土层", "深灰色，可塑")
    profile.add_layer(2.5, 3.0, "粉砂层", "灰色，中密")
    profile.add_layer(3.0, 4.0, "泥岩", "深灰色，层状构造")
    
    profile.generate_profile("example_5_thin_layers.png", figsize=(12, 12))
    print("✓ 已生成: example_5_thin_layers.png")


def main():
    """运行所有示例"""
    print("=" * 70)
    print("地质剖面图生成示例集")
    print("=" * 70)
    
    example_1_simple_profile()
    example_2_multi_layer_profile()
    example_3_detailed_profile()
    example_4_custom_colors()
    example_5_thin_layers()
    
    print("\n" + "=" * 70)
    print("所有示例已完成！")
    print("=" * 70)
    print("\n已生成以下文件：")
    print("  1. example_1_simple.png          - 简单两层结构")
    print("  2. example_2_multi_layer.png     - 复杂多层结构")
    print("  3. example_3_detailed.png        - 详细工程地质剖面")
    print("  4. example_4_custom_colors.png   - 自定义颜色方案")
    print("  5. example_5_thin_layers.png     - 薄互层结构")
    print("\n提示：可以编辑此脚本来创建您自己的地质剖面图！")


if __name__ == "__main__":
    main()
