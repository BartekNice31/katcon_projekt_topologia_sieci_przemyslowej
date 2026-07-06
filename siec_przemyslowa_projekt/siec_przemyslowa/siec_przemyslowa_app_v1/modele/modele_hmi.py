from django.db import models

class TypHMI(models.IntegerChoices):
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