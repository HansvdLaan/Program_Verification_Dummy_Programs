from src.battleship.CommandCenter import CommandCenter


def test_1():
    print("-------- Start Test 0 --------\n")
    commandcenter = CommandCenter(10)
    commandcenter.lock_target()
    commandcenter.fire_canon(0, 10)
    commandcenter.fire_canon(60, 100)
    commandcenter.fire_canon(20, 500)
    commandcenter.fire_canon(20, 300)
    commandcenter.fire_canon(80, 500)
    print("----------------------------\n\n")

test_1()