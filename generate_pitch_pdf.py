#!/usr/bin/env python3
"""Generate a polished investor pitch PDF for FuturesSquawk."""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch, mm
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, HRFlowable
)
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
import os

# Colors
DARK_BG = HexColor('#0a0e17')
CARD_BG = HexColor('#1a2035')
CYAN = HexColor('#06b6d4')
GREEN = HexColor('#22c55e')
RED = HexColor('#ef4444')
YELLOW = HexColor('#eab308')
ORANGE = HexColor('#f97316')
BLUE = HexColor('#3b82f6')
PURPLE = HexColor('#a855f7')
WHITE = HexColor('#e2e8f0')
MUTED = HexColor('#94a3b8')
DARK_MUTED = HexColor('#64748b')
ACCENT = HexColor('#06b6d4')
DARK_CARD = HexColor('#111827')
BORDER = HexColor('#2a3550')

# Light theme for print
BG = HexColor('#ffffff')
TEXT = HexColor('#1a1a2e')
TEXT_SEC = HexColor('#4a4a6a')
HEADING = HexColor('#0a0e17')
ACCENT_BLUE = HexColor('#1e40af')
ACCENT_CYAN = HexColor('#0891b2')
LIGHT_BG = HexColor('#f1f5f9')
TABLE_HEAD = HexColor('#0f172a')
TABLE_HEAD_TEXT = HexColor('#ffffff')
TABLE_ALT = HexColor('#f8fafc')
BORDER_LIGHT = HexColor('#e2e8f0')

output_path = os.path.join(os.path.dirname(__file__), 'FuturesSquawk_Investor_Pitch.pdf')

doc = SimpleDocTemplate(
    output_path,
    pagesize=A4,
    topMargin=0.6*inch,
    bottomMargin=0.6*inch,
    leftMargin=0.7*inch,
    rightMargin=0.7*inch,
)

# Styles
styles = {
    'title': ParagraphStyle('Title', fontName='Helvetica-Bold', fontSize=28, textColor=HEADING, spaceAfter=4, leading=34),
    'subtitle': ParagraphStyle('Subtitle', fontName='Helvetica', fontSize=14, textColor=ACCENT_CYAN, spaceAfter=2, leading=18),
    'date': ParagraphStyle('Date', fontName='Helvetica', fontSize=10, textColor=TEXT_SEC, spaceAfter=20),
    'h1': ParagraphStyle('H1', fontName='Helvetica-Bold', fontSize=20, textColor=HEADING, spaceBefore=20, spaceAfter=10, leading=26),
    'h2': ParagraphStyle('H2', fontName='Helvetica-Bold', fontSize=15, textColor=ACCENT_BLUE, spaceBefore=14, spaceAfter=8, leading=20),
    'h3': ParagraphStyle('H3', fontName='Helvetica-Bold', fontSize=12, textColor=HEADING, spaceBefore=10, spaceAfter=6, leading=16),
    'body': ParagraphStyle('Body', fontName='Helvetica', fontSize=10, textColor=TEXT, spaceAfter=6, leading=15),
    'body_bold': ParagraphStyle('BodyBold', fontName='Helvetica-Bold', fontSize=10, textColor=TEXT, spaceAfter=6, leading=15),
    'bullet': ParagraphStyle('Bullet', fontName='Helvetica', fontSize=10, textColor=TEXT, spaceAfter=4, leading=14, leftIndent=20, bulletIndent=8),
    'small': ParagraphStyle('Small', fontName='Helvetica', fontSize=8, textColor=TEXT_SEC, spaceAfter=4, leading=11),
    'highlight': ParagraphStyle('Highlight', fontName='Helvetica-Bold', fontSize=11, textColor=ACCENT_CYAN, spaceAfter=6, leading=15),
    'center': ParagraphStyle('Center', fontName='Helvetica', fontSize=10, textColor=TEXT_SEC, alignment=TA_CENTER, spaceAfter=6),
    'footer': ParagraphStyle('Footer', fontName='Helvetica-Oblique', fontSize=8, textColor=TEXT_SEC, alignment=TA_CENTER),
}

