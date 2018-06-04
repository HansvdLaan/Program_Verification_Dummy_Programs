from src.CommandCenter import CommandCenter


def test_1():
    print("-------- Start Test 0 --------\n")
    commandcenter = CommandCenter(10, 4)
    commandcenter.lock_target()
    commandcenter.fire_canon(0, 10 ,400)
    commandcenter.fire_canon(0, 60, 100)
    commandcenter.fire_canon(1, 20, 500)
    commandcenter.fire_canon(2, 20, 300)
    commandcenter.fire_canon(3, 80, 500)
    print("----------------------------\n\n")

test_1()