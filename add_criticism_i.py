import json
P='prepared-notes.json'
with open(P,encoding='utf-8') as f: d=json.load(f)
def n(id,title,body,lesson,questions,source,pre=False):
 r={'id':id,'title':title,'source':source,'text':f'# {title}\nLiterary Criticism I · Semester 5\n\n{body}\n\n## 50-minute lesson\n{lesson}\n\n## Questions\n{questions}\n\nTeaching draft: compare the prescribed extract, translation and edition before class.'}
 if pre:r['status']='preliminary'
 return r
d['course-27:0']=[
n('poetics','Aristotle · Poetics', '''## Context and central question
Aristotle’s surviving Poetics examines poetic making and representation, with extended attention to tragedy. It is an ancient critical text, not an absolute rulebook for every kind of drama. Translation affects terms such as mimesis and catharsis.

## Key ideas
Mimesis is representation or imitation: art represents action, but it need not merely copy a particular event. Poetry can present what is possible or probable; Aristotle distinguishes this from the historian’s account of particular events. Tragedy represents a serious, complete action in dramatic performance and, through pity and fear, brings about catharsis. Scholars debate whether catharsis is best understood as purgation, purification, clarification or another effect; Aristotle does not settle every detail in the surviving text.

Aristotle lists six parts: plot, character, thought, diction, song and spectacle. Plot is the arrangement of incidents and is especially important because tragedy represents action. A whole action has beginning, middle and end linked intelligibly, not simply a sequence of events.

A complex plot may involve peripeteia, a reversal, and anagnorisis, a movement from ignorance to knowledge. Hamartia can mean an error or mistake; translating it automatically as a fixed moral “tragic flaw” oversimplifies debate. In Oedipus the investigation and discoveries bring reversal and recognition together.

## Apply and question
Map a play’s actions and their causal connections. Ask whether pity and fear arise from plot or spectacle. Then consider whose dramatic practices Aristotle’s model includes or leaves out.''','0–10: define representation. 10–22: arrange a simple plot into beginning, middle and end. 22–32: identify reversal and recognition. 32–42: discuss translations of catharsis and hamartia. 42–50: apply one concept to a scene.','Why does Aristotle prioritise plot? What is the difference between recognition and reversal? Why is catharsis debated?','https://www.gutenberg.org/files/1974/1974-h/1974-h.htm'),
n('ars-poetica','Horace · Ars Poetica — writing and poetic craft', '''## Context
The Ars Poetica is a verse epistle by the Roman poet Horace, addressed to the Pisos. Its advice ranges across unity, genre, character, revision and the value of poetic skill. The syllabus prints “119–133” after the title, but does not identify the edition or say whether this refers to pages or verse lines. Check the course anthology before assuming its precise boundaries.

## Argument and examples
Horace begins with a grotesquely mismatched imagined figure to show the problem of parts that do not form a coherent whole. He asks writers to choose subjects suited to their powers and to make appropriate choices of style and genre. He discusses the challenge of handling inherited stories imaginatively and of introducing new ones.

In Latin lines 119–127 specifically, he advises writers either to follow tradition or invent a self-consistent character: famous figures such as Achilles carry inherited expectations, while a new character should remain coherent through the work. The surrounding passage discusses making familiar material one’s own. These line numbers are provided as one reference point, not a claim that they are the whole assigned extract.

Elsewhere the epistle values craft, revision and a combination of usefulness and pleasure. That broader formulation must not be treated as if it appears necessarily in the exact assigned passage.

## Critical application
Compare coherence with predictability: can a character change in a convincing way? Consider whether adherence to inherited expectations could also constrain imaginative reinterpretation.''','0–10: distinguish page numbers from verse numbers. 10–22: identify advice in the assigned passage. 22–32: discuss character consistency. 32–42: test a deliberate reinvention of a familiar character. 42–50: write one benefit and one limitation of Horace’s advice.','Why does Horace value coherence? How might a writer transform inherited material? What must be checked about “119–133”?','https://www.cambridge.org/core/books/senecas-characters/coherence/F1A4404DFD97E2A86D0537F9D5450510')]
d['course-27:1']=[
n('dryden','John Dryden · An Essay of Dramatic Poesy', '''## Form and setting
Published in 1668, Dryden’s essay presents a conversation among four speakers on a barge against the background of an English–Dutch naval encounter. The dialogue allows competing claims to be tested rather than simply listing rules. Neander is often associated with Dryden’s views, but the speakers should not be flattened into identical positions.

## The debate
Crites praises ancient drama and its achievement, including discipline associated with the dramatic unities. Eugenius answers that modern writers inherit the ancients’ strengths and may improve on them. Lisideius argues for the order and regularity of French drama. Neander defends English drama’s variety, lively characterisation, subplots and mixing of tragic and comic elements.

The unities concern action, time and place, as understood in later classical criticism; do not attribute every later formulation equally to Aristotle. Lisideius praises disciplined structure, while Neander asks whether strict observance may sacrifice dramatic richness. In a final exchange about rhyme, Crites objects to it as unnatural for dramatic speech; Neander argues that rhyme can suit elevated serious drama when handled skilfully.

## Critical reading
Ask what each speaker means by representing nature and whether plausibility is the same as literal everyday speech. Examine how dialogue allows concessions as well as disagreement.''','0–10: map four speakers. 10–22: compare ancient and modern. 22–32: compare French and English practices. 32–42: debate rhyme and dramatic plausibility. 42–50: write one argument with its counterargument.','Which speaker supports French drama? Why does Neander defend tragicomedy? Does a dialogue require one final answer?','https://www.supersummary.com/an-essay-of-dramatic-poesy/summary/'),
n('arnold','Matthew Arnold · The Study of Poetry', '''## The importance of poetry
Arnold argues that poetry can help people interpret and sustain life and will become increasingly important as other inherited certainties are questioned. His influential account of poetry as a criticism of life places high value on poetic truth, beauty and seriousness. These are Arnold’s evaluative claims, not neutral measurements.

## Three estimates
The historic estimate can overvalue a work because of its place in literary development. The personal estimate can overvalue work because it appeals to a reader’s attachment, taste or local pride. Arnold proposes a real estimate: attentive judgment of the work’s poetic quality rather than either kind of overvaluation. He is not saying historical knowledge or personal pleasure has no use whatsoever.

## Touchstones
Arnold suggests keeping brief passages from recognised major poets in mind as touchstones for sensing excellence in other work. This is comparative judgment, not a mechanical test in which a new poem must imitate the passage. Ask how choices of canonical “great masters” reflect cultural power, and whether the method can give fair attention to different traditions and genres.

## Practice
Compare two short passages in the assigned edition. Separate an observation about their language from a preference, and explain the standards used to make a judgment.''','0–10: name a favourite work and a reason. 10–22: distinguish three estimates. 22–32: try comparative close reading. 32–42: question the choice of touchstones. 42–50: write an assessment with transparent criteria.','What is a historic estimate? How does a touchstone work? Who gets to decide which poems serve as standards?','https://www.englishfresher.com/2023/11/study-of-poetry/'),
n('wordsworth','William Wordsworth · Poetry and Poetic Diction', '''## Context
The syllabus’s title points toward Wordsworth’s discussion of poetry and diction; confirm the exact prescribed extract. His Preface to Lyrical Ballads, introduced in 1800 and expanded in 1802, argues for renewed attention to common life and selected language associated with ordinary people, especially rural speakers.

## Main claims
Wordsworth opposes formulaic, ornamental poetic diction. The poet chooses and shapes language rather than merely transcribing every utterance. He describes the poet as a person speaking to people, distinguished by a greater capacity for feeling, observation and expression rather than belonging to a wholly different species.

His account of poetry joins powerful feeling with reflection: emotion is recollected in tranquillity, contemplated and reawakened in the process of composition. “Spontaneous” does not mean no thought, craft or revision. He argues that good prose and poetry can share language, while metre contributes to poetry’s distinctive effects.

## Evaluate
Consider how Wordsworth selects and idealises “rustic” experience. Compare his focus on feeling with Eliot’s later impersonal account without assuming either writer excludes craft or emotion entirely.''','0–10: compare ordinary and ornamental descriptions. 10–22: identify his argument about diction. 22–32: map experience, recollection and composition. 32–42: discuss selection and rural life. 42–50: rewrite a phrase and explain the effect.','Why is selected everyday language important? How do feeling and reflection work together?','https://genius.com/William-wordsworth-preface-to-lyrical-ballads-1802-version-annotated'),
n('eliot','T. S. Eliot · Tradition and the Individual Talent', '''## Argument
Eliot’s 1919 essay challenges the idea that a poet’s originality must mean complete separation from predecessors. Tradition is acquired through work. A historical sense involves seeing the past as present in relation to contemporary writing and locating a new work within an existing order. A significant new work can also alter how readers understand the relation among earlier works.

## Impersonality and the catalyst
Eliot argues that the poet’s mind transforms and combines feelings and experiences into artistic form rather than simply publishing a personal emotional history. His analogy compares the mind to a platinum catalyst involved in a reaction without being incorporated into the resulting product. It is a literary analogy, and the chemistry as Eliot states it has been criticised; do not learn it as a chemistry lesson.

When Eliot describes poetry as an escape from personality and emotion, he does not mean that poems are emotionless or that poets literally lack personalities. He asks readers to attend to emotion organised in the poem rather than treating biography as the final explanation.

## Compare
Wordsworth links poetic creation to feeling and reflection; Eliot stresses transformation, discipline and relation to tradition. Both positions are more complex than “emotion versus no emotion”. Ask whose works Eliot’s European-centred tradition privileges.''','0–10: distinguish inheritance from active tradition. 10–22: explain the historical sense. 22–32: sketch the catalyst analogy. 32–42: compare Wordsworth and Eliot. 42–50: write a claim about impersonality with a qualification.','How can a new work change the order of tradition? What does the catalyst analogy explain and what are its limits?','https://www.newyorker.com/books/page-turner/a-hundred-years-of-t-s-eliots-tradition-and-the-individual-talent')]
d['course-27:2']=[
n('shklovsky','Viktor Shklovsky · Art as Technique', '''## Argument
In this foundational Russian Formalist essay, also translated as “Art as Device”, Shklovsky argues that habitual perception becomes automatic. We recognise familiar things quickly without attending closely to them. Artistic devices can interrupt that automatic recognition and prolong perception.

## Defamiliarisation
Defamiliarisation makes something habitual seem strange so that it can be experienced anew. It is not simply using obscure words or making a text randomly difficult. The question is what particular device changes perception and how it works in context.

Shklovsky discusses Tolstoy’s descriptions that withhold familiar labels. In the story Kholstomer a horse’s perspective makes human ideas of ownership look strange: what people call “mine” is not necessarily something they actually use or care for. An unfamiliar viewpoint exposes a familiar social practice to scrutiny.

## Apply and evaluate
Describe a classroom object without naming it, then compare the experience of reading the description with immediate recognition. Ask whether all art must produce estrangement, and whether attending to technique alone can overlook political or historical meanings.''','0–10: describe an object without naming it. 10–22: define habitual perception. 22–32: examine a Tolstoy example. 32–42: compare estrangement and mere obscurity. 42–50: identify one device and its effect in a passage.','What is automatism? How does the horse’s point of view make ownership unfamiliar?','https://blogs.ubc.ca/span501/category/shklovsky/'),
n('brooks','Cleanth Brooks · The Language of Paradox', '''## Argument
Brooks, associated with New Criticism, argues that paradox is central to poetic language. A paradox brings apparently conflicting ideas together in a way that can reveal a complex relation. It is not simply an accidental contradiction or a puzzle to be discarded once a message is found.

Words carry associations as well as dictionary meanings; their effects depend on the other words and patterns around them. Brooks therefore practises close reading: a poem’s meaning emerges from the interaction of its language and form, not from a bare prose summary alone.

## Examples
In Wordsworth’s Westminster Bridge sonnet, Brooks draws attention to the seemingly unlikely experience of finding natural majesty and calm in a great city. In Donne’s The Canonization, the lovers are imagined through the language of sainthood: religious and secular love produce tensions that structure the poem. The point is not that the poem has no literal sense, but that paraphrase alone cannot reproduce all its relations.

## Evaluate
A close reading can make detail visible; ask also what happens when history, readers or social context receive less attention. Not every poem must be forced into a single paradox.''','0–10: distinguish paradox from error. 10–22: read a short passage closely. 22–32: map sacred and secular language in Donne. 32–42: consider strengths and limits of textual focus. 42–50: write a claim grounded in two details.','Why can paraphrase lose meaning? What tension does Brooks find in The Canonization?','https://literariness.org/2016/03/18/cleanth-brooks-concept-of-language-of-paradox/'),
n('jakobson','Roman Jakobson · Two Aspects of Language', '''## Two operations
Jakobson analyses language through selection and combination. Selection chooses among alternatives that could occupy a position: “child”, “student” and “singer” might each fit a sentence in a particular context. Combination joins elements in an actual sequence: words are arranged to produce a sentence. Both operations work together.

He relates selection to similarity and metaphor, and combination to contiguity and metonymy. A metaphor makes meaning through resemblance, as in describing a brave person as a lion. Metonymy uses an association or adjacency, as when “the crown” refers to a monarchy. Real expressions can involve multiple relations; neither entire poems nor whole genres are exclusively one pole.

## Aphasia and careful reading
Jakobson examines different language difficulties associated with aphasia to explore disruptions to selection and combination. These are theoretical and historical models, not a diagnostic tool. Aphasia varies widely by person; it does not imply a lack of intelligence. Do not diagnose individuals from classroom exercises.

## Application
Compare a resemblance-based image with a part-for-whole or institution-based association, and explain why each relation makes sense in context.''','0–10: replace one word in a sentence. 10–22: distinguish choice from sequence. 22–32: compare metaphor and metonymy. 32–42: discuss the limits of aphasia models. 42–50: analyse one example of each.','What changes when a word is substituted? How does metonymy differ from metaphor?','https://www.ieeff.org/jakobsonaphasiafull.pdf')]
d['course-27:3']=[
n('culler','Jonathan Culler · The Linguistic Foundation', '''## Structuralist question
In the chapter “The Linguistic Foundation” from Structuralist Poetics, Culler explores how linguistic models can help explain cultural meaning. Rather than treating a literary work as a self-explanatory object, structuralist poetics asks about the systems and conventions that make particular effects intelligible. Verify the assigned edition and selection.

## Concepts
Saussure distinguishes langue, the shared system of language, from parole, particular acts of speech or writing. Linguistic units gain value through relations and contrasts within a system. A sign joins a signifier, such as a sound-pattern, with a signified, a concept; their association is generally conventional rather than naturally required.

Culler considers relations, signs and the methods used to infer underlying systems from particular instances. Later parts of his book develop literary competence: the learned conventions that help readers recognise a genre or make sense of a text. This is related context, not necessarily content from the assigned chapter.

## Example
The opening of a detective story activates expectations about clues, suspicion and eventual explanation. These are conventions readers learn; a particular story may confirm or frustrate them. A structuralist asks what makes those expectations possible.''','0–10: identify a familiar genre convention. 10–22: explain system and instance. 22–32: compare signs and differences. 32–42: infer an interpretive convention from a passage. 42–50: distinguish chapter content from later related concepts.','How does langue differ from parole? What is gained by asking about conventions rather than only a single interpretation?','https://www.hugendubel.info/fachbuecher/kunst/kunst-allgemein/detail/ISBN-2244057173579/Culler-Jonathan/Structuralist-Poetics'),
n('saussure-incest','Saussure · “Incest and Myth” — attribution needs checking', '''## Important syllabus ambiguity
The extracted syllabus reads “Ferdinand de Sassure: Incest and Myth.” Ferdinand de Saussure is a foundational linguist; kinship, incest prohibitions and structural analysis of myths are especially associated with anthropologist Claude Lévi-Strauss, who drew on structural linguistics. A university course calendar separately lists Saussure and “Lévi-Strauss ‘Incest and Myth’”. This suggests a possible attribution or formatting error, but does not establish which reading Pondicherry University intended.

## Do not memorise an unverified attribution
Check the prescribed reader, teacher’s reading list or original course clarification. The exact extract and author are unverified. The following concepts are background, not a summary of the unidentified selection.

Saussure: signifier and signified; a sign’s conventional character; the relational value of linguistic elements; langue and parole. Lévi-Strauss: structural analysis of relations among kinship rules or variations of myth, including oppositions and how myths may work with them. His account of kinship and the “exchange of women” has been criticised for treating women as objects of exchange; introduce it critically, not as an endorsed prescription.

## Next step
Once the actual text is obtained, record its author, title, source, argument and examples directly, and revise this note.''','0–10: locate the exact reading. 10–22: separate linguistics from anthropology. 22–32: compare a sign relation and a kinship rule. 32–42: question assumptions about gender. 42–50: record what remains unverified.','Why must the attribution be checked? How did a linguistic model influence structural anthropology?','http://www.eng.fju.edu.tw/iacd_2005F/lit_crit/calendar.htm',True),
n('barthes','Roland Barthes · The Death of the Author', '''## Argument in sequence
Barthes begins with a passage from Balzac’s Sarrasine and asks who is speaking: a character, an individual author, an inherited cultural idea or something else? He questions the assumption that the author’s biography or intended message is the single key that fixes a text’s meaning.

He presents writing as woven from pre-existing languages, cultural codes and other texts. The “scriptor” is not an isolated origin of all meaning. The reader becomes a place where the text’s multiple voices can be brought together. The “death” of the Author is a theoretical challenge to interpretive authority, not a literal death or the claim that writers did not write works.

## Practice and critique
Read a passage for competing voices, conventions and possible meanings, supporting each interpretation with textual evidence. Openness does not mean that any claim is equally supported. Ask whether biography, historical position or accountability might still matter for some questions even when the author’s intention is not treated as final.''','0–10: ask who speaks in a fictional sentence. 10–22: trace Barthes’s challenge. 22–32: identify cultural voices in a passage. 32–42: compare reader and author-centred interpretations. 42–50: write a claim with evidence.','What does “death” mean here? Why does a reader’s interpretation still require evidence?','https://interestingliterature.com/2021/10/barthes-death-of-the-author-summary-analysis/'),
n('foucault','Michel Foucault · What is an Author?', '''## From person to function
Foucault asks how a name such as “Shakespeare” functions in the organisation and circulation of discourse. An author’s name can group texts, distinguish them from others and affect how they are received. The author-function is not identical to the biological person who wrote a text.

## Four features
Foucault describes the author-function as connected to legal and institutional systems of appropriation and responsibility; varying across kinds of discourse, periods and societies; produced by complex practices of attribution rather than simply discovered; and capable of organising several positions or voices rather than referring to one straightforward speaking self.

He also discusses founders of discursivity such as Marx and Freud: their names do more than identify a collection of works, because later writers develop, contest and return to fields of discourse associated with them. This is Foucault’s historically situated account and can be questioned.

## Comparison with Barthes
Barthes disputes the author’s final authority over meaning; Foucault investigates how authorship continues to operate through classification, law and institutions. Neither claim requires pretending actual writers do not exist.''','0–10: group book titles by an author name. 10–22: explain classification. 22–32: map the four features. 32–42: compare Barthes and Foucault. 42–50: apply the author-function to an example.','How does an author’s name classify texts? How does the author-function differ from the actual writer?','https://www.samvriti.com/2012/10/01/the-author-function/')]
d['course-27:4']=[
n('lyotard','Jean-François Lyotard · What is Postmodernism?', '''## Context and key distinction
In “Answering the Question: What is Postmodernism?” Lyotard questions demands that art provide reassuring, familiar representations. His use of the postmodern does not simply name a period after modernism. He describes a questioning or experimental moment within the modern itself.

## The unpresentable and the sublime
The “unpresentable” points to what established forms cannot adequately show. An artwork may make the limits of representation felt without offering a complete picture of what lies beyond them. Lyotard contrasts a modern attitude that can retain nostalgia for a lost whole with a postmodern search for new forms that resist the consolation of established rules. These are his distinctions, not labels that automatically classify every artwork.

Artists experiment without a complete prior rulebook; criteria may emerge through the work. His broader account of scepticism toward grand legitimating narratives is associated with The Postmodern Condition, but the assigned essay’s specific discussion of representation and the sublime should not be replaced by that slogan alone.

## Apply
Describe a work that interrupts a familiar form. Then ask what the interruption makes difficult to represent, and whether a claim about “the unpresentable” is actually supported by the work.''','0–10: list expectations of a familiar genre. 10–22: distinguish chronological “post” from a critical moment. 22–32: explain the unpresentable. 32–42: examine an experimental passage. 42–50: write a qualified definition.','Why is the postmodern not simply later than the modern? What is gained by challenging established forms?','https://plato.stanford.edu/entries/lyotard/'),
n('hutcheon','Linda Hutcheon · Historiographic Metafiction', '''## The concept
Hutcheon uses “historiographic metafiction” for fiction that engages recognisable historical events, people or documents while self-consciously drawing attention to its own making. Historiography is the writing and interpretation of history; metafiction makes aspects of fictional construction visible.

The combination is paradoxical: a novel draws on the past while asking how the past is narrated and known. This does not mean the past did not exist or that historical evidence and invented events are equally reliable. It asks readers to distinguish events from the narratives and archives through which we encounter them.

## Techniques and example
A narrator might interrupt to question their authority, present alternative endings, parody an earlier form or expose gaps in a document. The French Lieutenant’s Woman is often discussed in this context because it revisits Victorian settings while making narrative choice conspicuous. A historical novel is not automatically historiographic metafiction merely because it is set in the past; self-reflexive questioning is important.

## Critical task
Choose a passage that marks its own storytelling. Identify the historical claim, the fictional device and what evidence would be needed to verify the claim outside the novel.''','0–10: define historiography and metafiction separately. 10–22: combine the concepts. 22–32: identify a self-conscious narrative device. 32–42: distinguish historical evidence from invention. 42–50: explain the productive paradox.','Why is not every historical novel historiographic metafiction? Does questioning historical narration deny the existence of the past?','https://textjournal.scholasticahq.com/article/36983.pdf'),
n('bhabha','Homi K. Bhabha · Interrogating Identity', '''## Context
In “Interrogating Identity: Frantz Fanon and the Postcolonial Prerogative”, a chapter of The Location of Culture, Bhabha engages Fanon to question how colonial power shapes the representation and experience of identity. Identity is not simply a fixed inner essence expressed unchanged in every setting.

## Argument
Identification takes place in relation to others, images and the unequal social world. Colonial racial stereotypes attempt to assign the colonised a fixed position, yet the subject’s relation to those images can be divided and ambivalent. Bhabha’s engagement with Fanon attends to psychic as well as political experience: the way a person is seen by another can affect how identity is lived and negotiated.

The chapter’s argument should not be collapsed into the slogan “all cultures are mixed”. Bhabha’s wider work also develops hybridity, mimicry and in-between spaces, but those terms have particular contexts; cite the assigned passage before attributing a specific claim to it. Cultural negotiation can create openings for agency without making colonial violence or material inequality disappear.

## Application
Consider a fictional encounter in which one character is reduced to a racial stereotype. Distinguish the stereotype, the power relation that circulates it and the character’s response. Avoid reproducing slurs unnecessarily.''','0–10: distinguish identity from stereotyping. 10–22: introduce Fanon and colonial context. 22–32: trace image, recognition and power. 32–42: discuss ambiguity without romanticising oppression. 42–50: analyse a passage with evidence.','Why does recognition by another matter? How can identity be unstable without being unreal?','https://www.routledge.com/The-Location-of-Culture/Bhabha/p/book/9780415336390'),
n('anderson','Benedict Anderson · Imagined Communities', '''## Central definition
Anderson describes the nation as an imagined political community, imagined as limited and sovereign. “Imagined” does not mean fake: members cannot personally meet most fellow members, yet may experience a powerful sense of belonging. Limited means that even large nations have boundaries; sovereign points to claims to political self-determination. Community names an imagined horizontal bond, though actual societies can be deeply unequal.

## Print and historical development
Anderson argues that print capitalism helped people imagine shared worlds. Newspapers and novels, circulating through print languages, allow readers to imagine others engaging with events in a shared historical time. He also discusses administrative practices such as censuses, maps and museums in colonial settings. These institutions organise populations, territories and histories, but they do not by themselves explain every form of nationalism.

## Critical reading
Ask who has access to print, whose languages are privileged and who is excluded from national belonging. Print’s role is a historical argument, not a claim that every member must read the same newspaper. The syllabus specifies excerpts without page numbers: confirm which chapters are assigned.

## Apply
Analyse a newspaper, school map or national ceremony as a possible way of imagining collective belonging, while distinguishing the object itself from assumptions about every audience member.''','0–10: describe belonging among strangers. 10–22: unpack imagined, limited, sovereign and community. 22–32: map print and shared time. 32–42: discuss inequality and exclusion. 42–50: apply one concept to a sourced example.','Why is an imagined nation not necessarily unreal? How can a claim of horizontal community coexist with inequality?','https://www.britannica.com/biography/Benedict-Anderson')]
with open(P,'w',encoding='utf-8') as f:json.dump(d,f,ensure_ascii=False,indent=2)
print('Added Literary Criticism I: 17 selections across five units, including one preliminary attribution check.')
