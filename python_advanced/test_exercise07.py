from python_advanced import exercise07 as exer

test_manager = exer.GraphicManager()

test_manager.add_graphic(exer.Graphic())
test_manager.add_graphic(exer.Graphic())
test_manager.add_graphic(exer.Graphic())
test_manager.add_graphic(exer.Graphic())
test_manager.add_graphic(exer.Graphic())

for item in test_manager:
    print(item)
