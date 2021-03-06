from django.db import models


class Category(models.Model):
    name = models.CharField("Nome", max_length=100)
    slug = models.SlugField("Identificador", max_length=100)
    created = models.DateTimeField("criado em", auto_now_add=True)
    modified = models.DateTimeField("atualizado em", auto_now=True)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField("Nome", max_length=100)
    slug = models.SlugField("Identificador", max_length=100)
    category = models.ForeignKey(
        "catalog.Category", verbose_name="Categoria", on_delete=models.CASCADE
    )
    description = models.TextField("Descrição", blank=True)
    price = models.DecimalField("Preço", decimal_places=2, max_digits=8)
    created = models.DateTimeField("criado em", auto_now_add=True)
    modified = models.DateTimeField("atualizado em", auto_now=True)

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"

    def __str__(self):
        return self.name
