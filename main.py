import csv
import os
import random
import shutil
import img2pdf
import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image
from word_search_generator import WordSearch
from glob import glob

WIDTH, HEIGHT = 816, 1056
MARGIN_PER = 8
WHITE, BLACK = (255, 255, 255), (0, 0, 0)
H_MARGIN = int(WIDTH / 100) * MARGIN_PER
V_MARGIN = int(HEIGHT / 100) * MARGIN_PER
normal_page_pos = [(74, 160), (119.2, 160), (164.4, 160), (209.60000000000002, 160), (254.8, 160), (300.0, 160),
                   (345.2, 160), (390.4, 160), (435.59999999999997, 160), (480.79999999999995, 160), (526.0, 160),
                   (571.2, 160), (616.4000000000001, 160), (661.6000000000001, 160), (706.8000000000002, 160),
                   (74, 193.06666666666666), (119.2, 193.06666666666666), (164.4, 193.06666666666666),
                   (209.60000000000002, 193.06666666666666), (254.8, 193.06666666666666), (300.0, 193.06666666666666),
                   (345.2, 193.06666666666666), (390.4, 193.06666666666666), (435.59999999999997, 193.06666666666666),
                   (480.79999999999995, 193.06666666666666), (526.0, 193.06666666666666), (571.2, 193.06666666666666),
                   (616.4000000000001, 193.06666666666666), (661.6000000000001, 193.06666666666666),
                   (706.8000000000002, 193.06666666666666), (74, 226.13333333333333), (119.2, 226.13333333333333),
                   (164.4, 226.13333333333333), (209.60000000000002, 226.13333333333333), (254.8, 226.13333333333333),
                   (300.0, 226.13333333333333), (345.2, 226.13333333333333), (390.4, 226.13333333333333),
                   (435.59999999999997, 226.13333333333333), (480.79999999999995, 226.13333333333333),
                   (526.0, 226.13333333333333), (571.2, 226.13333333333333), (616.4000000000001, 226.13333333333333),
                   (661.6000000000001, 226.13333333333333), (706.8000000000002, 226.13333333333333), (74, 259.2),
                   (119.2, 259.2), (164.4, 259.2), (209.60000000000002, 259.2), (254.8, 259.2), (300.0, 259.2),
                   (345.2, 259.2), (390.4, 259.2), (435.59999999999997, 259.2), (480.79999999999995, 259.2),
                   (526.0, 259.2), (571.2, 259.2), (616.4000000000001, 259.2), (661.6000000000001, 259.2),
                   (706.8000000000002, 259.2), (74, 292.26666666666665), (119.2, 292.26666666666665),
                   (164.4, 292.26666666666665), (209.60000000000002, 292.26666666666665), (254.8, 292.26666666666665),
                   (300.0, 292.26666666666665), (345.2, 292.26666666666665), (390.4, 292.26666666666665),
                   (435.59999999999997, 292.26666666666665), (480.79999999999995, 292.26666666666665),
                   (526.0, 292.26666666666665), (571.2, 292.26666666666665), (616.4000000000001, 292.26666666666665),
                   (661.6000000000001, 292.26666666666665), (706.8000000000002, 292.26666666666665),
                   (74, 325.3333333333333), (119.2, 325.3333333333333), (164.4, 325.3333333333333),
                   (209.60000000000002, 325.3333333333333), (254.8, 325.3333333333333), (300.0, 325.3333333333333),
                   (345.2, 325.3333333333333), (390.4, 325.3333333333333), (435.59999999999997, 325.3333333333333),
                   (480.79999999999995, 325.3333333333333), (526.0, 325.3333333333333), (571.2, 325.3333333333333),
                   (616.4000000000001, 325.3333333333333), (661.6000000000001, 325.3333333333333),
                   (706.8000000000002, 325.3333333333333), (74, 358.4), (119.2, 358.4), (164.4, 358.4),
                   (209.60000000000002, 358.4), (254.8, 358.4), (300.0, 358.4), (345.2, 358.4), (390.4, 358.4),
                   (435.59999999999997, 358.4), (480.79999999999995, 358.4), (526.0, 358.4), (571.2, 358.4),
                   (616.4000000000001, 358.4), (661.6000000000001, 358.4), (706.8000000000002, 358.4),
                   (74, 391.46666666666664), (119.2, 391.46666666666664), (164.4, 391.46666666666664),
                   (209.60000000000002, 391.46666666666664), (254.8, 391.46666666666664), (300.0, 391.46666666666664),
                   (345.2, 391.46666666666664), (390.4, 391.46666666666664), (435.59999999999997, 391.46666666666664),
                   (480.79999999999995, 391.46666666666664), (526.0, 391.46666666666664), (571.2, 391.46666666666664),
                   (616.4000000000001, 391.46666666666664), (661.6000000000001, 391.46666666666664),
                   (706.8000000000002, 391.46666666666664), (74, 424.5333333333333), (119.2, 424.5333333333333),
                   (164.4, 424.5333333333333), (209.60000000000002, 424.5333333333333), (254.8, 424.5333333333333),
                   (300.0, 424.5333333333333), (345.2, 424.5333333333333), (390.4, 424.5333333333333),
                   (435.59999999999997, 424.5333333333333), (480.79999999999995, 424.5333333333333),
                   (526.0, 424.5333333333333), (571.2, 424.5333333333333), (616.4000000000001, 424.5333333333333),
                   (661.6000000000001, 424.5333333333333), (706.8000000000002, 424.5333333333333),
                   (74, 457.59999999999997), (119.2, 457.59999999999997), (164.4, 457.59999999999997),
                   (209.60000000000002, 457.59999999999997), (254.8, 457.59999999999997), (300.0, 457.59999999999997),
                   (345.2, 457.59999999999997), (390.4, 457.59999999999997), (435.59999999999997, 457.59999999999997),
                   (480.79999999999995, 457.59999999999997), (526.0, 457.59999999999997), (571.2, 457.59999999999997),
                   (616.4000000000001, 457.59999999999997), (661.6000000000001, 457.59999999999997),
                   (706.8000000000002, 457.59999999999997), (74, 490.66666666666663), (119.2, 490.66666666666663),
                   (164.4, 490.66666666666663), (209.60000000000002, 490.66666666666663), (254.8, 490.66666666666663),
                   (300.0, 490.66666666666663), (345.2, 490.66666666666663), (390.4, 490.66666666666663),
                   (435.59999999999997, 490.66666666666663), (480.79999999999995, 490.66666666666663),
                   (526.0, 490.66666666666663), (571.2, 490.66666666666663), (616.4000000000001, 490.66666666666663),
                   (661.6000000000001, 490.66666666666663), (706.8000000000002, 490.66666666666663),
                   (74, 523.7333333333333), (119.2, 523.7333333333333), (164.4, 523.7333333333333),
                   (209.60000000000002, 523.7333333333333), (254.8, 523.7333333333333), (300.0, 523.7333333333333),
                   (345.2, 523.7333333333333), (390.4, 523.7333333333333), (435.59999999999997, 523.7333333333333),
                   (480.79999999999995, 523.7333333333333), (526.0, 523.7333333333333), (571.2, 523.7333333333333),
                   (616.4000000000001, 523.7333333333333), (661.6000000000001, 523.7333333333333),
                   (706.8000000000002, 523.7333333333333), (74, 556.8000000000001), (119.2, 556.8000000000001),
                   (164.4, 556.8000000000001), (209.60000000000002, 556.8000000000001), (254.8, 556.8000000000001),
                   (300.0, 556.8000000000001), (345.2, 556.8000000000001), (390.4, 556.8000000000001),
                   (435.59999999999997, 556.8000000000001), (480.79999999999995, 556.8000000000001),
                   (526.0, 556.8000000000001), (571.2, 556.8000000000001), (616.4000000000001, 556.8000000000001),
                   (661.6000000000001, 556.8000000000001), (706.8000000000002, 556.8000000000001),
                   (74, 589.8666666666668), (119.2, 589.8666666666668), (164.4, 589.8666666666668),
                   (209.60000000000002, 589.8666666666668), (254.8, 589.8666666666668), (300.0, 589.8666666666668),
                   (345.2, 589.8666666666668), (390.4, 589.8666666666668), (435.59999999999997, 589.8666666666668),
                   (480.79999999999995, 589.8666666666668), (526.0, 589.8666666666668), (571.2, 589.8666666666668),
                   (616.4000000000001, 589.8666666666668), (661.6000000000001, 589.8666666666668),
                   (706.8000000000002, 589.8666666666668), (74, 622.9333333333335), (119.2, 622.9333333333335),
                   (164.4, 622.9333333333335), (209.60000000000002, 622.9333333333335), (254.8, 622.9333333333335),
                   (300.0, 622.9333333333335), (345.2, 622.9333333333335), (390.4, 622.9333333333335),
                   (435.59999999999997, 622.9333333333335), (480.79999999999995, 622.9333333333335),
                   (526.0, 622.9333333333335), (571.2, 622.9333333333335), (616.4000000000001, 622.9333333333335),
                   (661.6000000000001, 622.9333333333335), (706.8000000000002, 622.9333333333335)]
