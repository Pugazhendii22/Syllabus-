"""Checks for the targeted audit, independently of any external services."""
import json
from pathlib import Path
p=Path(__file__).resolve().parent.parent
notes=json.loads((p/'prepared-notes.json').read_text(encoding='utf-8'))
courses=json.loads((p/'courses.json').read_text(encoding='utf-8'))
for course in courses:
    if course['id'] in {'course-1','course-2','course-4','course-19','course-20'}:
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
# Spoken English follows Ammu's five-unit syllabus and gives examples and practice.
spoken_coverage = {
    0: ('spoken-grammar', ['Sentence construction', 'Types of sentences', 'Parts of speech', 'Auxiliary verbs', 'Singular and plural', 'Active and passive', 'Degrees of comparison', 'Subject–verb agreement', 'Determiners', 'Punctuation and common errors']),
    1: ('spoken-vocab', ['Word formation', 'Synonyms and antonyms', 'Homonyms and one-word substitutes', 'Changing parts of speech', 'Odd one out, idioms and phrases', 'Joining sentences', 'Vowel and consonant sounds', 'Word stress', 'Sentence stress and intonation', 'Pronunciation practice']),
    2: ('spoken-conversation', ['introductions, greetings and questions', 'Describing people', 'Describing places, situations and events', 'Extempore speech', 'Persuasive and descriptive speeches', 'narrating stories', 'Describing characters and situations']),
    3: ('spoken-group', ['Basics of group discussion', 'Assigning tasks', 'Appointing group leaders', 'Completing communication-based tasks', 'Group cohesion', 'Group presentations', 'PowerPoint']),
    4: ('spoken-listening', ['Importance of listening', 'Basics of listening', 'Barriers and responses', 'gist, style and tone', 'Voice recording exercises', 'Body language', 'Gestures, posture, eye contact and facial expressions', 'Etiquette']),
}
for i, (ident, topics) in spoken_coverage.items():
    text = get(f'course-4:{i}', ident)['text']
    assert len(text) > 4500 and 'practice' in text.casefold(), ident
    for topic in topics:
        assert topic.casefold() in text.casefold(), (ident, topic)
# Spoken English now has individual topic lessons, in syllabus order after the original unit note.
spoken_topic_ids = {
 0: ['spoken-topic-sentences','spoken-topic-parts','spoken-topic-auxiliaries','spoken-topic-number','spoken-topic-voice','spoken-topic-comparison','spoken-topic-agreement','spoken-topic-determiners','spoken-topic-editing'],
 1: ['spoken-topic-wordforms','spoken-topic-synonyms','spoken-topic-homonyms','spoken-topic-idioms','spoken-topic-joining','spoken-topic-sounds','spoken-topic-stress'],
 2: ['spoken-topic-greetings','spoken-topic-describing','spoken-topic-speeches','spoken-topic-narration'],
 3: ['spoken-topic-discussion','spoken-topic-tasks','spoken-topic-presentations'],
 4: ['spoken-topic-listening','spoken-topic-gist','spoken-topic-recording','spoken-topic-body'],
}
for unit, ids in spoken_topic_ids.items():
    entries = notes[f'course-4:{unit}']
    assert [x['id'] for x in entries[-len(ids):]] == ids
    for ident in ids:
        body = get(f'course-4:{unit}',ident)['text'].casefold()
        assert len(body) > 2200 and ('practice' in body or 'activity' in body), ident
        assert '## ' in body, ident
# Functional Communicative Writing: detailed topic notes in all five syllabus units.
writing_topics = {
    0: ['writing-topic-types','writing-topic-messages','writing-topic-descriptions','writing-topic-narrating'],
    1: ['writing-topic-paragraph','writing-topic-precis','writing-topic-blog','writing-topic-pictorial'],
    2: ['writing-topic-email','writing-topic-resume','writing-topic-cover','writing-topic-applications'],
    3: ['writing-topic-editor','writing-topic-news','writing-topic-report'],
    4: ['writing-topic-punctuation','writing-topic-synonyms','writing-topic-reported','writing-topic-errors'],
}
for unit, ids in writing_topics.items():
    selections = notes[f'course-20:{unit}']
    assert [x['id'] for x in selections[-len(ids):]] == ids
    for ident in ids:
        entry = get(f'course-20:{unit}', ident)
        text = entry['text'].casefold()
        assert len(text) > 2600 and 'practice' in text and ('example' in text or 'model' in text), ident
        assert 'purdue.edu' in entry['source'] or 'unc.edu' in entry['source'], ident
precis = get('course-20:1','writing-topic-precis')['text']
assert 'one-third' in precis and 'not universally required to be past' in precis
assert 'supported by textual evidence' in precis
print('PASS: syllabus keys, IDs, source selection, reading explanations and detailed writing-topic coverage')
