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
# Complete reading explanations must appear before the shorter teaching notes.
full_readings = {
    'course-1:0': ['chaucer-prologue', 'spenser-epithalamion', 'sonnet-116', 'sonnet-130'],
    'course-1:1': ['donne-valediction', 'milton-paradise-ix', 'pope-lock-canto1'],
    'course-19:0': ['o-henry-twenty', 'assadi-ring', 'kincaid-girl'],
    'course-19:1': ['raja-cow', 'huxley-beauty'],
}
for key, ids in full_readings.items():
    for ident in ids:
        text = get(key, ident)['text']
        first_heading = next(line for line in text.splitlines() if line.startswith('## '))
        assert first_heading.startswith('## Full '), (key, ident)
        assert len(text) > 6000, (key, ident)
assert 'after line 732' in get('course-1:1', 'milton-paradise-ix')['text']
assert 'not a verified copy' in get('course-19:0', 'assadi-ring')['text']
assert 'names Gandhi and the Master separately' in get('course-19:1', 'raja-cow')['text']
university_refs = {
    ('course-1:0','chaucer-prologue'): 'chaucer.fas.harvard.edu',
    ('course-1:0','spenser-epithalamion'): 'quod.lib.umich.edu',
    ('course-1:0','sonnet-116'): 'mason.gmu.edu',
    ('course-1:0','sonnet-130'): 'mason.gmu.edu',
    ('course-1:1','donne-valediction'): 'writing.upenn.edu',
    ('course-1:1','milton-paradise-ix'): 'milton.host.dartmouth.edu',
    ('course-1:1','pope-lock-canto1'): 'anthology.lib.virginia.edu',
    ('course-19:0','o-henry-twenty'): 'etc.usf.edu',
    ('course-19:0','kincaid-girl'): 'academicworks.cuny.edu',
}
for (key, ident), domain in university_refs.items():
    entry = get(key, ident)
    assert domain in entry['source'] and '## University reference' in entry['text']
assert 'transcription gives the hour as ten' in get('course-1:1','pope-lock-canto1')['text']
assert 'critical interpretation, not the primary text' in get('course-19:0','kincaid-girl')['text']
print('PASS: syllabus keys, note IDs, status, source selection and reading explanations')
