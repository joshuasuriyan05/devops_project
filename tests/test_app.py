# Ensure repo root is in sys.path for GitHub Actions
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.app import app

def test_homepage():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200

def test_appointments_page():
    client = app.test_client()
    response = client.get('/appointments')
    assert response.status_code == 200
