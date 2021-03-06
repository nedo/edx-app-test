# coding=utf-8
"""
    Course Dashboard Test Module
"""

from tests.android.pages.android_main_dashboard import AndroidMainDashboard
from tests.android.pages.android_whats_new import AndroidWhatsNew
from tests.android.pages.android_my_courses_list import AndroidMyCoursesList
from tests.android.pages.android_course_dashboard import AndroidCourseDashboard
from tests.common import strings
from tests.common.globals import Globals


class TestAndroidCourseDashboard:
    """
    Course Dashboard screen's Test Case

    """

    def test_start_main_dashboard_smoke(self, login, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify Main Dashboard screen is loaded successfully after successful login
        """

        global_contents = Globals(setup_logging)
        setup_logging.info('-- Starting {} Test Case'.format(TestAndroidCourseDashboard.__name__))
        if login:
            setup_logging.info('{} is successfully logged in'.format(global_contents.login_user_name))

        android_whats_new_page = AndroidWhatsNew(set_capabilities, setup_logging)
        android_whats_new_page.navigate_features()
        assert android_whats_new_page.navigate_features().text == strings.WHATS_NEW_DONE
        assert android_whats_new_page.exit_features() == Globals.MAIN_DASHBOARD_ACTIVITY_NAME

    def test_ui_elements_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
        Verify that Course Dashboard tab will show following contents,
        Header contents,
            Back icon,
            Specific "<course name>" as Title, Share icon, Course,
        Verify that user should be able to go back by clicking Back icon
        Verify that user should be able to view these Course contents:
            Course Image, Course Name, Course Provider, Course Ending date,
            Last accessed(if any), Course Content,
        Verify all screen contents have their default values
        """

        global_contents = Globals(setup_logging)
        android_course_dashboard_page = AndroidCourseDashboard(set_capabilities, setup_logging)
        android_my_courses_list_page = AndroidMyCoursesList(set_capabilities, setup_logging)
        android_main_dashboard_page = AndroidMainDashboard(set_capabilities, setup_logging)

        assert android_main_dashboard_page.load_courses_tab()
        if android_my_courses_list_page.get_my_courses_list_row():
            course_name = android_my_courses_list_page.get_first_course().text
            android_my_courses_list_page.get_first_course().click()
        else:
            setup_logging.info('No course enrolled by this user.')

        assert android_course_dashboard_page.get_navigation_icon().get_attribute('content-desc') \
            == strings.COURSE_DASHBOARD_NAVIGATION_ICON
        android_course_dashboard_page.get_navigation_icon().click()
        assert android_main_dashboard_page.on_screen() == global_contents.MAIN_DASHBOARD_ACTIVITY_NAME
        android_my_courses_list_page.load_course_details_screen()

        if course_name:
            # Verifing the title of the screen
            assert android_course_dashboard_page.get_all_text_views()[0].text in course_name

        assert android_course_dashboard_page.get_course_share_icon().get_attribute('content-desc') \
            == strings.COURSE_DASHBOARD_SHARE_COURSE
        assert android_course_dashboard_page.get_course_image()
        # verifing course name that is overlapping the course image
        assert android_course_dashboard_page.get_course_name().text in course_name
        assert android_course_dashboard_page.get_course_date()
        assert android_course_dashboard_page.get_course_last_access_row()
        assert android_course_dashboard_page.get_course_content_header()

    def test_load_contents_smoke(self, set_capabilities, setup_logging):
        """
        Scenarios:
            Verify on tapping "Videos" tab will load Videos screen
            Verify on tapping "Discussion" tab will load Discussions screen
            Verify on tapping "Dates" tab will load Dates screen
            Verify on tapping "Resources" tab will load Resources list
            Verify on tapping "Handouts" tab will load Handouts screen
            Verify on tapping "Announcements" tab will load Announcements screen
        """

        android_course_dashboard_page = AndroidCourseDashboard(set_capabilities, setup_logging)

        video_tab_element = android_course_dashboard_page.get_videos_tab()
        if video_tab_element:
            video_tab_element.click()
            assert video_tab_element.get_attribute('selected') == 'true'

        discussion_tab_element = android_course_dashboard_page.get_discussion_tab()
        if discussion_tab_element:
            discussion_tab_element.click()
            assert discussion_tab_element.get_attribute('selected') == 'true'

        dates_tab_element = android_course_dashboard_page.get_dates_tab()
        if dates_tab_element:
            dates_tab_element.click()
            assert dates_tab_element.get_attribute('selected') == 'true'

        resources_tab_element = android_course_dashboard_page.get_resources_tab()
        if resources_tab_element:
            resources_tab_element.click()
            assert resources_tab_element.get_attribute('selected') == 'true'

        course_tab_element = android_course_dashboard_page.get_course_tab()
        if course_tab_element:
            course_tab_element.click()
            assert course_tab_element.get_attribute('selected') == 'true'

        setup_logging.info('-- Ending Test Case --')
