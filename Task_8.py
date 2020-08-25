import platform

my_system = platform.uname()

print(f"System-{my_system.system}")
print(f"Node-{my_system.node}")
print(f"Release-{my_system.release}")
print(f"Version-{my_system.version}")
print(f"Machine-{my_system.machine}")
print(f"Processor-{my_system.processor}")
print(f"system:{my_system.system}")