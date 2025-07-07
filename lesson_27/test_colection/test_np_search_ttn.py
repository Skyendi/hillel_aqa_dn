import time

import pytest

from lesson_27.np_page_objects.search_page_np import NovaPoshtaSearchObj
from lesson_27.np_page_objects.result_np_page import ResultPage

from lesson_27.conftest import np_tracking


class TestSearchTTN:

    def test_nova_poshta_search_ttn_(self, np_tracking):
        np_tracking.open()

        np_tracking.input_search_ttn("20400461262522")

        result_np_page: ResultPage = np_tracking.click_search_button()
        result_np_page.ok_banner_button.click()
        assert "Отримана" in result_np_page.status.text
