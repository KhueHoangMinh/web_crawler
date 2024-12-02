from django.db import models
from selenium.webdriver.common.by import By
from django.contrib.postgres.fields import ArrayField


class Domain(models.Model):

    name = models.CharField(max_length=255)
    domain = models.CharField(max_length=255, unique=True)
    start_url = models.CharField(max_length=255)
    enable = models.BooleanField(default=False)


    class SelectorType(models.TextChoices):
        XPATH = By.XPATH, 'XPath'
        CLASSNAME = By.CLASS_NAME, 'Classname'
        CSS_SELECTOR = By.CSS_SELECTOR, 'CSS Selector'
        NAME = By.NAME, 'Name'
        ID = By.ID, 'ID'

    url_container_elements_type = models.CharField(
        max_length=20,
        choices=SelectorType.choices,
        null=True,
        blank=True
    )
    url_container_elements_property = ArrayField(models.CharField(max_length=255), default=list)

    title_type = models.CharField(
        max_length=20,
        choices=SelectorType.choices,
        null=True,
        blank=True
    )
    title_property = models.CharField(max_length=255, null=True, blank=True)

    images_type = models.CharField(
        max_length=20,
        choices=SelectorType.choices,
        null=True,
        blank=True
    )
    images_property = models.CharField(max_length=255, null=True, blank=True)

    brand_type = models.CharField(
        max_length=20,
        choices=SelectorType.choices,
        null=True,
        blank=True
    )
    brand_property = models.CharField(max_length=255, null=True, blank=True)

    price_type = models.CharField(
        max_length=20,
        choices=SelectorType.choices,
        null=True,
        blank=True
    )
    price_property = models.CharField(max_length=255, null=True, blank=True)

    type_type = models.CharField(
        max_length=20,
        choices=SelectorType.choices,
        null=True,
        blank=True
    )
    type_property = models.CharField(max_length=255, null=True, blank=True)

    transmission_type = models.CharField(
        max_length=20,
        choices=SelectorType.choices,
        null=True,
        blank=True
    )
    transmission_property = models.CharField(max_length=255, null=True, blank=True)

    engine_type = models.CharField(
        max_length=20,
        choices=SelectorType.choices,
        null=True,
        blank=True
    )
    engine_property = models.CharField(max_length=255, null=True, blank=True)

    seats_type = models.CharField(
        max_length=20,
        choices=SelectorType.choices,
        null=True,
        blank=True
    )
    seats_property = models.CharField(max_length=255, null=True, blank=True)

    gearbox_type = models.CharField(
        max_length=20,
        choices=SelectorType.choices,
        null=True,
        blank=True
    )
    gearbox_property = models.CharField(max_length=255, null=True, blank=True)

    date_type = models.CharField(
        max_length=20,
        choices=SelectorType.choices,
        null=True,
        blank=True
    )
    date_property = models.CharField(max_length=255, null=True, blank=True)

    odo_type = models.CharField(
        max_length=20,
        choices=SelectorType.choices,
        null=True,
        blank=True
    )
    odo_property = models.CharField(max_length=255, null=True, blank=True)

    contact_type = models.CharField(
        max_length=20,
        choices=SelectorType.choices,
        null=True,
        blank=True
    )
    contact_property = models.CharField(max_length=255, null=True, blank=True)

    description_type = models.CharField(
        max_length=20,
        choices=SelectorType.choices,
        null=True,
        blank=True
    )
    description_property = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.name


class Cache(models.Model):
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE, related_name='caches')
    url = models.CharField(max_length=255, unique=True)
    status = models.BooleanField(default=False)
    visited = models.BooleanField(default=False)

    def __str__(self):
        return self.url


class Property(models.Model):
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE, related_name='properties')
    cache = models.ForeignKey(Cache, on_delete=models.CASCADE, related_name='caches')
    title = models.CharField(max_length=2048)
    images = ArrayField(models.CharField(max_length=2048, null=False, blank=False), default=list)
    brand = models.CharField(max_length=2048, null=True, blank=True)
    price = models.CharField(max_length=2048)
    type = models.CharField(max_length=2048, null=True, blank=True)
    transmission = models.CharField(max_length=2048, null=True, blank=True)
    engine = models.CharField(max_length=2048, null=True, blank=True)
    seats = models.CharField(max_length=2048, null=True, blank=True)
    gearbox = models.CharField(max_length=2048, null=True, blank=True)
    date = models.CharField(max_length=2048, null=True, blank=True)
    odo = models.CharField(max_length=2048, null=True, blank=True)
    contact = models.CharField(max_length=2048, null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.title
