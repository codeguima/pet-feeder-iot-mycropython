def conecta(ssid, senha):
    import network
    wifi = network.WLAN(network.STA_IF)
    if not wifi.isconnected():
        #print('connecting to network...')
        wifi.active(True)
        wifi.connect(ssid, senha)
        
        while not wifi.isconnected():
            pass
    #print('network config:', wifi.ifconfig())

    return wifi