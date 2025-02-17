example_bg_prompt = "Below are some examples of email bodies and the titles generated in response"

example_1 = '''
body: Hi [Recipient's Name],\n\nCould you provide a brief update on the progress of the reports when you have a moment?\n\nSpecifically, I'm interested in:\n* Completion percentage\n* Any roadblocks you've encountered\n* Estimated completion date\n\nThanks!\n[Your Name]"

Quick sync on report progress
'''

example_2 = '''
body: "Hi Team,\n\nTo help understand the cause of the website outage this morning, could you please share the following information:\n\n* Exact time of the outage\n* Steps taken to restore the website\n* Initial assessment of the cause\n* Any known impact on users\n\nThanks!\n[Your Name]"

Looking for information about the website outage this morning.
'''

example_3 = '''
body: "Hi [Recipient's Name],\n\nWould you mind taking a look at the marketing proposal and providing your feedback directly in the document [Link to Document]?\n\nI'm particularly interested in your thoughts on:\n* Overall clarity and persuasiveness\n* Accuracy of the data and claims\n* Alignment with the client's goals\n\nThanks!\n[Your Name]"

Marketing proposal review
'''

example_4 = '''
body: "Hi Acme Corp Team,\n\nWe hope your onboarding is going smoothly! Please feel free to reply to this email with any questions you may have about the process.\n\nWe're happy to help in any way we can.\n\nThanks!\n[Your Name]"

Your onboarding with us
'''

example_5 = '''
body: "Hi Team,\n\nTo facilitate a discussion around the feedback received on the Q3 product roadmap, please share your thoughts on the following:\n\n* Key areas of concern\n* Proposed solutions to address the feedback\n* Impact on timelines and resources\n\nThanks!\n[Your Name]"

Please give your feedback on the Q3 product roadmap.
'''

example_prompts = [example_bg_prompt, example_1, example_2, example_3, example_4, example_5]