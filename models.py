from peewee import Model, SqliteDatabase, CharField, TextField

db = SqliteDatabase('translations.db') #object relationship mapper

class TranslationModel(Model): #client sends text, langugae they want to translate from and to
    text = TextField()
    base_lang = CharField()
    final_lang = CharField()
    translation = TextField(null=True)

    class Meta:
        database = db

db.create_tables([TranslationModel])
