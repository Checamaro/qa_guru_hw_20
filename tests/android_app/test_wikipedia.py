from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


def test_search_paris():
    with step('Skip welcome screen'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_skip_button')).click()

    with step('Type search'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Поиск по Википедии')).click()
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_src_text')).type('paris')

    with step('Verify content found'):
        results = browser.all((AppiumBy.ID,
                               'org.wikipedia.alpha:id/page_list_item_title'))
        results.should(have.size_greater_than(0))
        results.first.should(have.text('Paris'))


def test_getting_started():
    with step('Checking 1 window'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).should(
            have.text("Свободная энциклопедия …более, чем на 300 языках"))

    with step('Tap Continue button'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()

    with step('Checking New way section'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).should(
            have.text('Новые способы исследований'))

    with step('Tap Continue button'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()

    with step('Checking Reading lists section'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).should(
            have.text('Списки для чтения с синхронизацией'))

    with step('Tap Continue button'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()

    with step('Checking Data and Privacy section'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).should(
            have.text('Данные и конфиденциальность'))

    with step('Tap Get started button'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_done_button')).click()

    with step('Checking Customize section'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/view_card_header_title')).should(
            have.text('Самое читаемое'))
