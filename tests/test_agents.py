import pytest
from vision_wagon.agents.operational.eroswriter_agent import ErosWriterAgent
from vision_wagon.agents.operational.assembly_agent import AssemblyAgent
from vision_wagon.agents.executive.adult_compliance_agent import AdultComplianceAgent
from vision_wagon.agents.operational.traffic_capture_agent import TrafficCaptureAgent

@pytest.fixture
def eros_writer_agent():
    return ErosWriterAgent()

@pytest.fixture
def assembly_agent():
    return AssemblyAgent()

@pytest.fixture
def adult_compliance_agent():
    return AdultComplianceAgent()

@pytest.fixture
def traffic_capture_agent():
    return TrafficCaptureAgent()

def test_eros_writer_agent_capabilities(eros_writer_agent):
    assert eros_writer_agent.has_capability("cultural_adaptation")
    assert eros_writer_agent.has_capability("cliffhanger_creation")
    assert eros_writer_agent.has_capability("character_consistency")

def test_assembly_agent_assemble_multimedia_package(assembly_agent):
    pkg = assembly_agent.assemble_multimedia_package("story", ["img.jpg"], "audio.mp3")
    assert pkg["narrative"]=="story"
    assert pkg["metadata"]["age_rating"]=="18+"

def test_compliance(adult_compliance_agent):
    pkg = {"narrative":"safe story","metadata":{"age_rating":"18+"}}
    assert adult_compliance_agent.run_compliance_check(pkg,"US",["OnlyFans"])