solution_page_pos_1 = [(74, 160), (119, 160), (164, 160), (209, 160), (254, 160), (300, 160), (345, 160), (390, 160),
                       (435, 160), (480, 160), (526, 160), (571, 160), (616, 160), (661, 160), (706, 160), (74, 182),
                       (119, 182), (164, 182), (209, 182), (254, 182), (300, 182), (345, 182), (390, 182), (435, 182),
                       (480, 182), (526, 182), (571, 182), (616, 182), (661, 182), (706, 182), (74, 204), (119, 204),
                       (164, 204), (209, 204), (254, 204), (300, 204), (345, 204), (390, 204), (435, 204), (480, 204),
                       (526, 204), (571, 204), (616, 204), (661, 204), (706, 204), (74, 227), (119, 227), (164, 227),
                       (209, 227), (254, 227), (300, 227), (345, 227), (390, 227), (435, 227), (480, 227), (526, 227),
                       (571, 227), (616, 227), (661, 227), (706, 227), (74, 249), (119, 249), (164, 249), (209, 249),
                       (254, 249), (300, 249), (345, 249), (390, 249), (435, 249), (480, 249), (526, 249), (571, 249),
                       (616, 249), (661, 249), (706, 249), (74, 272), (119, 272), (164, 272), (209, 272), (254, 272),
                       (300, 272), (345, 272), (390, 272), (435, 272), (480, 272), (526, 272), (571, 272), (616, 272),
                       (661, 272), (706, 272), (74, 294), (119, 294), (164, 294), (209, 294), (254, 294), (300, 294),
                       (345, 294), (390, 294), (435, 294), (480, 294), (526, 294), (571, 294), (616, 294), (661, 294),
                       (706, 294), (74, 316), (119, 316), (164, 316), (209, 316), (254, 316), (300, 316), (345, 316),
                       (390, 316), (435, 316), (480, 316), (526, 316), (571, 316), (616, 316), (661, 316), (706, 316),
                       (74, 339), (119, 339), (164, 339), (209, 339), (254, 339), (300, 339), (345, 339), (390, 339),
                       (435, 339), (480, 339), (526, 339), (571, 339), (616, 339), (661, 339), (706, 339), (74, 361),
                       (119, 361), (164, 361), (209, 361), (254, 361), (300, 361), (345, 361), (390, 361), (435, 361),
                       (480, 361), (526, 361), (571, 361), (616, 361), (661, 361), (706, 361), (74, 383), (119, 383),
                       (164, 383), (209, 383), (254, 383), (300, 383), (345, 383), (390, 383), (435, 383), (480, 383),
                       (526, 383), (571, 383), (616, 383), (661, 383), (706, 383), (74, 406), (119, 406), (164, 406),
                       (209, 406), (254, 406), (300, 406), (345, 406), (390, 406), (435, 406), (480, 406), (526, 406),
                       (571, 406), (616, 406), (661, 406), (706, 406), (74, 428), (119, 428), (164, 428), (209, 428),
                       (254, 428), (300, 428), (345, 428), (390, 428), (435, 428), (480, 428), (526, 428), (571, 428),
                       (616, 428), (661, 428), (706, 428), (74, 451), (119, 451), (164, 451), (209, 451), (254, 451),
                       (300, 451), (345, 451), (390, 451), (435, 451), (480, 451), (526, 451), (571, 451), (616, 451),
                       (661, 451), (706, 451), (74, 473), (119, 473), (164, 473), (209, 473), (254, 473), (300, 473),
                       (345, 473), (390, 473), (435, 473), (480, 473), (526, 473), (571, 473), (616, 473), (661, 473),
                       (706, 473)]
