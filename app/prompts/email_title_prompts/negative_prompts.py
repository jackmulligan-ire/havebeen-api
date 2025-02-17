negative_bg_prompt = "The following are some bad examples. Each has an email body, responses that you should avoid, why they're bad, and a good example."

negative_1 = '''
body: "Hi [Candidate's Name],

I just want to link in with you about your final round interview. How do you think it went? Do you have any feedback or questions?

Kind regards,
[Your Name]"

response to avoid:
Title: Final round interview

Why it's bad:
The response is prefaced with Title: The response should only be the actual title.

Correct response:
Final round interview
'''

negative_2 = '''
body: "Hi [Candidate's Name],

I just want to link in with you about your final round interview. How do you think it went? Do you have any feedback or questions?

Kind regards,
[Your Name]"

Response to avoid:
'Final round interview'

Why it's bad:
The response is wrapped in punctuation. The response should only be the actual title.

Correct response:
Final round interview
'''

negative_prompts = [negative_bg_prompt, negative_1, negative_2]