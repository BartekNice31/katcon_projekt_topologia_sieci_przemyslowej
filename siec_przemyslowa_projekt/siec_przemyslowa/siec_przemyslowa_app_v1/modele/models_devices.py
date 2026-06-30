from django.db import models

class TypUrzadzenia(models.IntegerChoices):
    #Sterowniki Siemens PLC Controllers
    # LOGO!
    LOGO_8 = 1, "LOGO! 8"
    LOGO_8_3 = 2, "LOGO! 8.3"

    # SIMATIC S7-200
    S7_200 = 10, "SIMATIC S7-200"
    S7_200_CN = 11, "SIMATIC S7-200 CN"

    # SIMATIC S7-200 SMART
    S7_200_SMART = 20, "SIMATIC S7-200 SMART"

    # SIMATIC S7-300
    S7_300 = 30, "SIMATIC S7-300"

    # SIMATIC S7-400
    S7_400 = 40, "SIMATIC S7-400"
    S7_400H = 41, "SIMATIC S7-400H"
    S7_400F = 42, "SIMATIC S7-400F"
    S7_400FH = 43, "SIMATIC S7-400FH"

    # SIMATIC S7-1200
    S7_1200 = 50, "SIMATIC S7-1200"
    S7_1200_G2 = 51, "SIMATIC S7-1200 G2"

    # SIMATIC S7-1500
    S7_1500 = 60, "SIMATIC S7-1500"
    S7_1500T = 61, "SIMATIC S7-1500T"
    S7_1500F = 62, "SIMATIC S7-1500F"
    S7_1500TF = 63, "SIMATIC S7-1500TF"
    S7_1500H = 64, "SIMATIC S7-1500H"
    S7_1500HF = 65, "SIMATIC S7-1500HF"
    S7_1500R = 66, "SIMATIC S7-1500R"
    S7_1500RF = 67, "SIMATIC S7-1500RF"

    # ET 200 CPU
    ET200SP_CPU = 70, "SIMATIC ET 200SP CPU"
    ET200PRO_CPU = 71, "SIMATIC ET 200pro CPU"
    ET200ECO_CPU = 72, "SIMATIC ET 200eco PN CPU"

    # Software Controllers
    S7_1500_SOFTWARE_CONTROLLER = 80, "SIMATIC S7-1500 Software Controller"
    WINAC = 81, "SIMATIC WinAC"

    # Open Controller
    S7_1500_OPEN_CONTROLLER = 90, "SIMATIC S7-1500 Open Controller"

    # Basic Panels
    KTP400_BASIC = 201, "KTP400 Basic"
    KTP700_BASIC = 202, "KTP700 Basic"
    KTP900_BASIC = 203, "KTP900 Basic"
    KTP1200_BASIC = 204, "KTP1200 Basic"

    # Comfort Panels
    TP700_COMFORT = 205, "TP700 Comfort"
    TP900_COMFORT = 206, "TP900 Comfort"
    TP1200_COMFORT = 207, "TP1200 Comfort"
    TP1500_COMFORT = 208, "TP1500 Comfort"
    TP1900_COMFORT = 209, "TP1900 Comfort"
    TP2200_COMFORT = 210, "TP2200 Comfort"

    KP700_COMFORT = 211, "KP700 Comfort"
    KP900_COMFORT = 212, "KP900 Comfort"
    KP1200_COMFORT = 213, "KP1200 Comfort"

    # Unified Comfort
    TP700_UNIFIED = 214, "Unified Comfort TP700"
    TP900_UNIFIED = 215, "Unified Comfort TP900"
    TP1200_UNIFIED = 216, "Unified Comfort TP1200"
    TP1500_UNIFIED = 217, "Unified Comfort TP1500"
    TP1900_UNIFIED = 218, "Unified Comfort TP1900"
    TP2200_UNIFIED = 219, "Unified Comfort TP2200"

    # Unified Basic
    MTP700_UNIFIED_BASIC = 220, "Unified Basic MTP700"
    MTP1000_UNIFIED_BASIC = 221, "Unified Basic MTP1000"

    # Mobile Panels
    MOBILE_PANEL_2ND_GEN = 222, "Mobile Panel 2nd Generation"
    MOBILE_PANEL_277 = 223, "Mobile Panel 277"

    # Key Panels
    KP8 = 224, "KP8"
    KP8F = 225, "KP8F"
    KP32F = 226, "KP32F"

    # Panel PC / IPC
    IPC127E = 227, "IPC127E"
    IPC227E = 228, "IPC227E"
    IPC427E = 229, "IPC427E"
    IPC477E = 230, "IPC477E Panel PC"
    IPC677E = 231, "IPC677E Panel PC"

    #skanery (czytniki kodów )
    # Keyence SR Series
    KEYENCE_SR700 = 301, "Keyence SR-700"
    KEYENCE_SR710 = 302, "Keyence SR-710"
    KEYENCE_SR750 = 303, "Keyence SR-750"
    KEYENCE_SR1000 = 304, "Keyence SR-1000"
    KEYENCE_SR1000W = 305, "Keyence SR-1000W"
    KEYENCE_SR2000 = 306, "Keyence SR-2000"
    KEYENCE_SR2000W = 307, "Keyence SR-2000W"

    # Keyence HR Series (ręczne)
    KEYENCE_HR50 = 308, "Keyence HR-50"
    KEYENCE_HR51 = 309, "Keyence HR-51"
    KEYENCE_HR52 = 310, "Keyence HR-52"

    # Cognex DataMan Series
    COGNEX_DATAMAN_150 = 320, "Cognex DataMan 150"
    COGNEX_DATAMAN_260 = 321, "Cognex DataMan 260"
    COGNEX_DATAMAN_262 = 322, "Cognex DataMan 262"
    COGNEX_DATAMAN_360 = 323, "Cognex DataMan 360"
    COGNEX_DATAMAN_370 = 324, "Cognex DataMan 370"
    COGNEX_DATAMAN_470 = 325, "Cognex DataMan 470"
    COGNEX_DATAMAN_475 = 326, "Cognex DataMan 475"
    COGNEX_DATAMAN_503 = 327, "Cognex DataMan 503"
    COGNEX_DATAMAN_8072 = 328, "Cognex DataMan 8072"

    # Cognex ręczne
    COGNEX_DATAMAN_8050 = 329, "Cognex DataMan 8050"
    COGNEX_DATAMAN_8050X = 330, "Cognex DataMan 8050X"
    COGNEX_DATAMAN_8700 = 331, "Cognex DataMan 8700" 

    # Festo servo

    URZADZENIE_NIEZNANE=1000,'Urządzenie nieznane' 