solution_page_pos_2 = [(74, 575), (119, 575), (164, 575), (209, 575), (254, 575), (300, 575), (345, 575), (390, 575),
                       (435, 575), (480, 575), (526, 575), (571, 575), (616, 575), (661, 575), (706, 575), (74, 598),
                       (119, 598), (164, 598), (209, 598), (254, 598), (300, 598), (345, 598), (390, 598), (435, 598),
                       (480, 598), (526, 598), (571, 598), (616, 598), (661, 598), (706, 598), (74, 620), (119, 620),
                       (164, 620), (209, 620), (254, 620), (300, 620), (345, 620), (390, 620), (435, 620), (480, 620),
                       (526, 620), (571, 620), (616, 620), (661, 620), (706, 620), (74, 643), (119, 643), (164, 643),
                       (209, 643), (254, 643), (300, 643), (345, 643), (390, 643), (435, 643), (480, 643), (526, 643),
                       (571, 643), (616, 643), (661, 643), (706, 643), (74, 665), (119, 665), (164, 665), (209, 665),
                       (254, 665), (300, 665), (345, 665), (390, 665), (435, 665), (480, 665), (526, 665), (571, 665),
                       (616, 665), (661, 665), (706, 665), (74, 687), (119, 687), (164, 687), (209, 687), (254, 687),
                       (300, 687), (345, 687), (390, 687), (435, 687), (480, 687), (526, 687), (571, 687), (616, 687),
                       (661, 687), (706, 687), (74, 710), (119, 710), (164, 710), (209, 710), (254, 710), (300, 710),
                       (345, 710), (390, 710), (435, 710), (480, 710), (526, 710), (571, 710), (616, 710), (661, 710),
                       (706, 710), (74, 732), (119, 732), (164, 732), (209, 732), (254, 732), (300, 732), (345, 732),
                       (390, 732), (435, 732), (480, 732), (526, 732), (571, 732), (616, 732), (661, 732), (706, 732),
                       (74, 755), (119, 755), (164, 755), (209, 755), (254, 755), (300, 755), (345, 755), (390, 755),
                       (435, 755), (480, 755), (526, 755), (571, 755), (616, 755), (661, 755), (706, 755), (74, 777),
                       (119, 777), (164, 777), (209, 777), (254, 777), (300, 777), (345, 777), (390, 777), (435, 777),
                       (480, 777), (526, 777), (571, 777), (616, 777), (661, 777), (706, 777), (74, 799), (119, 799),
                       (164, 799), (209, 799), (254, 799), (300, 799), (345, 799), (390, 799), (435, 799), (480, 799),
                       (526, 799), (571, 799), (616, 799), (661, 799), (706, 799), (74, 822), (119, 822), (164, 822),
                       (209, 822), (254, 822), (300, 822), (345, 822), (390, 822), (435, 822), (480, 822), (526, 822),
                       (571, 822), (616, 822), (661, 822), (706, 822), (74, 844), (119, 844), (164, 844), (209, 844),
                       (254, 844), (300, 844), (345, 844), (390, 844), (435, 844), (480, 844), (526, 844), (571, 844),
                       (616, 844), (661, 844), (706, 844), (74, 867), (119, 867), (164, 867), (209, 867), (254, 867),
                       (300, 867), (345, 867), (390, 867), (435, 867), (480, 867), (526, 867), (571, 867), (616, 867),
                       (661, 867), (706, 867), (74, 889), (119, 889), (164, 889), (209, 889), (254, 889), (300, 889),
                       (345, 889), (390, 889), (435, 889), (480, 889), (526, 889), (571, 889), (616, 889), (661, 889),
                       (706, 889)]


