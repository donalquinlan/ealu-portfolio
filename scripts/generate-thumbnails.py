#!/usr/bin/env python3
"""Generate LinkedIn featured-link thumbnails (1200x627) for the portfolio."""

from __future__ import annotations

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "thumbnails"
WIDTH = 1200
HEIGHT = 627

BG = "#f4f6f8"
BG_ALT = "#e8edf2"
NAVY = "#1a2332"
MUTED = "#5c6778"
ACCENT = "#1f4e79"
WHITE = "#ffffff"

FONT_SANS = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
FONT_SANS_REG = "/System/Library/Fonts/Supplemental/Arial.ttf"
FONT_SERIF = "/System/Library/Fonts/Supplemental/Georgia Bold.ttf"


def rgb(hex_color: str) -> tuple[int, int, int]:
    value = hex_color.lstrip("#")
    return tuple(int(value[i : i + 2], 16) for i in range(0, 6, 2))


def load_font(path: str, size: int) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    try:
        return ImageFont.truetype(path, size)
    except OSError:
        return ImageFont.load_default()


def wrap_text(text: str, font: ImageFont.FreeTypeFont, max_width: int) -> list[str]:
    words = text.split()
    lines: list[str] = []
    current = ""

    for word in words:
        candidate = word if not current else f"{current} {word}"
        if font.getbbox(candidate)[2] <= max_width:
            current = candidate
        else:
            if current:
                lines.append(current)
            current = word

    if current:
        lines.append(current)

    return lines or [text]


def draw_text_block(
    draw: ImageDraw.ImageDraw,
    *,
    x: int,
    y: int,
    max_width: int,
    lines: list[tuple[str, ImageFont.FreeTypeFont, str]],
    line_gap: int = 12,
) -> int:
    cursor_y = y
    for text, font, color in lines:
        for line in wrap_text(text, font, max_width):
            draw.text((x, cursor_y), line, font=font, fill=rgb(color))
            cursor_y += font.getbbox(line)[3] + line_gap
    return cursor_y


def base_canvas(accent: str, accent_soft: str) -> tuple[Image.Image, ImageDraw.ImageDraw]:
    image = Image.new("RGB", (WIDTH, HEIGHT), rgb(BG))
    draw = ImageDraw.Draw(image)

    draw.rectangle((0, 0, WIDTH, HEIGHT), fill=rgb(BG))
    draw.rectangle((0, 0, 12, HEIGHT), fill=rgb(accent))

    for x in range(720, WIDTH, 48):
        draw.line((x, 0, x, HEIGHT), fill=rgb(BG_ALT), width=1)

    draw.polygon(
        [
            (760, 0),
            (WIDTH, 0),
            (WIDTH, HEIGHT),
            (680, HEIGHT),
        ],
        fill=rgb(accent_soft),
    )

    return image, draw


def save(name: str, image: Image.Image) -> Path:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    path = OUT_DIR / name
    image.save(path, format="PNG", optimize=True)
    return path


def draw_portfolio() -> Path:
    image, draw = base_canvas(ACCENT, "#d5e0ea")
    accent = rgb(ACCENT)

    draw.rounded_rectangle((860, 96, 1110, 286), radius=18, outline=accent, width=3)
    draw.rounded_rectangle((900, 136, 1070, 176), radius=8, fill=accent)
    draw.rounded_rectangle((900, 196, 980, 216), radius=6, fill=rgb(MUTED))
    draw.rounded_rectangle((900, 232, 1040, 252), radius=6, fill=rgb(MUTED))

    draw.ellipse((880, 330, 940, 390), outline=accent, width=3)
    draw.line((910, 360, 980, 360), fill=accent, width=3)
    draw.line((945, 325, 945, 395), fill=accent, width=3)
    draw.line((980, 330, 1040, 390), fill=accent, width=3)
    draw.line((980, 390, 1040, 330), fill=accent, width=3)

    draw.rounded_rectangle((860, 430, 1110, 530), radius=18, outline=accent, width=3)
    for offset in (450, 470, 490):
        draw.rounded_rectangle((890, offset, 1080, offset + 12), radius=4, fill=accent)

    fonts = {
        "eyebrow": load_font(FONT_SANS_REG, 24),
        "name": load_font(FONT_SERIF, 58),
        "title": load_font(FONT_SANS, 34),
        "meta": load_font(FONT_SANS_REG, 26),
    }

    draw.text((56, 72), "PORTFOLIO", font=fonts["eyebrow"], fill=rgb(ACCENT))
    draw.text((56, 118), "Donal Quinlan", font=fonts["name"], fill=rgb(NAVY))
    draw_text_block(
        draw,
        x=56,
        y=210,
        max_width=640,
        lines=[
            ("Senior Technical Program Manager", fonts["title"], NAVY),
            (
                "Platform delivery · Release governance · Production readiness",
                fonts["meta"],
                MUTED,
            ),
        ],
        line_gap=16,
    )

    return save("portfolio.png", image)


