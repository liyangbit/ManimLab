# -*- coding: utf-8 -*-
"""
@Author: 阳哥
@出品：Python数据之道
@Homepage: liyangbit.com
"""

# Manim Community version 0.14

# from click import style
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
        WaterMark.construct(self)
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

# * 纯文本
# manim -pql manimce-02-text.py Demo1
class Demo1(Scene):
    def construct(self):
        WaterMark.construct(self)
        code_str_1 = """
        Text("Python数据之道")
        """
        code1 = Code(
            code=code_str_1,
            tab_width=4,
            background="window",
            language="Python",
            font="Monospace",
            insert_line_no=False,  # 是否显示代码行数
            style='monokai',
        )

        code1.to_edge(LEFT,buff=0.5)
        arr = Arrow(
            stroke_width=20,color=GRAY,
            buff=0.5,
            max_stroke_width_to_length_ratio=6,
            )
        arr.next_to(code1,RIGHT,buff=0.5)

        t1 = Text("Python数据之道")
        t1.next_to(arr,RIGHT,buff=0.5)

        self.add(code1)
        self.wait()
        self.add(arr)
        self.play(Write(t1))
        self.wait()

# 设置文本大小
class Demo2(Scene):
    def construct(self):
        WaterMark.construct(self)
        s = "Python数据之道"
        t1 = Text(s)
        t1.to_edge(UP,buff=0.5)
        t2 = Text(s).scale(2)
        t2.next_to(t1,DOWN)
        t3 = Text(s).set_width(10)
        t3.next_to(t2,DOWN)
        t4 = Text(s,font_size=40)
        t4.next_to(t3,DOWN)       
        self.add(t1)
        self.play(Write(t2))
        self.play(Create(t3))
        self.play(Write(t4))
        self.wait()

# 设置文本颜色
class Demo3(Scene):
    def construct(self):
        WaterMark.construct(self)
        s = "Python数据之道"
        t1 = Text(s,color=BLUE)
        t1.to_edge(UP,buff=2)
        t2 = Text("一份价值，一份收获",gradient=[BLUE,YELLOW,RED]).next_to(t1,DOWN)
        t3 = Text("Hello World",gradient=[BLUE,YELLOW,RED]).next_to(t2,DOWN)
        t4 = Text("@Python数据之道",gradient=[BLUE,YELLOW,RED],font_size=30,fill_opacity=0.8)
        t4.next_to(t3,DOWN)
        t5 = Text("Python数据之道",gradient=[BLUE,YELLOW,RED]).next_to(t4,DOWN)
        # 当英文和汉字混合时， 当前的manim社区版，使用 gradient 时会出现 bug
        self.add(t1)
        self.play(Write(t2))
        self.play(Create(t3))
        self.play(Write(t4))
        self.play(Write(t5))
        self.wait()


# 设置字体样式
class Demo4(Scene):
    def construct(self):
        WaterMark.construct(self)
        t1 = Text("Python数据之道",font="Alibaba PuHuiTi")
        t1.to_edge(UP,buff=0.5)
        t2 = Text("Python数据之道",color=BLUE,font="Times")
        t2.next_to(t1,DOWN)
        t3 = Text("Python数据之道", weight=BOLD)
        t3.next_to(t2,DOWN)
        t4 = Text("Python数据之道", slant=ITALIC)
        t4.next_to(t3,DOWN)
        t5 = Text("Python数据之道", fill_opacity=0.5)
        t5.next_to(t4,DOWN)
        t6 = Text("Hello\nPython", line_spacing=0.5)
        t6.next_to(t5,DOWN,buff=1).shift(LEFT)
        t7 = Text("Hello\nPython", line_spacing=2)
        t7.next_to(t6,RIGHT,buff=1)
        self.add(t1)
        self.play(Write(t2))
        self.play(Write(t3))
        self.play(Write(t4))
        self.play(Write(t5))
        self.add(t6,t7)
        self.wait()