def hr():
    return HRFlowable(width="100%", thickness=1, color=BORDER_LIGHT, spaceBefore=10, spaceAfter=10)

def spacer(h=10):
    return Spacer(1, h)

def make_table(headers, rows, col_widths=None):
    data = [headers] + rows
    w = col_widths or [doc.width / len(headers)] * len(headers)
    t = Table(data, colWidths=w, repeatRows=1)
    style = [
        ('BACKGROUND', (0, 0), (-1, 0), TABLE_HEAD),
        ('TEXTCOLOR', (0, 0), (-1, 0), TABLE_HEAD_TEXT),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 9),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 9),
        ('TEXTCOLOR', (0, 1), (-1, -1), TEXT),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('GRID', (0, 0), (-1, -1), 0.5, BORDER_LIGHT),
        ('TOPPADDING', (0, 0), (-1, -1), 5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 5),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
    ]
    # Alternate row colors
    for i in range(1, len(data)):
        if i % 2 == 0:
            style.append(('BACKGROUND', (0, i), (-1, i), TABLE_ALT))
    t.setStyle(TableStyle(style))
    return t

# Build content
story = []

# ── COVER PAGE ──
story.append(spacer(120))
story.append(Paragraph('FuturesSquawk', styles['title']))
story.append(Paragraph('Institutional-Grade Market Intelligence for Retail Traders', styles['subtitle']))
story.append(spacer(8))
story.append(Paragraph('Investor Pitch  |  April 2026  |  Confidential', styles['date']))
story.append(spacer(30))
story.append(HRFlowable(width="40%", thickness=2, color=ACCENT_CYAN, spaceBefore=0, spaceAfter=20))
story.append(spacer(20))
story.append(Paragraph('Live Product: sks11.github.io/futures-squawk', styles['body']))
story.append(Paragraph('Contact: shravanksinghdce@gmail.com', styles['body']))
story.append(PageBreak())

# ── THE PROBLEM ──
story.append(Paragraph('The Problem', styles['h1']))
story.append(hr())
story.append(Paragraph(
    'Every day, <b>165 million</b> retail traders in the US make decisions with delayed, fragmented information. '
    'When Trump posts about tariffs, oil spikes 5% in pre-market — by the time a retail trader reads the headline on CNBC, the move is done.',
    styles['body']))
story.append(spacer(8))
story.append(Paragraph('Meanwhile, institutions have:', styles['body_bold']))
story.append(Paragraph('&bull; Real-time political sentiment analysis', styles['bullet']))
story.append(Paragraph('&bull; Dark pool and options flow data', styles['bullet']))
story.append(Paragraph('&bull; Insider buying alerts', styles['bullet']))
story.append(Paragraph('&bull; Sector rotation tracking', styles['bullet']))
story.append(spacer(8))
story.append(Paragraph(
    '<b>Retail traders pay the "information delay tax" on every trade.</b> '
    'The tools that solve this cost $100-250/month and are designed for professionals, '
    'not the 75% of retail traders who trade from their phones.',
    styles['body']))

# ── THE SOLUTION ──
story.append(spacer(16))
story.append(Paragraph('The Solution', styles['h1']))
story.append(hr())
story.append(Paragraph(
    '<b>FuturesSquawk</b> is a real-time market intelligence platform that gives retail traders '
    'institutional-grade signals at <b>1/10th the cost</b>.',
    styles['body']))
story.append(spacer(8))

