"""Add American Literature II drafts without replacing existing units."""
import json
P='prepared-notes.json'
with open(P,encoding='utf8') as f:d=json.load(f)
def n(id,title,body,lesson,questions,source,preliminary=False):
 x={'id':id,'title':title,'source':source,'text':f'# {title}\nAmerican Literature II · Semester 7\n\n{body}\n\n## 50-minute lesson\n{lesson}\n\n## Discussion and revision\n{questions}\n\nTeaching draft: check the assigned edition or text, verify quotations and consider alternative interpretations before teaching.'}
 if preliminary:x['status']='preliminary'
 return x
d['course-39:0']=[
n('movements-early','American literature · Regionalism, modernism and Harlem', '''## Literary regionalism
Regionalist writing attends to a particular place, its speech, landscapes and social practices. It was prominent after the US Civil War but is not limited to one period. Ask who describes the region and whether dialect preserves local voices or risks stereotyping them.

## Modernism and the avant-garde
Modernism encompasses many responses to industrialisation, urban life, war and changing ideas about identity. Fragmented form, shifting perspective, unconventional syntax and experimentation appear in some works, but not all modernists write alike. “Avant-garde” points to experimental work challenging artistic conventions; it overlaps with modernism without naming exactly the same group.

## The Lost Generation
The phrase is associated with writers shaped by the First World War and its aftermath, including US expatriates such as Hemingway and Fitzgerald. Disillusionment, mobility and social change are recurring concerns, but not everyone shared one outlook. Fitzgerald’s “Winter Dreams” links aspiration to class and disappointed desire.

## Harlem Renaissance
The Harlem Renaissance was a diverse flowering of Black cultural and intellectual work centred in Harlem in the 1920s and early 1930s, with national and transnational connections. Hughes and McKay wrote in different forms and voices. Migration, racism, music, identity and debate over representation are important, but Black artistic history neither began nor ended with this movement.''','0–10: create a flexible timeline. 10–20: compare region and modernist experiment. 20–30: discuss the Lost Generation. 30–40: locate Harlem’s networks. 40–50: connect a prescribed text to a movement.','Why do movement dates overlap? How can regional speech both represent and stereotype a community?','https://masters.libguides.com/c.php?g=598462&p=6105472'),
n('movements-late','American literature · Civil rights, Beat and postmodernism', '''## Civil rights and cultural change
The Black freedom struggle long predates the mid-twentieth century, while mass movements of the 1950s–60s challenged segregation and voting discrimination through collective organising, litigation, protest and cultural work. Literature both responds to and participates in political debate; no single work represents the whole movement. Hansberry’s A Raisin in the Sun engages housing segregation and unequal opportunity.

## Beat movement
The Beat writers of the 1950s challenged aspects of conformity and materialism through travel, unconventional form, performance and spiritual exploration. Their work also invites criticism of gender and racial appropriation. A movement includes networks and disagreements, not only its most famous male authors.

## Postmodernism
Postmodern writing often uses irony, self-reference, fragmentation, mixed genres and scepticism toward complete or authoritative narratives. Such techniques overlap with modernism, so a text is not automatically postmodern because it is fragmented. Ask what the technique does in a particular work.

## Comparison
Place one poem and one play on the timeline. Which artistic forms and political contexts connect them, and where does the label obscure difference? Literary periods are interpretive tools, not sealed containers.''','0–10: distinguish social movement and literary category. 10–20: discuss collective civil-rights action. 20–30: outline Beat writing. 30–40: compare modernist and postmodern techniques. 40–50: apply one label critically.','How did literature engage housing discrimination? Why is it risky to reduce the Beats to a single type of rebellion?','https://masters.libguides.com/c.php?g=598462&p=6105472')]
d['course-39:1']=[
n('frost-wall','Robert Frost · Mending Wall', '''## Summary
Each spring the speaker and a neighbour repair a stone boundary wall damaged by frost and hunters. They walk on opposite sides, balancing stones together. The speaker questions why their apple orchard and pine trees need separation; the neighbour repeats a saying inherited from his father about fences and neighbours. The poem ends without resolving the argument.

## Meaning and form
The wall can protect boundaries while also dividing people. Its repair ironically creates an occasion for meeting. The speaker challenges habit but is also the one who contacts the neighbour and joins the work. Colloquial conversation moves within mostly blank verse, allowing a natural voice without eliminating careful form.

## Close reading
Compare the repeated opening idea that something resists a wall with the neighbour’s repeated proverb. Notice that the speaker’s description of the neighbour as primitive is a judgment, not an objective portrait. Does the poem favour openness, boundaries, or an uneasy mixture?''','0–10: reconstruct the task. 10–20: compare the two views. 20–30: discuss the paradox of shared repair. 30–40: examine repetition and voice. 40–50: defend an interpretation.','Why does the speaker still help mend the wall? How can a boundary both divide and connect?','https://www.litcharts.com/poetry/robert-frost/mending-wall'),
n('cummings-etc','E. E. Cummings · my sweet old etcetera', '''## Summary
The speaker remembers relatives’ responses to war: Aunt Lucy explains what people are fighting for; sister Isabel makes clothing; the mother hopes for a brave death; the father speaks enthusiastically of privilege. Meanwhile the speaker lies in deep mud, dreaming of an intimate beloved. Public language about sacrifice is set against bodily conditions and private desire.

## Technique
Repeated “etcetera” compresses or dismisses familiar phrases, but changes meaning as it appears in lists, slogans and the final intimate address. Lowercase, unusual line breaks, parentheses and fragmented syntax make readers pause and reconstruct connections. The ending’s desire does not erase danger or prove that the speaker survives.

## Interpretation
The poem satirises the distance between confident patriotic talk and the experience of someone at war. Avoid assuming every relative has identical motives: making socks is practical labour, while the poem’s tone gives the list an ironic edge.''','0–10: map each family response. 10–20: explain the repeated word. 20–30: contrast mud and public rhetoric. 30–40: examine typography. 40–50: discuss the ending.','How does “etcetera” change across the poem? What is the effect of placing the speaker in mud?','https://www.poetryverse.com/e-e-cummings-poems/my-sweet-old-etcetera'),
n('hughes-too','Langston Hughes · I, Too', '''## Summary
A Black speaker describes being sent away to eat in the kitchen when company arrives. Instead of accepting exclusion as permanent, the speaker imagines a future at the table, when those who excluded him will recognise his beauty and be ashamed. The closing claim asserts belonging to America itself.

## Technique and context
Short free-verse lines, repetition, conversational diction and the movement from present to “tomorrow” make the assertion direct and forceful. The kitchen and table suggest segregation and national belonging, while the speaker’s laughter and growing strength resist a narrative of passive victimhood. Hughes’s work is associated with the Harlem Renaissance; the poem can also be read in dialogue with Whitman’s national song without assuming every reader hears the same allusion.

## Questions
Whose hospitality is being challenged? Does “tomorrow” describe a guaranteed date or a political hope? Avoid suggesting racism ended simply because the poem anticipates a different future.''','0–10: map kitchen and table. 10–20: trace the shift in time. 20–30: read the final claim. 30–40: discuss the national voice. 40–50: write about dignity and exclusion.','What does moving from kitchen to table symbolise? How does the final line revise the opening claim?','https://www.poetryfoundation.org/poems/47558/i-too'),
n('plath-mirror','Sylvia Plath · Mirror', '''## Summary
A mirror speaks, describing its apparently exact reflection and its long view of a wall. In the second stanza it becomes a lake in which a woman searches for herself. She turns to softer light but returns repeatedly to the reflecting surface, distressed by what she sees. The final image contrasts a drowned younger self with an older woman rising toward her like a fish.

## Technique and tension
Personification gives an object a voice; the lake metaphor adds depth and danger to a flat surface. The mirror claims impartial truth, yet its possessive language and description of the woman invite readers to question whether reflection reveals a whole person. The poem addresses ageing and social judgments about appearance, not an objective verdict that older bodies are terrible.

## Form
The two balanced stanzas move from the mirror’s account of itself to the woman’s repeated encounter. Read the fish image as disturbing and interpretable, rather than as proof of the poet’s biography or a diagnosis.''','0–10: identify the speaker. 10–20: compare mirror and lake. 20–30: trace the woman’s visits. 30–40: question truth and appearance. 40–50: interpret the final image sensitively.','What can a mirror show, and what can it not show? Why does changing the mirror into a lake matter?','https://www.gradesaver.com/sylvia-plath-poems/study-guide/summary-mirror'),
n('warren-hawk','Robert Penn Warren · Evening Hawk', '''## Summary
At sunset a hawk emerges through light and shadow. Its wing is compared to a blade cutting down another day. The speaker urges attention to the bird, whose flight seems beyond human error; darkness gathers, a star appears, and the closing image imagines history dripping like a leaking pipe.

## Images and tone
Angular geometry, sweeping movement and the harvest-like scythe create both beauty and unease. The silent falling of time contrasts with the small, persistent sound imagined at the end. The star compared to Plato introduces a human philosophical reference into a scene that exceeds individual human control.

## Interpretation
The hawk can suggest time, mortality or a perspective indifferent to human judgments, but it is also a specific bird seen in flight. The leaking pipe can imply slow historical accumulation or neglect; it need not prove that all human action is meaningless. Support an interpretation through changes in imagery and tone.''','0–10: follow the hawk’s movement. 10–20: examine the scythe comparison. 20–30: track sound and silence. 30–40: debate the final image. 40–50: write a qualified interpretation.','How do the scythe and leaking pipe offer different images of time? What changes when the poem moves into darkness?','https://poemanalysis.com/robert-penn-warren/evening-hawk/'),
n('angelou-woman','Maya Angelou · Phenomenal Woman', '''## Summary
The speaker answers people who wonder about her presence although she does not conform to a fashion model’s measurements. She names her stride, body, smile and manner; she describes men’s attention but insists on an inner quality they cannot fully grasp. Repeated self-affirmation culminates in pride in her identity.

## Form and themes
Refrain, rhythmic lists, vivid bodily details and direct address create a performance of confidence. The poem challenges narrow standards of beauty while celebrating embodiment, self-possession and sensuality. Read it in relation to Angelou’s work as a Black woman without treating her speaker as the only possible model of womanhood.

## Discussion
The speaker notices others’ reactions, but her worth is not simply bestowed by male approval. Ask how the poem holds together outward movement and inward confidence. Students need not share personal details to discuss beauty standards.''','0–10: summarise the speaker’s answer. 10–20: identify a repeated refrain. 20–30: connect physical detail and confidence. 30–40: discuss standards of beauty. 40–50: analyse voice.','How does the refrain build self-definition? Why should confidence not be reduced to others’ approval?','https://www.poetryverse.com/maya-angelou-poems/phenomenal-woman'),
n('baraka-america','Amiri Baraka · Somebody Blew Up America', '''## Content and context
Written in response to the September 11, 2001 attacks, the long poem asks a barrage of questions about violence, racism, empire and historical responsibility. Its repeated questions, lists, performance rhythms and shifts in scale challenge readers to consider violence beyond one event.

## Reading the structure
The speaker moves among historical injustices, named public figures and urgent questions of who knew or benefited. The accumulating “who” creates force but does not make every accusation true. Distinguish a poem’s rhetorical claims from independently verified historical evidence.

## Essential factual and ethical caution
The poem repeats a false conspiracy claim that thousands of Israelis were warned to stay away from the World Trade Center. It has been criticised as invoking an antisemitic conspiracy trope; Baraka denied that his poem was antisemitic. Teach the claim as false and the controversy as part of the work’s reception, without equating Jewish people or Israelis collectively with government actions. The September 11 attacks were carried out by al-Qaeda.

## Classroom approach
Give a content warning for depictions of violence and prejudice. Analyse rhythm and political anger while critically examining misinformation; do not ask students to endorse a conspiracy in order to interpret the poem.''','0–10: establish 9/11 context and content warning. 10–20: map repeated questions. 20–30: distinguish rhetorical claim and evidence. 30–40: discuss the false conspiracy responsibly. 40–50: evaluate the poem’s reception.','How does repeated questioning shape the poem? Why must a literary accusation be checked against evidence?','https://www.jmu.edu/news/fightandfiddle/2015/montpelier-baraka.shtml')]
d['course-39:2']=[
n('streetcar-early','A Streetcar Named Desire · Scenes 1–6', '''## Content warning
The play includes domestic abuse, sexual violence, suicide and involuntary institutionalisation. Discuss without graphic re-enactment or blaming victims.

## Scenes 1–2: arrival and Belle Reve
Blanche DuBois arrives in New Orleans to stay with her sister Stella and Stella’s husband Stanley Kowalski. Blanche says the family estate Belle Reve has been lost. Her refined performance of status and her drinking contrast with the cramped apartment. Stanley examines documents and questions the loss; Stella’s pregnancy is revealed.

## Scenes 3–4: poker and violence
At a poker game Blanche meets Stanley’s friend Mitch. Stanley becomes angry, throws the radio and strikes Stella. The sisters seek safety upstairs, but Stella returns when Stanley calls her. The next morning Blanche urges Stella to leave; Stella describes her attachment to Stanley. Stanley overhears Blanche’s harsh description of him. Their different social positions do not excuse his abuse.

## Scenes 5–6: desire and memory
Blanche worries about rumours from her past and continues to pursue Mitch. On a date she recounts her young husband Allan’s death by suicide after she discovered his relationship with another man and reacted with disgust. Her grief and shame shape her account, but the play should not suggest his sexuality itself caused his death.

## Form
Music, light, a paper lantern and the small stage space reveal tension between perception, memory and self-presentation. Do not equate Blanche’s vulnerability with moral innocence in every action or treat Stanley’s violence as inevitable.''','0–10: give a content warning. 10–20: map the apartment and estate. 20–30: discuss poker night. 30–40: examine Blanche’s account of Allan sensitively. 40–50: interpret light.','How does Stanley respond to Belle Reve’s loss? Why should abuse be discussed without blaming Stella or Blanche?','https://www.thoughtco.com/a-streetcar-named-desire-summary-4685191'),
n('streetcar-late','A Streetcar Named Desire · Scenes 7–11', '''## Scenes 7–8: exposure
At Blanche’s birthday, Stanley tells Stella what he has learned about Blanche’s life in Laurel, including her dismissal after sexual involvement with an underage student. He has told Mitch; Mitch does not attend the party. Stanley gives Blanche a bus ticket. Stella goes into labour and is taken to hospital. Separate a character’s rumours from verified facts while also taking the student’s vulnerability seriously.

## Scenes 9–10: confrontation and assault
Mitch confronts Blanche about her past and demands to see her in strong light. She seeks understanding; he rejects marriage and behaves coercively. Later Stanley returns while Stella is away. Blanche imagines rescue by an old admirer, Shep Huntleigh. Stanley confronts and rapes her. The play signals the assault theatrically rather than requiring the audience to witness a graphic act.

## Scene 11: removal
Blanche has told Stella about the rape, but Stella says she cannot believe the story and go on living with Stanley. A doctor and matron arrive to take Blanche to an institution; she initially believes she is leaving with a wealthy admirer. Mitch is distressed, and Stanley comforts Stella as Blanche is led away.

## Interpretation
The final scene raises questions about credibility, gender, class and medical authority. Blanche’s illusions do not make Stanley’s assault her fault. Her institutionalisation is a dramatic event in a particular historical setting, not an argument against all mental-health care.''','0–10: warn about content. 10–20: trace Stanley’s disclosures. 20–30: discuss the two confrontations without graphic detail. 30–40: analyse Stella’s position and the ending. 40–50: write on credibility and power.','Why does Mitch’s visit change? How does the ending complicate the distinction between appearance and truth?','https://www.thoughtco.com/a-streetcar-named-desire-summary-4685191'),
n('salesman-act','Death of a Salesman · Acts I and II', '''## Structure and warning
Arthur Miller’s play moves between a present-day crisis and Willy Loman’s memories and imagined conversations. It includes suicide; discuss Willy’s reasoning as a character’s tragic belief, not an effective solution.

## Act I
Willy returns from a failed sales trip, exhausted and increasingly confused. His sons Biff and Happy are visiting. Memories show Willy encouraging Biff’s athletic promise while dismissing Bernard’s academic work, and reveal his affair through images of the Woman and stockings. Linda explains that Willy’s income is failing and that he has attempted to harm himself. Biff and Happy propose a business plan; Willy hopes Biff can obtain backing from a former employer, Bill Oliver.

## Act II
Willy asks Howard for local work but is dismissed. Charley offers him a job, which Willy refuses, although he accepts money from him. Biff discovers Oliver barely remembers him and impulsively steals a pen. At dinner the sons leave Willy behind. A memory of Biff’s visit to Boston reveals his discovery of Willy’s affair, which shattered his idealised image of his father.

At home Willy plants seeds and imagines talking to his dead brother Ben about insurance money. Biff tries to confront the family’s illusions and cries; Willy recognises his son’s love but interprets it through his dream of success. He drives away and dies in a crash. Do not assume the insurance payout is guaranteed.''','0–10: map present and memory. 10–20: discuss work and family expectations. 20–30: trace Oliver and the restaurant. 30–40: examine Boston and seeds. 40–50: discuss the ending sensitively.','Why does Biff’s Boston visit matter? How do memory scenes change the audience’s understanding of Willy?','https://www.litcharts.com/lit/death-of-a-salesman/summary'),
n('salesman-requiem','Death of a Salesman · Requiem and interpretation', '''## The graveside
In the short Requiem, Linda, Biff, Happy, Charley and Bernard respond to Willy’s death. The small attendance contrasts with Willy’s expectation of a crowded funeral. Linda has made the last mortgage payment but cannot understand how the family can be “free” when Willy is gone. Biff concludes that his father pursued an unsuitable dream; Happy vows to continue that dream. Charley offers a defence of a salesman’s need for hopes and dreams.

## Interpretation
The house, stockings, seeds and salesmanship can be read as material details as well as symbols. The play criticises a culture that measures people by sales, popularity and wealth, but Willy’s difficulties also involve family relationships and his own choices. Avoid presenting suicide as financially certain, heroic or morally required: the drama shows loss and conflicting responses.

## Comparison
Compare Willy’s dream of individual success with the Younger family’s shared struggle for housing in A Raisin in the Sun. Different histories of race and class matter; neither family is simply a copy of the other.''','0–10: list who attends. 10–20: compare Biff, Happy and Charley. 20–30: discuss Linda’s final response. 30–40: compare the Younger family. 40–50: write on the American Dream.','How do Biff and Happy interpret Willy’s life differently? What is ironic about the final house payment?','https://www.litcharts.com/lit/death-of-a-salesman/summary'),
n('raisin','Lorraine Hansberry · A Raisin in the Sun: act-by-act', '''## Act I
In a crowded Chicago apartment, the Younger family awaits a life-insurance payment after Big Walter’s death. Mama wants security and a home, Walter hopes to invest in a liquor store, and Beneatha wants to become a doctor. Ruth learns she is pregnant and considers an abortion amid financial strain. Beneatha’s discussions with Joseph Asagai and George Murchison raise questions of identity, gender and assimilation. The check arrives.

## Act II
Mama buys a house in Clybourne Park, a white neighbourhood. She later gives Walter the remaining money, instructing him to save a portion for Beneatha’s education. On moving day Karl Lindner offers to buy the family out to keep the neighbourhood segregated; the family refuses. Bobo then reports that Willy Harris has disappeared with Walter’s investment, including the money intended for Beneatha.

## Act III
Asagai invites Beneatha to consider a future in Nigeria; she has not made a final decision by the end. Walter initially plans to accept Lindner’s offer. With his son Travis present, he rejects the buyout and affirms the family’s intention to move. Mama leaves with her plant. The curtain falls as they depart the apartment, before the audience sees their life in the new neighbourhood.

## Themes
The insurance money connects family dreams to grief and unequal opportunity. The title invokes Langston Hughes’s question about a deferred dream. Resist treating the final decision as proof that housing racism has disappeared.''','0–10: map family dreams. 10–20: track the money. 20–30: examine Lindner’s proposal. 30–40: debate Walter and Beneatha’s choices. 40–50: analyse Mama’s plant.','What does Mama instruct Walter to do with part of the money? Does the play show the family settled safely in its new home?','https://www.coursehero.com/lit/A-Raisin-in-the-Sun/summaries/'),
n('sandbox','Edward Albee · The Sandbox', '''## Dramatic sequence
A Young Man performs exercises on a bare beach-like stage; a Musician sits nearby. Mommy and Daddy bring Grandma and place her in a sandbox. Their conversation and instructions to the Musician make the scene deliberately artificial. Grandma complains, addresses the audience and tells fragments of her life, interrupting the family’s sentimental treatment of her.

As light changes and an offstage rumble is heard, Mommy and Daddy perform grief and then prepare to move on. Grandma covers herself with sand and plays dead; after they leave she discovers she cannot move. The Young Man identifies himself as the Angel of Death and kisses her forehead. Grandma responds to his performance with warmth and comments on his acting.

## Analysis
The sandbox can suggest both childhood and a grave. Direct address, rapid changes of light, stock family names and references to acting expose theatrical conventions. The play criticises neglect and ritualised grief, but Grandma is witty and observant rather than simply an object of pity. Interpret the ending’s tenderness alongside its dark comedy.''','0–10: draw the bare stage. 10–20: trace Grandma’s treatment. 20–30: map light and music. 30–40: analyse the Young Man’s role. 40–50: discuss satire and tenderness.','How does the sandbox acquire more than one meaning? What changes when Grandma addresses the audience?','https://www.gradesaver.com/the-sandbox/study-guide/summary-part-2')]
d['course-39:3']=[
n('old-man','The Old Man and the Sea · story guide', '''## Before the voyage
Santiago is an ageing Cuban fisherman who has gone 84 days without catching a fish. His young friend Manolin cares for him, but his parents require him to fish on a luckier boat. They speak about baseball, including Joe DiMaggio, and Manolin brings food. Santiago dreams of lions on African beaches.

## At sea
On the eighty-fifth day Santiago sails far into the Gulf Stream. A huge marlin takes his bait and pulls the skiff for a long struggle. The old man suffers pain, cramp and exhaustion; he eats raw fish to keep his strength and wishes the boy were with him. He respects the marlin as a brother and worthy opponent even while trying to kill it. On the third day he draws it alongside and harpoons it.

## Return
Santiago lashes the marlin to the boat, but sharks attracted by blood attack it. He kills some sharks and uses or loses weapons while defending the fish; by the time he reaches harbour, little remains beyond the skeleton. Exhausted, he carries his mast to his shack and sleeps. Manolin weeps on seeing him and promises to fish with him again. Tourists mistake the remains for those of a shark; Santiago dreams of lions once more.

## Meaning
Skill, endurance, pride, companionship and ecological kinship coexist. The ending is not simply a victory or defeat: the fish’s flesh is lost, but human bonds and Santiago’s capacity to dream remain. The novella is continuous rather than a fixed chapter-by-chapter work.''','0–10: establish Santiago and Manolin. 10–20: follow the voyage. 20–30: consider the marlin and sharks. 30–40: debate success and loss. 40–50: interpret the lions.','Why does Santiago call the marlin a brother? What remains after the sharks’ attacks?','https://americanliterature.com/author/ernest-hemingway/novella/the-old-man-and-the-sea'),
n('grapes-early','The Grapes of Wrath · chapters 1–10', '''## Chapters 1–3
Drought and dust devastate Oklahoma farmland, threatening tenant families. Tom Joad, released on parole after imprisonment for killing a man in a fight, returns toward home. An interchapter follows a land turtle struggling across a road, an image of persistence whose meaning the reader must interpret.

## Chapters 4–6
Tom meets Jim Casy, a former preacher questioning his old beliefs about sin and holiness. They find the Joad place abandoned. Muley Graves explains that the tenant farmers have been driven off the land and Tom’s family has gone to Uncle John’s place. Casy’s changing thought links spiritual value to shared human life.

## Chapters 7–10
An interchapter exposes used-car dealers exploiting desperate migrants. Tom and Casy find the family preparing to leave for California, where handbills promise work. The family sells or abandons possessions and loads an old truck. Tom’s journey violates the terms of his parole. Grandpa resists leaving and is given medicine to make him sleep while they depart.

## Technique
Interchapters shift between the Joads’ particular story and wider economic forces. The “bank” functions as an impersonal system in characters’ explanations, but the narrative also shows human decisions and responsibility within it.''','0–10: locate the Dust Bowl and displacement. 10–20: trace Tom and Casy. 20–30: discuss eviction. 30–40: compare turtle and family journeys. 40–50: map the decision to leave.','Why are the Joads leaving? What does the turtle chapter add without literally recounting the family’s story?','https://www.sparknotes.com/lit/grapesofwrath/sparklets/'),
n('grapes-middle','The Grapes of Wrath · chapters 11–20', '''## Chapters 11–14: leaving and loss
Interchapters describe abandoned farms and the westward stream of migrants. On the road the Joads join the Wilsons, whose car needs help. Grandpa dies during the journey; the families bury him beside the road, leaving a note. They cooperate in travel.

## Chapters 15–18: road and crossing
An episode at a roadside diner shows both commercial hardness and acts of kindness. The travellers hear troubling accounts of California’s labour market. The Wilsons cannot continue with the Joads because Sairy is too ill; Noah leaves near the Colorado River. The family crosses the desert; Granma dies, but Ma keeps her death private until they reach the other side.

## Chapters 19–20: California
A historical interchapter describes land concentration and exploitation. In a miserable camp, the Joads encounter hunger, hostility and scarce work. A confrontation with a deputy ends with Casy taking responsibility and being arrested after Tom trips the officer. Connie, Rose of Sharon’s husband, leaves. The family must move again.

## Read carefully
Small acts of cooperation interrupt the myth that every family can solve structural hardship alone. Keep the Wilsons’ departure, Noah’s departure and Connie’s abandonment distinct.''','0–10: mark the route. 10–20: discuss Grandpa and Granma. 20–30: track separation from the Wilsons, Noah and Connie. 30–40: analyse the camp confrontation. 40–50: discuss mutual aid.','How do the Wilsons and Joads help one another? Why is California not the security promised by the handbills?','https://www.sparknotes.com/lit/grapesofwrath/sparklets/'),
n('grapes-late','The Grapes of Wrath · chapters 21–30', '''## Chapters 21–24: government camp
An interchapter describes migrants joining together and owners fearing organisation. At Weedpatch, a government camp, residents manage committees and sanitary facilities without police inside. Tom gets temporary work. A dance is threatened by men sent to provoke a fight, but the residents identify and remove the provocateurs. The camp offers dignity, though it cannot by itself provide enough work.

## Chapters 25–27: strike and hunger
One interchapter contrasts abundance with food destroyed to protect prices. The Joads take work picking peaches and discover a strike outside. Tom encounters Casy, now organising workers; a man kills Casy and Tom strikes the attacker, killing him. Tom hides because he is injured and wanted. Later an interchapter follows cotton-picking and exploitative weighing practices.

## Chapters 28–30: flood and the barn
The family picks cotton and shelters in a boxcar. Tom leaves, promising Ma he will carry forward Casy’s ideas about collective struggle. Rain floods the area. Rose of Sharon gives birth to a stillborn baby; Uncle John sends the small box containing the baby into the water. The family takes shelter in a barn, where a starving man lies with his son. Rose of Sharon nurses the man.

## Interpretation
The ending joins grief and physical care without guaranteeing the family’s future. Casy’s and Tom’s developing sense of shared life connects personal survival to collective action.''','0–10: compare Weedpatch with the earlier camp. 10–20: trace the strike. 20–30: discuss Tom’s departure. 30–40: explain the flood and final act with sensitivity. 40–50: write about solidarity.','Why is the government camp different? How does the ending connect loss and care without resolving poverty?','https://www.sparknotes.com/lit/grapesofwrath/sparklets/'),
n('purple','The Color Purple · narrative guide', '''## Content warning and form
Alice Walker’s novel is told through letters, first addressed by Celie to God and later exchanged with her sister Nettie. It includes sexual and domestic abuse, racism and colonial violence. Letters and their ordering vary in edition; this is a narrative guide, not a numbered chapter map.

## Separation and control
Celie is repeatedly raped by the man she believes is her father, gives birth to two children who are taken away, and is forced to marry Albert, whom she calls Mr. ____ for much of the narrative. Nettie escapes his household after he pursues her. Celie believes Nettie’s letters have stopped and struggles under domestic labour and abuse.

## Relationships and discovery
Singer Shug Avery initially seems distant but becomes Celie’s confidante and lover. Sofia, married to Albert’s son Harpo, resists being controlled and suffers severe punishment after a confrontation with the mayor’s wife. Shug helps Celie discover that Albert has hidden Nettie’s letters. Nettie has travelled to Africa with missionaries Samuel and Corrine and their adopted children, Olivia and Adam—Celie’s children.

## Independence and reunion
Through Nettie’s letters Celie learns about the Olinka community and the damaging effects of colonial power; the novel invites discussion of the limits of the missionaries’ perspective. Celie learns that the man who abused her was her stepfather. She leaves Albert, establishes a pants-making business and inherits her family home. Albert changes over time, though change does not erase his earlier abuse. Nettie, Samuel, Olivia and Adam eventually return, and the family reunites.

## Interpretation
Writing, friendship, spirituality, work and queer intimacy help Celie develop an independent voice. Avoid replacing the novel’s particular ending with details from a film adaptation.''','0–10: explain letters and content warning. 10–20: trace separation. 20–30: discuss Shug, Sofia and hidden letters. 30–40: examine Celie’s work and reunion. 40–50: analyse voice.','How do Nettie’s letters change Celie’s understanding? Why is Albert’s later change not an erasure of abuse?','https://crossref-it.info/textguide/the-color-purple/42/3179')]
d['course-39:4']=[
n('twenty-years','O. Henry · After Twenty Years', '''## Story
A patrolman on a New York street meets a man waiting in a dark doorway. The man, Bob, explains that he and his friend Jimmy Wells agreed twenty years earlier to meet there at ten o’clock. Bob went West to seek his fortune; Jimmy stayed in New York. When Bob lights a cigar, the patrolman sees his face. The patrolman leaves.

A man in a long coat arrives, identifies himself as Jimmy and walks with Bob. Under a bright light Bob sees that this man is not his old friend. The stranger is a plainclothes officer who arrests Bob, wanted in Chicago. He gives Bob a note: the first patrolman was Jimmy, who recognised the wanted man but could not bring himself to arrest his old friend personally, so sent the other officer.

## Analysis
The twist turns a reunion into a conflict between friendship and duty. Darkness delays recognition; the light of the cigar allows Jimmy to identify Bob, while the later light exposes the substitute to Bob. Jimmy honours the appointment but avoids the direct arrest. Discuss that decision rather than assuming the story settles whether it is morally ideal.''','0–10: reconstruct the appointment. 10–20: identify the two officers. 20–30: trace light and recognition. 30–40: discuss duty and loyalty. 40–50: explain the twist.','Who was the first patrolman? Why does Bob discover that the man walking with him is not Jimmy?','https://americanliterature.com/author/o-henry/short-story/after-twenty-years'),
n('bear','William Faulkner · The Bear: story and reading cautions', '''## Setting and narrative
In the wilderness of Mississippi, Isaac “Ike” McCaslin joins annual hunting parties led by experienced hunters including Sam Fathers. The legendary bear Old Ben has survived many hunters and traps. Ike learns patience, tracking and respect for the forest from Sam. A dog named Lion is trained to confront the bear. During a hunt Lion attacks Old Ben; Boon Hogganbeck kills the bear with a knife. Lion dies from injuries, and Sam also dies after the hunt.

## Family history
In the long fourth section of the version commonly included in Go Down, Moses, Ike studies family plantation ledgers with his cousin McCaslin Edmonds. He uncovers the brutal history of enslavement, exploitation and incest in his family. Rejecting the inherited plantation, Ike renounces his claim to ownership. His decision is morally important but does not undo enslavement or restore land and power to those harmed.

## Return and interpretation
On a later visit, logging and the railroad reveal changes to the forest. Boon guards a tree full of squirrels, angrily claiming them for himself. The story juxtaposes respect for wilderness with possession, racial inheritance and environmental destruction. Sam’s Indigenous and Black ancestry is represented through Faulkner’s particular language and perspective; do not treat the text as a transparent account of Indigenous peoples.

## Edition caution
The story exists in versions with different divisions or passages; use the assigned text to check the ledgers section and section numbering before close teaching.''','0–10: map the hunting party. 10–20: trace Sam’s teaching and Old Ben. 20–30: examine ledgers and renunciation. 30–40: discuss logging and Boon. 40–50: evaluate what Ike’s choice can and cannot repair.','How do hunting and inheritance connect? What are the limits of Ike’s renunciation?','https://www.penguinrandomhouse.com/books/48389/go-down-moses-by-william-faulkner/9780679732174/teachers-guide/',True),
n('winter-dreams','F. Scott Fitzgerald · Winter Dreams', '''## Story
Dexter Green, the son of a grocery owner, works as a caddie at a Minnesota golf club and dreams of wealth and status. As a boy he encounters the demanding young Judy Jones. He goes to college and builds a successful laundry business. Years later he meets Judy again at the club; he is drawn to her beauty and to the world of wealth and privilege she represents.

Their intermittent relationship alternates between intimacy and rejection as Judy sees other men. Dexter becomes engaged to Irene Scheerer, whose steadiness contrasts with Judy’s unpredictability, but breaks the engagement after Judy draws him back. That relationship also fails. Dexter serves in the First World War and later prospers in New York.

Years afterward an acquaintance, Devlin, tells Dexter that Judy has married an unfaithful husband and that her youthful beauty has faded. This is a secondhand report, not the reader’s direct access to Judy’s life. Dexter is overwhelmed by the loss of the dream he attached to her and to his own youth.

## Analysis
The title links seasonal landscape to desire. Judy is a person as well as an object in Dexter’s idealisation, although the narration offers limited access to her perspective. Class aspiration and the commodification of beauty shape his grief.''','0–10: trace Dexter’s social rise. 10–20: map Judy and Irene. 20–30: discuss the interrupted engagement. 30–40: question Devlin’s report. 40–50: analyse the dream.','What does Judy represent to Dexter beyond a romantic partner? Why must we treat Devlin’s account as secondhand?','https://www.shmoop.com/study-guides/winter-dreams/ending.html'),
n('fleur','Louise Erdrich · Fleur', '''## Content warning and narration
The story includes racism, sexual violence and deaths. Pauline, a young mixed-heritage narrator in Argus, tells much of Fleur Pillager’s story and is not a neutral all-knowing witness. Fleur is an Ojibwe woman associated in local stories with the water spirit Misshepeshu; rumours around her reflect fear and fascination as well as community belief.

## Story
Fleur is said to have survived drowning, while men connected with her rescue have died. She works at a butcher shop in Argus, where three men gamble with her. After she wins at cards, the men assault her. Pauline witnesses the aftermath and locks the men in the shop’s meat locker; a violent storm follows and they die. The story does not require readers to treat supernatural explanations as established fact.

Fleur later returns to her community and gives birth; the narrative leaves the child’s paternity uncertain. The short story was later adapted into the novel Tracks; details about Eli Kashpaw belong to that larger narrative and should not be assumed to appear in the original story. Pauline’s telling intertwines violence, gossip and spiritual possibility without granting the men the authority to define Fleur.

## Interpretation
Discuss how gendered and racialised power shapes what people say about Fleur. Her connection with water is not proof that she caused every death attributed to her. Avoid implying that her gambling or strength makes her responsible for the assault.''','0–10: content warning and narrator. 10–20: distinguish rumours from events. 20–30: explain the assault without graphic detail. 30–40: discuss the storm and uncertainty. 40–50: analyse power in storytelling.','How does Pauline’s position shape the story? Why is the child’s paternity not something a reader can confidently settle?','https://www.ebsco.com/research-starters/literature-and-writing/fleur-louise-erdrich')]
with open(P,'w',encoding='utf8') as f:json.dump(d,f,ensure_ascii=False,indent=2);f.write('\n')
print('Added',sum(len(d[f'course-39:{i}']) for i in range(5)),'selections')
