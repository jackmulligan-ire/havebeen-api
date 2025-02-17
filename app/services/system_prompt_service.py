class SystemPromptService:
    def __init__(self, system_prompts):
        self.system_prompts= system_prompts

    def get_system_prompt(self):
        system_prompt_list = [prompt for sublist in self.system_prompts for prompt in sublist]
        system_prompt_string = "\n".join(system_prompt_list)
        return system_prompt_string