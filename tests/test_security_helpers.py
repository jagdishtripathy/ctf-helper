from modules.osint import OSINT
from modules.web_exploits import WebExploits


def test_csrf_token_material_is_random_and_sufficiently_long():
    generator = WebExploits()

    first = generator.generate_csrf_token()
    second = generator.generate_csrf_token()

    assert first != second
    assert len(first) >= 40


def test_shodan_lookup_requires_environment_key(monkeypatch):
    monkeypatch.delenv("SHODAN_API_KEY", raising=False)

    result = OSINT().search_shodan("8.8.8.8")

    assert "SHODAN_API_KEY" in result
    assert "not configured" in result


def test_geolocation_rejects_invalid_ip():
    result = OSINT().ip_geolocation("not-an-ip")

    assert result == "Invalid IP address."
