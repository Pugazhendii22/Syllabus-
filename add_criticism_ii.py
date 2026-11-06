"""Add introductory, source-linked Semester 7 Literary Criticism II teaching drafts."""
import json
P='prepared-notes.json'
with open(P,encoding='utf8') as f:d=json.load(f)
def n(id,title,body,lesson,questions,source,preliminary=False):
 item={'id':id,'title':title,'source':source,'text':f'# {title}\nLiterary Criticism II · Semester 7\n\n{body}\n\n## 50-minute lesson\n{lesson}\n\n## Discussion and revision\n{questions}\n\nTeaching draft: consult the assigned text and edition; verify quotations and historical claims before teaching.'}
 if preliminary:item['status']='preliminary'
 return item
d['course-38:0']=[
n('freud-group','Sigmund Freud · Group Psychology and the Analysis of the Ego', '''## Scope
Freud’s 1921 book asks how people’s feelings and conduct change in groups. The syllabus gives the title but no chapter range: this guide introduces central arguments, not every chapter. Freud reviews earlier crowd theorists including Gustave Le Bon before developing his own psychoanalytic account.

## Emotional bonds
Freud uses “libido” broadly for energy associated with love and attachment, not only overt sexual activity. He argues that emotional ties help bind groups. His examples of organised groups include the church and the army, where members imagine a leader’s relationship with them and also form ties with one another.

## Identification and the ego ideal
Identification means taking another person or a shared quality as a model in forming the ego. In Freud’s model of a primary leader-centred group, members place the same object in the position of their ego ideal and identify with one another. This is a theory about a particular group formation, not proof that all communities need a leader or act irrationally.

## Reading critically
Freud’s comparisons with hypnosis and his speculation about primal history are contestable, not established laws of social psychology. Consider social institutions, material conditions, gender and individual differences alongside unconscious attachment. In a novel, ask how characters construct a leader’s image; avoid diagnosing an author from a fictional character.''','0–10: define the question of group psychology. 10–20: explain libido and emotional ties. 20–30: map leader and members. 30–40: test the model against a fictional group. 40–50: identify a limitation.','How do identification and the ego ideal help explain Freud’s leader-centred group? What might his model leave out?','https://en.wikisource.org/wiki/Group_Psychology_and_the_Analysis_of_the_Ego/Chapter_8',True),
n('lacan-mirror','Jacques Lacan · The Mirror Stage', '''## The scene
In his 1949 formulation, Lacan describes an infant approximately six to eighteen months old identifying with a reflected image. The image appears coordinated and whole while the child’s bodily capacities are still developing. Lacan uses this scene to theorise the formation of the ego or “I.”

## Identification and misrecognition
The child assumes an external image as an image of self. The apparently complete form offers an anticipation of mastery, but it is also outside the child. Lacan calls this identification alienating: the ego is constituted through an image that does not simply coincide with lived bodily experience. Misrecognition is structural in this account, not a claim that the infant cannot see a mirror accurately.

## Reading literature
A character may identify with a portrait, reflection, public role or idealised image. Ask what wholeness the image promises, what contradictions it conceals and how other people shape recognition. This is a critical analogy, not a diagnosis.

## Limits
The mirror stage is a psychoanalytic interpretation, not a settled universal developmental test. Modern child-development research should not be equated with Lacan’s speculative account. Different translations render his terminology differently.''','0–10: describe the mirror scene. 10–20: explain gestalt and anticipation. 20–30: distinguish recognition from misrecognition. 30–40: read an imagined portrait scene. 40–50: identify theoretical limits.','Why is identification with the image both enabling and alienating for Lacan? Why is this not a universal diagnostic test?','https://literariness.org/2016/04/22/lacans-concept-of-mirror-stage/')]
d['course-38:1']=[
n('showalter','Elaine Showalter · Feminist Criticism in the Wilderness', '''## Two approaches
In this 1981 essay, Showalter distinguishes feminist reading that examines representations and assumptions in texts from gynocritics: the study of women as writers, including the histories, conditions, genres and traditions of their writing. These approaches can overlap; one need not abandon the critique of male-authored texts to study women writers.

## Four models
Showalter surveys biological, linguistic, psychoanalytic and cultural approaches to women’s writing. Each raises questions: does embodiment matter? How is language structured and used? How might psychic development be theorised? How do institutions, history and culture shape writing? She argues for a cultural model able to address differences among women as well as shared constraints.

## The “wild zone”
The image of a space outside dominant male experience helps explore muted or less accessible aspects of women’s culture. Treat it as a theoretical model, not proof that all women share one hidden essence. Ask how race, caste, class, sexuality and language make experiences unequal and different.

## Application
Compare the publication conditions of two women writers in different places. Investigate publishers, readership and access to education; do not presume their work is alike simply because of gender.''','0–10: distinguish reader and writer approaches. 10–20: outline four models. 20–30: examine the cultural model. 30–40: test the wild-zone metaphor. 40–50: construct a research question.','What is gynocritics? Why does the cultural model need attention to differences among women?','https://www.jstor.org/stable/1343159'),
n('beauvoir-myth','Simone de Beauvoir · Myth and Reality', '''## Context
“Myth and Reality” belongs to the discussion of myths in The Second Sex (1949); English translations and section titles vary. Beauvoir asks how representations of “Woman” become confused with the lives of actual women.

## The eternal feminine
She analyses recurring, often contradictory images such as woman as mother, muse, virgin or temptress. These are not neutral portraits of every woman: they can express men’s hopes, fears and interests while treating women as the Other in relation to a supposedly universal male subject.

## Myth versus lived situation
A fixed image can persist even when individual women do not fit it; the exception may be dismissed instead of the image revised. Beauvoir connects ideas to material conditions and opportunities. A literary critic can ask whose perspective constructs a female character, what actions she is allowed, and whether stereotype conflicts with her particular situation.

## Critical discussion
Beauvoir’s analysis was influential, while later feminists have questioned its generalisations, historical claims and treatment of differences among women. Analyse these debates without assuming all women have the same body, choices or social position.''','0–10: define myth in this argument. 10–20: identify contradictory images. 20–30: compare representation and situation. 30–40: analyse a fictional example. 40–50: discuss limitations.','How can contradictory stereotypes serve the same social order? What is the difference between Woman as myth and women as persons?','https://www.sparknotes.com/philosophy/secondsex/summary/')]
d['course-38:2']=[
n('williams-base','Raymond Williams · Base and Superstructure', '''## The model
A simplified Marxist model describes an economic “base” of production and a “superstructure” including law, politics and culture. Williams challenges mechanical versions in which culture merely reflects a fixed economy. He asks how social relationships and cultural practices are themselves active and historical.

## Determination and practice
For Williams, determination can be understood as setting limits and exerting pressures rather than predicting a single inevitable outcome. The base is not a motionless foundation: productive relationships are made and changed by people. A novel is not merely an illustration of an economic formula; its creation and circulation are material practices too.

## Dominant, residual and emergent
Dominant forms organise a culture’s prevailing meanings. Residual practices formed in an earlier social formation remain active; emergent practices introduce new meanings and relationships. None is automatically emancipatory: an older practice may support or challenge authority, and a new practice may be absorbed into existing power.

## Example
Study how a publisher’s finances, readers’ expectations and a novel’s language interact. Avoid the claim that the writer can choose freely without pressures, or the opposite claim that economics alone dictates every sentence.''','0–10: sketch the base/superstructure model. 10–20: explain limits and pressures. 20–30: distinguish residual and emergent. 30–40: map publishing as practice. 40–50: write a non-reductive analysis.','How does Williams revise mechanical determination? Can a residual cultural form still be active?','https://philopedia.org/thinkers/raymond-henry-williams/'),
n('gramsci-hegemony','Antonio Gramsci · Hegemony', '''## Scope
The syllabus names “Hegemony” without identifying a specific extract. Gramsci develops related ideas across the Prison Notebooks, written during imprisonment under Italian fascism. This is an introductory guide; confirm the prescribed passage and translation.

## Leadership and power
Hegemony describes how a dominant group secures leadership and a degree of consent through institutions, alliances and shared assumptions, not force alone. Coercion remains important; consent and coercion are not mutually exclusive. Hegemony is made and maintained historically, so it can be contested and reshaped.

## Civil society and common sense
Schools, associations, media, churches and other institutions can help organise prevailing ideas. “Common sense” may contain contradictory beliefs rather than a perfectly unified doctrine. Intellectuals play roles in organising social ideas; “organic” intellectuals arise in connection with particular social groups.

## Applying the concept
Examine an advertisement or fictional school rule: what behaviour is made to look natural, and what alternatives are excluded? Evidence of influence is needed; do not assume every person agrees or every institution operates with one plan. Compare with Williams’s dynamic understanding of culture.''','0–10: distinguish coercion and consent. 10–20: describe hegemony. 20–30: identify institutional practices. 30–40: analyse an example and possible resistance. 40–50: compare Williams.','Why is hegemony not just another word for force? Why is consent not necessarily unanimous or permanent?','https://plato.stanford.edu/archives/win2025/entries/gramsci/',True),
n('althusser','Louis Althusser · Ideology and Ideological State Apparatuses', '''## The question
In his 1970 essay Althusser asks how societies reproduce the conditions of production, including labour and the social relations that organise it. Reproduction involves more than replacing machines or paying wages: people also learn practices and roles.

## Apparatuses
He distinguishes the repressive state apparatus, which functions primarily through repression, from ideological state apparatuses such as education, family, religion and media, which function primarily through ideology. The distinction is one of emphasis, not an absolute claim that one uses only force and the other none. Some ideological institutions are formally private.

## Ideology and interpellation
Ideology has material existence in practices and institutions; it also represents people’s imagined relation to their real conditions. Interpellation is often illustrated by a person recognising a call as addressed to them. The “hail” is an analogy for becoming a subject within social categories, not a literal origin story for every individual.

## Evaluation
Consider how school rules and assessments shape roles, while also asking how teachers and students contest them. Critics question whether Althusser leaves enough room for agency and historical change. A text can reproduce an assumption, question it, or do both.''','0–10: define reproduction. 10–20: compare apparatuses. 20–30: explain the hail. 30–40: examine a school example. 40–50: discuss agency.','How do the two kinds of apparatus differ in emphasis? Why is the police hail an analogy rather than an experiment?','https://plato.stanford.edu/entries/althusser/')]
d['course-38:3']=[
n('bakhtin-discourse','Mikhail Bakhtin · Discourse in the Novel', '''## Locate the essay
“Discourse in the Novel” studies language as socially and historically varied. The unit heading includes “New Criticism,” but Bakhtin’s dialogic account is not itself an example of Anglo-American New Criticism. Use the heading as a prompt for comparison, not a label to impose on every listed critic.

## Heteroglossia
Heteroglossia refers to the diversity and stratification of social languages or speech types: professional, generational, regional and institutional ways of speaking carry different values. A novel can bring these into relation through narration, dialogue, parody and reported speech.

## Dialogism and double voice
An utterance responds to previous words and anticipates others; meaning emerges in these relationships. Double-voiced discourse can carry a character’s accent and the author’s refracted intention at once, as in ironic imitation. Multiple voices do not automatically receive equal power in a text.

## Worked question
Imagine a narrator repeating a bureaucrat’s phrase about “efficient resettlement” beside a displaced family’s account. Ask how the two discourses qualify one another, and whether the narration invites distance from the official phrase. This is an invented example, not Bakhtin’s quotation.''','0–10: define social language. 10–20: explain heteroglossia. 20–30: examine double voice. 30–40: analyse the imagined example. 40–50: compare with formal close reading.','How does heteroglossia differ from merely using two languages? Why should Bakhtin not automatically be labelled a New Critic?','https://sites.duke.edu/novelproject/archives/31'),
n('greenblatt-energy','Stephen Greenblatt · The Circulation of Social Energy', '''## Text and approach
The opening chapter of Shakespearean Negotiations (1988), “The Circulation of Social Energy,” asks how works such as Renaissance plays gain and renew their power to affect readers and audiences. Greenblatt is associated with New Historicism; the syllabus spelling “Cuircualtion” refers to “Circulation.”

## Exchange rather than isolation
A play is made within networks of institutions, performances, practices and discourses. Theatre can appropriate, transform and return materials circulating in its culture. “Social energy” names a work’s historically mediated capacity to produce effects such as wonder, fear or pleasure; it is a critical metaphor, not a measurable physical quantity.

## A method
Put a scene in conversation with a contemporary legal record, religious pamphlet, travel narrative or performance practice. Ask what is exchanged, changed and made visible rather than treating the non-literary source as a simple explanation of the play. Later performances also change how the work acts in new contexts.

## Critical question
Does a reading of cultural negotiation make resistance seem always contained by power? Compare Sinfield’s concern with dissidence, and support any difference with passages rather than a rigid opposition.''','0–10: introduce New Historicism. 10–20: explain exchange. 20–30: pair a scene with another document. 30–40: question power and resistance. 40–50: define social energy carefully.','Why is social energy a metaphor rather than a physical measurement? How does exchange differ from treating context as background alone?','https://www.en.shakespeare-bibliothek.anglistik.uni-muenchen.de/miscellany/archive/miscellany5/index.html'),
n('sinfield-dissidence','Alan Sinfield · Reading Dissidence', '''## Context
“Reading Dissidence” appears within the chapter on cultural materialism, Othello and the politics of plausibility in Faultlines (1992). Sinfield investigates how critical readings and cultural institutions shape what counts as believable.

## Dissidence and containment
Dissidence contests an aspect of a dominant order. Because a challenge must work with the available language and structures it opposes, critics can always find traces of that order in it. Sinfield resists concluding automatically that all resistance is therefore absorbed and defeated. He prefers “dissidence” to a term that assumes successful subversion in advance.

## Reading and institutions
A text cannot control every future reading. Schools, theatres, publishers and critics help make some interpretations seem plausible and others unlikely. Cultural materialism studies these historically specific institutions and the critic’s own position in them, not merely contradictions inside an isolated text.

## Application
In Othello, compare interpretations of race, gender and authority, asking what evidence each uses and what historical conditions make it persuasive. A dissident reading needs argument; calling a reading resistant does not by itself prove its political effects.''','0–10: define dissidence. 10–20: explain the containment problem. 20–30: identify institutions of reading. 30–40: compare two plausible interpretations. 40–50: assess evidence.','Why can a dissident text still use dominant language? What does Sinfield mean by the politics of plausibility?','https://publishing.cdlib.org/ucpressebooks/view?docId=ft3199n7t4;chunk.id=d0e1218;doc.view=print')]
d['course-38:4']=[
n('ngugi-decolonising','Ngũgĩ wa Thiong’o · Decolonising the Mind', '''## Scope and context
The syllabus names the 1986 book without a chapter range. This overview focuses on the opening discussion of language and connects it to the wider project; check the selected chapter in the prescribed edition.

## Language and colonial education
Ngũgĩ recalls growing up with Gikuyu oral storytelling and attending a colonial school system that privileged English and punished or devalued African languages. He argues that language carries culture and ways of imagining the world as well as enabling communication. Education in a language elevated over one’s home language can create cultural alienation.

## Literary choices
He revisits debates over what counts as African literature, including the limitations of conferences organised around English-language writing. His decision to write creative work in Gikuyu is a practical intervention in cultural politics. He advocates education, publishing and literature in African languages, not a claim that every African speaks the same language.

## Debate
Compare arguments for writing in local languages with arguments for reshaping English and translating between communities. Language choices involve readership, access, power and material resources. Avoid implying that using English automatically erases a writer’s culture or that a change of language alone ends colonial inequality.''','0–10: map languages in schooling. 10–20: distinguish communication and culture. 20–30: discuss the conference problem. 30–40: compare language choices. 40–50: write a qualified argument.','Why does Ngũgĩ connect language with cultural power? What practical choices face writers working across languages?','https://brittlepaper.com/2025/06/ngugi-wa-thiongo-and-the-decolonial-imagination-a-reading-list/',True),
n('bhabha-signs','Homi K. Bhabha · Signs Taken for Wonders', '''## The encounter
Bhabha’s 1985 essay reads a missionary account of an encounter near Delhi in 1817 involving Anund Messeh, an Indian catechist, and a group who possess a Christian book. The episode is mediated by missionary records; readers do not have unfiltered access to every participant’s words.

## Authority and reinterpretation
The book appears as a sign of religious and colonial authority, yet the readers’ understanding of its origin and their conditions for accepting it do not simply reproduce missionary expectations. Their objections concerning the English and dietary practice complicate the claim that the text’s meaning can be transferred intact from one authority to another.

## Ambivalence and hybridity
Ambivalence describes the instability and contradictory effects within colonial authority. Hybridity, here, concerns transformations in meaning and authority produced through colonial encounters, not just a happy mixture of two pure cultures. Repetition and translation can unsettle an authority that depends on appearing original and secure.

## Critical caution
An interpretive disruption is not the same as the end of material colonial domination. Critics ask whether Bhabha’s linguistic focus sufficiently addresses economic and organised political struggles. Compare his reading with Ngũgĩ’s emphasis on institutions and language policy.''','0–10: identify the archived encounter. 10–20: map differing interpretations of the book. 20–30: define ambivalence. 30–40: discuss hybridity and power. 40–50: evaluate material limits.','Why is the book not simply a transparent vehicle of authority? What does hybridity mean in this analysis?','https://link.springer.com/chapter/10.1057/9781137540638_6'),
n('spivak-translation','Gayatri Chakravorty Spivak · The Politics of Translation', '''## Starting point
Spivak asks what it means to translate across unequal languages and cultures, especially in the context of feminist solidarity. Translation can make writing available to new readers, but it is not a neutral transfer of an unchanged message.

## Close reading and rhetoric
She calls translation an intimate form of reading. A translator needs to attend to the source language’s rhetoric, idiom, silences and particular social contexts, not merely convert a paraphrasable “message” into smooth English. She is concerned that a uniform, easy “translationese” can make very different writers sound alike.

## Solidarity and difference
Spivak questions the assumption that all women automatically share the same situation. Learning another language and its contexts can be part of a more responsible solidarity. This is an ethical demand to confront linguistic and political difference, not a guarantee that perfect translation or complete access to another person is possible.

## Application
Compare two translations of a short passage that is legally available or supplied in class. Note a choice of register, syntax or culturally specific term, then explain its effect. Do not assume one version is automatically correct without knowledge of the original and context.''','0–10: discuss translation as choice. 10–20: explain rhetoric and translationese. 20–30: compare two brief translations. 30–40: debate solidarity and difference. 40–50: reflect on uncertainty.','How can smooth translation erase difference? Why does Spivak connect language learning and solidarity?','https://benjamins.com/online/tsb/publications/11688')]
with open(P,'w',encoding='utf8') as f:json.dump(d,f,ensure_ascii=False,indent=2);f.write('\n')
print('Added',sum(len(v) for k,v in d.items() if k.startswith('course-38:')),'selections across five units')