story.append(make_table(
    ['Feature', 'What It Does'],
    [
        ['Real-Time News Feed', 'Aggregated headlines with AI sentiment (bullish/bearish/neutral)'],
        ['Trump & Political Alerts', 'Instant signals when political posts move markets'],
        ['Smart Money Tracker', '13F filings, insider buying, dark pool activity, fund flows'],
        ['Sector Rotation Heatmap', 'Where institutions are moving billions — 1mo/3mo/6mo views'],
        ['Momentum Screener', 'Reddit WSB buzz, unusual volume, pre-market movers'],
        ['Early Innings Detector', 'Stocks with multiple institutional signals converging'],
        ['Paper Trading Simulator', '$1,000 virtual portfolio with auto-trade from signals'],
        ['Trade Signals', 'BUY/SELL/HOLD with urgency levels and confidence scores'],
    ],
    [160, doc.width - 160]
))

story.append(PageBreak())

# ── MARKET OPPORTUNITY ──
story.append(Paragraph('Market Opportunity', styles['h1']))
story.append(hr())
story.append(Paragraph('Total Addressable Market', styles['h2']))

story.append(make_table(
    ['Metric', 'Value', 'Source'],
    [
        ['US retail stock traders', '165 million', 'BestBrokers 2026'],
        ['Retail equity inflows (2025)', '$302 billion (+53% YoY)', 'Gitnux Research'],
        ['Retail share of US equity volume', '20-25% (peaks at 35%)', 'MEMX 2025'],
        ['Global fintech SaaS market (2024)', '$320 billion', 'Virtue Market Research'],
        ['Projected fintech SaaS (2030)', '$725 billion (14.6% CAGR)', 'Virtue Market Research'],
        ['Algorithmic trading market (2024)', '$21 billion', 'Grand View Research'],
        ['Projected algo trading (2030)', '$43 billion (12.9% CAGR)', 'Grand View Research'],
    ],
    [160, 160, doc.width - 320]
))
story.append(spacer(10))
story.append(Paragraph('Serviceable Market', styles['h2']))
story.append(Paragraph('&bull; <b>Target:</b> Active retail traders who spend on trading tools', styles['bullet']))
story.append(Paragraph('&bull; Estimated 8-12 million US traders pay for at least one premium tool', styles['bullet']))
story.append(Paragraph('&bull; At $29-79/month average, this is a <b>$2.8B - $11.4B annual market</b>', styles['bullet']))
story.append(Paragraph('&bull; 75% trade on mobile — most existing tools are desktop-first', styles['bullet']))

# ── COMPETITIVE LANDSCAPE ──
story.append(spacer(16))
story.append(Paragraph('Competitive Landscape', styles['h1']))
story.append(hr())

story.append(make_table(
    ['Platform', 'Price', 'Strengths', 'Weaknesses'],
    [
        ['Benzinga Pro', '$99-177/mo', 'Fastest news desk', 'No smart money, no paper trading'],
        ['Unusual Whales', '$50/mo', 'Options flow, Congress trades', 'No news feed, no sector rotation'],
        ['FlowAlgo', '$29-149/mo', 'Dark pool, options sweeps', 'No political alerts, no social buzz'],
        ['Trade Ideas', '$167/mo', 'AI stock scanner', 'Very expensive, desktop-only'],
        ['TradingView', '$13-60/mo', 'Charts, community', 'No signals, no smart money'],
    ],
    [90, 75, 140, doc.width - 305]
))
story.append(spacer(10))
story.append(Paragraph('Our Competitive Advantage', styles['h2']))

story.append(make_table(
    ['Feature', 'Benzinga', 'UW', 'FlowAlgo', 'FuturesSquawk'],
    [
        ['Real-time news + sentiment', 'Yes', 'No', 'No', 'YES'],
        ['Political / Trump alerts', 'No', 'Partial', 'No', 'YES'],
        ['Smart money (13F + insider)', 'No', 'Partial', 'Partial', 'YES'],
        ['Sector rotation heatmap', 'No', 'No', 'No', 'YES'],
        ['Social / Reddit momentum', 'No', 'No', 'No', 'YES'],
        ['Paper trading', 'No', 'No', 'No', 'YES'],
        ['Auto-trade signals', 'No', 'No', 'No', 'YES'],
        ['Mobile-first', 'No', 'Yes', 'Yes', 'YES'],
        ['Price', '$99-177', '$50', '$29-149', '$29-79'],
    ],
    [130, 60, 45, 65, doc.width - 300]
))
story.append(spacer(6))
story.append(Paragraph(
    '<b>We are the only platform that combines news intelligence, smart money tracking, '
    'social momentum, political signals, AND paper trading in one mobile-first dashboard.</b>',
    styles['highlight']))

