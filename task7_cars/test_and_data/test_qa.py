import pytest
from framework.utils.other_utils.test_data import TestData
from test_and_data.pages.main_page import MainPage
from test_and_data.pages.research_page import ResearchPage
from test_and_data.pages.car_description_page import CarDescriptionPage
from test_and_data.pages.trim_comparison_page import TrimComparisonPage
from test_and_data.pages.side_by_side_copmare_page import SideBySideComparePage
from test_and_data.pages.car_comparison_page import ComparisonPage
from models.car import Car
from conftest import Logger

logger = Logger()


class TestCars:
    def test_one(self, driver):
        car1_make, car1_model, car1_year, car1_engine, car1_transmission = [None] * 5
        main_page = MainPage()
        research_page = ResearchPage()
        car_description_page = CarDescriptionPage()
        trim_comparison_page = TrimComparisonPage()
        logger.info("Start of CARS test")
        logger.info("Step1.Attempt to open main page")
        while not all([car1_make, car1_model, car1_year, car1_engine, car1_transmission]):
            assert main_page.wait_until_loaded_and_check_if_displayed(), "You are not on main page"
            logger.info("Step2.Trying to navigate to research page")
            main_page.click_on_research_button()
            assert research_page.wait_until_loaded_and_check_if_displayed(), "You are not on research page"
            logger.info("Step3.Trying to choose a random car and observe it")
            car1_make, car1_model, car1_year = research_page.car_selection_and_store_data()
            research_page.click_on_research_button()
            assert car_description_page.wait_until_loaded_and_check_if_displayed(), "You are not on car description page"
            logger.info("Step4.Attempt to go to trim comparison")
            car_description_page.go_to_trim_comparison()
            assert trim_comparison_page.wait_until_loaded_and_check_if_displayed(), "You are not on trim comparison page"
            trim_comparison_page.expand_model_info()
            logger.info("Step5.Getting car characteristics")
            car1_trim, car1_engine, car1_transmission = trim_comparison_page.get_some_characteristics()
            logger.info("Step6.Going to home page")
            trim_comparison_page.form.go_on_main_page()
            assert main_page.wait_until_loaded_and_check_if_displayed(), "You are not on main page"
            car_one = Car(car1_make, car1_model, car1_year, car1_trim, car1_engine, car1_transmission)
        car2_make, car2_model, car2_year, car2_engine, car2_transmission = [None] * 5
        while not all([car2_make, car2_model, car2_year, car2_engine, car2_transmission]):
            logger.info("Step2_2.Trying to navigate to research page")
            main_page.click_on_research_button()
            assert research_page.wait_until_loaded_and_check_if_displayed(), "You are not on research page"
            logger.info("Step3_2.Trying to choose a random car and observe it")
            car2_make, car2_model, car2_year = research_page.car_selection_and_store_data()
            research_page.click_on_research_button()
            assert car_description_page.wait_until_loaded_and_check_if_displayed(), "You are not on car description page"
            logger.info("Step4_2.Attempt to go to trim comparison")
            car_description_page.go_to_trim_comparison()
            assert trim_comparison_page.wait_until_loaded_and_check_if_displayed(), "You are not on trim comparison page"
            trim_comparison_page.expand_model_info()
            logger.info("Step5_2.Getting car characteristics")
            car2_trim, car2_engine, car2_transmission = trim_comparison_page.get_some_characteristics()
            car_two = Car(car2_make, car2_model, car2_year, car2_trim, car2_engine, car2_transmission)
        trim_comparison_page.form.go_to_research_page()
        logger.info("Step8.Going back research page")
        assert research_page.wait_until_loaded_and_check_if_displayed(), "You are not on research page"
        research_page.go_to_side_comparing_page()
        side_by_side_compare_page = SideBySideComparePage()
        logger.info("Step9.Checking if side compare page opened")
        assert side_by_side_compare_page.wait_until_loaded_and_check_if_displayed(), "You are not side by side" \
                                                                                     "compare page"
        side_by_side_compare_page.click_on_first_car_row()
        side_by_side_compare_page.add_car_to_compare(car_one.get_make(), car_one.get_model(), car_one.get_year(),
                                                     car_one.get_trim())
        logger.info("Step10.Checking if car one added to comparison")
        test_data = TestData("test_data.json")
        closing_timer = test_data.get_data("closing_timer")
        assert side_by_side_compare_page.is_car_one_chosen(closing_timer), "Car one is not added to comparison"
        side_by_side_compare_page.click_on_second_car_row()
        side_by_side_compare_page.add_car_to_compare(car_two.get_make(), car_two.get_model(), car_two.get_year(),
                                                     car_two.get_trim())
        logger.info("Step11.Checking that both cars were added")
        assert side_by_side_compare_page.is_car_two_chosen(closing_timer), "Car two is not added to comparison"
        side_by_side_compare_page.go_to_comparison_page()
        comparison_page = ComparisonPage()
        assert comparison_page.wait_until_loaded_and_check_if_displayed(), "You are not on comparison page"
        logger.info("Step12.Checking if options are the same")
        assert (car_one.get_engine(),
                car_one.get_transmission()) == comparison_page.get_first_car_options(), "Not same options of car one"
        assert (car_two.get_engine(),
                car_two.get_transmission()) == comparison_page.get_second_car_options(), "Not same options of car two"


if __name__ == "__main__":
    pytest.main()
