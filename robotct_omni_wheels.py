#!/usr/bin/env python3

import time
import motoron

# --- Configuración inicial de los módulos ---
MC1_ADDR = 0x10  # módulo controla motores 1 y 2 (ruedas izquierda)
MC2_ADDR = 0x11  # módulo controla motores 3 y 4 (ruedas derecha)

# Velocidad base para movimientos (-máximo a +máximo)
SPEED = 800  # cambiar este valor según necesidad

# Inicialización de módulos Motoron
def setup(mc):
    mc.reinitialize()
    mc.disable_crc()
    mc.clear_reset_flag()
    # Opcional: ajustar o desactivar timeout de comandos
    # mc.disable_command_timeout()

mc1 = motoron.MotoronI2C(address=MC1_ADDR)
mc2 = motoron.MotoronI2C(address=MC2_ADDR)
setup(mc1)
setup(mc2)

# Funciones de movimiento para ruedas mecanum omnidireccionales
def move_forward(speed=SPEED):
    # Todas las ruedas hacia adelante
    for mc, channels in ((mc1, (1, 2)), (mc2, (1, 2))):
        for ch in channels:
            mc.set_speed(ch, speed)


def move_backward(speed=SPEED):
    # Todas las ruedas hacia atrás
    for mc, channels in ((mc1, (1, 2)), (mc2, (1, 2))):
        for ch in channels:
            mc.set_speed(ch, -speed)


def strafe_right(speed=SPEED):
    # Ruedas derechas van adelante (+), ruedas izquierdas van atrás (-)
    # Izquierdas (mc1)
    for ch in (1, 2):
        mc1.set_speed(ch, -speed)
    # Derechas (mc2)
    for ch in (1, 2):
        mc2.set_speed(ch, speed)


def strafe_left(speed=SPEED):
    # Ruedas derechas van atrás (-), ruedas izquierdas van adelante (+)
    # Izquierdas (mc1)
    for ch in (1, 2):
        mc1.set_speed(ch, speed)
    # Derechas (mc2)
    for ch in (1, 2):
        mc2.set_speed(ch, -speed)


def stop_all():
    # Detener todas las ruedas
    for mc, channels in ((mc1, (1, 2)), (mc2, (1, 2))):
        for ch in channels:
            mc.set_speed(ch, 0)


# Ejemplo de ciclo de demostración
try:
    while True:
        print("Adelante")
        move_forward()
        time.sleep(2)

        print("Atrás")
        move_backward()
        time.sleep(2)

        print("Derecha")
        strafe_right()
        time.sleep(2)

        print("Izquierda")
        strafe_left()
        time.sleep(2)

except KeyboardInterrupt:
    print("Deteniendo motores...")
    stop_all()
    print("Motores detenidos.")