# 个性化设置部分文本的样式
class Demo5(Scene):
    def construct(self):
        WaterMark.construct(self)
        t1 = Text("Python数据之道",t2c={"Python":RED,'[7:9]':YELLOW})
        t1.to_edge(UP,buff=0.5)
        t2 = Text("Python数据之道",t2s={"Python":ITALIC})
        t2.next_to(t1,DOWN)
        t3 = Text("Python数据之道", t2w={"Python":BOLD})
        t3.next_to(t2,DOWN)
        t4 = Text("Python数据之道", t2f={"Python":"Times"})
        t4.next_to(t3,DOWN)
        t5 = Text(
            "Hello,PyDataLab", 
            t2g={
                'PyData':[BLUE,YELLOW,RED],
                # 'offset':"1",
            },
            )
        t5.next_to(t4,DOWN)
        t6 = Text(
            "Hello,Python数据之道", 
            t2g={
                'Python':[BLUE,YELLOW,RED],
            },
            )
        t6.next_to(t5,DOWN)
        t7 = Text(
            "一份价值，一份收获", 
            t2g={
                '一份价值':[BLUE,YELLOW,RED],
            },
            )
        t7.next_to(t6,DOWN)
        # "t2c"、"t2s"、"t2w"、"t2g"、"t2f" 参数设置，可以直接是 字符串，或者是 字符串的位置切片
        self.add(t1)
        self.play(Write(t2))
        self.play(Write(t3))
        self.play(Write(t4))
        self.play(Write(t5))
        self.play(Write(t6))
        self.play(Write(t7))
        self.wait()


# 应用案例
class Demo6(Scene):
    def construct(self):
        WaterMark.construct(self)
        text1 = Text(
            'Google',
            t2c={'[:1]': '#3174f0', '[1:2]': '#e53125',
                 '[2:3]': '#fbb003', '[3:4]': '#3174f0',
                 '[4:5]': '#269a43', '[5:]': '#e53125'}, font_size=58).scale(3)
        self.play(Write(text1),run_time=3)
        self.wait()
        self.play(FadeOut(text1))
        t2 = Text('Google',font_size=120)
        colors = [BLUE, ORANGE, PURPLE, PINK, TEAL,DARK_BROWN, RED,LIGHT_BROWN,GOLD,BLUE_L_C,ORANGE_L_A,PURPLE_E]*10
        # for i in range(len(t2)):
        #     t2[i].set_color(colors[i])
        for letter in t2:
            letter.set_color(np.random.choice(colors,size=1))
        self.play(Write(t2),run_time=3)
        self.wait()


# * 标记 文本

#  PangoMarkup is a small markup language like html and it helps you avoid using “range of characters” while coloring or styling a piece a Text. You can use this language with MarkupText.


class Markup01(Scene):
    def construct(self):
        WaterMark.construct(self)
        t1 = MarkupText('<span foreground="yellow" size="x-large">Hello, </span> <i>Welcome to </i>ValueLab !"')
        t1.to_edge(UP,buff=2)
        self.add(t1)
        self.wait()

        t2 = MarkupText('<span foreground="yellow" size="x-large">一份价值，</span> 一份 <i>收获</i>!"')
        t2.next_to(t1,DOWN,buff=1)
        self.add(t2)
        self.wait()

# 样式设置，加粗、下划线、斜体等
class Markup02(Scene):
    def construct(self):
        WaterMark.construct(self)
        text1 = MarkupText("<b>Hello</b> <i>welcome to</i> <b><i>ValueLab</i></b>")
        text2 = MarkupText("<s>foo</s> <u>bar</u> <big>big</big> <small>small</small>")
        text3 = MarkupText("H<sub>2</sub>O and H<sub>3</sub>O<sup>+</sup>")
        text4 = MarkupText("type <tt>help</tt> for help")
        text5 = MarkupText(
            '<span underline="double">foo</span> <span underline="error">bar</span>'
        )
        group = VGroup(text1, text2, text3, text4, text5).arrange(DOWN)
        self.add(group)

# 颜色设置，设置不同的颜色、渐变色等
class Markup03(Scene):
    def construct(self):
        text1 = MarkupText(
            f'all in red <span fgcolor="{YELLOW}">except this</span>', color=RED
        )
        text2 = MarkupText("nice gradient", gradient=(BLUE, GREEN))
        text3 = MarkupText(
            'nice <gradient from="RED" to="YELLOW">intermediate</gradient> gradient',
            gradient=(BLUE, GREEN),
        )
        text4 = MarkupText(
            'fl ligature <gradient from="RED" to="YELLOW">causing trouble</gradient> here'
        )
        text5 = MarkupText(
            'fl ligature <gradient from="RED" to="YELLOW" offset="1">defeated</gradient> with offset'
        )
        text6 = MarkupText(
            'fl ligature <gradient from="RED" to="YELLOW" offset="1">floating</gradient> inside'
        )
        text7 = MarkupText(
            'fl ligature <gradient from="RED" to="YELLOW" offset="1,1">floating</gradient> inside'
        )
        group = VGroup(text1, text2, text3, text4, text5, text6, text7).arrange(DOWN)
        self.add(group)

