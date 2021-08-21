
from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self, username, email, password, **other_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **other_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password, **other_fields):
        if not email:
            raise ValueError('Enter an email address')
        if not username:
            raise ValueError('Enter a username')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **other_fields)
        user.set_password(password)
        user.is_superuser = True
        # user.is_staff = True
        user.is_active = True
        user.is_admin = True
        user.save(using=self._db)
        print(user)
        return user


class PostManager(BaseUserManager):
    print("post manager")

    def create_post(self, text, created_at, updated_at, user, **otherfields):
        post = self.model(text=text, created_at=created_at, updated_at=updated_at, user=user)
        post.save(using=self._db)
        return post
