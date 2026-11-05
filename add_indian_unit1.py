import json
p='prepared-notes.json'; d=json.load(open(p)); key='course-23:0'; old=d.get(key,[])
def n(id,title,body,source,preliminary=False):
 x={'id':id,'title':title,'source':source,'text':'# '+title+'\nIndian Writing in English I · Semester 4, Unit I\n\n'+body+'\n\nTeaching draft: compare the prescribed text and edition before class.'}
 if preliminary:x['status']='preliminary'
 return x
macaulay=n('macaulay-minute','Background · Macaulay’s Minute on Indian Education (1835)','''## Historical situation
In the early nineteenth century, officials of the East India Company debated how public educational funds should be spent. The controversy commonly called Orientalist–Anglicist concerned languages, institutions and kinds of knowledge, though individuals’ positions were more varied than two perfectly uniform camps. Thomas Babington Macaulay’s Minute, dated 2 February 1835, intervened in that debate; Governor-General William Bentinck’s resolution followed in March.

## Argument
Macaulay claims that English can open access to European science and literature and argues against continuing to privilege Sanskrit and Arabic learning with the disputed funds. He makes a sweeping, hostile comparison between European and Indian/Arabic literary traditions and proposes educating an intermediary class of Indians who can communicate between the colonial rulers and the population. He also anticipates that this group could develop Indian languages and transmit knowledge more widely.

## Critical reading
His ranking of knowledge is a colonial argument, not an objective fact. Ask what he knew directly, whose educational aspirations he selected, and whose learning he dismissed. The document concerns funding and policy under colonial government; it did not instantly make everyone speak English or erase all other educational institutions. English education’s later history includes unequal access, new careers and writing, reform and anticolonial critique. These outcomes cannot all be reduced to one person’s intention.

## Lesson · 50 minutes
0–10: distinguish a historical source from a neutral account. 10–20: identify the policy question. 20–30: map claims, assumptions and intended audience. 30–40: question whose knowledge is valued. 40–50: compare consequences with authorial intentions.

## Questions
What did Macaulay propose to fund? How does he justify hierarchy between traditions? Why should later outcomes not be equated with his intentions?''','https://english.washington.edu/sites/english/files/documents/ewp/teaching_resources/minute_on_indian_education_1835_by_thomas_babington_macaulay.pdf')
auro=n('aurobindo-renaissance','Sri Aurobindo · The Renaissance in India, Chapter 1','''## Context and argument
The opening of Sri Aurobindo’s series on the Indian renaissance appeared in 1918. He considers what “renaissance” or rebirth might mean for India under the pressure of European influence. The chapter is an argument about culture and renewal, not a detached account on which every historian must agree.

## Following the essay
Aurobindo asks whether India is experiencing a genuine cultural awakening or merely adopting external forms. He compares the term with the European Renaissance but cautions against assuming that the two processes must be identical. In his account, renewal must involve the creative life of a people rather than only a fashionable change in institutions.

He argues that India’s cultural and spiritual inheritance has survived political subordination, while its outward intellectual, artistic and social forms have experienced stagnation. A true rebirth, he suggests, would reshape those forms rather than simply repeat the past or copy Europe. He resists the colonial stereotype that India is exclusively other-worldly and incapable of practical life, asserting that spiritual concerns can coexist with creative and active living.

## Critical questions
Distinguish Aurobindo’s claims about a shared Indian “spirit” from verifiable claims about every community. His broad generalisations about India and Europe invite scrutiny: whose voices are represented, and how might caste, gender, region and religion complicate a unified cultural account? He is not simply arguing that every outside influence is harmful; focus on what he says about creative response rather than mechanical imitation.

## Lesson · 50 minutes
0–10: define “renaissance” as a contested term. 10–20: map the contrast between imitation and renewal. 20–30: examine his response to a colonial stereotype. 30–40: test the idea of a single national spirit. 40–50: write a claim with a qualification.

## Questions
Why compare and distinguish Indian and European renaissances? What does he mean by new forms? What might a single cultural “soul” leave out?''','https://motherandsriaurobindo.in/Sri-Aurobindo/books/the-renaissance-in-india/')
captive=n('captive-ladie','Michael Madhusudan Dutt · The Captive Ladie — preliminary outline','''## Important limitation
This is an introductory outline, not the requested complete canto-by-canto explanation. The full prescribed text and edition have not yet been checked in sufficient detail. Do not infer unverified incidents or the exact wording of the ending from this outline.

## Context and broad narrative
Dutt published this English verse narrative in 1849. Its two cantos draw on traditions about Prithviraj, a princess of Kanauj and conflict culminating in his defeat by Muhammad Ghuri’s forces. Scholarship describes the princess’s confinement and her escape with the king among the narrative’s major elements. Names, historical interpretations and details may differ across sources and editions: distinguish a literary retelling of a legendary past from a direct historical record.

## Ways to read
Consider how the title foregrounds a captive woman while martial heroism, love and political conflict also shape the narrative. Ask how much agency the princess is given and how descriptions of opponents create a perspective on power. Dutt’s use of English narrative verse and South Asian material also invites discussion of literary influence without suggesting that either culture is uniform.

## Interim lesson · 50 minutes
0–10: explain that the outline is incomplete. 10–25: read the opening of the assigned canto and identify speaker and setting. 25–35: map characters and relationships using textual evidence. 35–45: examine one image of captivity or heroism. 45–50: list unanswered plot questions to investigate in the text.

## Questions
Whose perspective dominates the assigned passage? What is the difference between an epic retelling and historical evidence? What remains to be verified?''','https://home.uchicago.edu/~cbs2/Megha.pdf.files/intro_Megha.pdf',True)
others=[
n('tagore-chanting','Rabindranath Tagore · Leave This Chanting','''## Summary in sequence
The speaker addresses someone worshipping in a closed, dark temple and urges them to leave chanting and counting beads. Rather than imagining the divine as confined to the sanctuary, the speaker locates God with the tiller working hard ground and the pathmaker breaking stones, in sun and rain and covered with dust.

The worshipper is asked to put aside the outward mantle of holiness and join the workers. The poem questions deliverance conceived as escape from life: the divine has accepted the bonds of creation and remains connected with the world. Its conclusion invites the listener to meet God through work and participation, even if their clothes become dusty.

## Interpretation
Imperatives and rhetorical questions create an urgent challenge. The contrast between closed temple and open workplace gives spiritual value to labour and solidarity. This is a critique of a particular isolated form of devotion, not proof that every ritual or worshipper is insincere. Discuss how it might be read alongside the dignity and actual conditions of workers.

## Lesson · 50 minutes
0–10: identify the addressee. 10–20: paraphrase temple and workplace images. 20–30: examine the question about deliverance. 30–40: discuss labour and devotion. 40–50: write a claim supported by an image.

## Questions
Where does the speaker locate God? What is questioned about deliverance? Why is dust important?''','https://www.poetryverse.com/rabindranath-tagore-poems/leave-this'),
n('tagore-purity','Rabindranath Tagore · Purity','''## Text identification
Some anthologies title the fourth English Gitanjali lyric “Purity”; its opening addresses the divine as the life of the speaker’s life. Check that this is the version assigned in class because titles can vary across editions.

## Summary
The speaker promises to keep the body pure because of a sense of divine presence in it. The next commitment concerns thought: the speaker will resist untruth, associating the divine with truth and the light of reason. The third concerns the heart: the speaker will strive to keep evil away and allow love to flower, imagining the heart as an inner shrine. Finally, the speaker intends to make the divine visible through actions, recognising a power that makes action possible.

## Interpretation
The movement joins body, thought, feeling and conduct rather than treating purity as outward appearance alone. Repetition of future intention makes the lyric a prayer and an ongoing ethical commitment; “try” and “endeavour” leave room for effort rather than claiming perfection. Body purity should be understood in the devotional language of the poem, not used to stigmatise illness, disability, menstruation or other bodily experiences.

## Lesson · 50 minutes
0–10: identify the addressee and repeated promise. 10–22: map the four areas of life. 22–32: examine light, flower and shrine images. 32–42: compare inner conviction and action. 42–50: compose a paraphrase without copying the poem.

## Questions
How do the four commitments develop? Why does the speaker mention reason? How is love represented?''','https://www.cmi.ac.in/~shuvra/attch/gitanjali.html'),
n('summer-woods','Sarojini Naidu · Summer Woods','''## Summary
The speaker is tired of decorated interiors, public conflict, festivities and fame. She longs instead for the colour and movement of summer woods, with gulmohars and flowering cassia. She calls her beloved to accompany her where koels sing, away from public toil and praise.

She imagines resting and dreaming beneath trees, wearing jasmine and playing flutes near banyan roots. The lovers would wander by the river and bathe in pools where panthers drink. At the end they are companions through dawn and night, compared with Krishna and Radhika. These are desires and imagined activities, not a factual travel report.

## Reading closely
Rich visual, musical and fragrant imagery makes the imagined forest an alternative to public life. The contrast does not require the claim that cities or all social activities are inherently bad. The allusion to Krishna and Radha gives the couple’s intimacy a cultural and devotional resonance; readers can ask how myth and sensual pleasure interact. The syllabic movement and repeated invitation produce a songlike tone.

## Lesson · 50 minutes
0–10: contrast the poem’s two settings. 10–22: collect images associated with the senses. 22–32: trace the speaker’s invitation. 32–42: discuss the mythological comparison. 42–50: write about one image without treating imagined details as events.

## Questions
What does the speaker wish to leave? How do sounds and scents shape the woods? What does the Krishna–Radhika allusion add?''','https://www.englitmail.com/2020/02/summer-woods-by-sarojini-naidu.html'),
n('palanquin','Sarojini Naidu · The Palanquin Bearers','''## Summary
The speakers are palanquin bearers singing as they carry a woman. In the first stanza they describe her swaying like a flower, skimming like a bird and floating like laughter from a dream. Their repeated words suggest a gentle, rhythmic journey. They compare her to a pearl carried on a string.

In the second stanza the images shift to a star, a beam on water and a tear from a bride’s eyes. The tear introduces the possibility of sadness within the otherwise light song. The poem repeats the image of the pearl and the movement of carrying. Although wedding travel is a common context for interpretation, the comparison to a bride does not supply every detail of the passenger’s destination or feelings.

## Technique and discussion
Repetition and musical rhythm evoke coordinated movement; similes make the passenger seem delicate and precious. The bearers speak collectively, but the woman does not speak for herself. Ask how poetic beauty, the workers’ labour and the passenger’s absent perspective can be considered together without inventing a detailed story.

## Lesson · 50 minutes
0–10: identify who speaks. 10–20: read aloud and notice repeated sounds. 20–30: compare images of laughter and a tear. 30–40: discuss what the poem does and does not tell us. 40–50: explain the effect of one simile.

## Questions
How does repetition create motion? What mood might the tear introduce? Whose perspective is missing?''','https://www.poetry-archive.com/n/palanquin_bearers/'),
n('pushpa','Nissim Ezekiel · Goodbye Party for Miss Pushpa T. S.','''## Summary
A speaker addresses a farewell gathering for Miss Pushpa, who is soon going abroad to improve her prospects. The speaker praises her sweetness, both outward and inward, and says she smiles readily. He mentions her family and her father’s work as an advocate, but becomes uncertain about the place and digresses into a memory of visiting acquaintances and enjoying their hospitality.

Returning to Pushpa, he calls her popular and praises her willingness to help. She readily says yes to requests. The speaker wishes her a good journey, invites others to speak and says that Pushpa will sum up afterwards. We hear the occasion through his speech; Pushpa’s own speech is not included.

## Language and interpretation
The dramatic monologue’s repetitions, digression and conversational phrasing create humour and an individual voice. The poem stylises a variety of Indian English; Indian English is a legitimate, diverse variety, not a collection of errors to be corrected against British usage. Discuss whether the satire targets formulaic public praise, social aspiration or the speaker’s self-importance, and whether the humour also invites stereotypes. Different readings are possible.

## Lesson · 50 minutes
0–10: identify occasion and speaker. 10–22: follow the digression and return to Pushpa. 22–32: identify what we learn and do not learn about her. 32–42: discuss humour without mocking a community’s speech. 42–50: write a farewell opening that keeps the guest at its centre.

## Questions
What causes the speaker’s digression? How does the monologue create humour? Why does Pushpa’s missing voice matter?''','https://www.indo-anglianpoetry.in/2023/04/poem-goodbye-party-for-miss-pushpa-t-s-summary-and-critical-analysis.html'),
n('night-scorpion','Nissim Ezekiel · Night of the Scorpion','''## Summary
The adult speaker remembers a rainy night when a scorpion, driven indoors beneath a sack of rice, stung his mother and escaped. Neighbours arrive with candles and lanterns and search without finding it. They say that the creature’s movement will move the poison in her blood, and offer prayers and explanations involving past and future lives, suffering and purification.

While the neighbours gather, the mother twists and groans on a mat. The speaker’s father, described as a sceptic and rationalist, tries remedies and blessings; he even pours paraffin on the affected toe and lights it. A holy man performs a rite. After twenty hours the sting loses its force. The mother thanks God that she rather than her children was stung.

## Technique and interpretation
The repeated “they said” gives prominence to communal voices, while the crowd, light and rain surround the suffering woman. The father’s mixture of approaches complicates any simple division between “rational” and “traditional.” The mother speaks only at the end, shifting attention to her care for her children. This final remark is moving, but it should not be used to suggest that all mothers must silently accept pain.

## Safety note
The father’s burning of the toe is part of the poem, not medical advice. Scorpion stings can be dangerous, especially for children. Do not burn, cut or apply chemicals to a sting; seek urgent medical advice, particularly for severe symptoms.

## Lesson · 50 minutes
0–10: sequence the sting and gathering. 10–22: separate neighbours’ beliefs from observed events. 22–32: examine the father’s response. 32–42: analyse the delayed final voice. 42–50: explain how the poem changes focus.

## Questions
Why do neighbours search for the scorpion? What complicates the father’s rationalist label? How does the mother’s final statement alter the poem?''','https://guidingliterature.com/the-night-of-the-scorpion-by-nissim-ezekiel/'),
n('das-introduction','Kamala Das · An Introduction','''## Overview
The speaker introduces herself through nationality, colour, place, languages, gender and personal experience, then resists others’ attempts to define her. The poem uses a strongly personal voice, but a reader should distinguish the crafted speaker from an uncomplicated autobiography of Kamala Das.

## Movement of the poem
The opening refers to male political authority and then asserts the speaker’s identity as an Indian from Malabar who speaks, writes and dreams in different languages. She recalls being told not to write in English because it is not her mother tongue. She responds that the language she speaks becomes her own: its mixed and distinctive qualities carry her experience.

The poem turns to growing up and an early marriage, using painful bodily images to describe a loss of freedom and an unequal encounter with expectations of adulthood. The speaker also describes being instructed to fit feminine roles and names. She rejects attempts to confine her identity to those categories.

Toward the end, the pronoun “I” moves between the speaker and figures of male power or desire. Her insistence that she too can say “I” challenges the assumption that only certain people can claim a full, authoritative self. The shifting pronouns allow both overlap and conflict; follow the wording carefully rather than assigning every “I” to the same person automatically.

## Teaching and discussion
Free verse, direct address, repetition and abrupt shifts of subject give the poem a confrontational energy. The account includes intimate and potentially distressing experiences: offer students a respectful way to discuss imagery without disclosing personal experiences. In 50 minutes: 0–10 map opening identity claims; 10–22 discuss language ownership; 22–32 trace pressures on the body and roles; 32–42 examine shifting pronouns; 42–50 write a claim using a chosen passage.

## Questions
Why does the speaker claim English as hers? What roles do others prescribe? How does the meaning of “I” shift?''','https://suprahow.com/an-introduction-by-kamala-das-poem-analysis/'),
n('someone-song','Kamala Das · Someone Else’s Song','''## Summary, stanza by stanza
The speaker declares herself to be countless people speaking together, comparing the clamour to women at village wells. A single “I” is already multiple rather than a stable solitary voice.

Next the speaker identifies with countless deaths. Images of disease and drying seeds suggest pain and also the possibility that something will be shed and grow as another person’s memory. In the third stanza, countless births appear in blood and an unsettling growing figure whose long-nailed hands mark the air. Birth is energetic but not simply gentle or reassuring.

The final stanza turns from voices to countless silences, imagined as crystal beads strung onto someone else’s song. The ending raises a question: does another’s song preserve those silences, use them without giving the speaker control, or both? The poem does not settle the answer.

## Technique and interpretation
The repeated opening phrase links the four stanzas while the images move through speech, death, birth and silence. The tension between “I” and “someone else” invites reflection on individuality, social roles and artistic ownership. A seed can imply continuity through memory, but the frightening birth-image complicates an easy reading of rebirth as triumph.

## Lesson · 50 minutes
0–10: list the four repeated identifications. 10–22: paraphrase the changing images. 22–32: contrast speech and silence. 32–42: debate the final song’s ownership. 42–50: support two possible interpretations with details.

## Questions
Why multiply the speaker into “a million” voices? How do death and birth connect? Who controls the final song?''','https://www.theguardian.com/books/2015/aug/03/poem-of-the-week-someone-elses-song-by-kamala-das'),
n('mahapatra-freedom','Jayanta Mahapatra · Freedom','''## Summary in movement
The speaker imagines the country’s body floating somewhere down a river and likens his own isolation to a partly disembodied bamboo at the bank. Old widows and dying men pray; children desire the freedom to transform the world. The speaker fears drifting toward either position and speaks of being alone.

That solitude is not innocent. He imagines avoiding a woman and child in a remote village who have lacked enough rice, and avoiding the light on Parliament House. These juxtapositions bring hunger, national political institutions and the observer’s distance into the same field of vision. In a nearby temple the priest is said to know freedom while God hides like an outsider.

The speaker continues searching for light and the freedom of a body alone, then evokes shale, coal and streambeds. The poem closes with ashes the speaker tries to keep away. Its images resist a single, certain definition of freedom; solitude can feel like release, withdrawal or a failure to face others’ suffering.

## Interpretation
The floating body is a striking metaphor, not a documented account of the whole nation’s fate. Ask how the poem compares formal national freedom with material deprivation. The temple and Parliament images raise questions about institutions without proving that the poem rejects every religious or political practice. Its uncertainties are part of its force.

## Lesson · 50 minutes
0–10: collect different meanings of freedom. 10–22: follow the river and bamboo images. 22–32: analyse the hungry family and Parliament. 32–42: compare temple and solitude. 42–50: write a tentative interpretation with textual evidence.

## Questions
What kinds of freedom do different figures desire? Why is the speaker uneasy about solitude? How does hunger challenge a purely political definition of freedom?''','https://indianpoetry.wordpress.com/2013/10/10/freedom-a-poem-by-jayanta-mohapatra/'),
n('mahapatra-twilight','Jayanta Mahapatra · Twilight','''## Summary
An orange flare of late daylight illuminates the pale windows of a hospital; it is not yet dark. In a children’s ward, the speaker sees a mother’s face and the dead, described as always so young. The poem’s compressed phrasing does not offer a detailed history of the child or explain how death occurred.

The scene shifts toward water in a river whose startling sound is imagined as a cry. The speaker asks whether it is a plea to share a curse. Twilight will fall elsewhere too and hide the whiteness of jasmine about to bloom. Lights come on in houses across the street as the speaker looks at a wet August evening, which seems to hold the vast unknown in small, delicate hands.

## Interpretation
The movement from hospital to river, flowers and houses places personal grief beside an ordinary world continuing into evening. Light and darkness, youth and death, blooming and concealment remain in tension. The river’s “cry” and evening’s “hands” personify the landscape, but their precise meaning is uncertain: do not assume that nature is literally mourning or that the mother’s complete thoughts are known.

## Lesson · 50 minutes
0–10: describe the opening light. 10–22: paraphrase the hospital scene without adding facts. 22–32: trace shifts from river to jasmine to houses. 32–42: discuss the last image’s mixture of vastness and delicacy. 42–50: write a supported response to one unresolved question.

## Questions
How does the poem move between human and natural scenes? What does “not yet dark” contribute? Why leave the river’s cry as a question?''','https://www.researchgate.net/publication/360384240_Twilight_by_Jayanta_Mahapatra')]
# Preserve the four already-authored selections and place the new readings in syllabus order.
byid={x['id']:x for x in old}; byid.update({x['id']:x for x in others})
order=['harp-india','orphan-girl','casuarina','lakshman-dutt']
ordered=[macaulay,auro]+[byid[i] for i in order]+[captive]+[byid[x['id']] for x in others]
d[key]=ordered
json.dump(d,open(p,'w'),ensure_ascii=False,indent=2)
print('Unit I selections:',len(ordered),'including preliminary Captive Ladie outline')
