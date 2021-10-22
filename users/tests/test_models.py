from django.test import TestCase
from django.contrib.auth import get_user_model
from users.models import Profile


USER = get_user_model()


class TestCustomUser(TestCase):
    @classmethod
    def setUpTestData(cls):
        USER.objects.create(
                username="user",
                email="email@email.com",
                first_name="usern",
                last_name="lname",
                role="Student"
                )

    def test_username(self):
        user = USER.objects.get(username="user")
        username = user.username
        self.assertEqual(username, "user")

    def test_role_verbose_name(self):
        user = USER.objects.get(username="user")
        verbose_name = user._meta.get_field("role").verbose_name
        self.assertEqual(verbose_name, 'Role of User')

    def test___str__(self):
        user = USER.objects.get(username="user")
        self.assertEqual(str(user), 'usern lname')


class TestProfile(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = USER.objects.create(
                username="user",
                email="email@email.com",
                first_name="usern",
                last_name="lname",
                role="Student"
                )
        Profile.objects.get_or_create(
                user=user,
                title="Test Driven Development",
                description="Code without test is bad design",
                tags=["django", "python", "postgresql"],
                languages=["nepali", "hindi", "english"],
                )

    def test_user_of_profile(self):
        user = USER.objects.get(username="user")
        profile = Profile.objects.get(user=user)
        profile_username = profile.user.username
        self.assertEqual(user.username, profile_username)

    def test_tags(self):
        user = USER.objects.get(username="user")
        tags = user.profile.tags
        self.assertEqual(type(tags), type([]))
        self.assertEqual(len(tags), 3)

    def test_avatar_name(self):
        user = USER.objects.get(username="user")
        avatar_name = f"https://ui-avatars.com/api/?name={user.first_name}+{user.last_name}&background=0D8ABC&color=fff"
        self.assertEqual(user.profile.avatar, avatar_name)
