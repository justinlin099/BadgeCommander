import ScanCode

def ScriptToHex(scriptPath):
    with open(scriptPath, 'r') as file:
        script = file.read()
    script = script.encode('utf-8')
    hexData = script.hex()
    return hexData