class Puzzle:
    def __init__(self, words):
        self.pos = []
        words = [x.replace(" ", "").replace("-", "") for x in words]
        self.word_search = WordSearch(", ".join(words), size=15, level=2)
        self.max_word = len(self.word_search.key.keys())


class Page:
    def __init__(self, words, word_search, background, font="fonts/Roboto-Regular.ttf", header_bold=1,
                 header_color=(0, 0, 0), header_size=25, font_size=20, word_bold=1):
        self.grid = None
        self.words = words
        self.pos = normal_page_pos
        self.img = 255 * np.ones((HEIGHT, WIDTH, 3), np.uint8)
        self.header_bold = header_bold
        self.header_color = header_color
        self.header_size = header_size
        self.pos = [tuple(int(y) for y in x) for x in self.pos]
        self.word_search = word_search
        self.word_bold = word_bold
        self.font = font
        self.font_size = font_size
        print(background)
        self.img = cv2.resize(cv2.imread(background), (WIDTH, HEIGHT)) if len(background) > 0 else self.img
        cv2.rectangle(self.img, (H_MARGIN, V_MARGIN), (WIDTH - H_MARGIN + 10, HEIGHT - V_MARGIN), WHITE, -1)
        self.horiz_mult = (WIDTH - 2 * H_MARGIN - 10) / 15
        self.vert_mult = (HEIGHT - 7 * V_MARGIN) / 15

    def draw_all_border(self):
        # cv2.rectangle(self.img, (H_MARGIN, V_MARGIN), (WIDTH - H_MARGIN, HEIGHT - V_MARGIN), BLACK, 3)
        cv2.rectangle(self.img, (self.pos[0]),
                      (self.pos[-1][0] + int(self.horiz_mult), self.pos[-1][1] + int(self.vert_mult) + 10), BLACK, 3)

    def get_pos(self):
        self.pos = []
        temp_x, temp_y = H_MARGIN + 10, 2 * V_MARGIN
        for j in range(15):
            for i in range(15):
                self.pos.append((temp_x, temp_y))
                temp_x += self.horiz_mult
            temp_x = H_MARGIN + 10
            temp_y += self.vert_mult
        print(self.pos)

    def write_puzzle(self, grid):
        self.grid = grid
        i = 0
        for row in self.grid:
            for data in row:
                self.write_text(self.pos[i][0], self.pos[i][1], data.upper(), bold=self.word_bold, center=True)
                i += 1

    def write_words(self):
        pil_im = Image.fromarray(self.img)
        draw = ImageDraw.Draw(pil_im)
        font = ImageFont.truetype(self.font, 25)
        w, h = draw.textsize("W", font=font)
        start_x, start_y = (WIDTH - 2 * H_MARGIN) / 4 - 20, HEIGHT - 2.5 * V_MARGIN - (5 * h + 15)
        for index, word in enumerate(self.words):
            word = word.strip().replace(' ', "-")
            if index % 5 == 0 and index > 0:
                start_x += (WIDTH - 2 * H_MARGIN) / 3
                start_y = HEIGHT - 2.5 * V_MARGIN - (5 * h + 15)
            self.write_text(start_x, start_y, word.upper(), self.word_bold, True)
            start_y += h + 15

    def write_text(self, x, y, text, bold, center=True):
        pil_im = Image.fromarray(self.img)
        draw = ImageDraw.Draw(pil_im)
        font = ImageFont.truetype(self.font, self.font_size)
        w, h = draw.textsize(text, font=font)
        max_r_w = draw.textsize("W", font=font)[0]
        width_adjust = int((max_r_w - w) / 2) if center else 0
        draw.text((x + 8 + width_adjust, y + 8), text, (0, 0, 0), font=font, stroke_width=bold)
        self.img = cv2.cvtColor(np.array(pil_im), cv2.COLOR_RGB2BGR)

    def write_header(self, text="Temp Text"):
        x, y = int(WIDTH / 2), int(V_MARGIN) + 30
        pil_im = Image.fromarray(self.img)
        draw = ImageDraw.Draw(pil_im)
        font = ImageFont.truetype(self.font, self.header_size)
        w, h = draw.textsize(text, font=font)
        draw.text((int(x - w / 2), y), text, self.header_color, font=font, stroke_width=self.header_bold)
        self.img = cv2.cvtColor(np.array(pil_im), cv2.COLOR_RGB2BGR)

    def show_image(self):
        cv2.imshow("win", cv2.resize(self.img, (0, 0), fx=0.8, fy=0.8))
        if cv2.waitKey(0) & 0xFF == ord("q"):
            cv2.destroyAllWindows()

    def save_image(self, filename="output/temp.png"):
        cv2.imwrite(filename, self.img)


