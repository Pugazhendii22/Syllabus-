import json
P='prepared-notes.json'
with open(P,encoding='utf-8') as f:d=json.load(f)
def n(id,title,body,lesson,questions,source,pre=False):
 r={'id':id,'title':title,'source':source,'text':f'# {title}\nNew Literatures in English · Semester 5\n\n{body}\n\n## 50-minute lesson\n{lesson}\n\n## Questions\n{questions}\n\nTeaching draft: check the prescribed text, translation and edition before class.'}
 if pre:r['status']='preliminary'
 return r
d['course-31:0']=[n('new-lit-intro','Introduction · New literatures and translation', '''## What the course means
The course surveys writing associated with regions beyond Britain, including Sri Lanka, the Caribbean, Australia, Latin America, Canada, Japan, China, New Zealand and Africa. “New literatures” is an institutional label, not a claim that these societies lacked literature before English or European colonialism. Many have long, diverse oral and written traditions.

## Language and power
English spread through trade, migration and colonial rule, but writers use it in different ways, drawing on local speech, Indigenous languages and literary traditions. Some works on this syllabus, including those of Borges, Saramago, Mishima and Gao, were originally written in languages other than English and are studied in English translation. Translation choices matter; compare a passage’s translator and edition, not just the author’s nationality.

## Reading comparatively
Ask how each work represents place, class, gender, migration, colonial rule and ecology. Avoid treating a whole continent or nation as a uniform culture. Settler-colonial and Indigenous experiences, for example, are not interchangeable. A comparison should link specific passages and allow important differences to remain.''','0–10: question the label “new.” 10–20: map listed regions. 20–30: identify original language and translator. 30–40: compare two accounts of place. 40–50: write a comparison without generalising a region.','Why can “new” be misleading? What changes when a work is read in translation?','https://www.pondiuni.edu.in/wp-content/uploads/2024/03/SyllabusNEP-B.A.HonorsEnglish2023-24.pdf')]
d['course-31:1']=[
n('country-towns','Kenneth Slessor · Country Towns', '''## Summary · non-detailed in syllabus
The speaker addresses Australian country towns, recalling their trees and squares, farmers, old public houses and general stores. An out-of-date entertainment notice lies under flies, suggesting a place where time moves slowly. On verandas people sleep; dogs seem to lick the sunshine and settle again after a distant sound. In the final stanza the speaker asks the towns for shade, sweetness, a bench and sleep, imagining an afternoon so leisurely that late day feels like noon.

## Technique
Playful sound, vivid similes and accumulated local details create a comic, sleepy atmosphere. The poem’s affectionate caricature is one perspective on country life, not a complete account of those communities or of Indigenous histories.''','0–10: identify setting. 10–20: paraphrase town details. 20–30: discuss old notice and sleeping dogs. 30–40: examine the speaker’s invitation to rest. 40–50: write about tone.','How does the poem make time seem slow? What is the effect of addressing towns directly?','https://mywordinyourear.com/2018/12/12/country-towns-kenneth-slessor-analysis/'),
n('year-foxes','David Malouf · The Year of the Foxes', '''## Summary · non-detailed
A speaker remembers being ten when his mother, seeing a chance to make money, brings fox-fur garments into the family sitting room for sale. Brisbane women arrive to buy them during wartime. At night the child imagines the foxes crying, their eyes and tails alive with danger. Yet among elegant cups and glasses the fur pieces remain dead animals. Later the fashionable buyers fasten the limp paws and wear the furs out into the street.

## Reading
The contrast between living imagination and dead commodities links childhood memory, wartime consumption and animal life. Domestic luxury is both ordinary and unsettling. The speaker’s dream should not be confused with a claim that the furs are literally alive.''','0–10: map household and buyers. 10–20: sequence the sale. 20–30: compare dream and display. 30–40: discuss fashion and the animal body. 40–50: describe the poem’s mixed tone.','Why do dead foxes appear alive to the child? How do luxury objects alter the scene?','https://www.poetryinternational.com/en/poets-poems/poems/poem/103-7290_The-Year-of-the-Foxes'),
n('journey-interior','Margaret Atwood · Journey to the Interior', '''## Summary · detailed
The speaker compares a journey into the mind with travel through a physical landscape. Hills and routes may look simple from a distance but become complicated when approached. The interior resembles an overgrown territory with shifting light and obstructing branches, yet differs from ordinary exploration: reliable maps and fixed routes are unavailable. Familiar small objects and fragments of thought interrupt the journey; the speaker wonders whether she is moving in circles. The ending warns that inward exploration can be dangerous and requires keeping one’s bearings.

## Close reading
The opening comparison between similarity and difference builds an extended metaphor, but mind and landscape never match perfectly. Changes of scale—from broad terrain to domestic objects—show how attention shifts. Irregular lines and movement across line breaks can make the reader experience uncertainty. “Getting lost” is an image of the difficulty of self-understanding, not a medical diagnosis.

## Discuss
Does the poem promise a final discovery, or emphasise the journey and its risks? Support either view with a detail from your assigned edition.''','0–10: sketch the landscape. 10–20: paraphrase similarities. 20–30: list differences and distractions. 30–40: discuss the danger of losing direction. 40–50: explain one image in a short paragraph.','Why are maps unreliable in the interior? How do domestic details interrupt the journey?','https://www.markedbyteachers.com/gcse/english/journey-to-the-interior-by-margaret-atwood.html'),
n('framed-harris','Claire Harris · Framed', '''## Summary · non-detailed
The speaker addresses a viewer who has bought a painting of island houses. Within the apparently picturesque image stands a woman carrying laundry, wearing worn shoes and bearing the marks of labour. The speaker recalls a close relationship with her: the woman gives the speaker the better plate and cup while keeping less for herself, works constantly and hopes for a different future for her. The speaker studies, distances herself and later leaves. The painting is put away, but the speaker imagines herself still inside it, pushing against its frame.

## Reading
A decorative picture becomes a way to examine unequal labour, aspiration, shame, memory and representation. The speaker’s relation to the woman can be discussed through textual evidence without inventing a relationship the poem does not explicitly settle. The frame both captures and restricts what an outsider sees.''','0–10: describe the painting. 10–20: trace the working woman’s actions. 20–30: discuss the speaker’s response. 30–40: interpret the frame. 40–50: explain the difference between picturesque view and lived labour.','What does the buyer’s picture conceal? Why does the speaker push against the frame?','https://muse.jhu.edu/article/6527/summary'),
n('musk-deer','A. D. Hope · Moschus Moschiferus', '''## Summary · non-detailed
Subtitled “A Song for St Cecilia’s Day,” the poem describes hunters seeking musk deer for the scent-bearing glands valued in perfume. As the animals grow scarce, hunters conceal themselves and one plays a flute. The beautiful music draws a deer from cover, where poisoned arrows kill it. The hunters remove the musk and leave the bodies. The closing address to Cecilia, patron of music, sets praise of music against its use as a trap.

## Reading
The poem connects beauty, commercial demand and violence. Its figures for numbers and predicted extinction are claims within the poem, not current conservation statistics. Discuss the irony of a song that celebrates music while showing music used to destroy.''','0–10: explain the title and setting. 10–20: sequence the hunt. 20–30: compare the music with its result. 30–40: discuss consumer demand. 40–50: write about the final address.','How does the flute change the hunt? Why is the dedication to Cecilia ironic?','https://www.austlit.edu.au/austlit/page/C199767'),
n('walcott-ruins','Derek Walcott · Ruined House — title to verify', '''## Title check · preliminary
The syllabus says “Ruined House.” A widely documented Walcott poem is “Ruins of a Great House”; it is likely but not verified that this is the intended text. Confirm the prescribed title and edition before relying on this guide.

## If the assigned poem is Ruins of a Great House
The speaker moves through the decayed remains of a grand house and its grounds. Rot, bones, limes and broken architecture evoke the passing of wealth and empire while calling attention to violence that made such grandeur possible. References to British literary and historical figures bring the culture of empire into the poem itself. The speaker’s anger at colonial crimes meets an impulse toward compassion, complicated by an allusion to John Donne’s reflections on human interconnectedness.

## Reading
The house’s ruin does not automatically erase historical harm: the poem suggests that its legacy persists. Avoid turning the ending into either simple forgiveness or the denial of anger. Check all allusions in the assigned edition.''','0–10: verify the title. 10–20: map images of decay. 20–30: trace the historical references. 30–40: discuss rage and compassion. 40–50: write a qualified interpretation.','Why must the title be checked? How do ruin and continuing injustice coexist?','https://kenanmalik.com/2017/05/04/derek-walcott-inside-the-ruins/',True),
n('sinbad-moraes','Dom Moraes · Sinbad', '''## Summary · detailed
The speaker addresses the legendary sailor Sinbad through compressed images of wind, waves, graves, diamonds, birds and travel. Journeys cross countries and require new maps. Old friends disappear into strange places while new acquaintances offer gestures whose warmth is uncertain. The speaker offers advice about choosing a rock and travelling companions, then returns to the wind and its unpredictable course. The final observation suggests that some people never know a stable home.

## Reading
The poem invokes the voyages of Sinbad without simply retelling all seven tales. Its fragmented lines and abrupt images make travel feel disorienting as well as adventurous. A travelling identity is one possible reading; avoid asserting that every line records an event in Moraes’s own life or assigning a single fixed meaning to every image.''','0–10: introduce the legendary traveller. 10–20: trace sea and wind. 20–30: compare old and new friends. 30–40: discuss home and movement. 40–50: explain an image using two possible readings.','What does the allusion to Sinbad contribute? Why is travel both exciting and unsettling?','https://sde.uoc.ac.in/sites/default/files/sde_videos/eng2c08.pdf'),
n('compass-borges','Jorge Luis Borges · A Compass', '''## Summary · detailed
In this poem, originally “Una brújula” in Spanish, the speaker imagines everything as words in a language through which someone or something continually writes the world’s history. Ancient cities, the speaker and other people all pass through that immense, confused text. The speaker’s own life is difficult to understand, like a riddle or code; Babel suggests a multitude of voices and disorder. Behind names lies something that cannot be named. The speaker senses its shadow in the delicate moving needle of a compass, which reaches imaginatively towards a distant sea and resembles a clock in a dream or a stirring sleeping bird.

## Reading
An everyday instrument of orientation becomes an image of mystery rather than a final answer. Compare the huge scale of world history with the tiny needle. Translation can change rhythm, rhyme and individual word choices; identify your translator. This is a poem, not Borges’s detective story “Death and the Compass.”''','0–10: identify the language metaphor. 10–20: paraphrase history and Babel. 20–30: study the shift to the compass. 30–40: compare clock and bird images. 40–50: explain how direction coexists with mystery.','Why compare the world to language? What can a compass suggest without solving the mystery?','https://www.poetryfoundation.org/poetrymagazine/poems/38644/a-compass')]
d['course-31:2']=[
n('blindness','José Saramago · Blindness — major story sequence', '''## Content and access note
The novel contains confinement, sexual assault and violence. Blindness is used as a literary metaphor, a choice that blind readers and disability scholars may contest. Do not equate real blindness with moral failure, helplessness or social collapse. The novel was originally written in Portuguese; check your translator.

## The epidemic and quarantine
An unnamed driver suddenly sees only white while stopped at a traffic light. A man who helps him home steals his car and also loses his sight. An ophthalmologist examines the first man but cannot explain the condition; he and other patients soon become blind. Authorities confine affected people in a disused asylum guarded by soldiers. The doctor’s wife falsely claims to be blind so she can accompany him; she remains able to see.

## Life inside
More people arrive, food and sanitation deteriorate, and soldiers’ fear produces violence. A group of armed internees seizes the food and demands valuables. When valuables run out, the group demands that women be sent to them; the women are sexually assaulted and one dies. The doctor’s wife later kills the leader with scissors. Another woman sets fire to the occupiers’ ward. Survivors escape as the asylum burns and discover the epidemic has spread beyond the walls.

## City and fragile community
The doctor’s wife guides a small group through a city of hunger and disorder, including her husband, the first blind man and his wife, the girl with dark glasses, the boy and an old man with an eye patch. They find food and shelter in the doctor’s home and try to care for one another. A dog comforts the doctor’s wife. Her sight gives her practical power and a heavy burden; the others also form relationships and contribute to the group.

## Ending and interpretation
Members of the group unexpectedly regain their sight. Neither the cause nor the cure is explained. The wife fears for a moment that her own sight might fail. The novel asks about institutions, fear and responsibility, but its allegorical use of disability should be debated critically. This is a story guide, not a chapter-by-chapter commentary.''','0–10: set content and disability-aware boundaries. 10–20: trace epidemic and confinement. 20–30: discuss control of food. 30–40: compare harm and mutual care. 40–50: question the blindness metaphor.','How do institutions shape the crisis? What are the risks of using blindness as a metaphor for ethical failure?','https://www.litcharts.com/lit/blindness/summary'),
n('reef','Romesh Gunesekera · Reef — story sequence', '''## Narrative frame
The adult narrator Triton, now living in England, meets a young Sri Lankan at a petrol station. The encounter leads him back through memories of his childhood and work in Sri Lanka. The story’s retrospective voice matters: what we learn of others comes through Triton’s attention and limitations.

## The household
As a boy Triton enters the home of Mister Salgado, an educated man interested in marine life and the erosion of coral reefs. The older servant Joseph intimidates him; after Joseph is dismissed and the cook Lucy leaves, Triton takes increasing responsibility for the household. He becomes a skilled cook, finds purpose in feeding guests and watches conversations about science and politics.

## Nili and change
Salgado’s relationship with Nili transforms the house. Triton helps create their shared occasions through elaborate meals and is emotionally invested in their happiness. Their relationship later breaks down amid jealousy and tension. Outside the house political conflict grows, although the sheltered domestic viewpoint does not show every event directly.

## Departure
Salgado and Triton leave for England. Triton gradually builds a more independent life and eventually runs a restaurant. Salgado later returns to Sri Lanka after news concerning Nili; Triton remains in London. Their different trajectories complicate the earlier bond between employer and servant.

## Interpretation
The reef suggests an ecosystem and a vulnerable boundary, but it need not stand for only one thing. Compare ecological change with political instability and ask how class and service shape Triton’s admiration. Verify chapter divisions in the assigned edition.''','0–10: explain the memory frame. 10–20: map the household. 20–30: trace Nili’s arrival and departure. 30–40: compare reef and political change. 40–50: write about Triton’s viewpoint.','How does food mediate relationships? What can Triton observe, and what might his loyalty obscure?','https://www.romeshg.com/reviews-page-reef'),
n('things-fall-apart','Chinua Achebe · Things Fall Apart — major story sequence', '''## Content note
The novel includes domestic violence, the death of children, colonial violence and suicide. It depicts Igbo communities with internal debate and variation, not a single timeless “African culture.”

## Umuofia and Okonkwo
Okonkwo becomes respected through wrestling, farming and hard work, determined not to resemble his indebted father Unoka. His fear of appearing weak influences his treatment of his family. After a conflict between communities, the boy Ikemefuna comes to live in Okonkwo’s household. He grows close to Nwoye and calls Okonkwo father. When the community decides Ikemefuna must die, an elder advises Okonkwo not to take part; afraid of seeming weak, Okonkwo strikes him. Nwoye is deeply affected.

## Family and exile
Okonkwo values his daughter Ezinma, whose mother Ekwefi has endured the deaths of other children. Community ceremonies, stories and institutions show a complex social world, not just Okonkwo’s viewpoint. At the funeral of the elder Ezeudu, Okonkwo’s gun accidentally kills Ezeudu’s son. Because the killing is accidental, he and his family must leave for seven years. His maternal relatives receive him in Mbanta; his friend Obierika helps protect his interests.

## Mission and colonial rule
During exile missionaries gain converts, including Nwoye, who finds something meaningful in their message. His choice reflects both colonial intervention and tensions already present in his family and community. Political power and courts grow alongside the mission. On returning to Umuofia, Okonkwo finds the situation changed. Mr Brown’s approach to local leaders differs from that of his successor Mr Smith; neither stands for every colonial actor.

## Crisis and ending
After a convert unmasks an ancestral spirit during a ceremony, clan members destroy the church. The District Commissioner summons and imprisons leaders, including Okonkwo, and they are humiliated and fined. At a later meeting Okonkwo kills a court messenger; the others do not follow him into war. He dies by suicide. The commissioner imagines reducing the complex life to a small part of his own colonial book, exposing the violence of an outside narrative that refuses local voices.

## Interpretation
Analyse Okonkwo’s choices and gendered expectations alongside colonial institutions; neither alone explains the whole novel. This outline covers major events rather than all chapters.''','0–10: locate community and protagonist. 10–20: trace Ikemefuna and family. 20–30: explain exile and Nwoye’s conversion. 30–40: follow church and court conflict. 40–50: discuss the commissioner’s final framing.','Why does Okonkwo join Ikemefuna’s killing? How does Achebe challenge the commissioner’s account of the community?','https://www.thoughtco.com/things-fall-apart-overview-4693544')]
d['course-31:3']=[
n('damask-drum','Yukio Mishima · The Damask Drum', '''## Context and warning
Mishima adapts a traditional Japanese Noh story into a modern setting. Read the assigned translation and distinguish this version from the older play. The plot includes humiliation and suicide.

## Story
An elderly janitor working in a Tokyo office building becomes infatuated with a woman associated with a dress shop across the way. Others learn of his feelings and cruelly tell him that he can win her attention if she hears him beat a drum. The drum is covered in damask cloth and cannot sound in the way promised. His effort becomes an impossible test and a spectacle for others. Humiliated and despairing, he kills himself.

His ghost returns and continues the effort to make himself heard. Unlike the revenge of the traditional version as commonly described, the modern version leaves the woman unable to hear the ghostly drum, and his suffering continues. The silence raises questions about desire, cruelty, communication and the limits of revenge.

## Performance
Discuss sound and silence, the modern office and the presence of a ghost. A person’s refusal to return affection does not itself justify harassment; distinguish the janitor’s longing from the deliberate humiliation by others.''','0–10: introduce adaptation and content warning. 10–20: sequence the impossible task. 20–30: compare living man and ghost. 30–40: discuss sound and cruelty. 40–50: compare modern and traditional versions cautiously.','Why is the drum an impossible promise? What does silence do in performance?','http://atecnet.org/en/performances_more/496.html'),
n('no-sugar','Jack Davis · No Sugar', '''## Context and content
Set in Western Australia during the Great Depression, the play depicts the Millimurra–Munday Aboriginal family under racist so-called protection policies. It includes forced removal, imprisonment and sexual violence. Its characters speak in English and Nyoongah; language is part of the play’s resistance and community life.

## Northam and forced removal
Gran, Jimmy, Milly, Sam and their family live at Government Well near Northam, managing inadequate rations and limited opportunities. Jimmy and Gran challenge officials. Authorities plan to move the Aboriginal community to Moore River, using alleged disease as a justification while disregarding the families’ wishes. The family is removed despite its protests.

## Life at Moore River
The settlement is controlled by officials, including superintendent Neal. The family maintains relationships, humour and resistance under restriction. Joe and Mary fall in love; Mary becomes pregnant. They escape together and return toward Northam, but are caught. Joe is imprisoned and Mary is returned to the settlement.

## Violence and ending
Neal punishes Mary, whipping her after she resists work that she fears will expose her to his sexual advances. Gran and Milly support her, and her baby is born at the settlement. During an official Australia Day ceremony Jimmy challenges the rhetoric of protection; he collapses and dies. Joe returns, names the baby Jimmy after his uncle and obtains permission to leave with Mary and their child. Their departure suggests continuing family and resistance, not an end to the system’s violence.

## Performance
Contrast official speeches with family dialogue and song. The play dramatises colonial control from an Aboriginal perspective and should be read in relation to the particular people and policies it represents.''','0–10: introduce setting and content. 10–20: trace forced removal. 20–30: discuss Joe and Mary. 30–40: compare official language with family experience. 40–50: consider the ending and song.','What does “protection” mean to the officials and the family? How does family support function as resistance?','https://www.litcharts.com/lit/no-sugar/summary')]
d['course-31:4']=[
n('temple-gao','Gao Xingjian · The Temple', '''## Translation and story
The assigned story is available in Mabel Lee’s English translation from Chinese. A narrator and his new wife Fangfang, happy on their honeymoon after difficult years, leave a delayed train on impulse to explore a town. The apparently peaceful place turns out to be busy and commercial. Directed to an old temple, they cross a river, climb a hill and find a neglected building with broken walls, weeds and traces of ordinary agricultural use.

A stern-looking man arrives carrying melons. He shares one with the couple, who offer cake in return. A boy with him wants to catch grasshoppers. The narrator asks if the child is his son; the man explains that he is a cousin’s child whom he hopes to adopt. When Fangfang asks about his wife, he says nothing and walks away. The couple recognise that their question may have touched a painful subject, but the story does not explain his circumstances.

They notice a precarious roof tile that may fall. From a distance they watch the man and boy leave together; the child runs ahead and back, holding his cage. Fangfang playfully imagines that the man caught the five grasshoppers the boy wanted. The story closes with the narrator returning to the memory of the temple.

## Reading
The fleeting encounter qualifies the couple’s happiness with an awareness of other lives and unspoken pain. The tile suggests vulnerability, but the text does not say it falls or injures anyone. Hospitality crosses the travellers’ initial assumptions about the man.''','0–10: map the journey. 10–20: describe the temple. 20–30: trace food and conversation. 30–40: discuss silence and the loose tile. 40–50: write what the ending does and does not establish.','How do the couple’s assumptions change? What remains unspoken about the man?','https://www.newyorker.com/magazine/2003/02/17/the-temple'),
n('suburban-fairy','Katherine Mansfield · A Suburban Fairy Tale', '''## Story sequence
Mr and Mrs B sit in their warm suburban dining room after wartime rationing, enjoying breakfast and discussing desirable food. Their small, delicate son Little B notices hungry sparrows outside in the cold and asks his parents to feed them. Absorbed in their newspaper and meal, they dismiss his request and refuse to open the window.

Behind the curtain Little B sees the sparrows become little boys in brown coats, crying for food. He tries to make his parents see and hear, while his father dismisses talk of famine. The parents discover their child apparently outside among the hungry boys, himself asking for food. They finally open the window and invite them in, but the boys turn back into sparrows and fly away. The story ends before any simple rescue is achieved.

## Reading
The fairy-tale transformation interrupts the comfort of the breakfast room. The parents’ abundance and denial contrast with the child’s imaginative attention to hunger. The boundary of the window separates security from need; its opening comes too late. Discuss whether the transformation is literal, imagined or deliberately unresolved.''','0–10: compare inside and outside. 10–20: track the parents’ food talk. 20–30: retell the transformation. 30–40: discuss famine and the late opening. 40–50: write about the ending’s ambiguity.','Why do the parents finally act? What does the story leave uncertain about the transformation?','https://americanliterature.com/author/katherine-mansfield/short-story/a-suburban-fairy-tale')]
with open(P,'w',encoding='utf-8') as f:json.dump(d,f,ensure_ascii=False,indent=2);f.write('\n')
