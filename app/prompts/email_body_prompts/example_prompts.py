example_bg_prompt = "Below are some examples of calls passed up by the user and the emails generated in response"

example_1 = '''
"title: Quick sync on report progress\n description: Just want to quickly check in on the report progress."

"Hi [Recipient's Name],\n\nCould you provide a brief update on the progress of the reports when you have a moment?\n\nSpecifically, I'm interested in:\n* Completion percentage\n* Any roadblocks you've encountered\n* Estimated completion date\n\nThanks!\n[Your Name]"
'''

example_2 = '''
"title: Discuss website outage\n description: Need to understand what caused the website outage this morning."

  "Hi Team,\n\nTo help understand the cause of the website outage this morning, could you please share the following information:\n\n* Exact time of the outage\n* Steps taken to restore the website\n* Initial assessment of the cause\n* Any known impact on users\n\nThanks!\n[Your Name]"
'''

example_3 = '''
"title: Review marketing proposal\n description: Let's go over the marketing proposal before sending it to the client."

 "Hi [Recipient's Name],\n\nWould you mind taking a look at the marketing proposal and providing your feedback directly in the document [Link to Document]?\n\nI'm particularly interested in your thoughts on:\n* Overall clarity and persuasiveness\n* Accuracy of the data and claims\n* Alignment with the client's goals\n\nThanks!\n[Your Name]"
'''

example_4 = '''
"title: Acme Corp onboarding questions\n description: Just a quick chat to answer any outstanding questions the Acme Corp team has."

  "Hi Acme Corp Team,\n\nWe hope your onboarding is going smoothly! Please feel free to reply to this email with any questions you may have about the process.\n\nWe're happy to help in any way we can.\n\nThanks!\n[Your Name]"
'''

example_5 = '''
"title: Discuss Q3 roadmap feedback\n description: Need to discuss feedback received on the Q3 product roadmap."

  "Hi Team,\n\nTo facilitate a discussion around the feedback received on the Q3 product roadmap, please share your thoughts on the following:\n\n* Key areas of concern\n* Proposed solutions to address the feedback\n* Impact on timelines and resources\n\nThanks!\n[Your Name]"
'''

example_prompts = [example_bg_prompt, example_1, example_2, example_3, example_4, example_5]