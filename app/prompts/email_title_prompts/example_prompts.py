example_bg_prompt = "Below are some examples of email bodies and the titles generated in response"

example_1 = '''
body: "Hi [Recipient's Name],\n\nHope that you’re doing well!\n\nHow have you been getting on with the report? Would you mind providing an update on your progress so far? Are there any blockers I can assist you with?\n\nWhat are you planning to work on next? Do you need input from anyone else or from me to complete the next part?\n\nAlso, just wanted to check that you’re on track to complete the report according to the agreed timeline.\n\nKind regards,\n[Your Name]"

Report Progress
'''

example_2 = '''
body: "Hi [Recipient's Name],\n\nWe need to understand what caused the website to go down today so we can prevent the same issue in the future. Could you please investigate what happened and provide a summary in an email?\n\nThank you also for restoring the website. It’d be best to document the steps taken so we can have a runbook on how to respond should the same happen in the future. Would you mind adding the steps you took to resolve the outage to our documentation?\n\nKind regards,\n[Your Name]"

Website Outage - Debrief
'''

example_3 = '''
body: "Hi [Recipient's Name],\n\nI wanted to check in on the progress of the marketing brief before we go to C-Level later this week.\n\nWould you mind providing a higher-level summary of the most important points covered in terms of the campaign objective, target audience and the key message? Could you also send over the timeline and budget we’re proposing for the campaign.\n\nHappier to discuss anything that’s not clear on a call..\n\nKind regards,\n[Your Name]"

Marketing brief update
'''

example_4 = '''
body: "Hi [Recipient's Name],\n\nI just wanted to check in with you about how your onboarding with the company has been so far.\n\nDo you have any questions about the processes you’ve been introduced to, or is anything unclear? Are you comfortable with the tools you’ve been shown?\n\nHow are you settling in with the team? If there are any catch-ups you’d like me to arrange with colleagues, please let me know.\n\nDon’t hesitate to reach out if you’re facing any challenges I can help with!\n\nKind regards,\n[Your Name]"

Onboarding - How's it going?
'''

example_5 = '''
body: "Hi [Recipient's Name],\n\nI wanted to get your thoughts on the feedback we received for the Q3 roadmap.\n\nThere’ve been a few changes recommended in terms of the timing of features, with some new ones brought in for the quarter. Do you think the timelines for these are realistic?I’m not so sure…\n\nThere also seemed to be some questions around what we’re projecting out in terms of how many users would make use of the core feature we’re planning to deliver this quarter. Could you take a look at that and report back?n\nKind regards,\n[Your Name]"

Q3 Product Roadmap - Please give your feedback.
'''

example_6 = '''
body: "Hi [Recipient’s Name],\n\nPlease send me a brief update on your current tasks and progress for this week. If there are any blockers or support you need, feel free to mention those as well.\n\nLooking forward to your update.\n\nKind regards,\n[Your Name]"

Weekly check-in
'''

example_7 = '''
body: "Hi [Recipient’s Name],\n\nPlease find attached the agenda for our upcoming meeting scheduled for early next week. Let me know if you have any additional points to add or if you’d like to raise the order being rearranged.\n\nThanks,\n[Your Name]"

Agenda - Final call for changes
'''

example_8 = '''
body: "Hi [Recipient’s Name],\n\nI wanted to inform you about an important update regarding our remote work policy. Starting soon, employees will be allowed to work remotely up to three days per week.\n\nPlease review the updated policy document attached. If you have any questions or concerns, feel free to reach out.\n\nThank you for your attention to this.\n\nBest regards,\n[Your Name]"

Changes to remote work policy.
'''

example_9 = '''
body: "Hi [Recipient’s Name],\n\nI wanted to provide an update on the current budget status for the project. We have spent approximately 60% of the allocated funds so far, and there are a few upcoming expenses to consider.\n\nPlease let me know if you have any questions or if you’d like me to provide a detailed breakdown.\n\nKind regards,\n[Your Name]"

Budget status
'''

example_10 = '''
body: "Hi [Recipient’s Name],\n\nI wanted to provide you with a detailed update on the planning progress for our launch event.\n\nVenue: I’m still awaiting confirmation from the venue, hopefully we hear back soon.\n\nInvitations: Invitations were sent out last week, and we’ve received a good response for this so far.\n\nSpeakers: The speaker list is nearly complete, with a few confirmations pending. We are actively following up to secure final commitments.\n\nLogistics: Catering options and audio-visual arrangements are being coordinated and will be finalized soon.\n\nMarketing: Promotional materials are in development and will be distributed next week to boost attendance.\n\nPlease let me know if you have any questions, suggestions, or if there are additional aspects you’d like us to cover as we move forward.\n\nKind regards,\n[Your Name]"

Launch Event - Progress Report
'''

example_prompts = [
  example_bg_prompt, 
  example_1, 
  example_2, 
  example_3, 
  example_4, 
  example_5,
  example_6,
  example_7,
  example_8,
  example_9,
  example_10
]