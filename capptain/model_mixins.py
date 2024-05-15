from typing import Iterable, Protocol, Self

class DjangoModel(Protocol):
    def save(
        self: Self,
        force_insert: bool = False,
        force_update: bool = False,
        using: str | None = "default",
        update_fields: Iterable[str] | None = None,
    ) -> None: ...

    def full_clean(
        self,
        exclude: Iterable[str] | None = None,
        validate_unique: bool = True,
        validate_constraints: bool = True,
    ) -> None: ...


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
        using: str | None = "default",  # DEFAULT_DB_ALIAS
        update_fields: Iterable[str] | None = None,
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

        # Type ignore, because even though mypy is correct that calling
        # save on super() here directly is not safe, we don't do that
        # in our codebase. Instead it's called on the instance using the
        # mixing. Ideally we'd use direct inheritance instead of a mixin,
        # so we can guarantee super.save exists. But Django's tabel names
        # rely on the first class inheriting models.Model being the last one.
        super().save(force_insert, force_update, using, update_fields)  # type: ignore[safe-super]
