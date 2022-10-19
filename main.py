import pygame
from pygame.locals import *
import sys


def main():
    pygame.init()
    FONT_PATH = 'fonts/ipag.ttc'
    font = pygame.font.Font(FONT_PATH, 30)
    w = 600
    h = 600
    screen = pygame.display.set_mode((w, h))
    pygame.display.set_caption("moving dog")
    img_dog = pygame.image.load("images/dog.png")
    img_dog = pygame.transform.scale(img_dog, (100, 100))
    rect = img_dog.get_rect()
    rect.center = (w / 2, h / 2)

    while True:
        screen.fill((255, 255, 255))
        text = font.render("1. 画面をクリックしてください。", True, (0, 0, 0))
        screen.blit(text, [20, 100])
        text2 = font.render("2. キーボードの十字キーで操作してください。", True, (0, 0, 0))
        screen.blit(text2, [20, 130])
        screen.blit(img_dog, rect)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # キーを押したとき
            if event.type == KEYDOWN:
                # ESCキーなら終了
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                # 矢印キーなら円の中心座標を矢印の方向に移動
                if event.key == K_LEFT:
                    rect.move_ip(-10, 0)
                if event.key == K_RIGHT:
                    rect.move_ip(10, 0)
                if event.key == K_UP:
                    rect.move_ip(0, -10)
                if event.key == K_DOWN:
                    rect.move_ip(0, 10)


if __name__ == "__main__":
    main()
