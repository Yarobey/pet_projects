from main import next_board_state, render


def check_next(init_state, expected_new_state, test_num):
    actual_next_state = next_board_state(init_state)
    if expected_new_state == actual_next_state:
        print(f"PASSED {test_num}")
    else:
        print(f"FAILED {test_num}")
        print("Expected:")
        render(expected_new_state)
        print("Got:")
        render(actual_next_state)
    return test_num+1


if __name__ == "__main__":
    test_num = 1
    # TEST 1: dead cells with no live neighbors
    # should stay dead.
    init_state1 = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]
    expected_next_state1 = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]

    test_num = check_next(init_state1, expected_next_state1, test_num)

    # TEST 2: dead cells with exactly 3 neighbors
    # should come alive.
    init_state2 = [
        [0,0,1],
        [0,1,1],
        [0,0,0]
    ]
    expected_next_state2 = [
        [0,1,1],
        [0,1,1],
        [0,0,0]
    ]
    test_num = check_next(init_state2, expected_next_state2, test_num)
