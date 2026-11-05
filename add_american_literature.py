import json
p='prepared-notes.json';d=json.load(open(p))
def n(id,title,body,source):
 return {'id':id,'title':title,'source':source,'text':'# '+title+'\nAmerican Literature I · Semester 4\n\n'+body+'\n\nCompare this teaching draft with the assigned text and edition.'}
d['course-22:0']=[n('american-context','Puritanism to American Realism · historical context','''## Orientation
American literature is not a single voice or a simple succession of movements. The writers on this course worked in a society shaped by Indigenous dispossession, colonial settlement, slavery, revolutionary government, unequal citizenship, immigration and reform. Dates below are approximate; themes and movements overlap.

## Puritanism and its legacies
English Puritan communities in seventeenth-century New England valued religious discipline and interpreted experience through Christian belief. Their writing includes sermons, journals, histories and poetry. Do not assume that all colonial writing was Puritan or that all members held identical views. Anne Bradstreet wrote within this culture while negotiating expectations placed on women.

## Romanticism and the American Renaissance
Nineteenth-century American Romantic writing often values imagination, individual experience, emotion and nature. The term “American Renaissance,” associated with a mid-nineteenth-century concentration of influential works, is a critical label rather than a movement with a fixed membership. Its traditional canon has been criticised for excluding women, Indigenous writers and Black writers; broaden the discussion beyond a list of famous male authors.

## Transcendentalism
Transcendentalist thinkers such as Emerson and Thoreau explored individual conscience, spiritual insight and the relationship between humanity and nature. Their positions differ: read each argument rather than assuming that self-reliance means isolation or indifference to others.

## Slavery, abolition and Civil War
Millions of Africans and their descendants were enslaved in the United States. Abolitionists, including Black activists and writers, resisted slavery through organising, writing, escape and other actions. Wheatley Peters and Horton wrote under the constraints of enslavement; do not reduce their work to a single subject. The US Civil War (1861–1865) was fought over secession in a conflict centrally tied to slavery. The Thirteenth Amendment abolished slavery and involuntary servitude except as punishment for a crime following conviction. Reconstruction and its aftermath brought constitutional change alongside violent resistance and continuing racial inequality.

## Realism
Realist writing associated with the later nineteenth century often attends to social settings, ordinary experience, dialogue and the pressures of institutions. Realism is not a transparent copy of life: selection, narrative voice and literary conventions shape representation. Twain’s novel offers opportunities to examine vernacular, race and social criticism while being attentive to its racist language.

## 50-minute lesson
0–10: place key events on an approximate timeline. 10–20: discuss categories and exclusions in a literary canon. 20–30: connect Puritanism and Bradstreet. 30–40: discuss slavery, abolition and literary voice. 40–50: compare Romantic and realist interests, noting overlap.

## Questions
Why should a movement label be used cautiously? How does abolition connect literature with political action? What can realism select or leave out?''','https://www.britannica.com/art/American-literature')]
d['course-22:1']=[
n('bradstreet-prologue','Anne Bradstreet · The Prologue','''## Context
Anne Bradstreet (c. 1612–1672) wrote in colonial New England. “The Prologue” introduces the poetic project while confronting readers who dismiss women’s intellectual and artistic work. It uses a public language of modesty, but whether every self-deprecating statement is sincere, strategic or ironic is open to discussion.

## Movement through the poem
The speaker begins by saying that grand public subjects—wars, captains and kings—are beyond her supposed powers. She admires the poetry of Guillaume de Saluste Du Bartas and wishes she had greater ability. Images of weakness, flawed craft and damaged music seem to explain why she cannot rival celebrated writers.

The argument changes as the speaker directly names a hostile critic who says a needle suits her hand better than a poet’s pen. Even good writing, she complains, may be dismissed as stolen or accidental because its author is a woman. This is a double bind: failure confirms prejudice, while success is not credited to her.

She points to the ancient Greek Muses, female figures associated with inspiration, but anticipates that critics can dismiss the argument. She appears to grant male precedence while asking for some acknowledgement of women’s work. Finally, she contrasts the great poets’ laurel with a humbler wreath of kitchen herbs. The contrast can sound modest and cutting at once: an accomplished poem performs the ability its society denies.

## Form and interpretation
The poem uses patterned six-line stanzas, rhyme and formal argument. Notice the movement between praise, apparent concession, complaint and satire. The needle and pen contrast assigned domestic roles with authorship; neither domestic work nor the people performing it should be treated as inherently unimportant. Avoid assuming that the speaker’s voice perfectly reveals Bradstreet’s private feelings.

## 50-minute lesson
0–10: discuss who receives recognition for creative work. 10–22: trace the speaker’s stated limitations. 22–32: analyse the needle-and-pen objection. 32–42: debate the final wreath’s tone. 42–50: write an interpretation supported by a short passage.

## Questions
How does the poem expose a double standard? Why invoke the Muses? What different tones can the final wreath carry?''','https://www.ebsco.com/research-starters/womens-studies-and-feminism/prologue-anne-bradstreet/'),
n('wheatley-evening','Phillis Wheatley Peters · A Hymn to the Evening','''## Context
Phillis Wheatley Peters (c. 1753–1784) was taken from West Africa as a child and enslaved in Boston. Her 1773 collection demonstrates sophisticated engagement with Christian, classical and eighteenth-century poetic traditions. The title is also printed as “An Hymn to the Evening”; check the assigned edition.

## Summary in sequence
The poem opens as the sun has departed, thunder sounds and a gentle breeze carries the fragrance of spring. Streams and birds contribute to a harmonious natural scene. The sky displays beautiful colours, with the deepest red in the west. The speaker turns from observation to a prayer that people’s hearts may glow with virtue and become living temples of God.

As darkness arrives, the speaker praises the divine power associated with day and night and wishes that sleep may soothe tired minds. Waking should bring renewed moral and spiritual alertness, with labour undertaken more guarded against sin. At the close, night’s heavy sceptre seals the speaker’s eyes; the song must pause until Aurora, the classical figure of dawn, rises.

## Reading closely
Sensory details—sound, colour and fragrance—turn evening into an experience of both grandeur and calm. The hymn moves from natural description to collective spiritual aspiration and individual sleep. Personification makes night appear as a ruler; the classical name Aurora joins a Christian devotional framework. It is possible to discuss the tension between Christian ideals and the world of slavery as context, but this poem should not be treated as a straightforward narrative of enslavement when its images do not explicitly say that.

## 50-minute lesson
0–10: list senses used in the opening. 10–22: paraphrase the movement from landscape to prayer. 22–32: analyse the living-temple image. 32–42: compare the personifications of night and dawn. 42–50: write how the ending changes the poem’s pace.

## Questions
How do natural sounds shape the opening? What moral hope follows the description of the sky? Why does the song stop at the end?''','https://www.gradesaver.com/phillis-wheatley-poems/study-guide/summary-a-hymn-to-the-evening'),
n('horton-liberty','George Moses Horton · On Liberty and Slavery','''## Context
George Moses Horton (c. 1798–c. 1883) was an African American poet enslaved in North Carolina for much of his life. His early collection The Hope of Liberty appeared in 1829. He wrote within formal poetic traditions while speaking against enslavement; consult the assigned text for its punctuation and stanza arrangement.

## Summary in sequence
The speaker opens by asking whether he was born to wear a chain and endure slavery’s misery. He describes grief, oppression and the fear that relief may come only at death. These questions challenge the idea that enslavement is a natural or just condition.

The speaker then calls on Liberty as a welcome sound that might drive away fear. He commands oppression to cease and tyrants to stop raging. A dove and its wings become images of movement and release; the poem also invokes Africa. Liberty is a precious prize, imagined as a rising sacred sun, while Slavery appears as a disfigured figure who should hide her face. The speaker does not accept the condition in which he is forced to live.

In the closing movement, Liberty is imagined as a place of refuge and healing. A comparison to a swan returning to a nest expresses a longing for safety. Shade and calm answer the earlier storm, and the poem ends with songs of liberty. This is an appeal and an imaginative anticipation, not proof that the speaker has already been freed.

## Form and themes
Direct address to Liberty and personification of Slavery turn political abstractions into figures the speaker can confront. Repeated exclamations and the contrast between chains and flight dramatise both suffering and desire. Notice the movement from the singular speaker’s pain toward a collective appeal for freedom. Interpretations of the dove and sun should remain grounded in their contexts rather than treating symbols as fixed codes.

## 50-minute lesson
0–10: distinguish the poet’s historical context from the speaker’s voice. 10–22: map the shift from questions to appeal. 22–32: examine chains, dove and sun. 32–42: discuss how the final refuge responds to the opening. 42–50: write a claim with evidence.

## Questions
Why does the first question challenge slavery? How do personification and direct address work? Is the final freedom achieved or desired?''','https://www.byanyothernerd.com/2021/01/poem-3-on-liberty-and-slavery-by-george.html'),
n('whitman-cradle','Walt Whitman · Out of the Cradle Endlessly Rocking','''## Overview
The adult speaker recalls a boy’s experience on the Long Island shore, called Paumanok in the poem. A nesting pair of mockingbirds, the disappearance of one bird, the other’s lament and the sea’s whispered word awaken the boy’s poetic consciousness. The absent bird is presumed lost; the poem does not establish the circumstances of her disappearance.

## Detailed movement
At the opening, the speaker gathers memories out of the sea’s rocking and the mockingbird’s song. The boy leaves his bed at night and wanders by the shore. Two birds nest together; their repeated calls express an imagined closeness and the joy of being together. The boy listens and later renders their sounds in human language.

One day the female bird does not return. The remaining male bird waits and sings, sometimes under the moon, calling on the sea winds and the natural world to bring his mate back. The speaker’s translation of the bird’s long aria moves between hope, misunderstanding, longing and despair: shadows, wind and spray can seem to offer signs before absence is felt again.

The listening boy becomes intensely moved. The bird’s song releases emotions and questions in him and helps awaken his vocation as a singer. He asks the sea for an answer; it seems to whisper the word “death” repeatedly. The adult poet gathers the memory of the bird’s song and the sea’s word into his own later song. Death is at once unsettling, intimate and inseparable from the account of love; it should not be reduced to an unambiguously comforting answer.

## Technique
Free verse, repetition and apostrophe give the work musical force without regular fixed stanzas. The bird, boy and sea form interacting voices, but the bird’s words are the poet-speaker’s imaginative translation, not an independently verified statement by an animal. The rocking cradle suggests rhythmic movement and emergence; consider how it can hold both birth and loss.

## 50-minute lesson
0–10: map narrator, boy, bird and sea. 10–22: sequence the nesting and disappearance. 22–32: trace changes in the aria. 32–42: discuss the sea’s answer and its ambiguity. 42–50: explain how listening contributes to the poet’s emergence.

## Questions
What is known and unknown about the missing bird? Why translate the bird’s song? How does the poem connect love, mourning and artistic voice?''','https://www.poetryverse.com/walt-whitman-poems/out-cradle-endlessly-rocking'),
n('dickinson-success','Emily Dickinson · Success is counted sweetest','''## Summary, stanza by stanza
The opening proposes a paradox: those who do not succeed may value success most intensely. The speaker compares success to nectar and suggests that acute need is necessary to comprehend it fully. This is the poem’s claim, not an empirical law that everyone must accept.

The second stanza introduces a victorious “purple Host” that has captured a flag. The people who possess victory cannot define it as clearly as the person introduced in the final stanza. The poem moves from an abstract generalisation to a concrete scene of conflict.

The third stanza completes the comparison: a defeated, dying person hears distant sounds of triumph. The music reaches an ear described as “forbidden,” and its clarity is agonising. The victor’s celebration becomes painful evidence of what the dying figure cannot share. The poem does not identify a particular battle or tell us that the soldier later succeeds.

## Analysis
Sweetness and nectar make success a matter of taste and need; the end shifts to hearing. The flag can represent a military victory, and purple may suggest power or splendour, although no single symbolic reading is compulsory. The poem’s compact stanzas, compressed syntax and dashes slow and intensify its argument. “Agonized and clear” joins pain and understanding instead of simply praising suffering.

## 50-minute lesson
0–10: ask whether people value what they lack. 10–20: paraphrase the opening claim. 20–30: connect the second stanza to the third. 30–40: examine the shift from taste to sound. 40–50: write a supported response that either accepts or questions the generalisation.

## Questions
What is the opening paradox? Who captures the flag, and who hears triumph from afar? Why is the final perception both clear and painful?''','https://www.poetryfoundation.org/poems/45721/success-is-counted-sweetest-112')]
d['course-22:2']=[n('emerson-self','Ralph Waldo Emerson · Self-Reliance','''## Argument and context
Published in 1841, “Self-Reliance” is associated with American Transcendentalism. Emerson urges readers to trust their own insight rather than surrender judgment to convention. His argument is spiritual and philosophical as well as social: self-trust is not merely a recipe for financial independence.

## Following the argument
Emerson begins by valuing original perception. He contrasts genuine conviction with imitation and warns that society rewards conformity. Individuals face pressure from other people’s disapproval and from the fear of seeming inconsistent. He criticises “foolish” consistency: repeating yesterday’s opinion solely to preserve a public image, even when present judgment has changed. This does not mean that every inconsistency is wise or that promises never matter.

The essay also questions habits of dependence, inherited beliefs and the uncritical worship of institutions, travel, property or admired figures. Emerson argues that spiritual authority and creative power are not confined to the past or to famous individuals. His forceful aphorisms and sweeping claims ask the reader to test familiar assumptions.

## Questions for critical discussion
How does the call to follow conscience relate to obligations to other people? Who has the resources and social freedom to act independently? Emerson’s broad declarations can be read alongside exclusions and inequalities in nineteenth-century America. Distinguish the essay’s argument from a modern slogan that says people need no community or help.

## 50-minute lesson
0–10: consider a situation involving conformity. 10–22: paraphrase self-trust and imitation. 22–32: discuss what makes consistency “foolish.” 32–42: test the argument against responsibility and unequal opportunity. 42–50: write a claim and a qualification.

## Questions
How does Emerson distinguish self-trust from conformity? Why qualify consistency as foolish? What potential conflict arises between independence and obligation?''','https://www.encyclopedia.com/arts/culture-magazines/self-reliance-0'),
n('thoreau-civil','Henry David Thoreau · Civil Disobedience','''## Context and central problem
The essay first appeared in 1849 as “Resistance to Civil Government” and was later published under the title “Civil Disobedience.” Thoreau criticises a government implicated in slavery and the US war with Mexico and asks what an individual should do when law and conscience conflict.

## Argument in sequence
Thoreau begins by questioning the assumption that majority rule is automatically just. A government’s power may depend on numbers or force rather than moral right. He argues that people should not allow institutions to turn them into instruments of injustice.

He considers objections to acting against unjust laws. Waiting for a majority to correct a wrong can perpetuate it; voting alone may register a preference without removing one’s own participation. He argues that an individual should withdraw support from injustice, even when this carries consequences. His example of refusing the poll tax and spending a night in jail turns an abstract claim into a reflection on the state’s power over the body and the limits of that power over conscience. The essay does not require the claim that every illegal act is justified.

Thoreau’s account is not a complete, universally applicable rulebook for modern civil-disobedience campaigns. People have different risks, responsibilities and means of resistance. His emphasis on individual action can be compared with collective abolitionist organising and with later movements without assuming all used identical strategies.

## Relation to Emerson
Both writers value conscience and question conformity. Thoreau’s essay applies such questions to taxes, imprisonment and direct complicity in state injustice. Their arguments are related but should not be treated as identical.

## 50-minute lesson
0–10: distinguish legality and justice. 10–22: identify Thoreau’s reasons for resistance. 22–32: discuss voting, participation and waiting. 32–42: analyse the jail example and risks of action. 42–50: compare a position in Emerson with one in Thoreau.

## Questions
Why does Thoreau distrust an unjust majority? What distinction does he draw between voting and acting? What are the risks and limitations of an individual-conscience model?''','https://iep.utm.edu/thoreau/')]
json.dump(d,open(p,'w'),ensure_ascii=False,indent=2)
print('Added American Literature I: context, five poems and two essays')
