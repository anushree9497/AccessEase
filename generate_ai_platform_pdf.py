#!/usr/bin/env python3
"""Generate polished and one-page AI Platform Experience PDFs."""

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import HRFlowable, Paragraph, SimpleDocTemplate, Spacer
from reportlab.lib.colors import HexColor

LINKEDIN = "https://www.linkedin.com/in/thanushree-uppoor"
ACCENT = HexColor("#1a365d")
MUTED = HexColor("#4a5568")
LIGHT_RULE = HexColor("#cbd5e0")

PROJECTS = [
    {
        "title": "AirTalk — Enterprise Conversational AI Platform",
        "arch": [
            "Defined product vision for Nike's first enterprise AI assistant.",
            "Partnered with 12+ engineers and data scientists.",
            "Evaluated RAG vs. fine-tuning, balancing latency, cost, and accuracy.",
            "Drove experimentation across prompt strategies and retrieval pipelines.",
        ],
        "outcomes": [
            "Reduced employee queries by 65%; response time 12s → 3s.",
            "85% satisfaction, 99.2% uptime.",
            "First-contact resolution 45% → 72% across 8 engineering teams.",
        ],
    },
    {
        "title": "AI Cost Intelligence & Governance",
        "arch": [
            "Launched AI cost intelligence on Databricks.",
            "Worked with MLflow, model evaluation, deployment gating, observability, and AI governance.",
            "Created Nike's AI Product Development Lifecycle (PDLC) with Directors/VPs across 12 teams.",
        ],
        "outcomes": [
            "Identified $2.44M annual cost-optimization opportunity; $133K validated savings in Q1.",
            "90% weekly active usage; reduced AI token spend by 50–70%.",
            "Secured $3M+ platform funding.",
        ],
    },
    {
        "title": "Platform Console — Internal Developer Marketplace",
        "arch": [
            "Consolidated 15+ fragmented developer tools into a unified platform.",
            "Defined API-first architecture and micro-frontend strategy.",
            "Enabled global self-service onboarding for engineering teams.",
        ],
        "outcomes": [
            "$6.5M annual savings; $5M TCO reduction.",
            "92% adoption across Nike Engineering.",
        ],
    },
    {
        "title": "Nike Insights Marketplace — Data Marketplace Platform",
        "arch": [
            "Launched federated data marketplace using service-oriented architecture.",
            "Conducted 30+ customer discovery interviews; defined adoption, time-to-first-insight, and NPS metrics.",
            "Shipped ML-powered recommendations with engineering.",
        ],
        "outcomes": [
            "Identified $4M+ productivity opportunity; secured executive sponsorship.",
            "Validated product-market fit with 50+ early users.",
        ],
    },
]

SKILLS = [
    ("AI / ML", "RAG, LLMs, LangGraph, prompt strategies, retrieval pipelines, model evaluation, deployment gating, AI governance"),
    ("Data / ML Platforms", "Databricks, MLflow, SQL, data modeling"),
    ("Architecture", "APIs, microservices, service-oriented architecture, micro-frontends"),
    ("Cloud / Infrastructure", "AWS — Lambda, DynamoDB, AppSync, S3"),
    ("Observability", "New Relic, OpenTelemetry"),
    ("Product", "Product strategy, discovery, PRDs/RFCs, roadmap prioritization, experimentation, KPIs/OKRs, Agile/Scrum"),
]

SUMMARY = (
    "Senior Technical Product Manager with experience leading enterprise AI platforms, developer platforms, "
    "and data products at Nike. I work closely with engineering, data science, and leadership teams to "
    "translate complex technical capabilities into scalable products with measurable business outcomes."
)

RELEVANCE = (
    "Experience bridging engineering, data science, product, and executive stakeholders to define AI platform "
    "strategy, make architecture and technology trade-offs, establish evaluation and governance practices, "
    "improve platform adoption and reliability, and connect technical investments to measurable business value."
)

