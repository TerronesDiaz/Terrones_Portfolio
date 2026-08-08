from pathlib import Path
from shutil import copyfile

from pypdf import PdfReader
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.platypus import (
    HRFlowable,
    KeepTogether,
    ListFlowable,
    ListItem,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "output" / "pdf"
PUBLIC_DIR = ROOT / "public" / "cv"

INK = colors.HexColor("#071426")
BLUE = colors.HexColor("#1769E0")
BLUE_DARK = colors.HexColor("#0F4FB4")
BLUE_PALE = colors.HexColor("#EAF2FF")
MUTED = colors.HexColor("#4F6077")
LINE = colors.HexColor("#D8E1ED")
WHITE = colors.white


CVS = {
    "es": {
        "filename": "francisco-terrones-cv-es.pdf",
        "document_title": "CV de Francisco Javier Terrones Díaz",
        "role": "Ingeniero de Software / Desarrollador SAP Business One",
        "location": "Colima, México",
        "summary_title": "Perfil profesional",
        "summary": (
            "Ingeniero de software enfocado en diseñar soluciones a medida que conectan procesos "
            "operativos con tecnología. Experiencia en SAP Business One, puntos de venta, portales "
            "internos, optimización SQL y desarrollo web de extremo a extremo."
        ),
        "experience_title": "Experiencia",
        "experience": [
            {
                "role": "Ingeniero de Software / Desarrollador SAP Business One",
                "company": "Surtidora de Ferretería y Materiales SFM",
                "place": "Colima, México",
                "period": "Julio 2024 - Hoy",
                "bullets": [
                    "Diseñé e implementé un POS integral conectado con SAP Business One para ofertas, pedidos, ventas y facturación.",
                    "Desarrollé un portal interno para venta, programación documental, logística de embarque y reportes administrativos.",
                    "Optimicé consultas SQL y procesos críticos para reducir cuellos de botella y mejorar el rendimiento general.",
                ],
            },
            {
                "role": "Desarrollador de software independiente",
                "company": "Soluciones para pequeñas y medianas empresas",
                "place": "México",
                "period": "2022 - Hoy",
                "bullets": [
                    "Creo aplicaciones web, móviles y de escritorio orientadas a necesidades operativas concretas.",
                    "Diseño productos mantenibles con énfasis en automatización, usabilidad y crecimiento sostenible.",
                ],
            },
            {
                "role": "Desarrollador Web",
                "company": "Puerto Inteligente Seguro",
                "place": "Manzanillo, México",
                "period": "Enero 2023 - Diciembre 2023",
                "bullets": [
                    "Desarrollé formularios dinámicos y reportes a medida para información operativa y análisis de seguridad portuaria.",
                ],
            },
        ],
        "education_title": "Formación",
        "education": "Ingeniería de Software<br/>Universidad de Colima<br/><font color='#4F6077'>2019 - 2023</font>",
        "skills_title": "Tecnologías",
        "skills": ["JavaScript", "C# / .NET", "Svelte", "SQL", "SAP Business One", "Astro", "Tailwind CSS"],
        "focus_title": "Especialidades",
        "focus": ["Integración de sistemas", "POS y operaciones", "Frontend y backend", "Optimización de procesos", "Reportes y automatización"],
        "strengths_title": "Fortalezas",
        "strengths": ["Resolución de problemas", "Comunicación", "Pensamiento analítico", "Adaptabilidad"],
        "footer": "Portafolio y proyectos en terrones.dev",
    },
    "en": {
        "filename": "francisco-terrones-cv-en.pdf",
        "document_title": "Francisco Javier Terrones Díaz Resume",
        "role": "Software Engineer / SAP Business One Developer",
        "location": "Colima, Mexico",
        "summary_title": "Professional profile",
        "summary": (
            "Software engineer focused on custom solutions that connect operational processes with "
            "technology. Experienced in SAP Business One, point-of-sale systems, internal portals, "
            "SQL optimization and end-to-end web development."
        ),
        "experience_title": "Experience",
        "experience": [
            {
                "role": "Software Engineer / SAP Business One Developer",
                "company": "Surtidora de Ferretería y Materiales SFM",
                "place": "Colima, Mexico",
                "period": "July 2024 - Present",
                "bullets": [
                    "Designed and implemented an end-to-end POS connected to SAP Business One for quotations, orders, sales and invoicing.",
                    "Built an internal portal for sales, document scheduling, shipping logistics and administrative reporting.",
                    "Optimized SQL queries and critical processes to reduce bottlenecks and improve overall performance.",
                ],
            },
            {
                "role": "Independent Software Developer",
                "company": "Solutions for small and medium-sized businesses",
                "place": "Mexico",
                "period": "2022 - Present",
                "bullets": [
                    "Build web, mobile and desktop applications around concrete operational needs.",
                    "Design maintainable products centered on automation, usability and sustainable growth.",
                ],
            },
            {
                "role": "Web Developer",
                "company": "Puerto Inteligente Seguro",
                "place": "Manzanillo, Mexico",
                "period": "January 2023 - December 2023",
                "bullets": [
                    "Developed dynamic forms and custom reports for port operations data and security analysis.",
                ],
            },
        ],
        "education_title": "Education",
        "education": "B.S. in Software Engineering<br/>University of Colima<br/><font color='#4F6077'>2019 - 2023</font>",
        "skills_title": "Technologies",
        "skills": ["JavaScript", "C# / .NET", "Svelte", "SQL", "SAP Business One", "Astro", "Tailwind CSS"],
        "focus_title": "Specialties",
        "focus": ["Systems integration", "POS and operations", "Frontend and backend", "Process optimization", "Reporting and automation"],
        "strengths_title": "Strengths",
        "strengths": ["Problem solving", "Communication", "Analytical thinking", "Adaptability"],
        "footer": "Portfolio and selected work at terrones.dev",
    },
}


def styles():
    base = getSampleStyleSheet()
    return {
        "name": ParagraphStyle(
            "Name",
            parent=base["Normal"],
            fontName="Helvetica-Bold",
            fontSize=23,
            leading=25,
            textColor=INK,
            spaceAfter=3,
        ),
        "role": ParagraphStyle(
            "Role",
            parent=base["Normal"],
            fontName="Helvetica-Bold",
            fontSize=10.5,
            leading=13,
            textColor=BLUE_DARK,
            spaceAfter=7,
        ),
        "contact": ParagraphStyle(
            "Contact",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=7.6,
            leading=10,
            textColor=MUTED,
        ),
        "section": ParagraphStyle(
            "Section",
            parent=base["Normal"],
            fontName="Helvetica-Bold",
            fontSize=8.5,
            leading=10,
            textColor=BLUE_DARK,
            spaceBefore=4,
            spaceAfter=5,
            uppercase=True,
        ),
        "body": ParagraphStyle(
            "Body",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=8.2,
            leading=11,
            textColor=MUTED,
            alignment=TA_LEFT,
        ),
        "role_line": ParagraphStyle(
            "RoleLine",
            parent=base["Normal"],
            fontName="Helvetica-Bold",
            fontSize=9.2,
            leading=11.4,
            textColor=INK,
            spaceAfter=1.5,
        ),
        "company": ParagraphStyle(
            "Company",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=7.7,
            leading=10,
            textColor=BLUE_DARK,
            spaceAfter=3,
        ),
        "period": ParagraphStyle(
            "Period",
            parent=base["Normal"],
            fontName="Helvetica-Bold",
            fontSize=7.4,
            leading=9,
            textColor=MUTED,
        ),
        "bullet": ParagraphStyle(
            "Bullet",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=7.7,
            leading=10.2,
            textColor=MUTED,
            leftIndent=0,
        ),
        "side": ParagraphStyle(
            "Side",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=7.8,
            leading=10.5,
            textColor=INK,
        ),
        "footer": ParagraphStyle(
            "Footer",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=7,
            leading=8,
            textColor=MUTED,
        ),
    }


def section_title(text, style):
    table = Table([[Paragraph(text.upper(), style)]], colWidths=["100%"])
    table.setStyle(
        TableStyle(
            [
                ("LINEBELOW", (0, 0), (-1, -1), 0.7, LINE),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 2),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
            ]
        )
    )
    return table


