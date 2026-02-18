#!/bin/bash
# 一键生成并发布博客

cd ~/blog  # 确保在正确目录

# 激活虚拟环境
source venv/bin/activate

# 生成静态网站
pelican content -s pelicanconf.py

# 复制到 Nginx 目录
cp -r output/* /var/www/blog/

# 退出虚拟环境
deactivate

echo "✅ 博客更新完成！"
