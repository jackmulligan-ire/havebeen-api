negative_bg_prompt = "The following are some bad examples. They have user requests, responses that you should avoid, why they're bad, and a good example."

negative_1 = '''
User Input:
"title: Discuss Q3 roadmap feedback\n description: Need to discuss feedback received on the Q3 product roadmap."

Bad response:
"Hi [Recipient's Name],

Could you provide a brief update on the progress of the reports when you have a moment?

Specifically, I'm interested in:
* Completion percentage
* Any roadblocks you've encountered
* Estimated completion date

Thanks!"

"Hi Team,

To help understand the cause of the website outage this morning, could you please share the following information:

* Exact time of the outage
* Steps taken to restore the website
* Initial assessment of the cause
* Any known impact on users

Thanks!"

"Hi [Recipient's Name],

Would you mind taking a look at the marketing proposal and providing your feedback directly in the document [Link to Document]?

I'm particularly interested in your thoughts on:
* Overall clarity and persuasiveness
* Accuracy of the data and claims
* Alignment with the client's goals

Thanks!"

Why it's bad:
Multiple responses to the answer, we just want a single response.

Good response to this:
"Hi Team,

To facilitate a discussion around the feedback received on the Q3 product roadmap, please share your thoughts on the following:

* Key areas of concern
* Proposed solutions to address the feedback
* Impact on timelines and resources

Thanks!"
'''

negative_2 = '''
User Input:
title: "Sync call on your final round interview",\ndescription: "Just want to catch up on how the interview went"

Bad response:
"Hi [Recipient's Name],

Could you provide a brief update on the progress of the reports when you have a moment?

Specifically, I'm interested in:
* Completion percentage
* Any roadblocks you've encountered
* Estimated completion date

Thanks!"

Why it's bad:
Just using one of the training examples. Not changing the email body to model the user's request.

Good response to this:
"Hi [Candidate's Name],

I just want to link in with you about your final round interview. How do you think it went? Do you have any feedback or questions?

Kind regards,
[Your Name]"
'''

negative_3 = '''
User Input:
title: "Sync call on your final round interview",\ndescription: "Just want to catch up on how the interview went"

Bad response:
"
Here is the response email:
"Hi [Candidate's Name],

I just want to link in with you about your final round interview. How do you think it went? Do you have any feedback or questions?

Kind regards,
[Your Name]"

Why it's bad:
It prefaced the email with text. The response should only be an email.

Good response to this:
"Hi [Candidate's Name],

I just want to link in with you about your final round interview. How do you think it went? Do you have any feedback or questions?

Kind regards,
[Your Name]"
'''

negative_prompts = [negative_bg_prompt, negative_1, negative_2, negative_3]