#!/usr/bin/env python3
"""Generate downloadable editions of the user's Spoken English PDF.
Requires python-docx and pypdf; reads only the supplied PDF and its existing unit transcriptions.
"""
import json
import re
from pathlib import Path
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from pypdf import PdfReader, PdfWriter

ROOT = Path(__file__).resolve().parent.parent
DEST = ROOT/'notes/spoken-english/downloads'
ORIGINAL = ROOT/'notes/spoken-english/Spoken_English_Notes.pdf'
NOTES = json.loads((ROOT/'prepared-notes.json').read_text(encoding='utf-8'))
PAGES = [(1, 11), (11, 21), (21, 26), (26, 30), (30, 35)] # zero-based, inclusive start/exclusive end
ROMAN = ['I','II','III','IV','V']
DEST.mkdir(parents=True, exist_ok=True)
reader = PdfReader(str(ORIGINAL))
assert len(reader.pages) == 35

def inline(paragraph, text):
    parts=re.split(r'(\*\*.*?\*\*)', text)
    for part in parts:
        bold=part.startswith('**') and part.endswith('**')
        run=paragraph.add_run(part[2:-2] if bold else part)
        run.bold=bold

def shade(cell):
    tcpr=cell._tc.get_or_add_tcPr(); shd=OxmlElement('w:shd'); shd.set(qn('w:fill'),'DCEFFA'); tcpr.append(shd)

def render(doc, text):
    lines=text.splitlines(); i=0
    while i < len(lines):
        line=lines[i].strip()
        if not line:
            i+=1; continue
        if line.startswith('|') and i+1<len(lines) and re.fullmatch(r'\|(?:\s*:?-+:?\s*\|)+',lines[i+1].strip()):
            split=lambda x:[c.strip() for c in x.strip().strip('|').split('|')]
            header=split(line); rows=[]; i+=2
            while i<len(lines) and lines[i].strip().startswith('|'):
                rows.append(split(lines[i])); i+=1
            table=doc.add_table(rows=1, cols=len(header));table.style='Table Grid';table.alignment=WD_TABLE_ALIGNMENT.CENTER
            for c,val in zip(table.rows[0].cells,header): inline(c.paragraphs[0],val); shade(c)
            for row in rows:
                cells=table.add_row().cells
                for c,val in zip(cells,row): inline(c.paragraphs[0],val)
            for row in table.rows:
                for cell in row.cells:
                    for p in cell.paragraphs:
                        for run in p.runs: run.font.size=Pt(9)
            doc.add_paragraph(''); continue
        if line.startswith('## '):
            doc.add_heading(line[3:],level=1 if line.startswith('## UNIT ') else 2); i+=1; continue
        if line.startswith('•'):
            chunks=[line[1:].strip()];i+=1
            while i<len(lines):
                nextline=lines[i].strip()
                if not nextline or nextline.startswith(('•','## ','|')) or re.match(r'^\d+\. ',nextline): break
                chunks.append(nextline);i+=1
            paragraph=doc.add_paragraph(style='List Bullet');inline(paragraph,' '.join(chunks));continue
        # Preserve source paragraphs: join line-wrapped PDF lines, not adjacent numbered examples or dialogue lines.
        chunks=[line];i+=1
        while i<len(lines):
            nxt=lines[i].strip()
            if not nxt or nxt.startswith(('•','## ','|')) or re.match(r'^\d+\. ',nxt) or re.match(r'^(?:A|B|C|D|Priya|Arun|Tourist|Local|Opening|Close|Closing|Point \d+): ',nxt): break
            if re.match(r'^\d+\. ',chunks[0]): break
            chunks.append(nxt);i+=1
        paragraph=doc.add_paragraph(); inline(paragraph,' '.join(chunks))

def doc_template():
    doc=Document(); sec=doc.sections[0];sec.top_margin=Inches(.7);sec.bottom_margin=Inches(.7);sec.left_margin=Inches(.72);sec.right_margin=Inches(.72)
    style=doc.styles['Normal'];style.font.name='Calibri';style.font.size=Pt(11);style.paragraph_format.space_after=Pt(5)
    for name in ['Heading 1','Heading 2']:
        doc.styles[name].font.name='Calibri';doc.styles[name].font.color.rgb=RGBColor.from_string('205B80')
    return doc

transcripts=[]
for i in range(5):
    entry=next(n for n in NOTES[f'course-4:{i}'] if n['id']==f'spoken-original-pdf-unit-{i+1}')
    marker='\n\nThe wording below is transcribed from the shared Spoken English PDF. Open the reference above for the original pages and formatting.\n\n'
    assert marker in entry['text']; transcripts.append(entry['text'].split(marker,1)[1].strip())
unit1_heading='## UNIT I - WORKING WITH GRAMMAR'; assert unit1_heading in transcripts[0]
unit_transcripts=[transcripts[0][transcripts[0].index(unit1_heading):]]+transcripts[1:]
for i,((start,end),text) in enumerate(zip(PAGES,unit_transcripts),1):
    writer=PdfWriter()
    for page in reader.pages[start:end]:writer.add_page(page)
    with (DEST/f'Spoken-English-Unit-{i}.pdf').open('wb') as f:writer.write(f)
    doc=doc_template();render(doc,text);doc.save(DEST/f'Spoken-English-Unit-{i}.docx')
doc=doc_template()
for i,text in enumerate(transcripts):
    if i:doc.add_page_break()
    render(doc,text)
doc.save(DEST/'Spoken-English-All-Units.docx')
print('Generated five unit PDFs and six Word documents; the original PDF remains the all-units PDF.')
