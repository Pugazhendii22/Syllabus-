"""Remove generic repeated teaching-draft boilerplate, preserving specific caveats."""
import json
from pathlib import Path
p=Path(__file__).with_name('prepared-notes.json')
d=json.loads(p.read_text(encoding='utf8'))
exact={
 'Compare this teaching draft with the assigned text and edition.',
 'Use the assigned text and edition alongside these teaching notes; check details and interpretations before teaching.',
 'Read the assigned text and verify its wording and selection against the course anthology.',
}
removed=0
for entries in d.values():
 for note in entries:
  kept=[]
  for line in note['text'].splitlines():
   if line.startswith('Teaching draft:') or line in exact:
    removed+=1
    continue
   if line=='This is an extended story overview, not a complete chapter-by-chapter guide. Check the assigned novel and edition before teaching.':
    line='This is a story overview rather than a chapter-by-chapter guide.'
   kept.append(line)
  note['text']='\n'.join(kept).rstrip()+'\n'
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
print(f'Removed {removed} repeated generic notices; kept specific content and preliminary statuses.')