story.append(PageBreak())

# ── BUSINESS MODEL ──
story.append(Paragraph('Business Model', styles['h1']))
story.append(hr())
story.append(Paragraph('Pricing Tiers', styles['h2']))

story.append(make_table(
    ['Tier', 'Price', 'Key Features', 'Target'],
    [
        ['Free', '$0/mo', 'Delayed news, basic sentiment, paper trading, 3 scans/day', 'Lead gen, viral growth'],
        ['Pro', '$29/mo', 'Real-time news, smart money, Trump alerts, unlimited scans', 'Active retail traders'],
        ['Elite', '$79/mo', 'Pro + options flow, dark pool, LLM sentiment, SMS alerts', 'Serious day traders'],
        ['API', '$199/mo', 'Programmatic access to all signals and data', 'Algo traders, devs'],
    ],
    [50, 55, 250, doc.width - 355]
))

story.append(spacer(10))
story.append(Paragraph('Revenue Projections', styles['h2']))

story.append(make_table(
    ['Metric', 'Year 1', 'Year 2', 'Year 3'],
    [
        ['Free users', '10,000', '50,000', '200,000'],
        ['Pro subscribers', '500', '3,000', '15,000'],
        ['Elite subscribers', '100', '800', '4,000'],
        ['API subscribers', '10', '50', '200'],
        ['Monthly Revenue', '$22,490', '$133,850', '$787,300'],
        ['Annual Revenue', '$269,880', '$1.6M', '$9.4M'],
        ['Free → Paid conversion', '6%', '7.6%', '9.6%'],
    ],
    [130, (doc.width-130)/3, (doc.width-130)/3, (doc.width-130)/3]
))

story.append(spacer(10))
story.append(Paragraph('Unit Economics', styles['h2']))

story.append(make_table(
    ['Metric', 'Value'],
    [
        ['Customer Acquisition Cost (CAC)', '$15-25 (content marketing + viral)'],
        ['LTV at 8-month avg retention', '$232 (Pro) / $632 (Elite)'],
        ['LTV:CAC Ratio', '9:1 - 25:1'],
        ['Gross Margin', '85-90%'],
        ['Monthly infra cost per user', '~$0.50'],
    ],
    [180, doc.width - 180]
))

# ── TRACTION ──
story.append(spacer(16))
story.append(Paragraph('Traction & Validation', styles['h1']))
story.append(hr())
story.append(Paragraph('Current State (Pre-Revenue)', styles['h2']))
story.append(Paragraph('&bull; <b>Working product</b> deployed live at sks11.github.io/futures-squawk', styles['bullet']))
story.append(Paragraph('&bull; Zero infrastructure cost — single HTML file proves the concept', styles['bullet']))
story.append(Paragraph('&bull; Paper trading simulator with $1,000 virtual portfolios', styles['bullet']))
story.append(Paragraph('&bull; 10+ sector ETFs tracked for rotation analysis', styles['bullet']))
story.append(Paragraph('&bull; 15+ data feeds aggregated in real-time', styles['bullet']))
story.append(Paragraph('&bull; Smart money scanner: 13F filings, insider buying, fund flows', styles['bullet']))
story.append(Paragraph('&bull; Mobile-responsive design', styles['bullet']))
story.append(spacer(6))
story.append(Paragraph('Early Signals', styles['h2']))
story.append(Paragraph('&bull; Organic interest from trader community before any marketing', styles['bullet']))
story.append(Paragraph('&bull; Feature requests from beta users (login, portfolios, real-money trading)', styles['bullet']))
story.append(Paragraph('&bull; Problem validated: users asking for "early innings institutional flow detection"', styles['bullet']))
story.append(Paragraph('&bull; Every feature built in response to real user demand, not speculation', styles['bullet']))

