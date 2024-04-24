from typing import TypeVar

from django.db import models

DjangoModel = TypeVar("DjangoModel", bound=models.Model)


class ValidateModelMixin:
    """Make model.save() call model.full_clean()

    Warning: This should be the left-most mixin/super-class of a model,
    to ensure that its save() method is called fist (Python's MRO).

    Django's model.save() doesn't call full_clean() by default. More info:
    * "Why doesn't django's model.save() call full clean?"
        http://stackoverflow.com/questions/4441539/
    * "Model docs imply that ModelForm will call Model.full_clean(),
        but it won't."
        https://code.djangoproject.com/ticket/13100
    """

    def save(
        self: DjangoModel,
        force_insert: bool = False,
        force_update: bool = False,
        *args: bool | str | None,
        **kwargs: bool | str | None,
    ) -> None:
        """Override the save method to call full_clean before saving the model.

        Takes into account the force_insert and force_update flags, as they
        are passed to the save method when trying to skip the validation.
        Also passes on any positional and keyword arguments that were passed
        at the original call-site of the method.
        """
        # Only validate the model if the force-flags are not enabled
        if not (force_insert or force_update):
            self.full_clean()

        # Then save the model, passing in the original arguments
        super().save(force_insert, force_update, *args, **kwargs)  # type: ignore
