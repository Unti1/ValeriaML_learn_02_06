# Глобальная область
s = 10

def func():
    # Локальная область
    s = 20
    def func2():
        s = 30
        print(locals())
        
    func2()
    print(locals())
        
print(globals())
print()
print()
func()