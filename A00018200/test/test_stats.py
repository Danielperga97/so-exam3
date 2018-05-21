import sys
import pytest
sys.path.append('/home/so-exam3/A00018200')

from op_stats.stats import Stats
from op_stats.app import app

@pytest.fixture
def client():
    client = app.test_client()
    return client

def test_getCPU(mocker,client):
    mocker.patch.object(Stats,'get_cpu',return_value=80)
    response = client.get('v1/stats/cpu')
    assert response.data.decode('utf-8')=='{"cpu_percent": 80}'
    assert response.status_code == 200

def test_getMemory(mocker,client):
    mocker.patch.object(Stats,'get_memory',return_value=5000)
    response = client.get('v1/stats/memory')
    assert response.data.decode('utf-8')=='{"memory_percent": 5000}'
    assert response.status_code == 200

def test_getDisk(mocker,client):
    mocker.patch.object(Stats,'get_disk',return_value=30000)
    response = client.get('v1/stats/disk')
    assert response.data.decode('utf-8')=='{"disk_percent": 30000}'
    assert response.status_code == 200

