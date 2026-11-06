import json
P='prepared-notes.json'
with open(P,encoding='utf-8') as f:d=json.load(f)
def n(id,title,body,lesson,questions,source,pre=False):
 r={'id':id,'title':title,'source':source,'text':f'# {title}\nModern Poetry · Semester 6\n\n{body}\n\n## 50-minute lesson\n{lesson}\n\n## Discussion and revision\n{questions}\n\nTeaching draft: read the assigned poem and edition alongside this guide; support interpretations with specific textual evidence.'}
 if pre:r['status']='preliminary'
 return r
d['course-33:0']=[
n('modern-context','From the 1890s to modern poetry', '''## A change, not a clean break
At the end of the nineteenth century, British and Irish poetry included Victorian inheritance, aestheticism, symbolism, empire and debates about religious belief, industrial society and artistic form. Thomas Hardy bridges periods rather than fitting neatly into an automatic division between Victorian and modern. The early twentieth century brought experiments in diction, image, perspective and form, alongside continuing use of sonnets, ballads and other inherited structures.

## Georgians and war
“Georgian poetry” often refers to writers associated with anthologies published in the reign of George V. Landscape and accessible lyric are common, but the poets are diverse; do not equate every pastoral poem with a single political viewpoint. The First World War (1914–18) produced very different responses: Brooke’s patriotic idealisation and Owen’s account of a wounded veteran cannot simply be merged into one “war poetry” position.

## Imagism and modernism
Imagism favoured direct treatment, precision and economical language; its practitioners and publications changed over time. Pound’s and Eliot’s wider modernist work uses resources such as allusion, abrupt juxtaposition, multiple voices and formal experiment. Eliot’s The Waste Land should not simply be labelled an Imagist poem: the syllabus groups works under that heading, but the poem exceeds the movement.

## Irish poetry
The Irish literary revival developed through cultural and political debates, folklore, theatre and poetry. Yeats’s work connects Irish traditions with mythology, modern politics and his own symbolic system. Avoid treating Irish writing as merely a branch of English nationalism.

## Comparative method
Compare how landscape works in Belloc and how a city works in Eliot, or how Brooke and Owen present a soldier. Identify voice, form, historical context and a difference; movements are useful descriptions, not rigid boxes.''','0–10: timeline and prior ideas. 10–20: compare landscape and city. 20–30: define Imagism without reducing modernism to it. 30–40: compare two wartime perspectives. 40–50: write one continuity and one change.','How do Imagism and modernism overlap without being identical? Why should Georgian poets not all be treated alike?','https://www.poetryfoundation.org/learn/glossary-terms/imagism')]
d['course-33:1']=[
n('south-country','Hilaire Belloc · The South Country', '''## Summary in sequence
Living in the Midlands, the speaker remembers the hills of the south and imagines walking there with childhood companions. He acknowledges the distinctive landscapes of northern and western England, yet describes the South Country, especially Sussex, with particular affection. Pines, sand and the bare Downs revive his sense of home.

The poem’s mood darkens when the speaker admits he cannot recover all that is lost and fears solitude in old age. He imagines friendship among people of the Sussex Weald and, if fortune permits, a thatched house near woods and sea, filled with local songs and old friends.

## How it works
Repetition, simple rhythms and recurring references to landscape give the poem a song-like quality. Place is emotional and social, not merely scenery: the desired country promises continuity and companionship. Its praise of southerners is the speaker’s affectionate preference, not an objective ranking of regions. Notice that the wished-for home remains a future hope rather than an event already achieved.''','0–10: map the speaker’s locations. 10–20: paraphrase the landscape. 20–30: trace the turn to loneliness. 30–40: discuss the imagined house. 40–50: write about place and memory.','Why does the speaker remember childhood friends? How does anxiety complicate the celebration of Sussex?','https://www.simple-poetry.com/poems/the-south-country-68840703577'),
n('prayer-darkness','G. K. Chesterton · A Prayer in Darkness', '''## Summary
The speaker asks heaven not to make personal anguish the centre of the universe: even if the speaker descends into despair or dies by suicide, the world should continue to be nourished and grass should grow. The next stanzas acknowledge sun, rain and fruit, then express gratitude that stars, moth and flower remain beyond the speaker’s power to damage through grief or anger.

The final image imagines Christ at the Crucifixion hearing crickets despite accounts of the darkened sun. It juxtaposes extreme suffering with the continuance of ordinary life. The speaker’s imagined response is a theological and poetic claim, not a factual account that students must accept.

## Interpretation and care
Prayer, apostrophe, seasonal images and sharp contrasts move between darkness and gratitude. The poem can be read as seeking humility and comfort in a world not controlled by personal pain, while its difficult suggestion of divine “scorn” complicates easy consolation. It refers to suicide; discuss the imagery sensitively without suggesting that distress should be dismissed or that a person should endure it alone.''','0–10: identify the prayer’s addressee. 10–20: paraphrase the four stanzas. 20–30: compare grief and nature. 30–40: interpret the Crucifixion image with care. 40–50: explain one tension.','How do images of ordinary life continue beside suffering? Why is the ending open to more than one response?','https://journeywithjesus.net/poemsandprayers/524-gk-chesterton-a-prayer-in-darkness'),
n('sane-revolution','D. H. Lawrence · A Sane Revolution', '''## Summary
The speaker proposes revolution for enjoyment rather than solemnity, hatred, money or a conventional political programme. He mischievously dismisses equality and a revolution supposedly made for the working classes, imagining instead people able to live as independent “little aristocracies.” The final movement opposes exhausting labour to work that might be enjoyed.

## Tone and questions
The poem’s repeated imperatives and colloquial, deliberately provocative statements make it sound like a spoken challenge. Its irony unsettles expectations: “sane” does not mean careful policy, and the speaker’s rejection of equality deserves critical scrutiny, not automatic endorsement. Ask whose freedom a revolution defined this way might secure and whose structural inequality it might overlook.

## Reading strategy
Trace each “don’t” to the alternative proposed. Then distinguish the speaker’s playful provocation from a complete or coherent blueprint for social reform.''','0–10: define revolution and tone. 10–20: list rejected motives. 20–30: analyse humour and imperatives. 30–40: debate the equality claim. 40–50: write a balanced response.','What distinction does the speaker draw between work and labour? What makes the poem’s politics provocative?','https://www.poetrysoup.com/famous/poem/a_sane_revolution_6216'),
n('the-soldier','Rupert Brooke · The Soldier', '''## Summary
A soldier imagines dying abroad. He asks to be remembered through the idea that his buried body would make a corner of foreign soil permanently English. He presents England as the source of his body, landscape, experiences, friendship and values. In the concluding movement he imagines his purified heart returning those gifts in a peaceful, idealised afterlife.

## Form and interpretation
The 14-line sonnet gives a formal, concentrated shape to patriotic feeling. Personification makes England a nurturing presence; images of flowers, rivers and home turn national identity into intimate memory. The poem was written early in the First World War and expresses a particular ideal of sacrifice, not the only contemporary experience of it.

The phrase about a foreign field can be read both as devotion and as a claim that English identity transforms another land; invite discussion of whose land and perspective are absent. Compare with Owen’s “Disabled”: the contrast is useful but neither poet stands for every soldier.''','0–10: note speaker and imagined situation. 10–20: paraphrase the octave and sestet. 20–30: examine England as a nurturing figure. 30–40: question national perspective. 40–50: compare with Owen.','How does the sonnet connect the soldier’s body and homeland? What does the poem leave outside its idealised vision?','https://poets.org/poem/soldier-0'),
n('god-poetry','Robert Graves · The God Called Poetry', '''## Summary
The speaker imagines poetry as an ancient god who trains the poet through increasingly difficult feats, like a creature jumping through hoops. The playful image of a singing cricket or grasshopper suggests both performance and dependence on a demanding master. Poetry is older than the landscape and appears in different voices and forces.

The god’s conflicting commands push the poet toward both harsh denunciation and gentler, compassionate song. Poetry is a powerful, contradictory presence rather than one fixed mood; the speaker must learn to respond to its opposing impulses.

## Techniques
Personification turns an art into an unpredictable deity. Comic comparisons sit beside images of immense age and authority, making artistic vocation at once exhilarating and demanding. Contrast the poet’s apparent freedom to sing with the master’s power to command. Read the assigned text carefully before reducing the poem to a single moral about art.''','0–10: identify speaker and god. 10–20: track the performance images. 20–30: compare contrary instructions. 30–40: discuss power and creativity. 40–50: write an interpretation.','Why is the hoop-jumping image both comic and serious? What do the god’s contrasting voices suggest about poetry?','https://poemanalysis.com/robert-graves/the-god-called-poetry/')]
d['course-33:2']=[
n('poet-as-hero','Siegfried Sassoon · The Poet as Hero', '''## Summary
The speaker addresses listeners who know his angry attacks on war and ask why his earlier sweetness has changed. He recalls an idealised youthful image of himself as a shining knight seeking the Grail. He now says goodbye to Galahad, the chivalric figure, and replaces heroic fantasy with anger, hatred and the memory of killed friends. His songs become an attempted response to the wrongs done to them and a source of absolution.

## Analysis
The sonnet form joins an inherited heroic tradition to a voice that questions heroic display. Arthurian allusion makes the change of self-image vivid. Yet the closing desire to avenge wounds is not entirely peaceful: the poem exposes the speaker’s own violent feelings even as it rejects a romantic picture of war. “Absolution” invites debate about whether poetry can heal guilt, avenge friends or only express grief.''','0–10: explain the Grail and Galahad. 10–20: paraphrase the speaker’s change. 20–30: analyse the address to listeners. 30–40: discuss anger and absolution. 40–50: contrast Brooke.','Why does the speaker reject Galahad? How does the poem complicate a simple opposition between violence and protest?','https://www.poetryfoundation.org/poems/57270/the-poet-as-hero'),
n('disabled','Wilfred Owen · Disabled', '''## Summary in sequence
A young veteran sits in a wheeled chair, waiting for dark; he has lost limbs in war and depends on others. Sounds of boys playing bring memories of an earlier life when he was admired, active and physically confident. The poem moves back to the night he decided to enlist: drink, uniform, social approval and a desire to impress contributed to his decision; he was underage, but an officer accepted him.

After injury, his return draws little public celebration. He remembers compliments from before the war and observes that people now treat him differently. At the end he anticipates institutional routines and wonders why the people who should put him to bed do not come.

## Form and interpretation
Shifts between past and present make social abandonment visible; sound and colour contrast earlier pleasure with the present setting. Owen criticises recruitment culture and public neglect, not merely an individual decision. Discuss the period’s assumptions about masculinity and attractiveness critically: disability does not make a person’s life inherently worthless. The veteran’s isolation is intensified by social attitudes and lack of support, not simply by his impairment.''','0–10: identify present and flashback. 10–20: reconstruct recruitment and return. 20–30: examine sound, colour and contrast. 30–40: discuss social responses to disability. 40–50: compare a claim with evidence.','What influences the veteran’s enlistment? How do public attitudes contribute to his isolation?','https://www.tandfonline.com/doi/full/10.1080/09687599.2014.902364'),
n('sir-nameless','Thomas Hardy · The Children and Sir Nameless', '''## Summary
Sir Nameless complains about children playing in his park and congratulates himself on having no offspring. Hoping to preserve his greatness, he commissions a large armed alabaster effigy for after his death. Three hundred years later, church restorers cannot trace his descendants and put the statue in the floor beneath schoolchildren’s seats. Their shoes wear away its name and nose; bored during the sermon, they wonder who the old stone man was.

## Analysis
The irony is carefully constructed: the children he rejected become the agents of his physical and historical erasure. His chosen memorial does not deliver the control over remembrance he imagined. Three eight-line stanzas compress centuries into a brief narrative. The poem questions pride and monuments, but need not be reduced to an instruction that everyone must have children; time, chance and institutions also shape what survives.

## Placement in the syllabus
The poem appears in the unit headed “War Poets,” but its story concerns memory, vanity and time rather than a battlefield. Do not invent a war setting to force a match with the heading.''','0–10: narrate the three stages. 10–20: explain the commissioned effigy. 20–30: identify the final reversal. 30–40: consider memory and institutions. 40–50: write on irony.','What happens to the effigy after 300 years? Why is the ending ironic?','https://www.gutenberg.org/files/4758/4758-h/4758-h.htm'),
n('refugee-blues','W. H. Auden · Refugee Blues', '''## Summary
A speaker addresses a beloved companion as German Jewish refugees face exclusion. The city contains wealth and poverty, yet no home for them. Their former country remains on the map but is inaccessible; old passports cannot renew themselves like a tree. A consul’s declaration that a person without a passport is officially dead clashes with the speakers’ undeniable survival. A committee postpones help, while public prejudice and Hitler’s threat make danger explicit.

Animals appear to move or receive shelter more freely than the refugees. In a dream a huge building offers them no room; the ending imagines soldiers searching for the pair in snow.

## Form and historical context
Recurring three-line stanzas, repeated address and refrain draw on blues lyric techniques. Blues has African American musical roots; the poem adapts a tradition rather than inventing it. The 1939 setting concerns Nazi persecution and restrictive asylum policies. Its intimate “you and me” makes bureaucratic decisions personal, while the repeated contrasts between life and official recognition expose the cruelty of treating documents as more real than people.''','0–10: outline 1930s context. 10–20: trace passport and committee scenes. 20–30: listen to repeated phrases and form. 30–40: compare animals and refugees. 40–50: discuss the ending.','Why is “officially dead” ironic? What does the recurring address to a loved one achieve?','https://www.lieder.net/get_text.html?TextId=28378'),
n('ultima-ratio','Stephen Spender · Ultima Ratio Regum', '''## Summary
The title means “the last argument of kings,” a phrase associated with guns as instruments of power. The speaker sees a young person dead under olive trees and contrasts that particular life with the economic and military forces behind the shooting. The boy had no prominent place in employment records, fashionable institutions or newspapers; a wall separates the powerless from wealth.

In the remembered scene, spring petals and the casually dropped cap give way to machine-gun fire. The final section asks readers to consider a life counted as valueless by bureaucratic and economic measures, and asks whether the expenditure of bullets can justify the death.

## Analysis
The contrast between spring imagery and industrial weapons makes violence interrupt ordinary possibility. Monetary and statistical language is used ironically, not as the speaker’s own measure of human worth. The poem is commonly associated with the era of the Spanish Civil War; the text does not establish every detail of the boy’s biography, so avoid inventing his identity or motives.''','0–10: translate the title. 10–20: trace images of the young person. 20–30: contrast money and life. 30–40: analyse the final questions. 40–50: write one evidence-based paragraph.','Why does the speaker invoke economic records and bullets? How does spring imagery affect the scene?','https://allpoetry.com/Ultima-Ratio-Regum')]
d['course-33:3']=[
n('waste-land-overview','T. S. Eliot · The Waste Land: map and method', '''## What kind of poem?
Published in 1922, The Waste Land is a five-part modernist poem made from shifting voices, scenes, registers, languages and literary or religious allusions. It has no single straightforward plot or reliably continuous speaker. Its discontinuities invite readers to make connections without assuming that every voice is Eliot’s personal opinion. Ezra Pound’s editorial role in shaping the published poem is important.

## Five-part map
1. The Burial of the Dead: spring, memory, a distressed landscape, prophecy and the crowd in an unreal city.
2. A Game of Chess: a luxurious interior and anxious conversation juxtaposed with a pub conversation about Lil and Albert.
3. The Fire Sermon: the Thames, fishing, voices and a typist’s encounter, followed by allusions to Augustine and the Buddha.
4. Death by Water: the drowned Phlebas and a warning to remember mortality.
5. What the Thunder Said: a difficult journey through drought and ruins, thunder’s commands and fragments of possible peace.

## Recurring questions
Water can suggest both renewal and drowning; fragments can be ruins and resources for rebuilding. The poem’s treatments of gender, sexuality, class, empire and antisemitic stereotypes deserve critical discussion rather than unqualified celebration. Its ending does not establish that the whole world has been healed. Use the next five notes to teach each section in sequence.''','0–10: place 1922 and the war. 10–20: map five sections. 20–30: track water across the poem. 30–40: identify changing voices. 40–50: distinguish interpretation from a single plot.','Why is it risky to assign every voice to one speaker? How can water carry opposing meanings?','https://www.poetryfoundation.org/poems/47311/the-waste-land'),
n('waste-land-i','The Waste Land · I. The Burial of the Dead', '''## Sequence
Spring, conventionally a season of renewal, is described as cruel because it stirs memory and desire from apparently protective winter. A voice recalls childhood in the mountains and a sledging episode; the poem then moves into a dry landscape of broken images. An encounter associated with hyacinths ends in a moment of speechless uncertainty. A fortune-teller, Madame Sosostris, displays cards including a drowned figure. The scene shifts to a London crowd crossing the bridge under the pressure of modern routine and literary echoes of the dead.

## Teach the connections
Rather than treating these episodes as one continuous autobiography, ask what happens when remembering or awakening is painful. The fortune-teller’s warning about water is not a simple plot prediction that resolves all later imagery. The confrontation with Stetson and the buried corpse disturbs the boundary between planting and death. The city crowd can evoke alienation and the aftermath of war; Dantean echoes make historical and literary layers interact.''','0–10: map the changes in voice. 10–20: discuss spring and winter. 20–30: examine prophecy. 30–40: connect crowd and burial images. 40–50: write one supported interpretation.','Why is spring’s usual symbolism reversed? What is unsettling about the buried corpse?','https://www.poetryfoundation.org/poems/47311/the-waste-land'),
n('waste-land-ii','The Waste Land · II. A Game of Chess', '''## Sequence
A richly decorated interior is described through objects, perfume and literary allusions, including the violent myth of Philomela. A tense exchange follows: one speaker presses for conversation and reassurance, while the other’s responses are fragmentary or internal. A second scene shifts to a pub voice telling another woman about Lil, her husband Albert’s return, her health, appearance and the pressures placed on her. Repeated closing-time calls interrupt the account; the section ends with echoes of Ophelia’s farewells.

## Interpretation
The juxtaposition links different social settings without making the experiences identical. Communication is strained, and intimacy is shaped by violence, economics, gender expectations and reproductive pressure. Chess suggests strategic relations, but not every figure needs to be assigned a chess piece. Philomela’s story of rape and silencing should be handled sensitively. Lil is talked about by another voice; ask how that affects our access to her experience.''','0–10: identify the two settings. 10–20: annotate voice changes. 20–30: discuss silence and speech. 30–40: analyse Lil’s situation with care. 40–50: compare the scenes without flattening class differences.','How do the two scenes contrast? Why does the Philomela allusion complicate the beautiful interior?','https://www.poetryfoundation.org/poems/47311/the-waste-land'),
n('waste-land-iii','The Waste Land · III. The Fire Sermon', '''## Sequence
The Thames appears with traces of litter and absent festivities, while voices and fragments move between river, city and memory. A fisher figure and the prophet Tiresias become points of connection. The typist comes home; a young man visits and initiates a mechanical sexual encounter that the poem presents as indifferent and lacking mutual intimacy. The typist resumes her routine afterwards.

The section moves through further river voices and allusions to Augustine and the Buddha’s Fire Sermon. “Fire” can suggest desire, spiritual suffering and the possibility of release, though the different traditions cannot simply be equated.

## Close reading
Ask who sees, who speaks and what information is missing. Tiresias’s presence does not make every other character reducible to him. Discuss the encounter’s imbalance and lack of meaningful consent carefully; avoid blaming the typist. Note how quotations from song, ritual and canonical literature mingle with ordinary modern settings.''','0–10: map river and city. 10–20: identify Tiresias. 20–30: discuss the typist episode sensitively. 30–40: compare fire and water. 40–50: analyse a shift in register.','How does the Thames connect different fragments? Why should the typist’s viewpoint not be assumed to be fully known?','https://www.poetryfoundation.org/poems/47311/the-waste-land'),
n('waste-land-iv-v','The Waste Land · IV–V. Death by Water and What the Thunder Said', '''## IV. Death by Water
Phlebas the Phoenician, once concerned with profit and loss, has drowned; currents have carried away the details of his worldly life. The brief section addresses the reader, urging remembrance of a shared mortality. Water here destroys rather than automatically purifies.

## V. What the Thunder Said
Images of rock, thirst, difficult travel and ruined cities dominate. A mysterious additional figure accompanies travellers in one passage; the chapel and the approach of rain raise possibilities that remain unstable. Thunder’s syllable “Da” prompts references to giving, sympathy and self-control from the Brihadaranyaka Upanishad. The speaker then gathers fragments, including several languages and literary references, ending with the repeated Sanskrit word “Shantih,” traditionally associated with peace.

## Interpreting the ending
Some readers hear a movement toward renewal; others stress discontinuity and unresolved crisis. Both should be tested against the words rather than presented as certain recovery or total despair. Eliot adapts religious materials through his own cultural position: discuss the source tradition respectfully and avoid treating it merely as exotic decoration.''','0–10: paraphrase Phlebas. 10–20: follow the journey through drought. 20–30: explain the thunder references. 30–40: compare alternative endings. 40–50: write a claim and evidence.','Why does Phlebas complicate water as a symbol? Does the final word prove complete renewal? Explain.','https://www.poetryfoundation.org/poems/47311/the-waste-land'),
n('the-return','Ezra Pound · The Return', '''## Summary
The speaker calls attention to a group returning hesitantly, their slow and wavering movement compared with snow in the wind. They are identified as gods once associated with awe and winged shoes. Silver hounds accompany them; remembered as swift and dangerous, the hunters and leash-men now seem slow and pale.

## Form and interpretation
Uneven line lengths, pauses and shifts in rhythm enact hesitation before recalling earlier speed. Classical imagery evokes a possible return of ancient powers, but the poem does not give a simple narrative explaining where they have been or exactly what their return means. Readers may see a revival of neglected artistic or spiritual energies, or the diminished survival of old gods; these are interpretations rather than stated facts.

The condensed image and musical movement relate to Pound’s modernist experiments. The poem was written around the time of early Imagism, but it should be read as a particular work, not as a checklist of movement rules.''','0–10: identify repeated movement words. 10–20: contrast returning gods and remembered speed. 20–30: read line breaks aloud or silently. 30–40: offer alternative interpretations. 40–50: support one with detail.','How do rhythm and line breaks suggest hesitation? What changes between the past and the returning figures?','https://www.poeticous.com/ezra-pound/the-return'),
n('expostulation-uncertain','“An Expostulation” · attribution needs confirmation', '''## Important syllabus uncertainty
The syllabus attributes “An Expostulation” to “C. D. Lewis,” normally understood as Cecil Day-Lewis. A poem with that exact title beginning with a complaint against science-fiction writers is widely attributed to C. S. Lewis, a different author. The title match alone does not establish that the syllabus intended this poem or that it intended to name C. S. Lewis. Confirm the assigned anthology or ask the department before teaching an attribution.

## Conditional orientation only
If the assigned text is C. S. Lewis’s poem subtitled “Against too many writers of science fiction,” its speaker questions journeys across immense fictional space that reproduce familiar earthly plots, and asks for strangeness, beauty and wonder instead. Its argument contrasts scale with imaginative discovery. This is not a verified summary of a Cecil Day-Lewis text.

## Classroom step
Compare author initials, opening line, subtitle and publication details in the prescribed edition. Once identified, replace this outline with an edition-specific reading. Do not silently substitute one author for the other.''','0–10: compare names and initials. 10–20: locate the assigned text. 20–30: compare title and opening line with a reliable edition. 30–40: discuss the conditional text only if confirmed. 40–50: record the bibliographic evidence.','Why are C. S. Lewis and C. Day-Lewis not interchangeable? Which evidence would establish the intended poem?','https://www.poeticous.com/c-s-lewis/an-expostulation',True),
n('hawk-rain','Ted Hughes · The Hawk in the Rain', '''## Summary
The first-person speaker struggles through rain and mud, feeling the earth pull at each step and the wind beat the body. Above, a hawk appears to hang still and controlled in the violent air. Its unshaken eye becomes a fixed point for the speaker, who contrasts the bird’s apparent mastery with human vulnerability.

In the final movement the speaker imagines a possible future in which the storm eventually throws the hawk down and its blood meets the land. This is a projection of mortality, not a report that the hawk has already crashed.

## Technique
Violent verbs and alliteration make weather and earth feel physically forceful. The vertical contrast between human below and bird above is complicated by their shared exposure to death. The hawk can be read as an image of will, instinct or a disturbing ideal of mastery, but the poem does not tell us exactly what the bird thinks.''','0–10: map speaker and hawk. 10–20: collect weather verbs. 20–30: compare movement and stillness. 30–40: distinguish imagined future from observed action. 40–50: explain one reading of the hawk.','Why is the hawk’s final fall conditional? What links the bird and the speaker despite their different responses?','https://www.eng-literature.com/2022/10/the-hawk-in-the-rain-summary-analysis.html')]
d['course-33:4']=[
n('second-coming','W. B. Yeats · The Second Coming', '''## Summary
The opening describes a falcon moving beyond the falconer’s hearing as order seems to break apart: violence spreads, innocence is overwhelmed, and the most certain voices may be the worst. Expecting revelation and a Christian Second Coming, the speaker instead receives a disturbing vision from “Spiritus Mundi,” a concept of a shared symbolic store.

A sphinx-like shape with a lion’s body and a human head moves through desert sand. Darkness returns, but the speaker imagines a new historical era awakening after twenty centuries. The poem ends with a question about a rough beast moving towards Bethlehem to be born.

## Interpretation
The widening gyre relates to Yeats’s cyclical theory of history, while the inverted nativity makes birth ominous rather than reassuring. Written after the First World War amid wider upheaval, the poem does not identify the beast with one specific politician or event. Its rhetorical question and unresolved image make the future frighteningly uncertain.''','0–10: explain falcon/falconer. 10–20: map order and disorder. 20–30: examine the unexpected vision. 30–40: discuss cyclical history and Bethlehem. 40–50: write a supported interpretation.','What expectation does the title create and how is it unsettled? Why should the beast not be assigned one certain identity?','https://americanliterature.com/author/william-butler-yeats/poem/the-second-coming'),
n('epitaphs-war','Rudyard Kipling · Epitaphs of the War', '''## What the sequence does
An epitaph is an inscription associated with the dead. Kipling’s sequence uses short imagined inscriptions in different voices and situations rather than telling one continuous story. The syllabus does not specify which individual epitaphs are assigned; confirm the course anthology before claiming that a particular selection is prescribed.

## Representative readings
“Common Form” gives the dead a bitter explanation that blames an older generation’s lies. “A Dead Statesman” imagines a politician confronting the young people killed through his falsehoods. “The Coward” gives a compressed account of a man led to death, inviting thought about fear and judgment. “Hindu Sepoy in France” acknowledges the bravery of an Indian soldier through a British speaker who does not know his religious powers; it invites discussion of both recognition and the limits of an imperial perspective.

Other epitaphs range from affirming military transformation to bitter irony, grief or accusation. Do not flatten the sequence into one anti-war slogan, or assume every speaker is Kipling. His own son John died in the First World War; biography can illuminate grief but should not be used as automatic proof for every voice.''','0–10: define epitaph. 10–20: compare two contrasting voices. 20–30: consider irony and brevity. 30–40: discuss imperial perspective. 40–50: check which epitaphs the class is assigned.','How does an epitaph give the dead a voice? What differs between the dead statesman and the Hindu sepoy?','https://www.bartleby.com/364/202.html'),
n('whitsun-weddings','Philip Larkin · The Whitsun Weddings', '''## Summary in sequence
On a hot Whitsun Saturday, a speaker travels south by train. The journey begins with an almost empty carriage and observations of houses, farmland, canals, towns and industry. At successive stops the speaker gradually notices wedding parties on platforms and newly married couples boarding the train.

He observes relatives’ clothing and reactions: pride, embarrassment, boredom and excitement appear together. The couples sit in the same carriage without necessarily knowing one another. Their separate lives share this brief hour as the train approaches London. As it slows, the ending imagines a shower of arrows travelling out of sight and becoming rain.

## Interpretation
The poem moves from detached observation to an imaginative sense of shared transition. Its portraits can sound affectionate, comic or class-conscious and judgmental; students can test these tones against details. The final arrows and rain suggest several possibilities, including release, change, fertility or disappointment. They do not settle the future of each marriage. Whitsun is a Christian festival period; the poem presents wedding journeys, not a single ceremony.''','0–10: plot the train route. 10–20: identify changes in the speaker’s attention. 20–30: compare wedding guests’ reactions. 30–40: debate the final image. 40–50: explain tone using evidence.','What links couples who do not know one another? Why can the final image support more than one reading?','https://www.poetryfoundation.org/articles/68946/philip-larkin-the-whitsun-weddings'),
n('melancholia','Robert Bridges · Melancholia', '''## Summary
The poem describes desire turning toward despair: the sufferer forgets other people and praise, finding temporary relief in sleep. Uncertainty, once a space for hopeful ambition, now looks like a dark, starless wall. The second movement addresses the sufferer sharply as a “fool” for impossible desires and impatient despair, arguing that joy, love, beauty and youth still exist even when they cannot be felt.

## Form and interpretation
The 14-line poem moves from a description of suffering to an admonition. Darkness and constriction contrast with the imagined continuing splendour of the world. Its final claim that the sufferer is figuratively dead expresses the poem’s severe judgment; it is not a medical diagnosis or sound advice to blame people experiencing depression. Readers can question the speaker’s limited compassion while also exploring the contrast between outer life and inner perception.

## Edition check
Search results sometimes misattribute another poem called “Melancholia” to Bridges. The intended Bridges poem begins by describing the “sickness of desire”; check the assigned edition.''','0–10: paraphrase the first eight lines. 10–20: identify the shift in address. 20–30: compare dark imagery and continuing beauty. 30–40: discuss the judgment sensitively. 40–50: write on tone.','What changes about uncertainty in the poem? Why should its severe rebuke not be treated as mental-health advice?','https://www.gutenberg.org/files/37804/37804-h/37804-h.htm'),
n('prayer-before-birth','Louis MacNeice · Prayer Before Birth', '''## Summary in sequence
An imagined unborn speaker repeatedly asks to be heard, comforted, provided for, forgiven and protected. Early threats include frightening creatures; the poem quickly turns toward dangers created by human beings: confinement, deception, drugs and violence. The speaker also asks for water, grass, trees, sky and an inner light.

The prayer anticipates being made to participate in wrong and asks for forgiveness and preparation for future encounters. It begs not to be turned into an obedient mechanism or an interchangeable object. The final extreme plea asks for death rather than such complete destruction of self.

## Analysis and context
The repeated opening and escalating requests imitate a litany. Alliteration and accumulation make danger feel relentless. The poem’s Second World War context informs its fear of coercion, but the unborn voice is an imaginative dramatic device, not a literal report of a baby’s thoughts. Its ending is disturbing: discuss it as a poetic expression of fear, not a recommendation for real-life action.''','0–10: identify the imagined speaker. 10–20: group the requests. 20–30: examine repetition and sound. 30–40: discuss coercion and the ending sensitively. 40–50: write about one contrast between fear and hope.','Why is the unborn voice effective? How does the poem connect individual identity with coercion?','https://poemanalysis.com/louis-macneice/prayer-before-birth/')]
with open(P,'w',encoding='utf-8') as f:json.dump(d,f,ensure_ascii=False,indent=2);f.write('\n')
print('Wrote',sum(len(v) for k,v in d.items() if k.startswith('course-33:')),'Modern Poetry selections across 5 units')
