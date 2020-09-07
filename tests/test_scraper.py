from web_scraper.scraper import get_citations_needed_count, get_citations_needed_report

def test_get_number_of_citation_needed():
    URL = "https://en.wikipedia.org/wiki/History_of_Mexico"
    actual = 5
    expected = get_citations_needed_count(URL)
    assert actual == expected

def test_get_report_of_citation_needed():
    URL = "https://en.wikipedia.org/wiki/History_of_Mexico"
    li1 = get_citations_needed_report(URL)
    assert "The first people to settle in Mexico encountered a climate far milder than the current one. In particular, the Valley of Mexico contained several large paleo-lakes (known collectively as Lake Texcoco) surrounded by dense forest. Deer were found in this area, but most fauna were small land animals and fish and other lacustrine animals were found in the lake region.[citation needed][7] Such conditions encouraged the initial pursuit of a hunter-gatherer existence.\n"
    assert "The first people to settle in Mexico encountered a climate far milder than the current one. In particular, the Valley of Mexico contained several large paleo-lakes (known collectively as Lake Texcoco) surrounded by dense forest. Deer were found in this area, but most fauna were small land animals and fish and other lacustrine animals were found in the lake region."
    assert "During the three centuries of colonial rule, fewer than 700,000 Spaniards, most of them men, settled in Mexico."