import CSP_6_02_reading_files as HW

def test_longest_line():
    assert HW.longestLine("CSP_6_02_test_file.txt") == "I like listening to music\n"

def test_to_binary():
    assert HW.toBinary("CSP_6_02_binary_file.txt") == ["0101", "1110", "0000"]