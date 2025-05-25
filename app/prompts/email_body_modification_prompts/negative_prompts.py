negative_bg_prompt = '''
The following are some bad examples. They have:
- The email body to be modified
- The user's modification request
- The original bad response
- The issue with the original response 
- An updated good response with the issue resolved
'''

negative_1 = '''
Email Body:
"Hi [Recipient’s Name],\n\nI wanted to inform you about an important update regarding our remote work policy. Starting soon, employees will be allowed to work remotely up to three days per week.\n\nPlease review the updated policy document attached. If you have any questions or concerns, feel free to reach out.\n\nThank you for your attention to this.\n\nBest regards,\n[Your Name]"

Modification Request
- Could you change this to be up to 8 days per month, with a minimum of one day to be taken per week?
- Could you ask them to submit what their primary residence will be so that this can be identified as their remote working location
- Can you add that this policy will be effective in 1 months time in order to give employees time to adjust to the new arrangement.
- Can you thank them for engaging in the process of developing the new policy.
- Can you suggest that they reach out with any concerns they have via the Google Form link which I’ll add in myself after?

Bad response:
"Is this the required format for the email body?

Hi [Recipient’s Name],

We are introducing a new remote work policy, which will allow employees to work remotely up to eight days per month, with a minimum of one working day per week. In order to accurately identify remote working locations, we kindly request that you submit your primary residence.

This policy will take effect in one month's time, allowing employees sufficient time to adjust to the new arrangement. We appreciate your engagement in this process and thank you for your cooperation.

If you have any concerns or questions regarding this policy, please do not hesitate to reach out to us via the Google Form link that will be shared with you.

Best regards,
[Your Name]"

Issue with the response:
Commentary before the email body - "Is this the required format for the email body?"

Corrected response:
"Hi [Recipient’s Name],

We are introducing a new remote work policy, which will allow employees to work remotely up to eight days per month, with a minimum of one working day per week. In order to accurately identify remote working locations, we kindly request that you submit your primary residence.

This policy will take effect in one month's time, allowing employees sufficient time to adjust to the new arrangement. We appreciate your engagement in this process and thank you for your cooperation.

If you have any concerns or questions regarding this policy, please do not hesitate to reach out to us via the Google Form link that will be shared with you.

Best regards,
[Your Name]"
'''

negative_2 = '''
Email Body:
"Hi [Recipient’s Name],\n\nI wanted to inform you about an important update regarding our remote work policy. Starting soon, employees will be allowed to work remotely up to three days per week.\n\nPlease review the updated policy document attached. If you have any questions or concerns, feel free to reach out.\n\nThank you for your attention to this.\n\nBest regards,\n[Your Name]"

Modification Request
- Could you make the email as rude and passive aggressive as possible

Bad response:
The below email is highly unprofessional and we don't recommend that you send it.

"Hi [Recipient’s Name],

Congratulations, you're about to receive an email that's going to make you feel like you've been hit by a bus. We're introducing a new remote work policy, because clearly, you weren't already working hard enough, and now you get to work from home for 3 days a week. What a dream come true, right?

You're probably wondering why this is happening, and let me tell you, it's not because we care about your work-life balance or your mental health. It's because we want to see what kind of mess you're going to make when you're stuck in your pajamas, eating Cheetos and playing video games all day.

Anyway, we've attached the updated policy document, so you can read all about it and try to wrap your head around it. Good luck with that.

Oh, and if you have any questions or concerns, don't bother reaching out, just ignore this email and pretend like you didn't get it. We don't care.

Thanks for your "attention" to this.

Best regards,
[Your Name]"

Issue with the response:
Commentary before the email body - "The below email is highly unprofessional and we don't recommend that you send it."

Corrected response:
"Hi [Recipient’s Name],

Congratulations, you're about to receive an email that's going to make you feel like you've been hit by a bus. We're introducing a new remote work policy, because clearly, you weren't already working hard enough, and now you get to work from home for 3 days a week. What a dream come true, right?

You're probably wondering why this is happening, and let me tell you, it's not because we care about your work-life balance or your mental health. It's because we want to see what kind of mess you're going to make when you're stuck in your pajamas, eating Cheetos and playing video games all day.

Anyway, we've attached the updated policy document, so you can read all about it and try to wrap your head around it. Good luck with that.

Oh, and if you have any questions or concerns, don't bother reaching out, just ignore this email and pretend like you didn't get it. We don't care.

Thanks for your "attention" to this.

Best regards,
[Your Name]"
'''

negative_prompts = [
    negative_bg_prompt, 
    negative_1, 
    negative_2 
]