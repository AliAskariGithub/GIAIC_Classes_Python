import cal

def test_main() -> int:
    response1 : cal.add = cal.add(2, 3)
    assert response1 ==  5, "Expected 2 + 5 is equal to 5"
    response2 : cal.add = cal.add(0, 0)
    assert response2 ==  0, "Expected 0 + 0 is equal to 0"
    response3 : cal.add = cal.add(-1, -1)
    assert response3 ==  -2, "Expected -1 + -1 is equal to -2"