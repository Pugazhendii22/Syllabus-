import json
p='prepared-notes.json';d=json.load(open(p))
def add(i,title,body,source):
 d[f'course-18:{i}']=[{'id':f'content-writing-{i+1}','title':title,'source':source,'text':f'# {title}\nContent Writing · Semester 3, Unit {i+1}\n\n{body}'}]
add(0,'Content writing · purpose, audience and process','''## What is content writing?
Content writing creates written material for a defined audience and purpose: to explain, inform, help a reader complete a task, build a relationship or support an action. Forms include web pages, articles, newsletters, reports, case studies and product information. Not every piece is an advertisement. A good content writer works with subject specialists, editors, designers and publishers, and checks that claims are supported.

## Role and responsibilities
A writer interprets a brief, researches, identifies the audience’s questions, structures information, drafts, edits and adapts the work to its medium. Responsibilities include accuracy, accessible language, respectful representation, source acknowledgement, deadlines and adherence to the organisation’s style guide. An editor or subject expert may review specialist claims; a writer should not invent credentials or first-hand experience.

## Print and web
A print reader may encounter a continuous page sequence; a web reader may arrive directly at one section from a search or link. Online headings, informative link text and mobile-friendly paragraphs help navigation. Print also needs clear structure. Neither medium requires a fixed sentence length or arbitrary word count. Search engine optimisation (SEO) can make useful content easier to discover, but repeated keywords and empty claims do not substitute for helping the reader.

## The content process
1. Brief: define audience, topic, desired outcome, format, deadline, evidence and approval process.
2. Research: use reliable sources, note publication dates and record links or references.
3. Structure: arrange the answer in a useful order and identify gaps.
4. Draft: use clear headings, examples and a consistent voice.
5. Review: verify claims, links, accessibility, rights and style.
6. Publish and maintain: correct errors and revisit information when circumstances change.

## Worked example
Brief: “Help first-year students find library books.” Audience: new students. Outcome: find a book and know whom to ask. Outline: catalogue search, understanding availability, finding the shelf, requesting help. Do not invent the library’s hours or rules; verify them locally.

## 50-minute lesson
0–10: compare information and persuasion. 10–20: identify audience and purpose in a brief. 20–30: draft a practical outline. 30–42: write the opening and one section. 42–50: peer-check usefulness and identify two facts requiring verification.

## Check yourself
What distinguishes audience from purpose? How does a web heading help a reader? Why is publishing not the end of the process?''','https://developers.google.com/search/blog/2022/08/helpful-content-update')
add(1,'Content formats · research, drafting and editing','''## From brief to draft
Clarify the reader, objective, length, medium, deadline and constraints. Generate ideas, then research before choosing the strongest supported ones. Organise a logical outline and write a draft. Check the style sheet for spelling, punctuation, capitalisation, terminology, tone and citation conventions. Edit structure and flow before proofreading individual errors.

## Formats and purposes
An essay develops an idea or argument with explanations and evidence. A report presents information or findings for a defined purpose, often with sections and recommendations. Newspaper writing gives readers relevant verified information, distinguishes reporting from opinion and answers important questions clearly. Advertising aims to persuade and should not disguise unsupported claims as facts.

A blog can explain, reflect, report or advise; a useful post has a clear topic, helpful headings and sources where appropriate. A case study describes a particular situation, the action taken and the results, supported by evidence and permission; do not invent customer outcomes. A white paper explores a complex issue or proposed solution in detail and should distinguish evidence from a company’s promotional interest.

## Corporate writing
B2B addresses organisations; a reader may need compatibility, procurement and implementation details. B2C addresses individual consumers; a reader may need price, availability and practical benefits. Neither audience is uniform. A press release gives newsworthy, verifiable information with an attributable contact and date; it is not a guarantee of media coverage. A newsletter selects useful updates for subscribers and makes any promotional purpose clear.

## Tone, jargon and market research
Choose a formal or informal register for the reader and context. Explain necessary specialist terms; avoid jargon used only to sound impressive. Market research can include interviews, surveys and analysis of common questions, but respect consent and privacy. Separate verified findings from assumptions about the audience.

## Example: one fact in two formats
Verified event information: a library workshop is on Friday at 4 p.m. A news brief reports the event and source. An invitation might say, “Join the library workshop on Friday at 4 p.m.” Neither version should invent a venue, registration link or promised outcome.

## 50-minute lesson
0–10: unpack a brief. 10–20: compare blog, report and press release. 20–32: outline a case study without fabricating results. 32–42: revise for audience and style sheet. 42–50: exchange proofreading checklists and write one evidence question.

## Questions
How does a case study differ from a white paper? Why can a B2B reader still need plain language? What should be checked before a press release is sent?''','https://owl.purdue.edu/owl/subject_specific_writing/professional_technical_writing/business_writing_for_administrative_and_clerical_staff/genre_and_medium.html')
add(2,'Visual and interactive content','''## Visual content
An infographic combines visual organisation with information to make relationships or processes easier to understand. Begin with a clear point and reliable data; label units, dates and sources. Avoid misleading scales, distorted comparisons and visual decoration that obscures the message. An accompanying text summary or data table makes complex information available to readers who cannot use the graphic.

Images and screenshots can illustrate a product, step or situation. Choose images relevant to the message; obtain appropriate permission or a suitable licence. Check screenshots for private information, old interfaces and unreadably small text. Alternative text should convey an informative image’s purpose in context; decorative images can use an empty alternative. A complex chart needs more than a short alt text: supply its information in nearby text or a table.

## Video, memes and demonstrations
A product demonstration shows a real task in a sequence: introduce the goal, show the steps, explain limitations and give the next action. Use accurate captions for meaningful audio and provide a transcript; describe important visual information as needed. Memes and GIFs draw on shared conventions and can create humour, but context, copyright, access and potential offence matter. Avoid essential information conveyed only through a moving image.

The syllabus extract says “30-degree videos.” This may be a formatting or source error; check the original syllabus and teacher’s instruction before assuming it means 360-degree video. If 360-degree video is intended, the viewer can explore a recorded environment; offer an accessible alternative and consider motion sensitivity.

## Interactive content
A quiz asks questions and provides feedback; a poll collects responses; an interactive white paper lets readers navigate or explore information. State purpose, explain how responses will be used, avoid collecting unnecessary personal data and test keyboard and screen-reader access. A poll is not automatically representative research: describe who responded and how they were selected.

## Free and paid tools
Choose tools by task, accessibility, data protection, export format, collaboration, licensing and total cost—not just the “free” label. Free tiers, limits and prices change. Do not upload confidential material to an external service without permission.

## 50-minute lesson
0–10: compare a graphic and its text equivalent. 10–22: sketch an accessible infographic with a source. 22–32: draft a short demonstration script. 32–42: design a poll and identify sampling limitations. 42–50: peer-check rights, accessibility and privacy.

## Questions
What makes a visual misleading? Why do captions and text equivalents matter? What can a voluntary poll legitimately tell us?''','https://www.w3.org/WAI/tutorials/images/tips/')
add(3,'Social media, public relations and originality','''## Social media writing
A social-media post should fit its audience, platform and purpose while remaining understandable outside its original context. State the main message clearly, use accessible wording and link to a reliable source when a claim needs support. A platform may truncate text or display it differently on a phone, so place essential information where readers can find it. Check images, captions and contrast.

## Public relations
Public relations concerns communication and relationships between an organisation and its publics, including staff, customers, communities and journalists. A PR statement should identify the organisation, explain what is known and what action is being taken, and avoid claiming certainty where facts are still being checked. PR, advertising and independent journalism have different roles even when all use similar channels.

Example: “The library is closed today because of a power issue. We will share an update by 2 p.m.” is useful only if those details have been verified and someone will deliver the update. If the reopening time is unknown, say so rather than inventing one.

## Plagiarism and copyright are not identical
Plagiarism is presenting another’s words, ideas or work as one’s own under the relevant academic or professional rules. Copyright is a legal system governing certain uses of protected works; legal outcomes depend on jurisdiction, rights, licences and exceptions. Attribution alone does not necessarily grant permission to reuse a copyrighted image or text. Conversely, use may be lawful in a situation while still requiring attribution under a professional or institutional policy. Do not treat these notes as legal advice.

## Writing original copy
Record sources while researching. Put copied wording in quotation marks in notes, then draft your own structure and wording. Attribute ideas and quotations, verify permissions and licences, and check any AI-assisted text for accuracy, originality and rights issues. A similarity score is a prompt for review, not proof by itself of plagiarism or innocence.

## 50-minute lesson
0–10: analyse an organisation’s audience and purpose. 10–22: write a clear service update. 22–35: distinguish quotation, paraphrase and copied text. 35–45: discuss attribution versus permission using an image example. 45–50: exit ticket naming one check before publication.

## Questions
Why should a crisis message identify uncertainty? Does crediting an image always give permission to use it? What makes a paraphrase genuinely independent?''','https://owl.purdue.edu/owl/resources/preventing_plagiarism/contextualizing_plagiarism/handout_comparing_policies.html')
add(4,'Copywriting for print, email, social media and websites','''## Copywriting and audience
Copywriting uses words to support a specific response, such as learning about an event, comparing a product or signing up for a service. It may be persuasive, but should be accurate and clear. Before writing, identify the reader, their problem, the offer, supporting evidence, medium and desired action. A call to action (CTA) tells the reader what to do next; it should match a real destination or process.

## Build and edit a message
A practical sequence is audience need → relevant benefit → evidence → next step. A feature is what something does; a benefit is why that feature may matter to a particular reader. Example: “The reading room has adjustable lamps” is a feature; “Adjust the light for comfortable reading” is a possible benefit. Do not claim every person will find it comfortable, or imply a feature exists without verification.

## Adapt by medium
Print advertising must communicate the offer, necessary conditions and action in the space available. Email marketing needs a meaningful subject line, a relevant message, a clear action and compliance with applicable consent and unsubscribe requirements. Social copy may be brief, but should not omit important qualifications. Website content should help readers understand the offer and complete a task; headings and descriptive links support navigation. Avoid fake urgency, invented testimonials, hidden fees and claims that cannot be substantiated.

## Sample adaptation
For a verified free library orientation: print headline: “Find your way around the library.” Email subject: “Library orientation: Friday at 4 p.m.” Website button: “See orientation details.” Confirm the time, location and link before publication; these examples do not imply a real event.

## Editing checklist
Does the first line address the reader? Is the main claim accurate and supported? Are terms and conditions visible? Is the CTA specific and functional? Can the text be read on mobile? Has a second person checked names, numbers, punctuation and links?

## 50-minute lesson
0–10: distinguish features and benefits. 10–20: write an audience brief. 20–32: draft print and email versions of one offer. 32–42: rewrite for a website and social post. 42–50: peer review for clarity, evidence and ethical claims.

## Questions
Why is “everyone needs this” a weak audience definition? What makes a CTA misleading? How can a writer persuade without exaggeration?''','https://developers.google.com/search/blog/2022/08/helpful-content-update')
json.dump(d,open(p,'w'),ensure_ascii=False,indent=2)
print('Added Content Writing: 5 units')
