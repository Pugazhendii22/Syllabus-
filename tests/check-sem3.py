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
# The first substantial lesson batch spans all four of Ammu's current subjects.
lesson_batch = {
    'course-1:0': ['chaucer-prologue', 'spenser-epithalamion', 'sonnet-116', 'sonnet-130'],
    'course-2:0': ['communication-basics', 'comm-practice-1'],
    'course-19:0': ['o-henry-twenty', 'assadi-ring', 'kincaid-girl', 'grammar-64–74'],
    'course-20:0': ['func-writing-1', 'writing-workshop-types'],
}
for key, ids in lesson_batch.items():
    for ident in ids:
        assert len(get(key, ident)['text']) > 3500, (key, ident)
second_batch = {
    'course-1:1': ['donne-valediction', 'milton-paradise-ix', 'pope-lock-canto1'],
    'course-2:1': ['listening-speaking', 'comm-practice-2'],
    'course-19:1': ['raja-cow', 'huxley-beauty', 'grammar-75–83'],
    'course-20:1': ['func-writing-2', 'writing-workshop-precis'],
}
for key, ids in second_batch.items():
    for ident in ids:
        assert len(get(key, ident)['text']) > 3200, (key, ident)
assert 'outside the specified lines' in get('course-1:1','milton-paradise-ix')['text']
assert get('course-19:1','grammar-75–83').get('status') == 'preliminary'
assert 'translation and any excerpt' in get('course-19:0','assadi-ring')['text']
assert 'do not establish' in get('course-19:0','grammar-64–74')['text']
print('PASS: target syllabus keys, fields, unique IDs, preliminary labels and audit content; two detailed lesson batches')