# 文字对齐
class Markup05(Scene):
    def construct(self):
        WaterMark.construct(self)
        ipsum_text = (
            "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
            "Praesent feugiat metus sit amet iaculis pulvinar. Nulla posuere "
            "quam a ex aliquam, eleifend consectetur tellus viverra. Aliquam "
            "fermentum interdum justo, nec rutrum elit pretium ac. Nam quis "
            "leo pulvinar, dignissim est at, venenatis nisi. Quisque mattis "
            "dolor ut euismod hendrerit. Nullam eu ante sollicitudin, commodo "
            "risus a, vehicula odio. Nam urna tortor, aliquam a nibh eu, commodo "
            "imperdiet arcu. Donec tincidunt commodo enim a tincidunt."
        )
        justified_text = MarkupText(ipsum_text, justify=True).scale(0.4)
        not_justified_text = MarkupText(ipsum_text, justify=False).scale(0.4)
        just_title = Title("Justified")
        njust_title = Title("Not Justified")
        self.add(njust_title, not_justified_text)
        self.play(
            Transform(
                not_justified_text,
                justified_text,
            ),
            Transform(
                njust_title,
                just_title,
            ),
            run_time=2,
        )
        self.wait(1)

# * Latex 文本

# latex 文本，需要你的电脑环境中已经安装了 latex的相关软件和支持工具

class DemoTex01(Scene):
    def construct(self):
        WaterMark.construct(self)
        tex1 = Tex(r"\LaTeX", font_size=144)
        tex1.to_edge(UP,buff=1)
        self.add(tex1)
        self.wait()

        tex2 = Tex(r'$x^2 + y^2 = z^2$', font_size=144)
        tex2.next_to(tex1,DOWN,buff=0.5)
        tex3 = MathTex(r'x^2 + y^2 = z^2', font_size=144,color=BLUE)
        tex3.next_to(tex2,DOWN,buff=0.5)
        self.add(tex2)
        self.wait()
        self.add(tex3)
        self.wait()

# 使用 latex 工具包
class DemoTex02(Scene):
    def construct(self):
        WaterMark.construct(self)
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{mathrsfs}")
        tex = Tex(r'$\mathscr{H} \rightarrow \mathbb{H}$}', tex_template=myTemplate, font_size=144)
        self.add(tex)

# 数学公式的颜色设置
class DemoTex03(Scene):
    def construct(self):
        WaterMark.construct(self)
        eq1 = MathTex(
            r"e^x = x^0 + x^1 + \frac{1}{2} x^2 + \frac{1}{6} x^3 + \cdots + \frac{1}{n!} x^n + \cdots"
        )
        eq1.scale(1.2)
        eq1.set_color_by_tex("x", YELLOW)
        eq1.to_edge(UP,buff=2)
        self.add(eq1)
        self.wait()
        # self.play(FadeOut(eq1))

        eq2 = MathTex(
            r"e^x = x^0 + x^1 + \frac{1}{2} x^2 + \frac{1}{6} x^3 + \cdots + \frac{1}{n!} x^n + \cdots",
            substrings_to_isolate="x",
        )
        eq2.scale(1.2)
        eq2.set_color_by_tex("x", RED)
        eq2.next_to(eq1,DOWN,buff=1)
        self.add(eq2)
        self.wait()

class DemoTex04(Scene):
    def construct(self):
        WaterMark.construct(self)
        equations = VGroup(
            MathTex(
                r"1.01^{365} = 37.8",
                # size=80,
            ),
            MathTex(
                r"1.00^{365} = 1.00",
                # size=80,
            ),
            MathTex(
                r"0.99^{365} = 0.03",
                # size=80,
            ),
        )

        # 设置宽度
        # equations.set_width(FRAME_WIDTH-4)
        equations.set_width(8)

        for equation in equations:
            equation.set_color_by_tex_to_color_map({
                "1.01": BLUE,
                "0.99": RED,
            })

        equations.arrange(DOWN, buff=0.7, aligned_edge=LEFT)
        self.play(Write(equations[0]))
        self.wait()

        self.play(Write(equations[2]))
        self.wait()

        self.play(Write(equations[1]))
        self.wait()

        self.play(equations[1].animate.set_opacity(0.2))
        self.wait()


