"""Checks for the targeted audit, independently of any external services."""
import json
from pathlib import Path
p=Path(__file__).resolve().parent.parent
notes=json.loads((p/'prepared-notes.json').read_text(encoding='utf-8'))
courses=json.loads((p/'courses.json').read_text(encoding='utf-8'))
for course in courses:
    if course['id'] in {'course-1','course-2','course-19','course-20'}:
        for i in range(len(course['units'])):
            assert f"{course['id']}:{i}" in notes
for key, selections in notes.items():
    assert len({x['id'] for x in selections})==len(selections), key
    assert all(all(x.get(field) for field in ('id','title','source','text')) for x in selections), key

def get(k, ident):
    return next(x for x in notes[k] if x['id']==ident)
for key,ident in [('course-19:0','assadi-ring'),('course-19:2','ghosh-sea')]:
    assert get(key,ident).get('status')=='preliminary'
for i in range(5):
    grammar=[n for n in notes[f'course-19:{i}'] if n['id'].startswith('grammar-')]
    assert len(grammar)==1 and grammar[0].get('status')=='preliminary'
assert 'separately named Mahatma' in get('course-19:1','raja-cow')['text']
assert '30.' in get('course-2:2','reading-skills')['text']
assert '20.' in get('course-2:3','writing-skills')['text']
assert '| Type | Direct speech | Possible indirect form |' in get('course-20:4','func-writing-5')['text']
print('PASS: target syllabus keys, fields, unique IDs, preliminary labels and audit content')
