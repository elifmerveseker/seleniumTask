import time

from pages.careers_page import CareersPage
from pages.home_page import HomePage
from pages.qa_career_page import QaCareerPage
from tests.base_test import BaseTest


class AdvancedAutomationPath(BaseTest):

    def test_check_advanced_automation_path(self):
        home_page = HomePage(self.driver)
        home_page.go_to_url(home_page.website_url)
        self.assertEqual(home_page.website_url, home_page.get_current_url(), 'You are not on Insider homepage.')
        home_page.hover_company_from_navigation_bar()
        home_page.click_careers_button()
        careers_page = CareersPage(self.driver)
        careers_page.verify_element_visibility(careers_page.OUR_LOCATIONS)
        self.assertTrue(careers_page.verify_element_visibility(careers_page.OUR_LOCATIONS),
                        "locations can not be found")
        self.assertTrue(careers_page.verify_element_visibility(careers_page.TEAMS), "teams can not be found")
        self.assertTrue(careers_page.verify_element_visibility(careers_page.LIFE_AT_INSIDER),
                        "life at insider can not be found")
        qa_career_page = QaCareerPage(self.driver)
        careers_page.go_to_url(qa_career_page.qa_website_url)
        self.assertIn(qa_career_page.qa_website_url, careers_page.get_current_url(), 'you are not on Qa page.')
        qa_career_page.click_see_all_jobs_button()
        time.sleep(10)
        qa_career_page.click_filter_by_location()
        qa_career_page.select_location_option(*qa_career_page.FILTER_OPTION_ISTANBUL_TURKIYE)
        self.assertEqual(qa_career_page.get_text(qa_career_page.FILTER_BY_DEPARTMENT),
                         qa_career_page.qa_department_text, 'QA department is not selected')
        self.assertTrue(qa_career_page.verify_element_visibility(qa_career_page.SHOWING_LISTING),
                        "Jobs are not listed")
        time.sleep(1)
        self.assertIn(qa_career_page.job_title_and_department, qa_career_page.get_job_title_text(),
                      "Job title does not include Quality Assurance")
        self.assertIn(qa_career_page.job_title_and_department, qa_career_page.get_job_department_text(),
                      "Job department does not include Quality Assurance")
        self.assertIn(qa_career_page.istanbul_turkey_location_text, qa_career_page.get_job_location_text(),
                      "Job location does not include Istanbul, Turkiye")
        qa_career_page.click_view_role()
        time.sleep(1)
        qa_career_page.switch_tab()
        self.assertIn(qa_career_page.lever_application, qa_career_page.get_current_url(),
                      "You are not on Lever Application form")
