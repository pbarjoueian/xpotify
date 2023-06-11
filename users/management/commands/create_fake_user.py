from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    help = "create fake user with company"

    def handle(self, *args, **kwargs):
        user = User.objects.create_user(
            email="user@test.com",
            password="123456789",
            first_name="fake",
            last_name="user",
        )

        self.stdout.write(self.style.SUCCESS('Successfully created : "%s"' % user.id))
