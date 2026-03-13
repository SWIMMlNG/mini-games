# 🎮 小游戏合集 - Mini Games Collection

一个精美的网页小游戏合集，随时随地畅玩！支持单人、多人联机等多种游戏模式。

🔗 **在线试玩：** https://SWIMMlNG.github.io/mini-games

---

## 🎯 游戏列表

### 🐍 [贪吃蛇](snake_game/) 
- **类型：** HTML5 / Python
- **玩法：** 经典贪吃蛇，吃掉食物变长，不要撞到自己
- **特色：** 支持网页版和Python桌面版，精美视觉效果，蛇头有可爱眼睛

### 🃏 [记忆翻牌](memory_game/)
- **类型：** HTML5 / 益智
- **玩法：** 翻开卡片找到相同配对，考验记忆力
- **特色：** 计步计时，配对动画效果

### 🧱 [打砖块](breakout/)
- **类型：** HTML5 / 动作
- **玩法：** 控制挡板反弹小球，击碎所有砖块
- **特色：** 粒子爆炸效果，多关卡难度递增

### 🎮 [俄罗斯方块](tetris/)
- **类型：** HTML5 / 经典
- **玩法：** 旋转、移动、消除方块，挑战高分
- **特色：** 幽灵预览，等级系统，侧边栏显示下一个方块

### ✈️ [飞机大战](airplane/)
- **类型：** HTML5 / 射击
- **玩法：** 驾驶战机消灭敌机，躲避弹幕
- **特色：** 波次系统，血条显示，粒子爆炸效果

### 🌲 [生存聊天室](survival_chat/) ⭐ 多人联机
- **类型：** HTML5 / 多人联机
- **玩法：** 多人在线生存，收集资源，实时聊天
- **特色：**
  - 🔥 实时多人联机（基于 Firebase）
  - 💬 类微信聊天框，实时消息同步
  - 🌲 饥荒风格森林地图
  - 👥 看到其他在线玩家位置
  - 🎮 WASD/方向键移动

---

## 🚀 本地运行

### 方式一：Python 简易服务器
```bash
cd mini-games
python3 -m http.server 8080
# 浏览器访问 http://localhost:8080
```

### 方式二：VS Code Live Server
1. 在 VS Code 中打开项目
2. 安装 Live Server 插件
3. 点击 "Go Live" 按钮

---

## 🛠️ 技术栈

- **HTML5** - 页面结构
- **CSS3** - 渐变、动画、响应式布局
- **JavaScript** - 游戏逻辑、Canvas API
- **Firebase** - 实时数据库（多人联机游戏）
- **Python** - Pygame（贪吃蛇桌面版）

---

## 📁 项目结构

```
mini-games/
├── index.html                  # 游戏大厅首页
├── README.md                   # 项目说明
├── snake_game/                 # 🐍 贪吃蛇
│   ├── index.html              # 网页版
│   ├── snake_game.py           # Python桌面版
│   └── run_snake.sh            # 启动脚本
├── memory_game/                # 🃏 记忆翻牌
│   └── index.html
├── breakout/                   # 🧱 打砖块
│   └── index.html
├── tetris/                     # 🎮 俄罗斯方块
│   └── index.html
├── airplane/                   # ✈️ 飞机大战
│   └── index.html
└── survival_chat/              # 🌲 生存聊天室（多人联机）
    └── index.html
```

---

## 🎮 添加新游戏

1. 在根目录创建新文件夹（如 `my_game/`）
2. 添加 `index.html` 作为游戏入口
3. 在根目录 `index.html` 中添加游戏卡片
4. 提交并推送到 GitHub

### 游戏开发规范
- 保持统一的深色主题风格
- 添加返回大厅按钮
- 支持响应式布局（手机/电脑）
- 游戏说明清晰易懂

---

## 🔧 多人联机游戏配置

生存聊天室使用 Firebase Realtime Database 实现多人联机。

如需部署自己的版本：
1. 创建 Firebase 项目：https://console.firebase.google.com/
2. 创建 Realtime Database（测试模式）
3. 替换 `survival_chat/index.html` 中的 `firebaseConfig`
4. 重新部署

---

## 👨‍💻 作者

**SWIMMlNG** & **丛雨酱** 🔪🌸

---

## 📄 许可证

MIT License - 自由使用和修改

---

*更多游戏开发中，敬请期待！* 🎮✨