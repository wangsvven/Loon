#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
地质剖面图模块测试
简单的功能测试，确保模块正常工作
"""

import os
import sys
from geological_profile import GeologicalProfile, GeologicalLayer


def test_geological_layer():
    """测试 GeologicalLayer 类"""
    print("测试 GeologicalLayer 类...")
    
    layer = GeologicalLayer(0.0, 1.5, "粉质黏土", "表层土壤", "#D2B48C")
    
    assert layer.depth_start == 0.0
    assert layer.depth_end == 1.5
    assert layer.rock_type == "粉质黏土"
    assert layer.description == "表层土壤"
    assert layer.color == "#D2B48C"
    assert layer.thickness == 1.5
    
    print("  ✓ GeologicalLayer 创建成功")
    print("  ✓ 属性访问正常")
    print("  ✓ 厚度计算正确")


def test_geological_profile_creation():
    """测试 GeologicalProfile 创建"""
    print("\n测试 GeologicalProfile 创建...")
    
    profile = GeologicalProfile(title="测试剖面")
    
    assert profile.title == "测试剖面"
    assert len(profile.layers) == 0
    
    print("  ✓ GeologicalProfile 创建成功")
    print("  ✓ 初始状态正确")


def test_add_layer():
    """测试添加地质层"""
    print("\n测试添加地质层...")
    
    profile = GeologicalProfile()
    
    layer1 = profile.add_layer(0.0, 1.0, "表土", "植物层")
    layer2 = profile.add_layer(1.0, 3.0, "粘土", "可塑")
    
    assert len(profile.layers) == 2
    assert profile.layers[0] == layer1
    assert profile.layers[1] == layer2
    assert profile.layers[0].rock_type == "表土"
    assert profile.layers[1].rock_type == "粘土"
    
    print("  ✓ 地质层添加成功")
    print("  ✓ 层数统计正确")
    print("  ✓ 数据存储正确")


def test_generate_profile():
    """测试生成剖面图"""
    print("\n测试生成剖面图...")
    
    profile = GeologicalProfile(title="测试生成")
    profile.add_layer(0.0, 1.0, "粉质黏土", "表层")
    profile.add_layer(1.0, 2.5, "灰岩", "中风化")
    
    output_file = "test_output.png"
    
    if os.path.exists(output_file):
        os.remove(output_file)
    
    profile.generate_profile(output_file=output_file, figsize=(10, 8))
    
    assert os.path.exists(output_file), "输出文件未生成"
    assert os.path.getsize(output_file) > 0, "输出文件大小为0"
    
    os.remove(output_file)
    
    print("  ✓ 剖面图生成成功")
    print("  ✓ 文件保存正常")
    print("  ✓ 文件大小有效")


def test_color_assignment():
    """测试颜色分配"""
    print("\n测试颜色分配...")
    
    profile = GeologicalProfile()
    
    layer1 = profile.add_layer(0.0, 1.0, "土层1", "描述1")
    layer2 = profile.add_layer(1.0, 2.0, "土层2", "描述2")
    layer3 = profile.add_layer(2.0, 3.0, "土层3", "描述3", color="#FF0000")
    
    assert layer1.color is not None, "默认颜色未分配"
    assert layer2.color is not None, "默认颜色未分配"
    assert layer3.color == "#FF0000", "自定义颜色未应用"
    
    print("  ✓ 默认颜色自动分配")
    print("  ✓ 自定义颜色正确应用")


def test_layer_sorting():
    """测试地层排序"""
    print("\n测试地层排序...")
    
    profile = GeologicalProfile()
    
    profile.add_layer(2.0, 4.0, "层3", "深层")
    profile.add_layer(0.0, 1.0, "层1", "表层")
    profile.add_layer(1.0, 2.0, "层2", "中层")
    
    output_file = "test_sorting.png"
    profile.generate_profile(output_file=output_file)
    
    sorted_layers = profile.layers
    assert sorted_layers[0].depth_start == 0.0
    assert sorted_layers[1].depth_start == 1.0
    assert sorted_layers[2].depth_start == 2.0
    
    if os.path.exists(output_file):
        os.remove(output_file)
    
    print("  ✓ 地层按深度正确排序")


def test_text_wrapping():
    """测试文本换行功能"""
    print("\n测试文本换行...")
    
    profile = GeologicalProfile()
    
    long_description = "这是一个非常长的描述文本，用于测试自动换行功能是否正常工作，应该被正确地分割成多行显示"
    short_description = "短文本"
    
    wrapped_long = profile._wrap_text(long_description, 20)
    wrapped_short = profile._wrap_text(short_description, 20)
    
    assert len(wrapped_long) > 1, "长文本未被换行"
    assert len(wrapped_short) == 1, "短文本不应该被换行"
    
    print("  ✓ 长文本正确换行")
    print("  ✓ 短文本保持完整")


def run_all_tests():
    """运行所有测试"""
    print("=" * 70)
    print("地质剖面图模块功能测试")
    print("=" * 70)
    
    try:
        test_geological_layer()
        test_geological_profile_creation()
        test_add_layer()
        test_generate_profile()
        test_color_assignment()
        test_layer_sorting()
        test_text_wrapping()
        
        print("\n" + "=" * 70)
        print("所有测试通过！✓")
        print("=" * 70)
        return True
        
    except AssertionError as e:
        print(f"\n✗ 测试失败: {e}")
        return False
    except Exception as e:
        print(f"\n✗ 测试出错: {e}")
        import traceback
        traceback.print_exc()
        return False


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
