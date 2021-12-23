# -*- coding: utf-8 -*-
"""
@Author: 阳哥
@出品：Python数据之道
@Homepage: liyangbit.com
"""

from manim import *
import pandas as pd

# * 设置默认参数
config.background_color = "#002e47"  # 272C3C  002e47
Text.set_default(font="Alibaba PuHuiTi")
GRAY_LEMON = "#c5c5c5"
BLUE_LIGHT_LEMON = "#deeaf6"
BLACK_LIGHT_LEMON = "#595959"
GREEN_LEMON = "#33ff00"
RED_LEMON = "#ff3300"

BLUE_L_BG = "#002e47"
BLUE_L_A = "#03436D"
BLUE_L_B = "#4b81ac"
BLUE_L_C = "#b3cbe4"
BLUE_L = BLUE_L_B
ORANGE_L_A = "#d66101"
ORANGE_L_B = "#FF9D28"
ORANGE_L = ORANGE_L_B


class BGBlue(Scene):
    def construct(self):
        self.add(FullScreenRectangle(color=BLUE_L_BG).set_fill(BLUE_L_BG, 1))
        self.wait(0.5)


class WaterMark(Scene):
    def construct(self):
        text_lst = [
            Text("Python数据之道", font_size=40, color=GRAY, fill_opacity=0.15)
            for i in range(3)
        ]
        text_group = Group(*text_lst)
        text_group.rotate(45 * DEGREES)
        text_group[0].to_corner(UL, buff=1)
        text_group[2].to_corner(DR, buff=1)
        self.add(text_group)
        # self.wait()


# manim -pql --disable_caching christmas-intro.py DemoSquare


class DemoSquare(Scene):
    def construct(self):
        WaterMark.construct(self)
        r = 1
        sq = Square(
            side_length=2 * r,
            color=GREEN_LEMON,
            fill_color=GREEN_LEMON,
            fill_opacity=1,
        )
        self.add(sq)


class DemoCircle(Scene):
    def construct(self):
        WaterMark.construct(self)
        r = 1
        circle = Circle(
            radius=r,
            color=GREEN_LEMON,
            fill_color=GREEN_LEMON,
            fill_opacity=1,
        )
        self.play(Create(circle))
        self.wait()


class Tree01(Scene):
    def construct(self):
        WaterMark.construct(self)
        stars_all = Group()
        buff = 0.5
        for i in range(5):
            stars_lst = [
                Star(color=GREEN_LEMON, fill_color=GREEN_LEMON, fill_opacity=1).scale(
                    0.25
                )
                for j in range(2 * i + 1)
            ]
            stars_group = Group(*stars_lst).arrange(RIGHT)
            stars_group.to_edge(UP, buff=buff)
            stars_all.add(stars_group)
            # self.add(stars_group)
            for star in stars_group:
                self.add(star)
                self.wait(0.1)
            buff += 0.7

        rect = Rectangle(
            width=1.5, height=3.5, color=RED_LEMON, fill_color=RED_LEMON, fill_opacity=1
        )
        rect.next_to(stars_all, DOWN, buff=0.2)
        self.play(DrawBorderThenFill(rect), run_time=3)
        self.wait()


