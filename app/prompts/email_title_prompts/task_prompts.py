task_bg_prompt = '''
  The user will also give you the body of an email.

  You have 1 goal:
    - Take the body of an email and return a title for this email.

  The purpose of this task is to take some call information and create an email out of it.
  '''
task_constraints_prompt = '''
The response should conform to the following constraints:
- Only the title of the email should be returned.
- The title of the email should just be returned as text.
- The title shouldn't be longer than 100 characters.
- No other commentary before or after the email.
- The email should be returned without any punctuation before-hand.
'''

task_prompts = [task_bg_prompt, task_constraints_prompt]