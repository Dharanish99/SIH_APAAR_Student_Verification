"""Render the canonical Markdown solution report to a readable, linked PDF.

Requires reportlab. Uses Windows Segoe UI fonts, or DejaVu Sans on Linux.
This is artifact tooling, not a project application.
"""
from pathlib import Path
import re
from html import escape
from urllib.parse import quote
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame, Paragraph,
    Spacer, PageBreak, LongTable, TableStyle, KeepTogether)
from reportlab.platypus.tableofcontents import TableOfContents

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'output/pdf/solution-report.pdf'
BLUE = colors.HexColor('#173650')
TEAL = colors.HexColor('#087e83')
INK = colors.HexColor('#233247')
MUTED = colors.HexColor('#596b7c')
PALE = colors.HexColor('#eef5f7')
BASE = 'https://github.com/Dharanish99/SIH_APAAR_Student_Verification/blob/main/'

def fonts():
    win = Path('C:/Windows/Fonts')
    if (win/'segoeui.ttf').exists():
        items = [('Body','segoeui.ttf'),('Body-Bold','segoeuib.ttf'),('Body-Italic','segoeuii.ttf')]
        folder = win
    else:
        folder = Path('/usr/share/fonts/truetype/dejavu')
        items = [('Body','DejaVuSans.ttf'),('Body-Bold','DejaVuSans-Bold.ttf'),('Body-Italic','DejaVuSans-Oblique.ttf')]
    for name, file in items:
        pdfmetrics.registerFont(TTFont(name, str(folder/file)))
    pdfmetrics.registerFontFamily('Body', normal='Body', bold='Body-Bold', italic='Body-Italic', boldItalic='Body-Bold')

fonts()
ST = getSampleStyleSheet()
ST.add(ParagraphStyle(name='Copy', fontName='Body', fontSize=9.7, leading=14.6, textColor=INK, spaceAfter=7))
ST.add(ParagraphStyle(name='Section', fontName='Body-Bold', fontSize=17, leading=21, textColor=BLUE, spaceBefore=15, spaceAfter=10, keepWithNext=True))
ST.add(ParagraphStyle(name='Subsection', fontName='Body-Bold', fontSize=11.8, leading=16, textColor=TEAL, spaceBefore=10, spaceAfter=6, keepWithNext=True))
ST.add(ParagraphStyle(name='Small', fontName='Body', fontSize=8.3, leading=11.5, textColor=MUTED, spaceAfter=5))
ST.add(ParagraphStyle(name='Cell', fontName='Body', fontSize=8.0, leading=11.3, textColor=INK))
ST.add(ParagraphStyle(name='CellHead', fontName='Body-Bold', fontSize=8.1, leading=11.3, textColor=colors.white))
ST.add(ParagraphStyle(name='BulletCopy', parent=ST['Copy'], leftIndent=12, firstLineIndent=-10, spaceAfter=5))
ST.add(ParagraphStyle(name='CodeCopy', fontName='Courier', fontSize=7.6, leading=11, textColor=INK, leftIndent=8, backColor=PALE, spaceAfter=7))

def normalize(s):
    return s.translate(str.maketrans({'\u2010':'-', '\u2011':'-', '\u2012':'-', '\u2013':'-', '\u2014':' - ', '\u2212':'-'}))

def inline(s):
    s = normalize(s)
    links = []
    def link(m):
        label, target = m.groups()
        if not re.match(r'https?://', target):
            path = (ROOT/'docs'/target.split('#')[0]).resolve()
            try:
                rel = path.relative_to(ROOT).as_posix()
                target = BASE + quote(rel)
            except ValueError:
                target = BASE+'docs/solution-report.md'
        token = f'ZZLINK{len(links)}ZZ'
        links.append(f'<a href="{escape(target, quote=True)}" color="#087e83"><u>{escape(label)}</u></a>')
        return token
    s = re.sub(r'\[([^\]]+)\]\(([^\s)]+)\)', link, s)
    s = escape(s)
    s = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', s)
    s = re.sub(r'`([^`]+)`', r'<font face="Courier" size="8.4">\1</font>', s)
    s = re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)', r'<i>\1</i>', s)
    for i, value in enumerate(links):
        s = s.replace(f'ZZLINK{i}ZZ', value)
    return s

class Report(BaseDocTemplate):
    def afterFlowable(self, flowable):
        if isinstance(flowable, Paragraph) and flowable.style.name in ('Section','Subsection'):
            level = 0 if flowable.style.name == 'Section' else 1
            text = flowable.getPlainText()
            key = 's'+str(self.seq.nextf('heading'))
            self.canv.bookmarkPage(key)
            if level == 0 and text != 'Report guide':
                self.canv.addOutlineEntry(text,key,0,False)
                self.notify('TOCEntry',(0,text,self.page,key))

def page(canvas, doc):
    w,h=A4
    canvas.saveState()
    if doc.page == 1:
        canvas.setFillColor(BLUE); canvas.rect(0,h-25,w,25,fill=1,stroke=0)
    else:
        canvas.setFont('Body',8); canvas.setFillColor(MUTED)
        canvas.drawString(43,h-30,'SIH26263  /  RESEARCH & SOLUTION DESIGN')
        canvas.setStrokeColor(colors.HexColor('#d6e2e8')); canvas.line(43,h-39,w-43,h-39)
    canvas.setFont('Body',7.5); canvas.setFillColor(MUTED)
    canvas.drawString(43,24,'27 OCT 2026  |  PROPOSAL - FIELD VALIDATION PENDING')
    canvas.drawRightString(w-43,24,str(doc.page))
    canvas.restoreState()

