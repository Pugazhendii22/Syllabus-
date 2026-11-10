#!/usr/bin/env python3
"""Validate downloadable file signatures, page counts and Word transcription order without dependencies."""
import json
import hashlib
import re
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

base=Path('notes/spoken-english')
notes=json.loads(Path('prepared-notes.json').read_text())
marker='\n\nThe wording below is transcribed from the shared Spoken English PDF. Open the reference above for the original pages and formatting.\n\n'
transcripts=[]
for i in range(1,6):
    entry=next(n for n in notes[f'course-4:{i-1}'] if n['id']==f'spoken-original-pdf-unit-{i}')
    transcripts.append(entry['text'].split(marker,1)[1].strip())
unit_texts=[transcripts[0][transcripts[0].index('## UNIT I - WORKING WITH GRAMMAR'):]]+transcripts[1:]

def tokens(s):
    # Markdown separators and formatting are not content.
    s='\n'.join(line for line in s.splitlines() if not re.fullmatch(r'\s*\|(?:\s*:?-+:?\s*\|)+\s*',line))
    s=s.replace('**','').replace('#','').replace('|',' ')
    return re.findall(r"[\w]+(?:['’-][\w]+)*",s)

def document_text(path):
    with zipfile.ZipFile(path) as z:
        assert z.testzip() is None
        root=ET.fromstring(z.read('word/document.xml'))
        return ' '.join(x.text or '' for x in root.iter('{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t'))

def check_docx(path, expected):
    got=tokens(document_text(path));want=tokens(expected)
    assert got==want, f'{path}: Word content differs from the ordered transcription'

def check_pdf(path,count):
    b=path.read_bytes(); assert b.startswith(b'%PDF-') and b.rstrip().endswith(b'%%EOF'),str(path)
    assert len(re.findall(rb'/Type\s*/Page\b',b))==count, f'{path}: unexpected page count'

check_pdf(base/'Spoken_English_Notes.pdf',35)
assert hashlib.sha256((base/'Spoken_English_Notes.pdf').read_bytes()).hexdigest() == '230ecaa948e0a86b0b2943e76f8a32be6caf17749b0e65da9c4c606cfa8577f6', 'original PDF must match the newly uploaded document'
for i,count in enumerate([10,10,5,4,5],1):
    check_pdf(base/f'downloads/Spoken-English-Unit-{i}.pdf',count)
    check_docx(base/f'downloads/Spoken-English-Unit-{i}.docx',unit_texts[i-1])
check_docx(base/'downloads/Spoken-English-All-Units.docx','\n'.join(transcripts))
assert all(x in transcripts[1] for x in ['**I** did not take your pen.', 'I did not **take** your pen.', 'I did not take **your** pen.', 'I did not take your **pen**.'])
with zipfile.ZipFile(base/'downloads/Spoken-English-Unit-2.docx') as z:
    xml=ET.fromstring(z.read('word/document.xml'))
    ns={'w':'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
    bold=[r.find('w:t',ns).text for r in xml.findall('.//w:r',ns) if r.find('w:rPr/w:b',ns) is not None and r.find('w:t',ns) is not None]
    assert all(x in bold for x in ['I','take','your','pen']), 'sentence-stress emphasis must survive Word conversion'
print('PASS: Spoken English download PDF signatures/page counts and ordered Word transcriptions')
