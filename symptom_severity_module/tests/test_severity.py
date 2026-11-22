"""Unit tests for the rule-based symptom severity prototype."""

import os
import sys

import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from src.severity_predictor import SymptomSeverityPredictor


@pytest.fixture
def predictor():
    return SymptomSeverityPredictor()


@pytest.mark.parametrize(
    ("symptoms", "expected"),
    [
        (["headache"], "Low Risk"),
        (["fatigue", "runny nose"], "Low Risk"),
        (["fever", "cough"], "Moderate Risk"),
        (["high fever", "body ache"], "Moderate Risk"),
        (["chest pain", "shortness of breath"], "High Risk"),
        (["confusion", "persistent high fever", "difficulty breathing"], "High Risk"),
    ],
)
def test_risk_categories(predictor, symptoms, expected):
    assert predictor.predict_severity(symptoms) == expected


def test_normalizes_whitespace_and_case(predictor):
    assert predictor.predict_severity(["  HEADACHE  "]) == "Low Risk"


def test_empty_or_unknown_symptoms_do_not_add_risk(predictor):
    assert predictor.predict_severity([]) == "Low Risk"
    assert predictor.predict_severity(["unlisted symptom"]) == "Low Risk"


def test_rejects_string_instead_of_symptom_list(predictor):
    with pytest.raises(TypeError):
        predictor.predict_severity("chest pain")


def test_rejects_non_string_symptom_values(predictor):
    with pytest.raises(TypeError):
        predictor.predict_severity(["headache", None])
