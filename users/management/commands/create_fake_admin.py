from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    help = "create fake admin with company"

    def handle(self, *args, **kwargs):
        user = User.objects.create_superuser(
            email="admin@test.com",
            password="123456789",
            first_name="fake",
            last_name="admin",
        )

        self.stdout.write(self.style.SUCCESS('Successfully created : "%s"' % user.id))