story.append(PageBreak())

# ── GO-TO-MARKET ──
story.append(Paragraph('Go-To-Market Strategy', styles['h1']))
story.append(hr())

story.append(Paragraph('Phase 1: Community-Led Growth (Month 1-3)', styles['h2']))
story.append(Paragraph('&bull; Launch free tier on Product Hunt, Reddit (r/wallstreetbets, r/stocks)', styles['bullet']))
story.append(Paragraph('&bull; Content play: "I paper-traded $1K based on Trump tweets for 30 days"', styles['bullet']))
story.append(Paragraph('&bull; This content format has <b>proven virality</b> on Twitter/X and Reddit', styles['bullet']))
story.append(Paragraph('&bull; Target: 1,000 free users, 50 paid conversions', styles['bullet']))

story.append(Paragraph('Phase 2: Content + SEO (Month 3-6)', styles['h2']))
story.append(Paragraph('&bull; Daily auto-generated market intelligence reports', styles['bullet']))
story.append(Paragraph('&bull; YouTube shorts: "Smart money is quietly buying [SECTOR]"', styles['bullet']))
story.append(Paragraph('&bull; Twitter/X bot posting signals (free marketing)', styles['bullet']))
story.append(Paragraph('&bull; Target: 10,000 free users, 500 paid', styles['bullet']))

story.append(Paragraph('Phase 3: Partnerships (Month 6-12)', styles['h2']))
story.append(Paragraph('&bull; Broker integration (Alpaca, Webull, Interactive Brokers)', styles['bullet']))
story.append(Paragraph('&bull; White-label for trading communities and Discord servers', styles['bullet']))
story.append(Paragraph('&bull; Affiliate program for finance influencers', styles['bullet']))
story.append(Paragraph('&bull; Target: 50,000 free users, 3,000 paid', styles['bullet']))

story.append(spacer(10))
story.append(Paragraph('Viral Mechanics', styles['h2']))
story.append(Paragraph('&bull; <b>Paper trading leaderboard</b> — users share P&L screenshots', styles['bullet']))
story.append(Paragraph('&bull; <b>Signal accuracy tracker</b> — public track record builds trust', styles['bullet']))
story.append(Paragraph('&bull; <b>Free tier is genuinely useful</b> — drives word of mouth', styles['bullet']))
story.append(Paragraph('&bull; <b>Political trading angle</b> — inherently newsworthy and shareable', styles['bullet']))

# ── TECHNOLOGY ──
story.append(spacer(16))
story.append(Paragraph('Technology', styles['h1']))
story.append(hr())

story.append(make_table(
    ['Layer', 'Technology', 'Cost'],
    [
        ['Frontend', 'Next.js (React)', 'Free'],
        ['Auth', 'Supabase Auth (Google/email login)', 'Free tier'],
        ['Database', 'Supabase Postgres', 'Free tier'],
        ['Backend', 'Next.js API Routes + Edge Functions', 'Free'],
        ['Real-time data', 'Finnhub WebSocket', 'Free tier'],
        ['Sentiment AI', 'Claude API (Anthropic)', '~$20/mo at scale'],
        ['Hosting', 'Vercel (auto-scaling)', 'Free tier'],
        ['Payments', 'Stripe', '2.9% + 30c per txn'],
    ],
    [100, 220, doc.width - 320]
))
story.append(spacer(6))
story.append(Paragraph('<b>Total cost to launch: $0/month</b> (all free tiers). Scales to 100K users at ~$2,500/month.', styles['highlight']))

