import json
p='prepared-notes.json';d=json.load(open(p))
def add(i,title,body,source):d[f'course-20:{i}']=[{'id':f'func-writing-{i+1}','title':title,'source':source,'text':f'# {title}\nFunctional Communicative Writing · Semester 3, Unit {i+1}\n\n{body}'}]
add(0,'Descriptions, narratives, exposition and persuasion','''## Four purposes
Descriptive writing creates a clear impression of a person, place, object or situation through selected details. Narrative writing presents events and their relationships in time. Expository writing explains a topic or process. Persuasive writing advances a claim and gives reasons for an audience to consider it. A single piece may combine more than one purpose.

## Describing effectively
Choose details that suit the purpose. A description of a library for a new student might include its location, layout, opening hours and accessibility, but only after verifying them. Organise spatially—from entrance to reading area—or by importance. Precise verbs and nouns are usually more helpful than a string of vague adjectives. Describe people respectfully and avoid defining them solely by appearance or stereotypes.

## Narrating an event
Establish what happened, where and when, then arrange significant events in an intelligible sequence. Include relevant causes and consequences and signal time shifts. If writing a factual report, distinguish witnessed facts from hearsay; if writing fiction, a narrator or non-linear sequence can be deliberately chosen.

## Exposition and persuasion
A short explanation of borrowing a book might introduce the goal, list the steps and identify whom to contact for help. A persuasive paragraph about library hours might state a proposal, give a reason, acknowledge staffing costs and support the proposal with actual evidence. Do not invent survey results.

## Short messages
A message should identify sender, recipient or intended audience, essential purpose and any action or deadline. Example: “Hello Ravi, the meeting has moved to Room 4 at 3 p.m. Please confirm you received this. — Meena.” The names, room and time are illustrative.

## 50-minute lesson
0–10: classify four short passages by purpose. 10–22: describe an object for a specific reader. 22–32: narrate an event in sequence. 32–42: write a proposal with one reason and qualification. 42–50: peer-check clarity, sequence and unsupported claims.

## Practice
Describe the same room for a visitor and for someone planning repairs. What information changes? Write a three-sentence narrative, then convert it into an explanation.''','https://owl.purdue.edu/owl/general_writing/academic_writing/essay_writing/index.html')
add(1,'Paragraphs, précis, blogs and pictorial writing','''## Paragraph writing
A paragraph develops a central idea through related sentences. A topic sentence can orient a reader; supporting sentences explain, provide evidence or illustrate; a final sentence may connect the idea to what follows. Not every paragraph must follow a rigid formula. Coherence comes from logical order, clear references and transitions rather than repeating linking words mechanically.

Example: “A reading timetable can help students prepare steadily. Setting aside a short daily period makes long texts less daunting. The timetable should allow rest and be adjusted when other responsibilities change.” The third sentence qualifies the claim instead of promising the same result for everyone.

## Précis writing
A précis is a concise restatement of a source’s central argument and key supporting ideas in your own words. Read the whole passage, identify its purpose and main claim, separate essential support from examples, draft in a logical sequence, then compare with the original for accuracy and proportion. Attribute the source when required. Do not add personal opinion or copy long phrases as if they were your own. Follow the length and format specified by the teacher rather than assume a fixed proportion.

## Blog writing
Identify the reader and useful purpose, choose a clear title, organise sections with meaningful headings and use examples or links where relevant. A personal voice is possible, but factual claims still need checking. Disclose sponsorship if applicable and protect others’ privacy.

## Pictorial writing
Picture-based writing begins with careful observation. List what is visible separately from what is inferred, then plan a description, narrative or report according to the prompt. If a picture shows people beside an umbrella, “they are waiting for a bus” is an inference unless a visible sign supports it. In a creative story, invented details are allowed; in a factual description they should not be presented as observed facts.

## 50-minute lesson
0–10: identify a paragraph’s main idea. 10–20: reorder supporting sentences. 20–30: write a short précis of an assigned paragraph. 30–40: turn a visual prompt into observed and inferred details. 40–50: peer-check fidelity to source and purposeful organisation.

## Questions
How does a précis differ from a response? What is the difference between observation and inference? How does a blog heading help the reader?''','https://owl.purdue.edu/owl/general_writing/the_writing_process/paragraphs_and_paragraphing/index.html')
add(2,'Letters, email, résumé, cover letters and applications','''## Formal letters and email
Begin by identifying the recipient and purpose. A formal letter commonly includes sender and recipient details, date, subject, salutation, body and closing; follow the institution’s required format. An email uses a concise subject, greeting, clear body, requested action and signature. Address the reader respectfully and proofread names, dates and attachments.

Example email subject: “Application for student volunteer role.” Opening: “Dear Coordinator, I am writing to apply for the student volunteer role advertised by the department.” State relevant facts and next steps without inventing an advertisement, address or vacancy.

## Résumé
A résumé summarises relevant education, skills and experience. Use clear headings and accurate dates; present genuine projects or responsibilities when employment experience is limited. A useful description specifies what you did and, where supported, a result. Do not fabricate qualifications, references, metrics or job titles. Personal information requirements vary by employer and law, so share only what is appropriate.

## Cover letter and application
A cover letter connects the applicant’s genuine experience to a specific role. One workable structure is purpose and role; a short paragraph explaining relevant evidence; a closing expressing interest and availability. An application may be a form, letter or email: answer each instruction, provide requested documents and check the submission method.

## Example
Weak: “I am the best candidate and can do anything.” Stronger, if true: “As a student volunteer, I helped organise reading sessions and kept attendance records.” The second gives an observable responsibility without an unsupported superlative.

## 50-minute lesson
0–10: identify the purpose of each document. 10–20: draft a subject line and professional opening. 20–32: build a truthful résumé section. 32–42: connect one real experience to a role in a cover letter. 42–50: peer-check clarity, dates and missing instructions.

## Questions
How does a cover letter complement rather than duplicate a résumé? Why should a subject line be specific? What should be checked before attaching a document?''','https://owl.purdue.edu/owl/subject_specific_writing/professional_technical_writing/job_search_writing/index.html')
add(3,'Newspaper articles, letters to the editor and reports','''## Newspaper article
A news article informs readers about a newsworthy event or issue using verified information and attributable sources. A lead gives the most significant information clearly; following paragraphs add context, evidence and relevant perspectives. Verify names, dates, place and quotations; distinguish allegations from established facts. A feature article may use a different structure from a straight news report.

## Letter to the editor
A letter to the editor responds to a public issue or published article. State the issue or article, make a focused claim, offer reasons or evidence and propose an action when appropriate. Use a courteous tone and follow the publication’s rules on length and identification. Avoid sharing private information or making unsupported accusations.

Model opening: “The article on public library access raises an important question about evening study space.” The rest should give locally verified evidence rather than inventing statistics.

## Reports
A report presents information for a defined audience and purpose. Depending on the assignment, sections may include title, purpose, methods or sources, findings, discussion and recommendations. A finding describes what the evidence indicates; a recommendation proposes what should be done. Example: “Three of five interviewed students mentioned limited seating” is a finding only if the interviews actually occurred; “consider a seating survey” is a recommendation. Five voluntary interviews cannot establish the views of all students.

## Editing and ethics
Cross-check sources and permissions, retain notes, correct errors, avoid misleading headlines and distinguish news from opinion or sponsored content. When reporting harm, protect privacy and avoid sensationalising people’s experiences.

## 50-minute lesson
0–10: distinguish news, opinion and a report. 10–22: organise verified event facts into a lead. 22–32: draft a letter on a local issue. 32–42: separate findings from recommendations. 42–50: peer-check claims, attribution and tone.

## Questions
What makes a headline misleading? How does a recommendation differ from a finding? What does a writer need to verify before quoting someone?''','https://owl.purdue.edu/owl/subject_specific_writing/journalism_and_journalistic_writing/index.html')
add(4,'Grammar, punctuation, vocabulary and reported speech','''## Punctuation and meaning
A full stop marks the end of a statement; a question mark marks a direct question. Commas can separate items or mark some introductory material, but should not automatically join two independent sentences. Compare “The library closed, we went home” with “The library closed, so we went home” or two separate sentences. A colon can introduce an explanation or list after a complete clause; a semicolon can join closely related independent clauses. Follow the relevant style guide where conventions differ.

## Synonyms and antonyms
Synonyms have similar meanings in a particular context; they are not always interchangeable. “Small” and “minor” can both suggest limited size or importance, but a “small room” is not normally a “minor room.” Antonyms express contrasts, such as “open” and “closed,” although some opposites are context-dependent or admit degrees. A dictionary and example sentence help confirm usage.

## Direct and indirect speech
Direct speech reports a speaker’s words using quotation marks: Meena said, “I am tired.” Indirect or reported speech integrates the content into the reporting sentence: Meena said that she was tired. Pronouns, tense and time expressions may change with the reporting context. Backshifting is common after a past reporting verb, but it is not mandatory in every situation; a statement that remains true can sometimes retain its present tense. Use the assignment’s conventions.

## Common errors and revision
Check subject–verb agreement (“The students are ready”), consistent time reference, complete sentences, pronoun reference and punctuation. Read for meaning before applying a rule: “Everyone should bring their book” is widely used, including with singular they; follow the institutional style while recognising legitimate variation. English language varieties differ, and not every unfamiliar form is an error.

## 50-minute lesson
0–10: compare punctuation choices. 10–20: replace words with context-appropriate synonyms. 20–30: convert direct speech to reported speech. 30–42: edit a paragraph and explain revisions. 42–50: exit ticket with one corrected sentence and reason.

## Practice
Report “We will meet tomorrow” the next day, supplying a clear time reference. Choose a synonym for “bright” in “bright light” and another in “bright student.” Why do they differ?''','https://owl.purdue.edu/owl/general_writing/punctuation/index.html')
json.dump(d,open(p,'w'),ensure_ascii=False,indent=2)
print('Added Functional Communicative Writing: 5 units')
