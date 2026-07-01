from django.db import models

class MaszynyProdukcyjnaQuerySet(models.QuerySet):
    def urzadzenia_maszyny_po_nazwie(self,maszyna_nazwa):
        maszyna=self.filter(Maszyna_nazwa=maszyna_nazwa).first()
        if maszyna is None:
            return self.model.objects.none()
        return maszyna.urzadzenia_maszyny_produkcyjnej.all()
    
class MaszynaProdukcyjnaManager(models.Manager):
    def get_queryset(self):
        return MaszynyProdukcyjnaQuerySet(self.model,using=self._db)
    def urzadzenia_maszyny_po_nazwie_funkcja(self,maszyna_nazwa):
        return self.get_queryset().urzadzenia_maszyny_po_nazwie(maszyna_nazwa=maszyna_nazwa)