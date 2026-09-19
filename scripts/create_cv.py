from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    HRFlowable,
    KeepTogether,
    PageTemplate,
    Paragraph,
    Spacer,
)


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "assets" / "pdf" / "CV.pdf"


def footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(colors.HexColor("#777777"))
    canvas.drawString(20 * mm, 12 * mm, "Gaohan Gao - Academic CV")
    canvas.drawRightString(A4[0] - 20 * mm, 12 * mm, f"Page {doc.page}")
    canvas.restoreState()


styles = getSampleStyleSheet()
name_style = ParagraphStyle(
    "Name",
    parent=styles["Title"],
    fontName="Helvetica-Bold",
    fontSize=23,
    leading=27,
    textColor=colors.HexColor("#111111"),
    spaceAfter=3,
)
role_style = ParagraphStyle(
    "Role",
    parent=styles["Normal"],
    fontName="Helvetica",
    fontSize=10.5,
    leading=14,
    textColor=colors.HexColor("#444444"),
    spaceAfter=2,
)
contact_style = ParagraphStyle(
    "Contact",
    parent=styles["Normal"],
    fontName="Helvetica",
    fontSize=9.2,
    leading=13,
    textColor=colors.HexColor("#555555"),
    spaceAfter=8,
)
section_style = ParagraphStyle(
    "Section",
    parent=styles["Heading2"],
    fontName="Helvetica-Bold",
    fontSize=11.5,
    leading=14,
    textColor=colors.HexColor("#111111"),
    spaceBefore=10,
    spaceAfter=4,
    keepWithNext=True,
)
entry_style = ParagraphStyle(
    "Entry",
    parent=styles["Normal"],
    fontName="Helvetica",
    fontSize=9.4,
    leading=13.2,
    textColor=colors.HexColor("#222222"),
    spaceAfter=4,
)
small_style = ParagraphStyle(
    "Small",
    parent=entry_style,
    fontSize=8.9,
    leading=12.3,
    leftIndent=10,
    firstLineIndent=-6,
    bulletIndent=0,
    spaceAfter=2.5,
)


def section(title):
    return [
        Paragraph(title.upper(), section_style),
        HRFlowable(width="100%", thickness=0.6, color=colors.HexColor("#B8B8B8"), spaceAfter=5),
    ]


def bullet(text):
    return Paragraph(f"• {text}", small_style)


doc = BaseDocTemplate(
    str(OUTPUT),
    pagesize=A4,
    rightMargin=20 * mm,
    leftMargin=20 * mm,
    topMargin=17 * mm,
    bottomMargin=18 * mm,
    title="Gaohan Gao Academic CV",
    author="Gaohan Gao",
)
frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="main")
doc.addPageTemplates(PageTemplate(id="academic", frames=[frame], onPage=footer))

story = [
    Paragraph("Gaohan Gao", name_style),
    Paragraph("Undergraduate Student in Software Engineering | Xi'an Jiaotong University", role_style),
    Paragraph(
        "Xi'an, Shaanxi, China &nbsp;&nbsp;|&nbsp;&nbsp; "
        "<link href='mailto:gaohan050121@outlook.com' color='#444444'>gaohan050121@outlook.com</link> &nbsp;&nbsp;|&nbsp;&nbsp; "
        "<link href='https://github.com/gaohan0121' color='#444444'>github.com/gaohan0121</link>",
        contact_style,
    ),
]

story += section("Research Profile")
story.append(
    Paragraph(
        "Undergraduate researcher working on multimodal artificial intelligence, remote sensing foundation models, "
        "vision-language learning, and agentic AI. Current work studies multimodal large language models for "
        "hyperspectral image change detection, SAR-RGB cross-modal retrieval, and tool-augmented multi-agent systems.",
        entry_style,
    )
)

story += section("Education")
story.append(
    KeepTogether(
        [
            Paragraph("<b>Xi'an Jiaotong University</b> <font color='#666666'>| Xi'an, China</font>", entry_style),
            Paragraph("B.E. in Software Engineering &nbsp;&nbsp;|&nbsp;&nbsp; September 2023 - Present", small_style),
        ]
    )
)

story += section("Research Experience")
story.extend(
    [
        Paragraph(
            "<b>Multimodal Large Language Models for Hyperspectral Image Change Detection</b> "
            "<font color='#666666'>| January 2026 - Present</font>",
            entry_style,
        ),
        bullet("Reformulated pixel-level change detection as a vision-language question-answering task for semantic interpretation."),
        bullet("Refined ground-truth labels and designed an automated pipeline for region-level captions and question-answer pairs."),
        bullet("Adapted multimodal models with supervised fine-tuning and parameter-efficient fine-tuning; conducted evaluation and analysis."),
        Spacer(1, 3),
        Paragraph(
            "<b>Structure-Aware SAR-RGB Cross-modal Image Retrieval</b> "
            "<font color='#666666'>| September 2025 - December 2025</font>",
            entry_style,
        ),
        bullet("Investigated cross-modal retrieval across heterogeneous sensing modalities using CLIP-style feature alignment."),
        bullet("Implemented strip-convolution modules to capture elongated ship structures and evaluated retrieval performance."),
        bullet("Completed model training, hyperparameter tuning, ablation studies, and comparative analysis."),
        Spacer(1, 3),
        Paragraph(
            "<b>Deep Learning for Cytological Diagnosis of Pleomorphic Adenoma</b> "
            "<font color='#666666'>| September 2025 - April 2026</font>",
            entry_style,
        ),
        bullet("Contributed to literature review, technical planning, data preparation, model discussion, and experimental analysis."),
    ]
)

story += section("Publications")
story.extend(
    [
        Paragraph(
            "<b>HSICD: Multimodal Large Language Model for Hyperspectral Image Change Detection.</b> "
            "Gaohan Gao et al. <i>IEEE Geoscience and Remote Sensing Magazine</i>. Under review.",
            entry_style,
        ),
        Paragraph(
            "<b>A Unified Algorithmic Framework for Battery Life Prediction Based on CTMC and Monte Carlo Simulation.</b> "
            "Gaohan Gao et al. <i>MEEML 2026</i>. Co-first author.",
            entry_style,
        ),
    ]
)

story += section("Selected Project")
story.extend(
    [
        Paragraph(
            "<b>Multi-Agent Literature Research Assistant</b> <font color='#666666'>| Independent project, March 2026</font>",
            entry_style,
        ),
        bullet("Designed a multi-agent workflow for paper discovery, ranking, question answering, novelty analysis, and literature synthesis."),
        bullet("Integrated tool-augmented agents with Zotero and Obsidian for research knowledge-base synchronization."),
        bullet("Built agent tracing for observable coordination and tool-use workflows using MCP, A2A, and RAG concepts."),
    ]
)

story += section("Technical Skills")
story.extend(
    [
        Paragraph("<b>Programming:</b> Python, C++, Java", entry_style),
        Paragraph("<b>Artificial Intelligence:</b> PyTorch, Transformers, CLIP, LoRA, LLM fine-tuning", entry_style),
        Paragraph("<b>Research Areas:</b> Multimodal LLMs, remote sensing, vision-language learning, change detection, cross-modal retrieval, agentic AI", entry_style),
    ]
)

doc.build(story)
print(OUTPUT)
