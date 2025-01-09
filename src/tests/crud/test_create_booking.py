import allure
import pytest
import logging    # This is used to print the messages or Logs

from src.helpers.api_requests_wrapper import post_request
from src.constants.api_constants import APIConstants
from src.helpers.payload_manager import payload_create_booking
from src.helpers.common_verification import *   # import all the verification
from src.utils.utils import Utils

class TestCreateBooking(object):

    @pytest.mark.positive
    @allure.title("Verify that Create Booking status and Booking Id should not be Null")
    @allure.description("Creating a Booking from Payload and verify that Booking Id should not be Null and Status Code should be 200 for the correct payload")
    def test_create_booking_positive(self):
        LOGGER = logging.getLogger(__name__)
        LOGGER.info("Starting the TestCase for TestCreate Booking")
        LOGGER.info("Post Request Started")
        response = post_request(
            url=APIConstants().url_create_booking(),
            auth= None,
            headers=Utils().common_headers_json(),
            payload=payload_create_booking(),
            in_json= False
        )
        LOGGER.info("Post Request Done")
        LOGGER.info("Now verify")
        verify_http_status_code(response_data=response,expected_data=200)
        LOGGER.info(response.json())
        LOGGER.info(response.json()["bookingid"])
        verify_json_key_not_null(response.json()["bookingid"])
        verify_json_key_greater_than_zero(response.json()["bookingid"])


    @pytest.mark.Negative
    @allure.title("Verify the Create Booking with invalid payload")
    @allure.description("Creating booking id, verify status code should be 500 for invalid payload")
    def test_create_booking_negative_tc1(self):
        response = post_request(
            url= APIConstants().url_create_booking(),
            auth= None,
            headers=Utils().common_headers_json(),
            payload={},
            in_json= False
        )
        verify_http_status_code(response_data=response, expected_data=500)

    @pytest.mark.Negative
    @allure.title("Verify the Create Booking with invalid payload")
    @allure.description("Creating booking id, verify status code should be 500 for invalid payload")
    def test_create_booking_negative_tc2(self):
        response = post_request(
            url= APIConstants().url_create_booking(),
            auth= None,
            headers=Utils().common_headers_json(),
            payload={"name": "Pratik"},
            in_json= False

        )
