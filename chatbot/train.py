from django.core.management.base import BaseCommand, CommandError

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

class Command(BaseCommand):
    help = 'Train the chatbot with a corpus'

    def handle(self, *args, **options):
        chatbot = ChatBot(
            'ChatBot name from settings.py CHATTERBOT',
            storage_adapter='chatterbot.storage.DjangoStorageAdapter',
        )

        trainer = ChatterBotCorpusTrainer(chatbot)
        trainer.train(
            "chatterbot.corpus.english"
        )

        self.stdout.write(self.style.SUCCESS('Successfully trained!'))