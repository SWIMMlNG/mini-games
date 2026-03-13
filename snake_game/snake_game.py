"""
贪吃蛇游戏 - Snake Game
作者: swimming大人 & 丛雨酱
版本: 1.0
"""

import pygame
import random
import sys
from enum import Enum
from typing import List, Tuple

# 初始化 pygame
pygame.init()

# 游戏常量
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
GRID_SIZE = 20
GRID_WIDTH = WINDOW_WIDTH // GRID_SIZE
GRID_HEIGHT = WINDOW_HEIGHT // GRID_SIZE

# 颜色定义
COLOR_BACKGROUND = (20, 20, 20)
COLOR_GRID = (40, 40, 40)
COLOR_SNAKE_HEAD = (0, 200, 0)
COLOR_SNAKE_BODY = (0, 150, 0)
COLOR_SNAKE_OUTLINE = (0, 100, 0)
COLOR_FOOD = (200, 50, 50)
COLOR_FOOD_GLOW = (255, 100, 100)
COLOR_TEXT = (255, 255, 255)
COLOR_SCORE = (200, 200, 200)

# 方向枚举
class Direction(Enum):
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

class SnakeGame:
    def __init__(self):
        # 创建游戏窗口
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("🐍 贪吃蛇 - Snake Game")
        self.clock = pygame.time.Clock()
        self.font_large = pygame.font.Font(None, 72)
        self.font_medium = pygame.font.Font(None, 48)
        self.font_small = pygame.font.Font(None, 36)
        
        self.reset_game()
    
    def reset_game(self):
        """重置游戏状态"""
        # 初始化蛇的位置（屏幕中央）
        start_x = GRID_WIDTH // 2
        start_y = GRID_HEIGHT // 2
        self.snake: List[Tuple[int, int]] = [
            (start_x, start_y),
            (start_x - 1, start_y),
            (start_x - 2, start_y)
        ]
        self.direction = Direction.RIGHT
        self.next_direction = Direction.RIGHT
        self.score = 0
        self.game_over = False
        self.paused = False
        self.spawn_food()
        self.game_speed = 8  # 初始速度
    
    def spawn_food(self):
        """生成食物"""
        while True:
            self.food = (
                random.randint(0, GRID_WIDTH - 1),
                random.randint(0, GRID_HEIGHT - 1)
            )
            if self.food not in self.snake:
                break
    
    def handle_events(self):
        """处理输入事件"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            
            if event.type == pygame.KEYDOWN:
                # 暂停游戏
                if event.key == pygame.K_SPACE and not self.game_over:
                    self.paused = not self.paused
                
                # 重新开始
                if event.key == pygame.K_r and self.game_over:
                    self.reset_game()
                
                # 退出游戏
                if event.key == pygame.K_ESCAPE:
                    return False
                
                # 方向控制（防止180度转向）
                if not self.paused and not self.game_over:
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        if self.direction != Direction.DOWN:
                            self.next_direction = Direction.UP
                    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        if self.direction != Direction.UP:
                            self.next_direction = Direction.DOWN
                    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                        if self.direction != Direction.RIGHT:
                            self.next_direction = Direction.LEFT
                    elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                        if self.direction != Direction.LEFT:
                            self.next_direction = Direction.RIGHT
        
        return True
    
    def update(self):
        """更新游戏状态"""
        if self.paused or self.game_over:
            return
        
        self.direction = self.next_direction
        
        # 计算新头部位置
        head_x, head_y = self.snake[0]
        dir_x, dir_y = self.direction.value
        new_head = ((head_x + dir_x) % GRID_WIDTH, (head_y + dir_y) % GRID_HEIGHT)
        
        # 检查撞到自己
        if new_head in self.snake:
            self.game_over = True
            return
        
        # 移动蛇
        self.snake.insert(0, new_head)
        
        # 检查是否吃到食物
        if new_head == self.food:
            self.score += 10
            self.game_speed = min(8 + self.score // 50, 20)  # 随分数增加速度
            self.spawn_food()
        else:
            self.snake.pop()
    
    def draw_grid(self):
        """绘制网格背景"""
        for x in range(0, WINDOW_WIDTH, GRID_SIZE):
            pygame.draw.line(self.screen, COLOR_GRID, (x, 0), (x, WINDOW_HEIGHT))
        for y in range(0, WINDOW_HEIGHT, GRID_SIZE):
            pygame.draw.line(self.screen, COLOR_GRID, (0, y), (WINDOW_WIDTH, y))
    
    def draw_snake(self):
        """绘制蛇"""
        for i, segment in enumerate(self.snake):
            x = segment[0] * GRID_SIZE
            y = segment[1] * GRID_SIZE
            
            # 头部用亮绿色，身体用暗绿色
            if i == 0:
                color = COLOR_SNAKE_HEAD
            else:
                # 身体渐变效果
                gradient = max(0.5, 1 - i * 0.05)
                color = (
                    int(COLOR_SNAKE_BODY[0] * gradient),
                    int(COLOR_SNAKE_BODY[1] * gradient),
                    int(COLOR_SNAKE_BODY[2] * gradient)
                )
            
            # 绘制圆角矩形
            rect = pygame.Rect(x + 1, y + 1, GRID_SIZE - 2, GRID_SIZE - 2)
            pygame.draw.rect(self.screen, color, rect, border_radius=5)
            pygame.draw.rect(self.screen, COLOR_SNAKE_OUTLINE, rect, 1, border_radius=5)
            
            # 绘制眼睛（只在头部）
            if i == 0:
                self.draw_snake_eyes(x, y)
    
    def draw_snake_eyes(self, x, y):
        """绘制蛇的眼睛"""
        eye_size = 4
        eye_offset = 5
        
        # 根据方向确定眼睛位置
        if self.direction == Direction.RIGHT:
            left_eye = (x + 12, y + 5)
            right_eye = (x + 12, y + 15)
        elif self.direction == Direction.LEFT:
            left_eye = (x + 8, y + 5)
            right_eye = (x + 8, y + 15)
        elif self.direction == Direction.UP:
            left_eye = (x + 5, y + 8)
            right_eye = (x + 15, y + 8)
        else:  # DOWN
            left_eye = (x + 5, y + 12)
            right_eye = (x + 15, y + 12)
        
        pygame.draw.circle(self.screen, (255, 255, 255), left_eye, eye_size)
        pygame.draw.circle(self.screen, (255, 255, 255), right_eye, eye_size)
        pygame.draw.circle(self.screen, (0, 0, 0), left_eye, eye_size // 2)
        pygame.draw.circle(self.screen, (0, 0, 0), right_eye, eye_size // 2)
    
    def draw_food(self):
        """绘制食物（带发光效果）"""
        x = self.food[0] * GRID_SIZE + GRID_SIZE // 2
        y = self.food[1] * GRID_SIZE + GRID_SIZE // 2
        
        # 发光效果
        for radius in range(15, 5, -3):
            alpha = int(50 - radius * 2)
            glow_surface = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)
            pygame.draw.circle(glow_surface, (*COLOR_FOOD_GLOW, alpha), (radius, radius), radius)
            self.screen.blit(glow_surface, (x - radius, y - radius))
        
        # 食物本体
        pygame.draw.circle(self.screen, COLOR_FOOD, (x, y), 8)
        pygame.draw.circle(self.screen, (255, 200, 200), (x - 2, y - 2), 3)
    
    def draw_ui(self):
        """绘制游戏界面"""
        # 分数
        score_text = self.font_small.render(f"得分: {self.score}", True, COLOR_SCORE)
        self.screen.blit(score_text, (10, 10))
        
        # 速度
        speed_text = self.font_small.render(f"速度: {self.game_speed}", True, COLOR_SCORE)
        self.screen.blit(speed_text, (10, 45))
        
        # 长度
        length_text = self.font_small.render(f"长度: {len(self.snake)}", True, COLOR_SCORE)
        self.screen.blit(length_text, (10, 80))
        
        # 暂停提示
        if self.paused:
            self.draw_centered_text("游戏暂停", "按空格键继续", COLOR_TEXT)
        
        # 游戏结束画面
        if self.game_over:
            overlay = pygame.Surface((WINDOW_WIDTH, WINDOW_HEIGHT))
            overlay.set_alpha(180)
            overlay.fill((0, 0, 0))
            self.screen.blit(overlay, (0, 0))
            self.draw_centered_text("游戏结束!", f"最终得分: {self.score}", COLOR_TEXT, "按 R 重新开始")
    
    def draw_centered_text(self, main_text: str, sub_text: str, color: Tuple[int, int, int], hint_text: str = None):
        """绘制居中文本"""
        # 主标题
        main_surface = self.font_large.render(main_text, True, color)
        main_rect = main_surface.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 - 50))
        self.screen.blit(main_surface, main_rect)
        
        # 副标题
        sub_surface = self.font_medium.render(sub_text, True, color)
        sub_rect = sub_surface.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 20))
        self.screen.blit(sub_surface, sub_rect)
        
        # 提示文字
        if hint_text:
            hint_surface = self.font_small.render(hint_text, True, (200, 200, 200))
            hint_rect = hint_surface.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 80))
            self.screen.blit(hint_surface, hint_rect)
    
    def draw(self):
        """绘制游戏画面"""
        self.screen.fill(COLOR_BACKGROUND)
        self.draw_grid()
        self.draw_food()
        self.draw_snake()
        self.draw_ui()
        pygame.display.flip()
    
    def run(self):
        """游戏主循环"""
        running = True
        
        while running:
            running = self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(self.game_speed)
        
        pygame.quit()
        sys.exit()

def main():
    """主函数"""
    print("=" * 50)
    print("🐍 贪吃蛇游戏 - Snake Game")
    print("=" * 50)
    print("操作说明:")
    print("  ↑/W - 向上移动")
    print("  ↓/S - 向下移动")
    print("  ←/A - 向左移动")
    print("  →/D - 向右移动")
    print("  空格 - 暂停/继续")
    print("  R    - 重新开始（游戏结束后）")
    print("  ESC  - 退出游戏")
    print("=" * 50)
    
    game = SnakeGame()
    game.run()

if __name__ == "__main__":
    main()