def draw_ppp() -> Path:
    image, draw = base_canvas("#b45309", "#fde6c8")
    accent = rgb("#b45309")

    draw.rounded_rectangle((860, 110, 1110, 360), radius=24, outline=accent, width=4)
    draw.ellipse((930, 170, 1040, 280), outline=accent, width=5)
    draw.line((985, 205, 985, 245), fill=accent, width=5)
    draw.line((985, 245, 1015, 265), fill=accent, width=5)
    for angle_x in (900, 950, 1000, 1050):
        draw.line((angle_x, 300, angle_x + 18, 330), fill=accent, width=4)

    fonts = {
        "tag": load_font(FONT_SANS_REG, 22),
        "title": load_font(FONT_SERIF, 46),
        "meta": load_font(FONT_SANS_REG, 28),
        "stat": load_font(FONT_SANS, 64),
    }

    draw.text((56, 72), "CASE STUDY · CRISIS PROGRAM", font=fonts["tag"], fill=accent)
    draw.text((56, 112), "Intuit Payroll", font=fonts["meta"], fill=rgb(MUTED))
    draw_text_block(
        draw,
        x=56,
        y=170,
        max_width=650,
        lines=[
            ("Delivering the Paycheck Protection Program in 18 Days", fonts["title"], NAVY),
        ],
        line_gap=10,
    )
    draw.text((56, 430), "18 days", font=fonts["stat"], fill=accent)
    draw.text((56, 510), "$10B+ enabled · 100K+ jobs protected", font=fonts["meta"], fill=rgb(MUTED))

    return save("case-ppp.png", image)


def draw_fiserv() -> Path:
    image, draw = base_canvas("#0f766e", "#ccfbf1")
    accent = rgb("#0f766e")

    start_x = 870
    for index, y in enumerate((420, 340, 260, 180)):
        width = 220 - index * 20
        draw.rounded_rectangle(
            (start_x + index * 18, y, start_x + index * 18 + width, y + 56),
            radius=12,
            outline=accent,
            width=3,
        )
        if index < 3:
            draw.polygon(
                [
                    (start_x + index * 18 + width - 8, y + 28),
                    (start_x + index * 18 + width + 28, y + 28),
                    (start_x + index * 18 + width + 14, y + 14),
                ],
                fill=accent,
            )

    draw.line((870, 500, 1110, 500), fill=accent, width=4)
    draw.text((900, 512), "8 min releases", font=load_font(FONT_SANS, 28), fill=accent)

    fonts = {
        "tag": load_font(FONT_SANS_REG, 22),
        "title": load_font(FONT_SERIF, 46),
        "meta": load_font(FONT_SANS_REG, 28),
    }

    draw.text((56, 72), "CASE STUDY · RELEASE ENGINEERING", font=fonts["tag"], fill=accent)
    draw.text((56, 112), "Fiserv", font=fonts["meta"], fill=rgb(MUTED))
    draw_text_block(
        draw,
        x=56,
        y=170,
        max_width=650,
        lines=[
            ("Modernizing Release Delivery at Scale", fonts["title"], NAVY),
            ("From two-hour deployments to eight-minute releases", fonts["meta"], MUTED),
        ],
        line_gap=18,
    )

    return save("case-fiserv.png", image)


