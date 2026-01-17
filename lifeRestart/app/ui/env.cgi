#!/bin/sh

# 添加 HTTP 响应头
echo "Content-Type: text/html; charset=utf-8"
echo ""

cat <<EOF
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
    <script>
      // 目标URL
      const targetURL ='https://liferestart.syaro.io/public/'

      // 尝试获取当前父级 iframe 元素
      let iframe = window.frameElement;
      if(iframe){
        iframe.src =targetURL;

        iframe.allow = "autoplay; fullscreen; keyboard-map *; pointer-lock";
        iframe.sandbox = "allow-pointer-lock allow-same-origin allow-scripts";

        iframe.scrolling = "no";   // 禁用滚动条
        iframe.frameBorder = "0"; // 兼容旧版
        iframe.setAttribute("allowfullscreen", "true");//全屏
      }else{
          //飞牛APP因跨源（cross-origin)获取不了，则直接跳转
          window.location.href = targetURL;
      }
    </script>
</body>
</html>
EOF