def markdown_story(text, width):
    lines=text.splitlines(); story=[]; i=0; buffer=[]
    def flush():
        if buffer:
            story.append(Paragraph(inline(' '.join(buffer)),ST['Copy'])); buffer.clear()
    while i<len(lines):
        line=lines[i].strip()
        if line.startswith('# '):
            flush(); i+=1; continue
        if line.startswith('```'):
            flush(); language=line[3:].strip(); code=[]; i+=1
            while i<len(lines) and not lines[i].strip().startswith('```'):
                code.append(lines[i]); i+=1
            if language=='mermaid':
                story.append(Paragraph('See the complete visual and editable source in the linked mind map.',ST['Small']))
            else:
                for c in code:
                    story.append(Paragraph(escape(normalize(c)).replace(' ','&#160;'),ST['CodeCopy']))
        elif line.startswith('|'):
            flush(); rows=[]
            while i<len(lines) and lines[i].strip().startswith('|'):
                cells=[x.strip() for x in lines[i].strip().strip('|').split('|')]
                if not all(re.fullmatch(r'[: -]+',c) for c in cells): rows.append(cells)
                i+=1
            i-=1
            if rows:
                n=max(len(r) for r in rows)
                weights=[min(65,max(18,max(len(r[j]) if j<len(r) else 0 for r in rows)**.73)) for j in range(n)]
                widths=[width*x/sum(weights) for x in weights]
                data=[[Paragraph(inline(c),ST['CellHead'] if ri==0 else ST['Cell']) for c in row] for ri,row in enumerate(rows)]
                table=LongTable(data,colWidths=widths,repeatRows=1,hAlign='LEFT')
                table.setStyle(TableStyle([
                    ('BACKGROUND',(0,0),(-1,0),BLUE),('VALIGN',(0,0),(-1,-1),'TOP'),
                    ('ROWBACKGROUNDS',(0,1),(-1,-1),[colors.white,PALE]),
                    ('LEFTPADDING',(0,0),(-1,-1),7),('RIGHTPADDING',(0,0),(-1,-1),7),
                    ('TOPPADDING',(0,0),(-1,-1),7),('BOTTOMPADDING',(0,0),(-1,-1),7),
                    ('LINEBELOW',(0,0),(-1,0),.4,BLUE),
                    ('LINEBELOW',(0,-1),(-1,-1),.4,colors.HexColor('#cadce2'))]))
                story.extend([table,Spacer(1,10)])
        elif line.startswith('## '):
            flush(); story.append(Paragraph(inline(line[3:]),ST['Section']))
        elif line.startswith('### '):
            flush(); story.append(Paragraph(inline(line[4:]),ST['Subsection']))
        elif re.match(r'^([-*]|\d+\.)\s+',line):
            flush(); story.append(Paragraph(inline(line),ST['BulletCopy']))
        elif line.startswith('> '):
            flush(); story.append(Paragraph(inline(line[2:]),ST['Small']))
        elif not line or line=='---': flush()
        else: buffer.append(line)
        i+=1
    flush(); return story

def main():
    OUT.parent.mkdir(parents=True,exist_ok=True)
    text=(ROOT/'docs/solution-report.md').read_text(encoding='utf-8-sig')
    title=text.splitlines()[0].lstrip('# ').strip()
    doc=Report(str(OUT),pagesize=A4,leftMargin=43,rightMargin=43,topMargin=55,bottomMargin=45,
               title=title,author='SIH research team - AI-assisted synthesis',subject='Research-grounded proposal with explicit validation limits')
    frame=Frame(43,45,A4[0]-86,A4[1]-100,id='body',leftPadding=0,rightPadding=0,topPadding=0,bottomPadding=0)
    doc.addPageTemplates(PageTemplate(id='normal',frames=[frame],onPage=page))
    cover_title=ParagraphStyle('CoverTitle',fontName='Body-Bold',fontSize=30,leading=38,textColor=BLUE,spaceAfter=20)
    cover_sub=ParagraphStyle('CoverSub',fontName='Body',fontSize=14,leading=21,textColor=MUTED,spaceAfter=22)
    story=[Spacer(1,55),Paragraph('RESEARCH TO SOLUTION',ST['Subsection']),Spacer(1,16),
        Paragraph(inline(title),cover_title),
        Paragraph('A student-centred proposal for trustworthy institutional reporting, traceable corrections and authorised verification.',cover_sub),
        Spacer(1,20),Paragraph('Evidence-led design / Complete proposed technology stack / Validation gates',ST['Copy']),
        Spacer(1,35),Paragraph('<b>Prepared 27 October 2026</b>',ST['Copy']),
        Paragraph('Built from the team\'s GitHub and Notion research, supplied uploads, specialist agent research and a reproduced synthetic experiment.',ST['Copy']),
        Paragraph('Dated research/design report; the repository now includes a separately tested synthetic prototype. No live government integration, operational deployment, institutional endorsement or field validation is claimed.',ST['Small']),
        PageBreak(),Paragraph('Report guide',ST['Section'])]
    toc=TableOfContents(); toc.levelStyles=[ParagraphStyle('TOC',fontName='Body',fontSize=10,leading=16,textColor=BLUE,spaceBefore=5,leftIndent=0,firstLineIndent=0)]
    story.extend([toc,Spacer(1,15),Paragraph('Links in the report open primary publications or the main-branch research files. The source ledgers record retrieval dates, sections and limits.',ST['Small']),PageBreak()])
    story+=markdown_story(text,A4[0]-86)
    doc.multiBuild(story)
    print(str(OUT))

if __name__=='__main__': main()
