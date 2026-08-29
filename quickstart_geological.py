#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
地质剖面图快速入门脚本
用于快速验证安装和生成第一个地质剖面图
"""

from geological_profile import GeologicalProfile


def main():
    print("=" * 60)
    print("地质剖面图快速入门")
    print("=" * 60)
    print("\n正在生成您的第一个地质剖面图...\n")
    
    profile = GeologicalProfile(title="我的第一个地质剖面图")
    
    print("添加地质层数据：")
    print("  - 0.0-0.6m: 粉质黏土（表层为植物层）")
    profile.add_layer(
        depth_start=0.0,
        depth_end=0.6,
        rock_type="粉质黏土",
        description="表层为植物层"
    )
    
    print("  - 0.6-2.0m: 灰岩（中风化）")
    profile.add_layer(
        depth_start=0.6,
        depth_end=2.0,
        rock_type="灰岩",
        description="粘土矿物，薄-中厚层状，节理裂隙较发育，岩体破碎，呈碎块状（中风化）"
    )
    
    print("\n生成剖面图...")
    profile.generate_profile("my_first_geological_profile.png")
    
    print("\n" + "=" * 60)
    print("成功！ ✓")
    print("=" * 60)
    print("\n已生成文件: my_first_geological_profile.png")
    print("\n接下来您可以：")
    print("  1. 查看生成的图片文件")
    print("  2. 运行 python3 geological_profile_example.py 查看更多示例")
    print("  3. 阅读 GEOLOGICAL_PROFILE_README.md 了解详细用法")
    print("  4. 修改此脚本来创建您自己的地质剖面图")
    print("\n" + "=" * 60)


if __name__ == "__main__":
    main()
