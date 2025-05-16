import pytest
from lesson_16.team_lead_class import *


def test_attributes():
    team_lead = TeamLead(name="Dmytro", salary=80000, department="AQA", programming_language="Python", team_size=3)
    assert hasattr(team_lead, "name"), "Attribute name is missing"
    assert hasattr(team_lead, "salary"),"Attribute salary is missing"
    assert hasattr(team_lead, "department"), "Attribute department is missing"
    assert hasattr(team_lead, "programming_language"), "Attribute programming_language is missing"
    assert hasattr(team_lead, "team_size"), "Attribute team_size is missing"
    return print(f"In {team_lead} all attributes are present")


if __name__ == "__main__":
    test_attributes()
