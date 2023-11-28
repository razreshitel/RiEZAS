from django.db import models

class Child(models.Model):
    """Информация о ребенке"""
    child_name = models.CharField(max_length=100, verbose_name="Имя ребенка")
    birth_date = models.DateField(verbose_name="Дата рождения")
    parent_name = models.CharField(max_length=100, verbose_name="Имя родителя")

    class Meta:
        verbose_name = "Ребенок"
        verbose_name_plural = "Дети"

    def __str__(self):
        return self.child_name

class EducationalMaterial(models.Model):
    """Учебные материалы и принадлежности"""
    name = models.CharField(max_length=100, verbose_name="Наименование")
    description = models.TextField(verbose_name="Описание")

    class Meta:
        verbose_name = "Учебный материал"
        verbose_name_plural = "Учебные материалы"

    def __str__(self):
        return self.name

class EducationalActivity(models.Model):
    """Образовательная активность"""
    activity_name = models.CharField(max_length=100, verbose_name='Название активности')
    child = models.ForeignKey(Child, on_delete=models.CASCADE, verbose_name="Идентификатор ребенка")
    date = models.DateField(verbose_name="Дата проведения")

    class Meta:
        verbose_name = "Образовательная активность"
        verbose_name_plural = "Образовательные активности"

    def __str__(self):
        return self.activity_name

class ParentRequest(models.Model):
    """Запросы и пожелания родителей"""
    child = models.ForeignKey(Child, on_delete=models.CASCADE, verbose_name="Идентификатор ребенка")
    request_description = models.TextField(verbose_name="Описание запроса")
    created_dt = models.DateTimeField(verbose_name="Дата создания", auto_now_add=True)

    class Meta:
        verbose_name = "Запрос родителя"
        verbose_name_plural = "Запросы родителей"

    def __str__(self):
        return f"Запрос от {self.child.parent_name}"
