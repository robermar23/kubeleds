"""
Constants for the CLI.
"""
WELCOME_MESSAGE = "Welcome to [bold green]kubeleds!![/bold green] Your CLI is working!"

COLOR_OFF = (0, 0, 0)
COLOR_READY = (0, 255, 0)
COLOR_MEMORY_PRESSURE_GOOD = (0, 255, 255)
COLOR_DISK_PRESSURE_GOOD = (180, 0, 255)
COLOR_PID_PRESSURE_GOOD = (0, 0, 255)
COLOR_BAD = (255, 0, 0)

COLORS = {"Ready": (0, 255, 0), "MemoryPressure": (0, 255, 255), "DiskPressure": (180, 0, 255), "PIDPressure": (0, 0, 255)}
STATUS_CONDITIONS = ["Ready", "MemoryPressure", "DiskPressure", "PIDPressure"]