IMPACT = [
    "$12.7M+ business value delivered across enterprise platforms",
    "2,000+ global engineering users | 10,000+ retail users | 5 enterprise platforms",
]


def divider(thickness=0.75, color=LIGHT_RULE, before=8, after=10):
    return HRFlowable(width="100%", thickness=thickness, color=color, spaceBefore=before, spaceAfter=after)


def make_styles(compact=False):
    base = getSampleStyleSheet()
    scale = 0.88 if compact else 1.0

    def ps(name, **kwargs):
        return ParagraphStyle(name, parent=base["Normal"], **kwargs)

    return {
        "title": ps(
            "title",
            fontName="Helvetica-Bold",
            fontSize=22 * scale,
            leading=26 * scale,
            spaceAfter=2,
            textColor=ACCENT,
            alignment=TA_CENTER,
        ),
        "tagline": ps(
            "tagline",
            fontName="Helvetica",
            fontSize=10.5 * scale,
            leading=13 * scale,
            spaceAfter=6,
            textColor=MUTED,
            alignment=TA_CENTER,
        ),
        "meta": ps(
            "meta",
            fontName="Helvetica",
            fontSize=9 * scale,
            leading=12 * scale,
            spaceAfter=1,
            textColor=MUTED,
            alignment=TA_CENTER,
        ),
        "link": ps(
            "link",
            fontName="Helvetica",
            fontSize=9 * scale,
            leading=12 * scale,
            spaceAfter=1,
            textColor=HexColor("#2563eb"),
            alignment=TA_CENTER,
        ),
        "section": ps(
            "section",
            fontName="Helvetica-Bold",
            fontSize=11.5 * scale,
            leading=14 * scale,
            spaceBefore=10 * scale if not compact else 6,
            spaceAfter=5,
            textColor=ACCENT,
        ),
        "project": ps(
            "project",
            fontName="Helvetica-Bold",
            fontSize=10.5 * scale,
            leading=13 * scale,
            spaceBefore=7 * scale if not compact else 4,
            spaceAfter=3,
            textColor=colors.black,
        ),
        "sub": ps(
            "sub",
            fontName="Helvetica-Bold",
            fontSize=9.5 * scale,
            leading=12 * scale,
            spaceBefore=2,
            spaceAfter=2,
            textColor=HexColor("#2d3748"),
        ),
        "body": ps(
            "body",
            fontName="Helvetica",
            fontSize=9.8 * scale,
            leading=13.5 * scale,
            spaceAfter=4,
            textColor=colors.black,
        ),
        "bullet": ps(
            "bullet",
            fontName="Helvetica",
            fontSize=9.5 * scale,
            leading=12.5 * scale,
            leftIndent=14,
            spaceAfter=1.5 if compact else 2,
            textColor=colors.black,
        ),
        "skills": ps(
            "skills",
            fontName="Helvetica",
            fontSize=9.2 * scale,
            leading=12.5 * scale,
            spaceAfter=2,
            textColor=colors.black,
        ),
        "closing": ps(
            "closing",
            fontName="Helvetica",
            fontSize=9.8 * scale,
            leading=13 * scale,
            spaceBefore=8,
        ),
    }


def bullet(text, style):
    return Paragraph(f"<font color='#1a365d'>▪</font> {text}", style)


def linkedin_paragraph(style):
    return Paragraph(
        f'LinkedIn: <a href="{LINKEDIN}" color="#2563eb"><u>{LINKEDIN}</u></a>',
        style,
    )


def header(story, s, compact=False):
    link_style = s.get("link", s["meta"])
    story.append(Paragraph("THANUSHREE UPPOOR", s["title"]))
    story.append(Paragraph("AI Platform Experience", s["tagline"]))
    story.append(
        Paragraph(
            "Technical Product Manager &nbsp;|&nbsp; AI, ML &amp; LLM Platforms",
            s["meta"],
        )
    )
    story.append(
        Paragraph(
            "Bengaluru, India &nbsp;|&nbsp; uthanushree@gmail.com &nbsp;|&nbsp; +91 96866 23194",
            s["meta"],
        )
    )
    story.append(linkedin_paragraph(link_style))
    story.append(divider(before=4 if compact else 6, after=8 if compact else 10))


