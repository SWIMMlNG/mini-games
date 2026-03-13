# 🐍 贪吃蛇游戏 - Snake Game

一个精美的贪吃蛇游戏，支持 **桌面版(Python)** 和 **网页版(HTML5)**！

## 📁 文件说明

```
snake_game/
├── snake_game.py           # Python 桌面版 (Pygame)
├── index.html              # 网页版 (HTML5 + Canvas)
├── run_snake.sh            # 桌面版启动脚本
└── README.md               # 使用说明
```

## 🎮 游戏特性

- ✨ 精美的视觉效果（渐变蛇身、发光食物、网格背景）
- 👀 蛇头有可爱的眼睛，会随方向转动
- 📈 速度随分数增加而加快
- ⏸️ 支持暂停功能
- 🔄 穿墙设计（从一边出去会从另一边进来）
- 📱 网页版支持手机触摸控制

---

## 🖥️ 桌面版 (Python)

### 运行方式

```bash
# 方式一：直接运行
python3 snake_game.py

# 方式二：使用启动脚本
./run_snake.sh
```

### 操作说明

| 按键 | 功能 |
|------|------|
| ↑ / W | 向上移动 |
| ↓ / S | 向下移动 |
| ← / A | 向左移动 |
| → / D | 向右移动 |
| 空格 | 暂停/继续 |
| R | 重新开始（游戏结束后） |
| ESC | 退出游戏 |

---

## 🌐 网页版 (HTML5)

### 运行方式

#### 方式一：VS Code Live Server（推荐）
1. 在 VS Code 中打开 `index.html`
2. 点击右下角的 "Go Live" 按钮
3. 浏览器会自动打开游戏页面

#### 方式二：直接打开
用浏览器直接打开 `index.html` 文件

#### 方式三：Python 简易服务器
```bash
cd /home/swimming/workspace/snake_game
python3 -m http.server 8080
# 然后浏览器访问 http://localhost:8080
```

### 操作说明

**键盘控制：**
- 方向键或 WASD 控制移动
- 空格键暂停/继续
- R键重新开始

**手机控制：**
- 使用屏幕上的方向按钮

---

## 🛠️ 技术栈

### 桌面版
- Python 3
- Pygame 2.6.1

### 网页版
- HTML5
- CSS3 (渐变、动画、响应式)
- JavaScript (Canvas API)

---

## 🎯 游戏目标

控制贪吃蛇吃掉红色的食物，每吃一个食物：
- 得分 +10
- 蛇身变长
- 速度加快

**注意：** 不要撞到自己的尾巴！

---

**作者:** swimming大人 & 丛雨酱 🔪🌸

**版本:** 1.0