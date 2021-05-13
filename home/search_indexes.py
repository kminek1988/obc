
from accounts.models import Profil
from haystack import indexes


class ProfilIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.EdgeNgramField(document=True, use_template=True, template_name='search/indexes/home/profil_text.txt')
    # profesja = indexes.CharField(model_attr='profesja', null=True)
    # miasto = indexes.CharField(model_attr='miasto', null=True)
    #
    # profesja = indexes.CharField(model_attr='profesja')
    # miasto = indexes.CharField(model_attr='miasto')


    def get_model(self):
        return Profil

    def index_queryset(self, using=None):
        return self.get_model().objects.all()

