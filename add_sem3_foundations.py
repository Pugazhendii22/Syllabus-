import json
p='prepared-notes.json';d=json.load(open(p))
def add(c,i,t,body):
 text=f'# {t}\nSemester 3 · Unit {i+1}\n\n'+body+'\n\n## 50-minute lesson\n0–10 min: recall the key terms. 10–25: work through the examples in pairs. 25–38: compare two forms or historical developments using a text from class. 38–45: groups share a claim and evidence. 45–50: write an exit response explaining one distinction.\n\n## Before teaching\nCheck period labels, examples and interpretations against a reliable literary history and the prescribed texts; dates and genre boundaries are approximate. This is an introductory study note, not a substitute for detailed readings.'
 d[f'{c}:{i}']=[{'id':f'{c}-{i}-foundation','title':t,'text':text,'source':'https://www.britannica.com/art/English-literature'}]
add('course-15',0,'Medieval literature to the English Revolution','''## Periods and languages
The syllabus groups Anglo-Saxon, medieval and early modern literature. The “Anglo-Saxon 5th–14th century” label in the extract overlaps later medieval English: Old English literature is conventionally associated with the period before and around the Norman Conquest of 1066, while Middle English develops after that. These are useful categories, not sudden switches; Latin and French also mattered.

## Medieval traditions
Old English poetry includes heroic narrative and religious writing; Beowulf survives in a later manuscript and should not be assigned a precise composition date without evidence. Middle English works include romance, religious writing and Chaucer’s late-fourteenth-century Canterbury Tales. Chaucer’s pilgrims tell varied stories, linking social observation to a framing narrative. Manuscript culture shaped circulation before printing became established in England under William Caxton in the late fifteenth century.

## Renaissance and Reformation
Renaissance humanism encouraged renewed engagement with classical learning, rhetoric and education; the Reformation transformed religious institutions and debates. Neither was a uniform break with everything medieval. The syllabus lists Tudor and Elizabethan, Jacobean and Caroline periods, followed by the Commonwealth or Interregnum (1649–1660): remember that political dates do not divide literary styles neatly.

Elizabethan and Jacobean drama developed in professional playhouses alongside court and popular entertainments. Shakespeare, Marlowe and Jonson worked in different dramatic modes. Poetry includes sonnet sequences and varied religious and secular verse; Donne is associated with metaphysical poetry. Civil war and censorship affect the later period. Ask how religious change, patronage and performance shape writing without reducing works to their historical background.

## Review
Trace a broad change from manuscript to print; explain why Old English is not the same as Middle English; compare period names with forms that cross their boundaries.''')
add('course-15',1,'Restoration, Augustan writing and Johnson’s age','''## Restoration and neoclassicism
The Restoration of Charles II in 1660 follows the Interregnum. The reopened commercial theatres produced comedy, tragedy and adaptations; women began appearing professionally on the English public stage. Restoration comedy often examines manners, marriage and reputation. Dryden’s work shows the importance of public controversy, satire and criticism.

Neoclassical writing values, in different ways, order, judgement, rhetoric and classical models; it is not a single set of rules followed identically by all writers. Augustan is a retrospective analogy to Roman literary culture, often applied to early eighteenth-century writers including Pope and Swift. Pope’s mock-epic treats a social dispute through elevated epic conventions; satire is not always equivalent to the author’s literal views.

## Print, prose and the novel
Periodicals, newspapers, coffee-house discussion and expanding print networks influenced prose forms and reading publics. Addison and Steele’s periodical essays address social behaviour and taste. Defoe, Richardson and Fielding are often discussed in histories of the English novel, but the novel has several histories and cannot be reduced to a single inventor.

## Johnson and the later century
Samuel Johnson contributed criticism, essays, biography and a major dictionary. Late eighteenth-century literature also contains forms of sensibility, early Gothic fiction and challenges to neat period boundaries. Questions about class, empire, slavery and women’s access to authorship complicate a story focused only on celebrated male writers.

## Review
How does a mock-epic use contrast? Why did expanding print matter? What is gained and lost by calling a period “Augustan”?''')
add('course-15',2,'Romanticism: poetry, fiction and Gothic','''## Historical frame
The Romantic period is often dated approximately from the 1790s to the 1830s; dates vary by literary history. The French Revolution, industrialisation, political reform and imperial expansion form important contexts. Romantic writers respond differently to these developments and should not be treated as a single school.

## Poetry
Wordsworth and Coleridge’s Lyrical Ballads (1798) is an important reference point for poetry, ordinary language and imagination. Other writers such as Blake, Byron, Shelley, Keats and women poets developed different forms and political positions. Nature in Romantic writing can be a landscape, a source of spiritual or imaginative reflection, and a site of social conflict; avoid assuming that it always provides comfort.

## Fiction and the Gothic
Austen’s fiction explores marriage, property and social judgement with irony and careful narration. The Gothic uses such resources as threatened spaces, secrecy, fear and unstable knowledge; it can also examine power and social boundaries. Mary Shelley’s Frankenstein (1818) combines Gothic and speculative elements to ask about creation, responsibility and exclusion. Its creature is not named Frankenstein: that is the creator’s surname.

## Reading questions
How does a speaker’s relationship to landscape affect a poem? Compare the handling of social constraint in a novel and a Gothic narrative. How can political history help interpretation without replacing close reading?''')
add('course-15',3,'Victorian literature and its contexts','''## Context
Victoria reigned from 1837 to 1901, while “Victorian” literature is often studied across a broader nineteenth-century context. The syllabus’s phrase “early 19th century (1832–1901)” spans much more than the early century; identify the dates explicitly instead of repeating the label uncritically. Industrialisation, urbanisation, the expansion of empire, religious debate, scientific developments and struggles over reform changed literary culture.

## Poetry and the novel
Tennyson and Browning use different poetic forms; the dramatic monologue can make a speaker reveal more than they intend. Elizabeth Barrett Browning’s poetry includes personal and public concerns. In fiction, Dickens depicts social institutions and inequality; the Brontës explore desire, constraint and narrative perspective; George Eliot examines moral choice and community. These are examples, not an exhaustive list.

Serial publication influenced how many novels reached readers. Education, journalism, class and women’s legal and economic position shape both authorship and subject matter. Imperial power and colonial resistance also matter, including in texts set in Britain.

## Questions
How can a dramatic speaker be distinct from the poet? What does serial publication change about reading? How do a novel’s characters encounter social institutions?''')
add('course-15',4,'Hardy and modernism','''## Thomas Hardy
Hardy’s fiction and poetry bridge conventional period divisions. His novels use the imagined region of Wessex to examine rural change, social expectation, chance and the limits imposed on individuals. Tess of the d’Urbervilles and Jude the Obscure should be read in their specific social contexts rather than reduced to the claim that fate alone controls everything.

## Modernism
Modernism is a broad and varied set of formal experiments, not simply a synonym for “modern.” The world wars, urbanisation, technological change, empire and changing ideas of self and society are important contexts. Fragmentation, shifting perspectives, nonlinear time, allusion and experiments with consciousness appear in some works, but no feature applies to every modernist text.

Woolf’s To the Lighthouse changes pace and perspective across three sections; Eliot’s The Waste Land combines voices and allusions. Compare their methods rather than assuming fragmentation has one meaning. The syllabus highlights 1914–1945, but modernist writing begins before 1914 and continues beyond 1945.

## Questions
How does Hardy connect individual experience with social structures? What does a shifting viewpoint allow? Why should a literary period not be treated as a perfectly bounded box?''')
add('course-16',0,'Tragedy, comedy, tragicomedy and satire','''## Tragedy
Tragedy often represents serious conflict, suffering and loss; the nature of the protagonist and ending vary across traditions. Aristotle’s discussion of tragedy is influential but is not a universal checklist for every play. Analyse what choices, institutions and circumstances contribute to the outcome.

## Comedy
Comedy can expose errors, misunderstandings and social pretensions. Some comedies end in reconciliation or marriage, but not all; laughter can be affectionate, critical or uncomfortable. Compare how Shaw uses comic contrast between idealised heroism and practical experience.

## Tragicomedy and satire
Tragicomedy combines or moves between serious danger and comic elements without necessarily producing a purely tragic ending. Satire criticises attitudes, institutions or conduct through irony, exaggeration, parody or ridicule. Its target must be argued from context: a satirical speaker’s claim is not automatically the writer’s own belief.

## Practice
Identify a scene’s emotional effect, the techniques producing it and the social assumptions under pressure. Can one scene be both funny and troubling?''')
add('course-16',1,'Drama, novel, short story and essay','''## Drama
Drama presents action for performance through dialogue, stage directions, movement, space and silence. A printed script and a particular production are related but not identical. Ask what audiences know and what characters know at each point.

## Novel and short story
A novel is an extended prose fiction capable of developing multiple events, characters and perspectives. A short story often concentrates on a smaller set of moments or relationships, though length alone does not determine its effect. Narrator, focalisation, sequence and selection influence both. A plot overview should not be mistaken for a full account of every chapter.

## Essay
An essay is prose organised around a subject or argument; essays may be personal, reflective, analytical or persuasive. Identify the central claim, structure, examples and implied audience. A literary essay may use voice and imagery as well as argument.

## Practice
Describe the same disagreement as a dialogue, a short narrative and a reflective essay. What can each form foreground?''')
add('course-16',2,'One-act play, biography, autobiography and melodrama','''## One-act play
A one-act play has a single act, often concentrating action within a limited span, setting or conflict. It can still contain shifts of scene and complex characters. Observe how quickly the opening establishes stakes and how stage action leads to a conclusion.

## Biography and autobiography
Biography narrates a person’s life written by another; autobiography is a life account written by the subject, although collaborative writing can complicate simple categories. Both involve selection, narrative shaping and evidence. A remembered event is a perspective on the past, not automatically a complete record.

## Melodrama
Melodrama emphasises heightened emotion, conflict and theatrical effect; in particular historical forms music accompanied action. It may use recognisable moral oppositions, but individual works can complicate them. Calling something melodramatic should not replace analysis of its actual conventions and audience.

## Practice
Rewrite a remembered event as an autobiographical paragraph; then list evidence a biographer would need to check. Discuss how a one-act scene might show the same event through action.''')
add('course-16',3,'Farce, ballad, masque and epic','''## Farce
Farce uses rapid complications, improbable situations, mistaken identities and physical or verbal comedy. Analyse timing and consequences rather than dismissing it as mere silliness.

## Ballad
A ballad is commonly a narrative song or poem associated with oral and written traditions. Repetition, dialogue and incremental variation appear in many examples, though not all ballads follow one fixed form. Compare versions before asserting a single authoritative text.

## Masque
A masque is a form of courtly entertainment associated with spectacle, music, dance, costume and allegory, especially prominent in early modern England. Its meaning depends partly on patronage and performance setting.

## Epic
Epic is a long narrative of significant action, often associated with heroic figures, communities and elevated style. Traditions vary greatly; oral and literary epics are not identical. A mock-epic applies epic conventions to an apparently minor subject for comic or critical effect.

## Practice
Compare the scale and purpose of an epic narrative with a ballad. What would be lost if a masque were studied without its spectacle?''')
add('course-16',4,'Lyric, sonnet, elegy, prosody and ode','''## Lyric, elegy and ode
A lyric generally foregrounds a voice, feeling or moment rather than an extended plot. An elegy mourns or reflects on loss, often moving through remembrance and consolation, though not every elegy follows that sequence. An ode is a sustained lyric address or meditation, frequently developed through formal patterns; different odes have different structures.

## Sonnet
A sonnet traditionally has fourteen lines. The English or Shakespearean form often uses three quatrains and a couplet, frequently rhyming ABAB CDCD EFEF GG; the Petrarchan form often has an octave and sestet with different patterns. A volta is a turn in thought or tone. These are conventions, not guarantees for every poem.

## Prosody
Prosody studies the sound and patterning of verse. A syllable is a unit of speech; stress gives relative prominence. An iamb is an unstressed–stressed pattern and pentameter has five metrical feet in a line. Real spoken lines can vary from a regular pattern. Rhyme concerns similar sounds, not merely spelling; rhythm also depends on syntax, pauses and performance.

## Practice
Read a short poem aloud. Mark a possible stress pattern and explain where performance permits more than one reading. Identify a turn and connect it to an argument.''')
json.dump(d,open(p,'w'),ensure_ascii=False,indent=2)
print('Added ten Semester 3 foundation notes')
