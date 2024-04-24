class ValidateModelMixin(object):
    """Make model.save() call model.full_clean()

    Warning: This should be the left-most mixin/super-class of a model.

    Django's model.save() doesn't call full_clean() by default. More info:
    * "Why doesn't django's model.save() call full clean?"
        http://stackoverflow.com/questions/4441539/
    * "Model docs imply that ModelForm will call Model.full_clean(),
        but it won't."
        https://code.djangoproject.com/ticket/13100
    """

    def save(self, *args, **kwargs):
        self.full_clean()
        super(ValidateModelMixin, self).save(*args, **kwargs)
