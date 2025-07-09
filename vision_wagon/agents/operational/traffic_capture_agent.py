from vision_wagon.agents.base_agent import BaseAgent

class TrafficCaptureAgent(BaseAgent):
    def __init__(self,name='TrafficCaptureAgent',capabilities=None):
        super().__init__(name, capabilities or [
            'teaser_generation','social_media_posting','engagement_monitoring'
        ])

    def generate_teaser(self,package:dict)->str:
        snippet = package.get('narrative','').split('.')[0]
        return f'¡Prepárate! Un adelanto: {snippet}...'

    def social_media_posting(self,teaser:str,platform:str)->dict:
        print(f'Posting to {platform}')
        return {'status':'success','platform':platform,'post_url':f'http://{platform}.com/post/123'}

    def engagement_monitoring(self,post_url:str)->dict:
        return {'likes':100,'comments':10,'shares':5}
