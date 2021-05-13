from accounts.models import Profil


profil_index = Index('profile')
profil_index.settings(
    number_of_shards=1,
    number_of_replicas=0
)
@profil_index.doc_type
class ProfilDocument(DocType):
    profesja = fields.TextField(attr='profesja')

    class Django:
        model = Profil
        fields = [
            'imie',
            'nazwisko',
            'profesja',
            'miasto',
        ]