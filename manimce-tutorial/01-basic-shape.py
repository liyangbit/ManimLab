# -*- coding: utf-8 -*-
"""
@Author: 阳哥
@出品：Python数据之道
@Homepage: liyangbit.com
"""

# Manim Community version 0.14.0

# from telnetlib import DO
from manim import *
import pandas as pd
import numpy as np


# * 设置默认参数
config.background_color = "#002e47"  # 272C3C  002e47
Text.set_default(font="Alibaba PuHuiTi")
GRAY_LEMON = "#c5c5c5"
BLUE_LEMON = "#0071c1"
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

# 设置切换背景
class BGBlue(Scene):
    def construct(self):
        self.add(FullScreenRectangle(color=BLUE_L_BG).set_fill(BLUE_L_BG, 1))
        self.wait(0.5)

# 设置水印
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


# 正方形
# manim -pql manimce-intro-01.py DemoSquare
class DemoSquare(Scene):
    def construct(self):
        WaterMark.construct(self)
        r = 1
        sq1 = Square(
            side_length=2 * r,
            color=BLUE,
        )
        sq1.to_corner(UL,buff=2)
        self.add(sq1)
        self.wait()

        sq2 = Square(
            side_length=2 * r,
            color=BLUE,
            stroke_width=10,  # 设置边框线的粗细
        )
        sq2.next_to(sq1,RIGHT,buff=1)
        self.add(sq2)
        self.wait()

        sq3 = Square(
            side_length=2 * r,
            color=BLUE,
            fill_color=ORANGE,  # 设置填充颜色
            fill_opacity=0.5,  # 设置透明度
        )
        sq3.next_to(sq2,RIGHT,buff=1)
        self.add(sq3)
        self.wait()

        # 形状大小变换
        sq4 = sq1.copy()
        sq4.scale(0.6) # 缩小到 60%
        sq4.next_to(sq1,DOWN,buff=0.5)
        self.add(sq4)
        self.wait()

        # 形状旋转
        sq5 = sq2.copy()
        sq5.rotate(45*DEGREES)  # 旋转45度
        sq5.next_to(sq2,DOWN,buff=0.5)
        self.add(sq5)
        self.wait()

# 点
class DemoDot(Scene):
    def construct(self):
        WaterMark.construct(self)
        g = Group(
            # 点
            Dot(color=PINK),
            AnnotationDot(stroke_color=YELLOW, fill_color=BLUE,fill_opacity=1),
            # 带文字标签的点
            LabeledDot(Tex("2022", color=RED)),
            LabeledDot(MathTex("a", color=GREEN)),
            LabeledDot(Text("Python数据之道", color=BLUE)).scale(0.3),
            LabeledDot("Lemon"),
        )
        g.arrange(RIGHT,buff=0.5).scale(1.5)
        g[:2].move_to(UP*1.5)
        g[2:].next_to(g[:2],DOWN,buff=1)
        for shape in g:
            self.add(shape)
            self.wait(0.5)

# 线
class DemoLine(Scene):
    def construct(self):
        WaterMark.construct(self)
        g = Group(
            # 线
            Line(0.5*LEFT,0.5*RIGHT,color=YELLOW),
            # 虚线
            DashedLine(0.5*LEFT,0.5*RIGHT,color=TEAL),
            # 箭头
            Arrow(color=BLUE), 
            Arrow(color= BLUE, tip_shape=ArrowCircleFilledTip), #  ArrowCircleTip
            Arrow(color= BLUE, tip_shape=ArrowSquareTip),# ArrowSquareFilledTip
            # 双箭头
            DoubleArrow(color=BLUE),
            # 弯曲的箭头
            CurvedArrow(LEFT,RIGHT,angle=90*DEGREES,color= BLUE), 
        )
        g.arrange(RIGHT,buff=0.5)
        g[:3].move_to(UP*1.5)
        g[3:].next_to(g[:3],DOWN,buff=1)
        for shape in g:
            self.add(shape)
            self.wait(0.5)

