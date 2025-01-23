# Alimentador Automático para Animais de Estimação (IoT)

Este projeto envolve o desenvolvimento de um alimentador automático para animais de estimação utilizando o **ESP32** e programado em **MicroPython**. O sistema é projetado para facilitar a alimentação de animais de estimação, permitindo o controle remoto e a automação das refeições.

## 📋 Funcionalidades

- **Conexão Wi-Fi**: O sistema se conecta a uma rede Wi-Fi para comunicação remota.
- **Integração com Firebase**: Armazena e sincroniza os dados no Firebase para acesso em tempo real.
- **Display LCD 20x4**: Exibe informações em tempo real sobre o status do alimentador.
- **Controle Remoto**: Permite o controle do alimentador através de um aplicativo móvel.
- **Automação de Alimentação**: Configurações de horários e porções para alimentar os animais de estimação automaticamente.

## 🛠️ Tecnologias Utilizadas

- **Microcontrolador**: ESP32
- **Linguagem de Programação**: MicroPython
- **Banco de Dados**: Firebase
- **Display**: LCD 20x4
- **Conectividade**: Wi-Fi

## 📦 Requisitos

- **Hardware**:
  - ESP32
  - Display LCD 20x4
  - Servo motor para controle da alimentação
  - Conexão Wi-Fi
  - Fonte de alimentação para o ESP32

- **Software**:
  - MicroPython instalado no ESP32
  - Firebase para armazenamento de dados
  - Aplicativo móvel para controle (pode ser desenvolvido usando frameworks como React Native ou Flutter)

## 🧑‍💻 Como Rodar o Projeto

### 1. Configuração do Hardware

1. **Conecte o ESP32**: Conecte o ESP32 à sua placa de alimentação e conecte o display LCD 20x4 ao ESP32.
2. **Servo Motor**: Conecte o servo motor para controlar a liberação da ração.

### 2. Configuração do Software

1. **Instalar MicroPython**: Instale o MicroPython no ESP32. Siga as instruções do [site oficial do MicroPython](https://micropython.org/download/esp32/) para instalar a firmware.
2. **Instalar Dependências**: Instale as bibliotecas necessárias para o display LCD e a comunicação com o Firebase. 
   
   Exemplo:
   ```python
   import network
   import machine
   import time
   from lcd import LCD
   from firebase import Firebase