story.append(PageBreak())

# ── THE ASK ──
story.append(Paragraph('The Ask', styles['h1']))
story.append(hr())
story.append(Paragraph('Seed Round: $250,000', styles['h2']))

story.append(make_table(
    ['Use of Funds', 'Amount', 'Purpose'],
    [
        ['Engineering (2 hires, 6 months)', '$150,000', 'Backend engineer + growth marketer'],
        ['Premium data APIs', '$30,000', 'Polygon, options flow, dark pool (12 months)'],
        ['Infrastructure & scaling', '$20,000', 'Vercel Pro, Supabase Pro, monitoring'],
        ['Marketing & launch', '$30,000', 'Content creation, ads, Product Hunt'],
        ['Legal & compliance', '$20,000', 'ToS, financial disclaimers, incorporation'],
    ],
    [160, 70, doc.width - 230]
))

story.append(spacer(14))
story.append(Paragraph('Milestones', styles['h2']))

story.append(make_table(
    ['Timeline', 'Milestone'],
    [
        ['Month 1-2', 'Next.js migration, auth, database, premium data integration'],
        ['Month 3', 'Public launch with Free + Pro tiers'],
        ['Month 4-6', '5,000 free users, 300 paying subscribers'],
        ['Month 6-9', 'Elite tier launch, broker integration, mobile app'],
        ['Month 9-12', '25,000 free users, 2,000 paying subscribers, $50K MRR'],
    ],
    [80, doc.width - 80]
))

story.append(spacer(14))
story.append(Paragraph('Return Potential', styles['h2']))
story.append(Paragraph(
    'At <b>$9.4M ARR</b> (Year 3) with a conservative 8x revenue multiple for fintech SaaS:',
    styles['body']))
story.append(spacer(4))
story.append(Paragraph('Projected valuation: <b>$75M</b>', styles['highlight']))
story.append(Paragraph('Seed investors at $250K on a $2M cap = <b>37.5x return</b>', styles['highlight']))

# ── WHY NOW ──
story.append(spacer(16))
story.append(Paragraph('Why Now?', styles['h1']))
story.append(hr())
story.append(Paragraph('1. <b>Political trading is a new asset class.</b> Trump\'s posts move markets instantly. No tool is purpose-built for this.', styles['body']))
story.append(Paragraph('2. <b>Retail trading has exploded.</b> $302B inflows in 2025 (+53% YoY). 165M Americans trade stocks.', styles['body']))
story.append(Paragraph('3. <b>75% trade on mobile.</b> Most institutional tools are desktop-first. Massive gap.', styles['body']))
story.append(Paragraph('4. <b>AI enables real-time sentiment at scale.</b> LLMs analyze headlines at institutional accuracy for pennies. Wasn\'t possible 2 years ago.', styles['body']))
story.append(Paragraph('5. <b>Smart money data is democratizing.</b> SEC EDGAR, FINRA provide free data that was institution-only. Someone needs to package it for retail.', styles['body']))

# ── CONTACT ──
story.append(spacer(30))
story.append(HRFlowable(width="100%", thickness=2, color=ACCENT_CYAN, spaceBefore=0, spaceAfter=14))
story.append(Paragraph('<b>Shravan Kumar Singh</b>  |  Founder & Developer', styles['body']))
story.append(Paragraph('shravanksinghdce@gmail.com', styles['body']))
story.append(Paragraph('Live Product: sks11.github.io/futures-squawk', styles['body']))
story.append(Paragraph('Source: github.com/sks11/futures-squawk', styles['body']))
story.append(spacer(20))
story.append(Paragraph(
    'This document is confidential and intended for potential investors only. '
    'FuturesSquawk does not provide financial advice. All trading signals are informational and for educational purposes.',
    styles['footer']))

# Build PDF
doc.build(story)
print(f"PDF generated: {output_path}")