def add_projects(story, s, compact=False):
    for project in PROJECTS:
        story.append(Paragraph(project["title"], s["project"]))
        story.append(Paragraph("Architecture &amp; Frameworks", s["sub"]))
        for item in project["arch"]:
            story.append(bullet(item, s["bullet"]))
        story.append(Paragraph("Outcomes", s["sub"]))
        for item in project["outcomes"]:
            story.append(bullet(item, s["bullet"]))


def build_polished(output_path):
    s = make_styles(compact=False)
    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        rightMargin=0.8 * inch,
        leftMargin=0.8 * inch,
        topMargin=0.65 * inch,
        bottomMargin=0.65 * inch,
    )
    story = []
    header(story, s)
    story.append(Paragraph("OVERVIEW", s["section"]))
    story.append(Paragraph(SUMMARY, s["body"]))
    story.append(divider(before=6, after=8))
    story.append(Paragraph("PLATFORM EXPERIENCE", s["section"]))
    add_projects(story, s)
    story.append(divider(before=8, after=8))
    story.append(Paragraph("TECHNICAL PLATFORM EXPERTISE", s["section"]))
    for label, value in SKILLS:
        story.append(Paragraph(f"<b>{label}:</b> {value}", s["skills"]))
    story.append(divider(before=8, after=8))
    story.append(Paragraph("BUSINESS IMPACT", s["section"]))
    for item in IMPACT:
        story.append(bullet(item, s["bullet"]))
    story.append(Spacer(1, 4))
    story.append(Paragraph("RELEVANCE TO AGODA", s["section"]))
    story.append(Paragraph(RELEVANCE, s["body"]))
    story.append(Spacer(1, 14))
    story.append(Paragraph("Thanks,", s["closing"]))
    story.append(Paragraph("Thanushree Uppoor", s["closing"]))
    doc.build(story)
    print(f"Created: {output_path}")


