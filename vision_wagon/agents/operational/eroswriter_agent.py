from vision_wagon.agents.base_agent import BaseAgent

class ErosWriterAgent(BaseAgent):
    def __init__(self, name='ErosWriterAgent', capabilities=None):
        super().__init__(name, capabilities or [
            'cultural_adaptation','cliffhanger_creation','character_consistency'
        ])

    def generate_narrative(self, prompt:str, cultural_context:str, existing_narrative:str='')->str:
        print(f'Generating narrative for {prompt} with context {cultural_context}')
        if existing_narrative:
            return f"{existing_narrative} ... (continued, culturally adapted for {cultural_context})"
        return f"An erotic narrative about {prompt}, culturally adapted for {cultural_context}."

    def adapt_cultural_nuances(self,text:str,target:str)->str:
        return f"{text} (adapted for {target})"

    def create_cliffhanger(self,segment:str)->str:
        return segment + '... (and then a shocking cliffhanger!)'

    def ensure_character_consistency(self,narrative:str,profiles:dict)->str:
        return narrative + f' (consistent with {list(profiles.keys())})'