# 圆形
class DemoCircle(Scene):
    def construct(self):
        WaterMark.construct(self)
        g = Group(
            # 圆形
            Circle(radius=0.8,color=YELLOW,fill_color=BLUE,fill_opacity=1),
            # 圆环
            Annulus(inner_radius=0.7, outer_radius=1,fill_color= DARK_BLUE, stroke_color=YELLOW, stroke_width=4), 
            # 椭圆
            Ellipse(color= BLUE),
            # 扇形
            Sector(inner_radius=0.7, outer_radius=1,fill_color= BLUE, stroke_color=YELLOW, stroke_width=4),
            # 弧形
            Arc(radius=1.3, start_angle=-PI/8, angle=PI,color= BLUE),
            ArcBetweenPoints(start=2 * RIGHT, end=2*LEFT, stroke_color=BLUE) ,
        )
        g.arrange(RIGHT,buff=0.5)
        g[:3].move_to(UP*1.5)
        g[3:].next_to(g[:3],DOWN,buff=1)
        for shape in g:
            self.add(shape)
            self.wait(0.5)

# 矩形
class DemoRect(Scene):
    def construct(self):
        WaterMark.construct(self)
        g = Group(
            # 矩形
            Rectangle(width=1,height=0.6,color=BLUE,fill_color=ORANGE,fill_opacity=1),
            Rectangle(width=1,height=0.6,color=BLUE,grid_xstep=0.5,grid_ystep=0.2),
            # 圆角矩形
            RoundedRectangle(corner_radius=0.3,width=1,height=0.6,fill_color=PURPLE,fill_opacity=1),
            # 正方形
            Square(
            side_length=1,
            color=BLUE,
            fill_color=ORANGE,  # 设置填充颜色
            fill_opacity=0.5,  # 设置透明度
            ),
        )
        g.arrange(RIGHT,buff=0.5).scale(2)
        for shape in g:
            self.add(shape)
            self.wait(0.5)


# 多边形
class DemoPolygon(Scene):
    def construct(self):
        WaterMark.construct(self)
        g = Group(
            # 正三角形
            Triangle(radius=2,color=BLUE),
            # 三角形
            Polygon([-5, 1.5, 0], [-2, 1.5, 0], [-3.5, -2, 0]),
            # 多边形
            Polygon([-5, 1.5, 0], [-2, 1.5, 0], [-2.5, -2, 0], [-4.5, -1.5, 0]),
            #正多边形
            RegularPolygon(n=6,color=BLUE),
            # 星型
            Star(color=BLUE),
            #多边形
            Polygram(
                [[0, 2, 0], [-np.sqrt(3), -1, 0], [np.sqrt(3), -1, 0]],
                [[-np.sqrt(3), 1, 0], [0, -2, 0], [np.sqrt(3), 1, 0]],),
            RegularPolygram(num_vertices = 7),
            RegularPolygram(5, radius=1),
        )
        g.arrange(RIGHT,buff=0.5).scale(0.7)
        g[:4].move_to(UP*1.5)
        g[4:].next_to(g[:3],DOWN,buff=1)
        for shape in g:
            self.add(shape)
            self.wait(0.5)

# 符号
class DemoCross(Scene):
    def construct(self):
        WaterMark.construct(self)

        # 十字叉
        cross = Cross(stroke_color = BLUE,stroke_width=20).scale(0.8)
        cross.to_corner(UL,buff=2)
        self.add(cross)
        self.wait(0.5)
        # 大括号
        br1 = Brace(Line(LEFT,RIGHT),color= BLUE)
        br1.next_to(cross,RIGHT,buff=0.5)
        self.add(br1)
        self.wait(0.5)

        # 带文字的大括号
        line=Line(LEFT,RIGHT) 
        br2= BraceLabel(line, text= "14cm", color= YELLOW, buff=0.1) 
        br2.submobjects[1].set_color(BLUE) 
        self.add(VGroup(line,br2).next_to(br1,RIGHT,buff=0.5))
        self.wait(0.5)

        # 带弧度的大括号
        arc = Arc(radius=1,start_angle=0,angle=3*PI/4) 
        br3 = ArcBrace(arc).set_color(BLUE)
        self.add(VGroup(arc,br3).next_to(VGroup(line,br2),RIGHT,buff=0.5))
        # self.add(arc,br3)
        self.wait(0.5)
