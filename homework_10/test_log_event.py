import pytest
from homework_10.log_event import log_event, logs_reeder


class TestLogsPositive:
    with open('login_system.log', 'w', encoding='utf-8') as f:
        pass

    def test_status_success_positive(self):
        username = "Dima"
        status = "success"
        level = "INFO"
        log_event(username, status)
        last_line = logs_reeder()

        assert status in last_line, f"status {status} is not in last_line"
        assert level in last_line, f"level {level} is not in last_line"
        assert username in last_line, f"username {username} is not in last_line"


    def test_status_expired_positive(self):
        username = "Dima"
        status = "expired"
        level = "WARNING"
        log_event(username, status)
        last_line = logs_reeder()

        assert status in last_line, f"status {status} is not in last_line"
        assert level in last_line, f"level {level} is not in last_line"
        assert username in last_line, f"username {username} is not in last_line"

    def test_status_failed_positive(self):
        username = "Dima"
        status = "failed"
        level = "ERROR"
        log_event(username, status)
        last_line = logs_reeder()

        assert status in last_line, f"status {status} is not in last_line"
        assert level in last_line, f"level {level} is not in last_line"
        assert username in last_line, f"username {username} is not in last_line"



class TestLogsNegative:
    with open('login_system.log', 'w', encoding='utf-8') as f:
        pass

    def test_status_success_negative(self):
        username = "Dima"
        status = "success"
        level = "INFO"
        log_event(username, status)
        last_line = logs_reeder()

        status = "failed"
        level = "WARNING"
        username = "Lena"

        assert status not in last_line, f"status {status} is in last_line"
        assert level not in last_line, f"level {level} is in last_line"
        assert username not in last_line, f"username {username} is in last_line"

    def test_status_expired_negative(self):
        username = "Dima"
        status = "expired"
        level = "WARNING"
        log_event(username, status)
        last_line = logs_reeder()

        status = "success"
        level = "ERROR"
        username = "Lena"


        assert status not in last_line, f"status {status} is in last_line"
        assert level not in last_line, f"level {level} is in last_line"
        assert username not in last_line, f"username {username} is in last_line"

    def test_status_failed_negative(self):
        username = "Dima"
        status = "failed"
        level = "ERROR"
        log_event(username, status)
        last_line = logs_reeder()

        status = "success"
        level = "INFO"
        username = "Lena"

        assert status not in last_line, f"status {status} is in last_line"
        assert level not in last_line, f"level {level} is in last_line"
        assert username not in last_line, f"username {username} is in last_line"



