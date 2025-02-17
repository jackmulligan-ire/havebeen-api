task_bg_prompt = "The user will give you the title and description of a meeting setup in a calendar app."

task_desc_prompt = '''
  You have 2 goals
    - Take this title and description and turn it into the body of an email.
    - Replace the need for a call through the email. The email shouldn't invite the person to a call. It should replace the call with the email.
  '''
task_constraints_prompt = '''
The response should conform to the following constraints:
- Only the body of the email should be returned.
- The body of the email should just be returned as text.
- No other commentary before or after the email (e.g. Okay here you go, this is the email you would send in response)
- The email should be returned without any punctuation before-hand
'''


task_prompts = [task_bg_prompt, task_desc_prompt, task_constraints_prompt]