from vision_wagon.agents.base_agent import BaseAgent

class AdultComplianceAgent(BaseAgent):
    def __init__(self,name='AdultComplianceAgent',capabilities=None):
        super().__init__(name, capabilities or [
            'age_verification_meta_check','jurisdiction_filter','platform_policy_check'
        ])

    def age_verification_meta_check(self,age_rating:str)->bool:
        return age_rating=='18+'

    def jurisdiction_filter(self,package:dict,jurisdiction:str)->bool:
        if jurisdiction=='Germany' and 'explicit sexual act' in package.get('narrative','').lower():
            return False
        return True

    def platform_policy_check(self,package:dict,policies:list[str])->bool:
        for p in policies:
            if p.lower() in package.get('narrative','').lower():
                return True
        return True

    def run_compliance_check(self,package:dict,target_jurisdiction:str,platform_policies:list[str])->bool:
        if not self.age_verification_meta_check(package.get('metadata',{}).get('age_rating')):
            return False
        if not self.jurisdiction_filter(package,target_jurisdiction):
            return False
        if not self.platform_policy_check(package,platform_policies):
            return False
        return True