class Solution:
    def __init__(self, word_search,
                 font="fonts/Roboto-Regular.ttf"):
        self.pos = solution_page_pos_1
        self.pos2 = solution_page_pos_2
        self.img = 255 * np.ones((HEIGHT, WIDTH, 3), np.uint8)
        self.pos = [tuple(int(y) for y in x) for x in self.pos]
        self.pos2 = [tuple(int(y) for y in x) for x in self.pos2]
        self.word_search = word_search
        self.header_bold = 1
        self.header_size = 25
        self.header_color = (0, 0, 0)
        self.font = font
        self.horiz_mult = (WIDTH - 2 * H_MARGIN - 10) / 15
        self.vert_mult = (HEIGHT - 9 * V_MARGIN) / 15

    def draw_all_border(self):
        # cv2.rectangle(self.img, (H_MARGIN, V_MARGIN), (WIDTH - H_MARGIN, HEIGHT - V_MARGIN), BLACK, 3)
        cv2.rectangle(self.img, (self.pos[0]),
                      (self.pos[-1][0] + int(self.horiz_mult), self.pos[-1][1] + int(self.vert_mult) + 10), BLACK, 3)
        cv2.rectangle(self.img, (self.pos2[0]),
                      (self.pos2[-1][0] + int(self.horiz_mult), self.pos2[-1][1] + int(self.vert_mult) + 10), BLACK, 3)

    def get_pos(self):
        self.pos = []

        temp_x, temp_y = H_MARGIN + 10, 2 * V_MARGIN
        for j in range(15):
            for i in range(15):
                self.pos.append((temp_x, temp_y))
                temp_x += self.horiz_mult
            temp_x = H_MARGIN + 10
            temp_y += self.vert_mult
        temp_y += 80
        for j in range(15):
            for i in range(15):
                self.pos2.append((temp_x, temp_y))
                temp_x += self.horiz_mult
            temp_x = H_MARGIN + 10
            temp_y += self.vert_mult

    def write_puzzle(self, grid, index=1):
        if index > 1:
            i = 0
            for row in grid:
                for data in row:
                    self.write_text(self.pos2[i][0], self.pos2[i][1], data.upper(), bold=0, center=True)
                    i += 1
        else:
            i = 0
            for row in grid:
                for data in row:
                    self.write_text(self.pos[i][0], self.pos[i][1], data.upper(), bold=0, center=True)
                    i += 1

    def write_text(self, x, y, text, bold, center=True, size=20):
        pil_im = Image.fromarray(self.img)
        draw = ImageDraw.Draw(pil_im)
        font = ImageFont.truetype(self.font, size)
        w, h = draw.textsize(text, font=font)
        max_r_w = draw.textsize("W", font=font)[0]
        width_adjust = int((max_r_w - w) / 2) if center else 0
        draw.text((x + 8 + width_adjust, y + 8), text, (0, 0, 0), font=font, stroke_width=bold)
        self.img = cv2.cvtColor(np.array(pil_im), cv2.COLOR_RGB2BGR)

    def show_image(self):
        cv2.imshow("win", cv2.resize(self.img, (0, 0), fx=0.8, fy=0.8))
        if cv2.waitKey(0) & 0xFF == ord("q"):
            cv2.destroyAllWindows()

    def generate_solution(self, pos_list, word_search):
        for word in word_search.key.keys():
            start, end = word_search.key[word]['start']
            x, y = pos_list[end + start * 15]
            x, y = int(x + self.horiz_mult / 2), int(y + self.horiz_mult / 2)
            if word_search.key[word]['direction'] == "E":
                cv2.line(self.img, (x - 5, y - 5), (int(x + self.horiz_mult * (len(word) - 1)) + 5, y - 5),
                         (199, 197, 202),
                         17)
            elif word_search.key[word]['direction'] == "S":
                cv2.line(self.img, (x - 5, y - 5), (x - 5, int(y + self.vert_mult * (len(word) - 1) + 5)),
                         (199, 197, 202),
                         16)
            elif word_search.key[word]['direction'] == "SE":
                cv2.line(self.img, (x - 5, y - 5),
                         (int(x + self.horiz_mult * (len(word) - 1) + 5), int(y + self.vert_mult * (len(word) - 1))),
                         (199, 197, 202),
                         17)
            elif word_search.key[word]['direction'] == "NE":
                cv2.line(self.img, (x - 5, y),
                         (int(x + self.horiz_mult * (len(word) - 1)), int(y - self.vert_mult * (len(word) - 1) - 3)),
                         (199, 197, 202),
                         17)

    def save_image(self, filename="output/tempsolution.png"):
        cv2.imwrite(filename, self.img)