def draw_vineti() -> Path:
    image, draw = base_canvas("#2563eb", "#dbeafe")
    accent = rgb("#2563eb")

    chart_left = 860
    chart_bottom = 500
    heights = [120, 190, 250, 310, 360]
    for index, height in enumerate(heights):
        x0 = chart_left + index * 48
        draw.rounded_rectangle(
            (x0, chart_bottom - height, x0 + 32, chart_bottom),
            radius=6,
            fill=accent if index >= 2 else rgb("#93c5fd"),
        )

    draw.line((850, chart_bottom, 1110, chart_bottom), fill=accent, width=3)
    draw.line((850, chart_bottom, 850, 120), fill=accent, width=3)

    fonts = {
        "tag": load_font(FONT_SANS_REG, 22),
        "title": load_font(FONT_SERIF, 46),
        "meta": load_font(FONT_SANS_REG, 28),
    }

    draw.text((56, 72), "CASE STUDY · PLATFORM DELIVERY", font=fonts["tag"], fill=accent)
    draw.text((56, 112), "Vineti", font=fonts["meta"], fill=rgb(MUTED))
    draw_text_block(
        draw,
        x=56,
        y=170,
        max_width=650,
        lines=[
            ("Restoring Predictable Delivery at Scale", fonts["title"], NAVY),
            ("Governance, visibility, and ~20% productivity gains", fonts["meta"], MUTED),
        ],
        line_gap=18,
    )

    return save("case-vineti.png", image)


def draw_centered_lines_in_box(
    draw: ImageDraw.ImageDraw,
    box: tuple[int, int, int, int],
    lines: list[str],
    font: ImageFont.FreeTypeFont,
    color: str,
    *,
    line_gap: int = 4,
) -> None:
    x0, y0, x1, y1 = box
    heights = [font.getbbox(line)[3] - font.getbbox(line)[1] for line in lines]
    total_height = sum(heights) + line_gap * (len(lines) - 1)
    cursor_y = y0 + ((y1 - y0) - total_height) // 2

    for line, height in zip(lines, heights):
        bbox = font.getbbox(line)
        text_width = bbox[2] - bbox[0]
        x = x0 + ((x1 - x0) - text_width) // 2
        draw.text((x, cursor_y), line, font=font, fill=rgb(color))
        cursor_y += height + line_gap


def draw_ealu() -> Path:
    image, draw = base_canvas("#6d28d9", "#ede9fe")
    accent = rgb("#6d28d9")

    nodes = [(930, 180), (1040, 140), (1080, 250), (980, 320), (890, 280), (910, 400), (1030, 430)]
    for x, y in nodes:
        draw.ellipse((x - 16, y - 16, x + 16, y + 16), fill=accent)

    connections = [
        (0, 1),
        (1, 2),
        (2, 3),
        (3, 4),
        (4, 0),
        (3, 5),
        (5, 6),
        (2, 6),
    ]
    for a, b in connections:
        x0, y0 = nodes[a]
        x1, y1 = nodes[b]
        draw.line((x0, y0, x1, y1), fill=accent, width=3)

    draw.rounded_rectangle((850, 462, 1120, 548), radius=14, outline=accent, width=3)
    draw_centered_lines_in_box(
        draw,
        (850, 462, 1120, 548),
        ["Governance", "by design"],
        load_font(FONT_SANS, 22),
        "#6d28d9",
    )

    fonts = {
        "tag": load_font(FONT_SANS_REG, 22),
        "title": load_font(FONT_SERIF, 44),
        "meta": load_font(FONT_SANS_REG, 28),
    }

    draw.text((56, 72), "CASE STUDY · AI PRODUCT DELIVERY", font=fonts["tag"], fill=accent)
    draw.text((56, 112), "Ealu.ai", font=fonts["meta"], fill=rgb(MUTED))
    draw_text_block(
        draw,
        x=56,
        y=170,
        max_width=650,
        lines=[
            (
                "Applying Product, Governance, and Delivery Principles to AI",
                fonts["title"],
                NAVY,
            ),
            ("Security, privacy, and trust as first-class requirements", fonts["meta"], MUTED),
        ],
        line_gap=18,
    )

    return save("case-ealu.png", image)


def main() -> None:
    paths = [
        draw_portfolio(),
        draw_ppp(),
        draw_fiserv(),
        draw_vineti(),
        draw_ealu(),
    ]
    for path in paths:
        print(path)


if __name__ == "__main__":
    main()