class Tree02(Scene):
    def construct(self):
        WaterMark.construct(self)
        r = 0.1
        buff_gap = 0.4
        time_wait = 0.1
        circle = Circle(radius=r, color=RED_LEMON, fill_color=RED_LEMON, fill_opacity=1)
        circle.to_edge(UP, buff=buff_gap)
        self.add(circle)
        self.wait(time_wait)

        def draw_tree(n, buff=1):
            shapes = Group()
            for i in range(4):
                sq_lst = [
                    Square(
                        side_length=2 * r,
                        color=GREEN_LEMON,
                        fill_color=GREEN_LEMON,
                        fill_opacity=1,
                    )
                    for j in range(2 * (i + n) + 1)
                ]
                sq_group = Group(*sq_lst).arrange(RIGHT)
                sq_group.to_edge(UP, buff=buff)
                if i == 2:
                    sq_side_lst = [
                        Square(
                            side_length=2 * r,
                            color=YELLOW,
                            fill_color=YELLOW,
                            fill_opacity=1,
                        )
                        for j in range(2)
                    ]
                    sq_side_group = Group(*sq_side_lst)
                    sq_side_group[0].next_to(sq_group, LEFT)
                    sq_side_group[1].next_to(sq_group, RIGHT)
                    self.add(sq_side_group[0])
                    self.wait(time_wait)
                    for sq in sq_group:
                        self.add(sq)
                        self.wait(time_wait)
                    self.add(sq_side_group[1])
                    self.wait(time_wait)
                    shapes.add(sq_side_group[0])
                    shapes.add(sq_group)
                    shapes.add(sq_side_group[1])
                elif i == 3:
                    circle_side_lst = [
                        Circle(
                            radius=r,
                            color=RED_LEMON,
                            fill_color=RED_LEMON,
                            fill_opacity=1,
                        )
                        for j in range(2)
                    ]
                    circle_side_group = Group(*circle_side_lst)
                    circle_side_group[0].next_to(sq_group, LEFT)
                    circle_side_group[1].next_to(sq_group, RIGHT)
                    self.add(circle_side_group[0])
                    self.wait(time_wait)
                    for sq in sq_group:
                        self.add(sq)
                        self.wait(time_wait)
                    self.add(circle_side_group[1])
                    self.wait(time_wait)
                    shapes.add(circle_side_group[0])
                    shapes.add(sq_group)
                    shapes.add(circle_side_group[1])

                else:
                    shapes.add(sq_group)
                    for sq in sq_group:
                        self.add(sq)
                        self.wait(time_wait)

                buff += buff_gap
            return shapes

        tree_caps = Group()
        for n in range(3):
            tree_cap = draw_tree(n, buff=buff_gap * 2 + buff_gap * n * 4)
            tree_caps.add(tree_cap)

        tree_root = Group()
        for i in range(3):
            sq_lst = [
                Square(
                    side_length=2 * r,
                    color=RED_LEMON,
                    fill_color=RED_LEMON,
                    fill_opacity=1,
                )
                for j in range(5)
            ]
            sq_group = Group(*sq_lst).arrange(RIGHT)
            tree_root.add(sq_group)
            # sq_group.to_edge(UP, buff=buff)
        for i in range(1, len(tree_root)):
            tree_root[i].next_to(tree_root[i - 1], DOWN, buff=buff_gap / 2)

        tree_root.next_to(tree_caps, DOWN, buff=buff_gap / 2)

        for i in range(len(tree_root)):
            for j in range(len(tree_root[i])):
                self.add(tree_root[i][j])
                self.wait(time_wait)
        self.wait()

        tree = Group(circle, tree_caps, tree_root)
        # self.play(tree.animate.rotate(-60*DEGREES),run_time=4)
        # self.play(tree.animate.rotate(120*DEGREES),run_time=4)
        # self.play(tree.animate.rotate(-60*DEGREES),run_time=4)
        self.play(tree.animate.move_to(ORIGIN).scale(0.5), run_time=4)
        self.play(tree.animate.scale(2), run_time=4)


class Tree03(Scene):
    def construct(self):
        WaterMark.construct(self)
        time_wait = 0.1
        star = Star(color=YELLOW, fill_color=YELLOW, fill_opacity=1).scale(0.5)
        star.to_edge(UP, buff=0.5)
        # self.add(star)
        self.play(Write(star))
        self.wait(time_wait)
        # tri = Triangle(color=GREEN_LEMON,fill_color=GREEN_LEMON, fill_opacity=1)
        tri = Polygon(
            [-5, 1.5, 0],
            [-2, 1.5, 0],
            [-3.5, 3, 0],
            color=GREEN_LEMON,
            fill_color=GREEN_LEMON,
            fill_opacity=1,
        ).scale(0.8)
        tri.next_to(star, DOWN, buff=-0.2)
        # self.add(tri)
        self.play(Write(tri))
        self.wait(time_wait)
        tri_2 = tri.copy().scale(1.4)
        tri_2.next_to(tri, DOWN, buff=-0.5)
        self.play(Write(tri_2))
        self.wait(time_wait)
        tri_3 = tri.copy().scale(2)
        tri_3.next_to(tri_2, DOWN, buff=-0.8)
        self.play(Write(tri_3))
        self.wait(time_wait)

        rect = Rectangle(
            width=1.2, height=2.6, color=RED_LEMON, fill_color=RED_LEMON, fill_opacity=1
        )
        rect.next_to(tri_3, DOWN, buff=0.05)
        self.play(DrawBorderThenFill(rect), run_time=3)
        self.wait()

        dots = Group(
            *[Dot(radius=0.2, color=BLUE_L_C, fill_opacity=1) for i in range(3)]
        )
        dots[0].move_to(tri.get_center()).shift(DOWN * 0.2)
        dots[1].move_to(tri_2.get_center()).shift(DOWN * 0.2)
        dots[2].move_to(tri_3.get_center()).shift(DOWN * 0.2)
        self.add(dots)
        self.wait()

        colors = [BLUE_L_C, YELLOW, RED_LEMON]

        for i in range(20):
            dots[0].set_color(colors[i % 3])
            self.wait(time_wait)
            dots[1].set_color(colors[(i + 1) % 3])
            self.wait(time_wait)
            dots[2].set_color(colors[(i + 2) % 3])
            self.wait(time_wait)


class AllScene(Scene):
    def construct(self):
        scene_list = [Tree01, Tree02, Tree03]
        for i in range(len(scene_list)):
            if i < len(scene_list) - 1:
                scene_list[i].construct(self)
                BGBlue.construct(self)
            else:
                scene_list[i].construct(self)