def get_content_csv(filename):
    return [[x[0], x[1].split(",")] for x in csv.reader(open(filename, "r", encoding="utf-8-sig"))]


def init_folder():
    try:
        shutil.rmtree("static/output")
        os.makedirs("static/output")
    except:
        pass


def main(csv_file, BACKGROUND_IMAGES, font, header_bold, header_size,
         header_color, word_bold, pagination_write=True, font_size=25):
    init_folder()
    csv_file = get_content_csv(csv_file)
    word_search_list = []
    pagination = 1
    for index, (heading, words) in enumerate(csv_file):
        words = words[:15]
        puzzle = Puzzle(words)
        page = Page(words, puzzle.word_search, BACKGROUND_IMAGES, font=font, header_bold=header_bold,
                    header_size=header_size,
                    header_color=header_color, font_size=font_size, word_bold=word_bold)

        page.draw_all_border()
        page.write_header(text=f"#{index + 1} {heading}")
        page.write_puzzle(puzzle.word_search.puzzle)
        page.write_words()
        page.write_text(385, 945, f"{pagination}", 1) if pagination_write else None
        page.save_image(filename=f"static/output/{pagination}puzzle.png")
        pagination += 1
        word_search_list.append(puzzle.word_search)

    for i in range(0, len(csv_file), 2):
        word_search_1 = word_search_list[i]
        word_search_2 = word_search_list[i + 1]
        solution = Solution(word_search_1)
        solution.draw_all_border()
        solution.generate_solution(solution.pos, word_search_1)
        solution.generate_solution(solution.pos2, word_search_2)
        solution.write_text(solution.pos[0][0] + int((WIDTH - 2 * H_MARGIN) / 2) - 20, solution.pos[0][1] - 60,
                            f"#{i + 1} {csv_file[i][0]}", 1, size=header_size)
        solution.write_puzzle(word_search_1.puzzle, index=1)
        solution.write_text(solution.pos2[0][0] + int((WIDTH - 2 * H_MARGIN) / 2) - 20, solution.pos2[0][1] - 60,
                            f"#{i + 1} {csv_file[i + 1][0]}", 1, size=header_size)
        solution.write_puzzle(word_search_2.puzzle, index=2)
        solution.write_text(385, 945, f"{pagination}", 1) if pagination_write else None
        solution.save_image(filename=f"static/output/{pagination}solution.png")
        pagination += 1

    with open("static/output/output.pdf", "wb") as f:
        f.write(img2pdf.convert(glob("static/output/*.png")))


if __name__ == "__main__":
    main(csv_file="word_list.csv",
         BACKGROUND_IMAGES=random.choice(glob("background/*")) if len(glob("background/*")) > 0 else [],
         font="fonts/arial.ttf",
         header_bold=1, header_size=25,
         header_color=(0, 0, 0), pagination_write=True, font_size=25, word_bold=1)