# tex 模板应用
class DemoTex05(Scene):
    def construct(self):
        WaterMark.construct(self)
        tex1 = Tex(r'$x^2 + y^2 = z^2$', tex_template=TexFontTemplates.french_cursive, font_size=144)
        tex1.to_edge(UP,buff=1)
        self.add(tex1)
        self.wait()

        tex2 = Tex(r'Hello 你好 \LaTeX', tex_template=TexTemplateLibrary.ctex, font_size=144)
        tex2.next_to(tex1,DOWN,buff=0.5)
        self.add(tex2)
        self.wait()

# 公式换行
class DemoTex06(Scene):
    def construct(self):
        WaterMark.construct(self)
        tex1 = MathTex(
            r'f(x) &= 3 + 2 + 1\\ &= 5 + 1 \\ &= 6', 
            font_size=96,
        )
        self.add(tex1)
        self.wait()
        self.play(FadeOut(tex1))

        tex2 = MathTex(
            r'f(x) &= 3 + 2 + 1\\ &= 5 + 1 \\ &= 6', 
            font_size=96,
            substrings_to_isolate=['5','3'],
        )
        tex2.set_color_by_tex_to_color_map({
                "5": BLUE,
                "3": RED,
            })
        self.add(tex2)
        self.wait()

# Title 对象应用
class DemoTex07(Scene):
    def construct(self):
        WaterMark.construct(self)
        title1 = Title("Hello,title")
        self.add(title1)
        self.wait()
        self.play(FadeOut(title1))

        # 使用 “Title” 对象，当有中文时，需要设置中文字体模板（电脑中需要安装了 ctex）
        title2 = Title("你好,title",tex_template=TexTemplateLibrary.ctex)
        self.add(title2)
        self.wait()

# 列表类型的文本
class DemoTex08(Scene):
    def construct(self):
        blist = BulletedList("Python", "Java", "C++", height=2, width=2)
        blist.set_color_by_tex("Python", RED)
        blist.set_color_by_tex("Java", GREEN)
        blist.set_color_by_tex("C++", BLUE)
        self.add(blist)


# 代码文本，代码高亮设置
# https://docs.manim.community/en/stable/reference/manim.mobject.svg.code_mobject.Code.html#manim.mobject.svg.code_mobject.Code
"""
style支持的样式
['default', 'emacs', 'friendly', 'colorful', 'autumn', 'murphy', 'manni', 'monokai', 'perldoc', 'pastie', 'borland', 'trac', 'native', 'fruity', 'bw', 'vim', 'vs', 'tango', 'rrt', 'xcode', 'igor', 'paraiso-light', 'paraiso-dark', 'lovelace', 'algol', 'algol_nu', 'arduino', 'rainbow_dash', 'abap', 'solarized-dark', 'solarized-light', 'sas', 'stata', 'stata-light', 'stata-dark', 'inkpot']
"""


class Code1(Scene):
    def construct(self):
        WaterMark.construct(self)
        code_str_1 = """
        def quickSort(Array):  
            n = len(Array)
            if n <= 1:
                return Array
            baseline = Array[0]
            left = [Array[i] for i in range(1, len(Array)) if Array[i] < baseline] 
            right = [Array[i] for i in range(1, len(Array)) if Array[i] >= baseline]
            return quickSort(left) + [baseline] + quickSort(right)
        """
        code1 = Code(
            code=code_str_1,
            tab_width=4,
            background="window",
            language="Python",
            font="Monospace",
            insert_line_no=False,  # 是否显示代码行数
            style='monokai',
        )

        code1.scale(0.8).to_edge(UP,buff=1)

        self.play(Write(code1))
        self.wait()

        code2 = Code(
            code=code_str_1,
            tab_width=4,
            background="rectangle", # rectangle , window
            language="Python",
            font="Monospace",
            insert_line_no=True,  # 是否显示代码行数
            style='solarized-light',
            # line_spacing=0.3,
        )

        code2.scale(0.8)
        code2.next_to(code1,DOWN,buff=0.5)

        self.play(Write(code2))
        self.wait()