def bullet_list(items, style, left=9):
    return ListFlowable(
        [ListItem(Paragraph(item, style), leftIndent=0) for item in items],
        bulletType="bullet",
        start="circle",
        leftIndent=left,
        bulletFontName="Helvetica",
        bulletFontSize=4.5,
        bulletColor=BLUE,
        spaceAfter=2,
    )


def experience_block(item, s):
    meta_table = Table(
        [[
            Paragraph(f'{item["company"]} · {item["place"]}', s["company"]),
            Paragraph(item["period"], s["period"]),
        ]],
        colWidths=[88 * mm, 32 * mm],
        hAlign="LEFT",
    )
    meta_table.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("ALIGN", (1, 0), (1, 0), "RIGHT"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
            ]
        )
    )
    return [
        Paragraph(item["role"], s["role_line"]),
        meta_table,
        bullet_list(item["bullets"], s["bullet"]),
        Spacer(1, 5),
    ]


def chip_table(items, style):
    rows = [[Paragraph(item, style)] for item in items]
    table = Table(rows, colWidths=[41 * mm], hAlign="LEFT")
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), BLUE_PALE),
                ("BOX", (0, 0), (-1, -1), 0.5, LINE),
                ("INNERGRID", (0, 0), (-1, -1), 0.5, WHITE),
                ("TEXTCOLOR", (0, 0), (-1, -1), INK),
                ("LEFTPADDING", (0, 0), (-1, -1), 6),
                ("RIGHTPADDING", (0, 0), (-1, -1), 6),
                ("TOPPADDING", (0, 0), (-1, -1), 3),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
            ]
        )
    )
    return table


