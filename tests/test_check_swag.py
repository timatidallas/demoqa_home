from pages.swag_labs import SwagLabs
def test_icon_exist(browser):
    demo_qa_page = SwagLabs(browser)
    demo_qa_page.visit()
    demo_qa_page.exit_icon()
    assert demo_qa_page.exit_icon()
    assert demo_qa_page.equal_url()