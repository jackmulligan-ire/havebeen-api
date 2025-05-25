example_bg_prompt = "Below are some examples of email bodies passed up by users, the modification requests, and the responses generated"

example_1 = '''
Email Body:
"Hi [Recipient's Name],\n\nI wanted to get your thoughts on the feedback we received for the Q3 roadmap.\n\nThere’ve been a few changes recommended in terms of the timing of features, with some new ones brought in for the quarter. Do you think the timelines for these are realistic?I’m not so sure…\n\nThere also seemed to be some questions around what we’re projecting out in terms of how many users would make use of the core feature we’re planning to deliver this quarter. Could you take a look at that and report back?n\nKind regards,\n[Your Name]"

Modification Request
- I'm writing this to the Chief Product Officer, could you adapt the tone for the audience?

Generated Response:
"
Dear [Recipient’s Name],

I’m looking to get your input on some feedback we received for the Q3 roadmap during the latest alignment meeting.

A request has been made to bring in additional features to the scope, but I’m having some concerns about whether we’ll be able to deliver on this by the end of the quarter. The BI team has also lowered their estimates for how many users would make use of the feature, although I’m not convinced by their analysis.

Would you mind reviewing the refined scope as well as the projections for the user adoption rate? You’ll find them attached. I’d really appreciate your input on this considering your depth of experience! Many thanks in advance.

Kind regards,
[Your Name]
"
'''

example_prompts = [
    example_bg_prompt, 
    example_1, 
]