def footer(canvas, doc, data, style):
    canvas.saveState()
    canvas.setStrokeColor(LINE)
    canvas.setLineWidth(0.6)
    canvas.line(doc.leftMargin, 13 * mm, A4[0] - doc.rightMargin, 13 * mm)
    footer_text = data["footer"]
    canvas.setFont("Helvetica", 7)
    canvas.setFillColor(MUTED)
    canvas.drawString(doc.leftMargin, 8.5 * mm, footer_text)
    page = "1 / 1"
    canvas.drawString(A4[0] - doc.rightMargin - stringWidth(page, "Helvetica", 7), 8.5 * mm, page)
    canvas.restoreState()


def build_cv(language):
    data = CVS[language]
    s = styles()
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    PUBLIC_DIR.mkdir(parents=True, exist_ok=True)
    output = OUTPUT_DIR / data["filename"]

    doc = SimpleDocTemplate(
        str(output),
        pagesize=A4,
        leftMargin=14 * mm,
        rightMargin=14 * mm,
        topMargin=13 * mm,
        bottomMargin=18 * mm,
        title=data["document_title"],
        author="Francisco Javier Terrones Díaz",
        subject=data["role"],
        allowSplitting=0,
    )

    contact = (
        f'{data["location"]} &nbsp;·&nbsp; '
        '<link href="mailto:f.terrones@outlook.com" color="#0F4FB4">f.terrones@outlook.com</link> &nbsp;·&nbsp; '
        '<link href="https://www.linkedin.com/in/francisco-javier-terrones-diaz" color="#0F4FB4">LinkedIn</link> &nbsp;·&nbsp; '
        '<link href="https://wa.me/523121111440" color="#0F4FB4">+52 312 111 1440</link>'
    )

    header = Table(
        [[
            [
                Paragraph("Francisco Javier Terrones Díaz", s["name"]),
                Paragraph(data["role"], s["role"]),
                Paragraph(contact, s["contact"]),
            ],
            Paragraph("FT", ParagraphStyle("Monogram", fontName="Helvetica-Bold", fontSize=19, leading=22, textColor=WHITE, alignment=1)),
        ]],
        colWidths=[158 * mm, 20 * mm],
    )
    header.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("BACKGROUND", (1, 0), (1, 0), BLUE),
                ("BOX", (1, 0), (1, 0), 0, BLUE),
                ("LEFTPADDING", (0, 0), (0, 0), 0),
                ("RIGHTPADDING", (0, 0), (0, 0), 5),
                ("LEFTPADDING", (1, 0), (1, 0), 0),
                ("RIGHTPADDING", (1, 0), (1, 0), 0),
                ("TOPPADDING", (1, 0), (1, 0), 11),
                ("BOTTOMPADDING", (1, 0), (1, 0), 11),
            ]
        )
    )

    left = [
        section_title(data["summary_title"], s["section"]),
        Paragraph(data["summary"], s["body"]),
        Spacer(1, 7),
        section_title(data["experience_title"], s["section"]),
    ]
    for item in data["experience"]:
        left.extend(experience_block(item, s))

    right = [
        section_title(data["education_title"], s["section"]),
        Paragraph(data["education"], s["side"]),
        Spacer(1, 8),
        section_title(data["skills_title"], s["section"]),
        chip_table(data["skills"], s["side"]),
        Spacer(1, 8),
        section_title(data["focus_title"], s["section"]),
        bullet_list(data["focus"], s["side"], left=9),
        Spacer(1, 6),
        section_title(data["strengths_title"], s["section"]),
        bullet_list(data["strengths"], s["side"], left=9),
    ]

    body = Table([[left, right]], colWidths=[128 * mm, 49 * mm], hAlign="LEFT")
    body.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (0, 0), 0),
                ("RIGHTPADDING", (0, 0), (0, 0), 8),
                ("LEFTPADDING", (1, 0), (1, 0), 8),
                ("RIGHTPADDING", (1, 0), (1, 0), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
                ("LINEBEFORE", (1, 0), (1, 0), 0.7, LINE),
            ]
        )
    )

    story = [header, Spacer(1, 8), body]
    doc.build(story, onFirstPage=lambda canvas, current_doc: footer(canvas, current_doc, data, s))

    reader = PdfReader(str(output))
    if len(reader.pages) != 1:
        raise RuntimeError(f"{output.name} must be one page, got {len(reader.pages)}")

    public_output = PUBLIC_DIR / data["filename"]
    copyfile(output, public_output)
    print(f"Created {output}")
    print(f"Published copy {public_output}")


if __name__ == "__main__":
    build_cv("es")
    build_cv("en")
