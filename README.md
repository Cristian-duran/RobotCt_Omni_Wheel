# RobotCt_Omni_Wheel
## Robotica2
### Nombres: Cristian Alejandro Durán Ignacio - Alfaro Ayzama José Fernando - Ever Rolando Rejas Espinoza
🚀 **Proyecto: Control de Ruedas Mecanum con Motoron**

💡 Este proyecto muestra cómo controlar un conjunto de cuatro ruedas mecanum omnidireccionales usando dos módulos Motoron I2C desde una Raspberry Pi (o cualquier host compatible con Python).

---

## 📌 Introducción

Utilizamos dos controladores Motoron (direcciones I2C `0x10` y `0x11`) para manejar cuatro motores con ruedas mecanum, logrando movimientos en cuatro direcciones: adelante, atrás, lateral derecha y lateral izquierda.  
La lógica de deslizamiento lateral aprovecha la configuración de los módulos:

- **Movimiento a la derecha**: ruedas derechas giran hacia adelante, ruedas izquierdas giran hacia atrás.  
- **Movimiento a la izquierda**: ruedas derechas giran hacia atrás, ruedas izquierdas giran hacia adelante.

---

## 🧰 Tecnologías y Librerías

- **Python 3**  
- **motoron** (driver I2C para módulos Motoron)  
- **time** (para temporización)
## 🚀 Para armado, instalación y ejecución de código
### Clonar el repositorio
bash
Copiar código
git clone https://github.com/Cristian-duran/RobotCt_Omni_Wheel
cd mecanum-control
Dependencias y librerías necesarias
🔧 Instalar todo de una:

bash
Copiar código
pip install -r requirements.txt
O, si prefieres instalar manual:

motoron

bash
Copiar código
pip install motoron

## ⚙️ Esquema de funcionamiento
Conecta ambos módulos Motoron a la Raspberry Pi vía I2C.

Ajusta las direcciones I2C en mecanum_control.py si fuese necesario:

python
Copiar código
MC1_ADDR = 0x10  # módulo controla motores 1 y 2 (izquierdas)
MC2_ADDR = 0x11  # módulo controla motores 3 y 4 (derechas)
Ajusta la velocidad base en la misma cabecera:

python
Copiar código
SPEED = 800  # rango de -máximo a +máximo
Ejecuta el script de demostración:

bash
Copiar código
python mecanum_control.py
Verás en consola la secuencia de movimientos:

Adelante (2 s)

Atrás (2 s)

Derecha (2 s)

Izquierda (2 s)

## 📌 Notas importantes
Asegúrate de que el bus I2C esté habilitado en tu Raspberry Pi (raspi-config).

La constante SPEED controla la potencia; prueba valores menores o mayores según el chasis y la carga.

Para integrar control por teclado, joystick o red, simplemente llama a las funciones move_forward(), move_backward(), strafe_right(), strafe_left() y stop_all() desde tu gestor de eventos o bucle principal.
