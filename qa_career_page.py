import time

from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class QaCareerPage(BasePage):
    SEE_ALL_QA_JOBS_BUTTON = (By.LINK_TEXT, 'See all QA jobs')
    FILTER_BY_LOCATION = (By.ID, 'select2-filter-by-location-container')
    FILTER_OPTION_ISTANBUL_TURKIYE = (By.CSS_SELECTOR, '.select2-results__option:nth-of-type(2)')
    FILTER_BY_DEPARTMENT = (By.ID, 'select2-filter-by-department-container')
    SHOWING_LISTING = (By.CLASS_NAME, 'currentResult')
    JOB_TITLE = (By.CSS_SELECTOR, '.position-title')
    JOB_DEPARTMENT = (By.CSS_SELECTOR, '.position-department')
    JOB_LOCATION = (By.CSS_SELECTOR, '.position-location')
    JOB_LIST = (By.CSS_SELECTOR, '.position-list-item')
    VIEW_ROLE_BUTTON = (By.LINK_TEXT, 'View Role')
    qa_website_url = 'https://useinsider.com/careers/quality-assurance/'
    istanbul_turkey_location_text = 'Istanbul, Turkiye'
    qa_department_text = '×\nQuality Assurance'
    job_title_and_department = 'Quality Assurance'
    lever_application = 'lever'

    def click_see_all_jobs_button(self):
        self.click_element(*self.SEE_ALL_QA_JOBS_BUTTON)

    def click_filter_by_location(self):
        self.click_element(*self.FILTER_BY_LOCATION)

    def select_location_option(self, *location_element):
        self.click_element(*location_element)

    def get_job_title_text(self):
        job_title_text = self.get_text(self.JOB_TITLE)
        return job_title_text

    def get_job_department_text(self):
        job_department_text = self.get_text(self.JOB_DEPARTMENT)
        return job_department_text

    def get_job_location_text(self):
        job_location_text = self.get_text(self.JOB_LOCATION)
        return job_location_text

    def click_view_role(self):
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight * 0.3);")
        time.sleep(1)
        self.hover_element(*self.JOB_TITLE)
        time.sleep(1)
        self.click_element(*self.VIEW_ROLE_BUTTON)

    def switch_tab(self):
        new_url = self.driver.window_handles[1]
        self.driver.switch_to.window(new_url)
