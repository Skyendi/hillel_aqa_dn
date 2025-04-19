import pytest
from homework_10.log_event import log_event, logs_reeder


class TestLogsPositive:
    with open('login_system.log', 'w', encoding='utf-8') as f:
        pass

    def test_status_success_positive(self):
        username = "Dima"
        status = "success"
        log_event(username, status)
        last_line = logs_reeder()

        assert status in last_line, f"status {status} is not in last_line"

    def test_status_expired_positive(self):
        username = "Dima"
        status = "expired"
        log_event(username, status)
        last_line = logs_reeder()

        assert status in last_line, f"status {status} is not in last_line"

    def test_status_failed_positive(self):
        username = "Dima"
        status = "failed"
        log_event(username, status)
        last_line = logs_reeder()

        assert status in last_line, f"status {status} is not in last_line"

    def test_username_positive(self):
        username = "Dima"
        status = "failed"
        log_event(username, status)
        last_line = logs_reeder()

        assert username in last_line, f"username {username} is not in last_line"


class TestLogsNegative:
    with open('login_system.log', 'w', encoding='utf-8') as f:
        pass

    def test_status_success_negative(self):
        username = "Dima"
        status = "success"
        log_event(username, status)
        last_line = logs_reeder()

        status = "expired"

        assert status not in last_line, f"status {status} is in last_line"

    def test_status_expired_negative(self):
        username = "Dima"
        status = "expired"
        log_event(username, status)
        last_line = logs_reeder()

        status = "success"

        assert status not in last_line, f"status {status} is in last_line"

    def test_status_failed_negative(self):
        username = "Dima"
        status = "failed"
        log_event(username, status)
        last_line = logs_reeder()

        status = "success"

        assert status not in last_line, f"status {status} is in last_line"

    def test_username_negative(self):
        username = "Dima"
        status = "failed"
        log_event(username, status)
        last_line = logs_reeder()
        username = "Lena"

        assert username not in last_line, f"username {username} is in last_line"
