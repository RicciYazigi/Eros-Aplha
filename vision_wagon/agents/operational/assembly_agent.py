from vision_wagon.agents.base_agent import BaseAgent

class AssemblyAgent(BaseAgent):
    def __init__(self,name='AssemblyAgent',capabilities=None):
        super().__init__(name, capabilities or [
            'erotic_content_assembly','create_multimedia_erotic_content'
        ])

    def assemble_multimedia_package(self,narrative:str,image_urls:list[str],audio_url:str)->dict:
        print('Assembling multimedia package')
        return {
            'narrative': narrative,
            'images': image_urls,
            'audio': audio_url,
            'metadata': {'type':'NSFW','age_rating':'18+'}
        }

    def create_multimedia_erotic_content(self,text_input:str,visual_style:str,audio_style:str)->dict:
        generated_image='http://example.com/img.jpg'
        generated_audio='http://example.com/audio.mp3'
        return self.assemble_multimedia_package(text_input,[generated_image],generated_audio)