def build_one_page(output_path):
    base = getSampleStyleSheet()

    def ps(name, **kwargs):
        return ParagraphStyle(name, parent=base["Normal"], **kwargs)

    s = {
        "title": ps("title", fontName="Helvetica-Bold", fontSize=17, leading=20, spaceAfter=1, textColor=ACCENT, alignment=TA_CENTER),
        "tagline": ps("tagline", fontName="Helvetica", fontSize=9, leading=11, spaceAfter=3, textColor=MUTED, alignment=TA_CENTER),
        "meta": ps("meta", fontName="Helvetica", fontSize=7.8, leading=10, spaceAfter=0.5, textColor=MUTED, alignment=TA_CENTER),
        "link": ps("link", fontName="Helvetica", fontSize=7.8, leading=10, spaceAfter=0.5, textColor=HexColor("#2563eb"), alignment=TA_CENTER),
        "section": ps("section", fontName="Helvetica-Bold", fontSize=9, leading=11, spaceBefore=4, spaceAfter=2, textColor=ACCENT),
        "project": ps("project", fontName="Helvetica-Bold", fontSize=8.6, leading=10.5, spaceBefore=3, spaceAfter=1, textColor=colors.black),
        "sub": ps("sub", fontName="Helvetica-Bold", fontSize=7.8, leading=9.5, spaceBefore=1, spaceAfter=0.5, textColor=HexColor("#2d3748")),
        "body": ps("body", fontName="Helvetica", fontSize=8.2, leading=10.5, spaceAfter=2, textColor=colors.black),
        "bullet": ps("bullet", fontName="Helvetica", fontSize=7.8, leading=9.8, leftIndent=10, spaceAfter=0.5, textColor=colors.black),
        "skills": ps("skills", fontName="Helvetica", fontSize=7.6, leading=9.5, spaceAfter=1, textColor=colors.black),
        "closing": ps("closing", fontName="Helvetica", fontSize=8.2, leading=10, spaceBefore=4),
    }

    one_page_projects = [
        {
            "title": "AirTalk — Enterprise Conversational AI",
            "arch": "RAG architecture, prompt/retrieval experimentation with 12+ engineers & data scientists.",
            "outcomes": "65% fewer queries; 12s→3s response; 85% satisfaction; FCR 45%→72%.",
        },
        {
            "title": "AI Cost Intelligence & Governance",
            "arch": "Databricks + MLflow platform; model evaluation, deployment gating, observability, AI PDLC.",
            "outcomes": "$2.44M opportunity identified; $133K Q1 savings; 50–70% token reduction; $3M+ funding.",
        },
        {
            "title": "Platform Console — Developer Marketplace",
            "arch": "Unified 15+ tools via API-first architecture and micro-frontends; global self-service onboarding.",
            "outcomes": "$6.5M savings; $5M TCO reduction; 92% engineering adoption.",
        },
        {
            "title": "Nike Insights Marketplace — Data Platform",
            "arch": "Federated data marketplace (SOA); 30+ discovery interviews; ML-powered recommendations.",
            "outcomes": "$4M+ productivity opportunity; executive sponsorship; 50+ early users.",
        },
    ]

    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        rightMargin=0.55 * inch,
        leftMargin=0.55 * inch,
        topMargin=0.45 * inch,
        bottomMargin=0.45 * inch,
    )
    story = []
    header(story, s, compact=True)
    story.append(Paragraph(SUMMARY, s["body"]))
    story.append(divider(before=2, after=4, thickness=0.5))
    story.append(Paragraph("PLATFORM EXPERIENCE", s["section"]))
    for project in one_page_projects:
        story.append(Paragraph(project["title"], s["project"]))
        story.append(Paragraph(f"<b>Architecture:</b> {project['arch']}", s["bullet"]))
        story.append(Paragraph(f"<b>Outcomes:</b> {project['outcomes']}", s["bullet"]))
    story.append(divider(before=3, after=3, thickness=0.5))
    story.append(Paragraph("TECHNICAL EXPERTISE", s["section"]))
    story.append(
        Paragraph(
            "<b>AI/ML:</b> RAG, LLMs, LangGraph, retrieval pipelines, model evaluation, AI governance &nbsp;|&nbsp; "
            "<b>Platforms:</b> Databricks, MLflow, AWS &nbsp;|&nbsp; "
            "<b>Architecture:</b> APIs, microservices, SOA, micro-frontends &nbsp;|&nbsp; "
            "<b>Observability:</b> New Relic, OpenTelemetry",
            s["skills"],
        )
    )
    story.append(Paragraph("BUSINESS IMPACT &amp; RELEVANCE TO AGODA", s["section"]))
    story.append(
        Paragraph(
            f"<b>Impact:</b> {IMPACT[0]}; {IMPACT[1]}. "
            f"<b>Relevance:</b> {RELEVANCE}",
            s["body"],
        )
    )
    story.append(Paragraph("Thanks, Thanushree Uppoor", s["closing"]))
    doc.build(story)
    print(f"Created: {output_path}")


if __name__ == "__main__":
    build_polished("/workspace/Thanushree_Uppoor_AI_Platform_Experience.pdf")
    build_one_page("/workspace/Thanushree_Uppoor_AI_Platform_Experience_OnePage.pdf")
    build_polished("/opt/cursor/artifacts/Thanushree_Uppoor_AI_Platform_Experience.pdf")
    build_one_page("/opt/cursor/artifacts/Thanushree_Uppoor_AI_Platform_Experience_OnePage.pdf")
