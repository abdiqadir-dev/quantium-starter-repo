from app import app

def test_header_exists(dash_duo):
    dash_duo.start_server(app)
    
    header = dash_duo.wait_for_element("h1", timeout=10)
    
    assert header.text == "Pink Morsel Sales Visualiser"

def test_visualization_exists(dash_duo):
    dash_duo.start_server(app)
    
    graph = dash_duo.wait_for_element("#sales-line-chart", timeout=10)
    
    assert graph.is_displayed()

def test_region_picker_exists(dash_duo):
    dash_duo.start_server(app)
    
    picker = dash_duo.wait_for_element("#region-filter", timeout=10)
    
    assert picker.is_displayed()