from django.db import models
from django.core import validators

class RankId(models.Model):
   rank1 = models.IntegerField(
    verbose_name='rank1',
    blank=True,
    null=True,
    default=0,
    validators=[validators.MinValueValidator(0),
                validators.MaxValueValidator(100)]
  )

   rank2 = models.IntegerField(
     verbose_name='rank2',
     blank=True,
     null=True,
     default=0,
     validators=[validators.MinValueValidator(0),
                 validators.MaxValueValidator(100)]
   )

   rank3 = models.IntegerField(
     verbose_name='rank3',
     blank=True,
     null=True,
     default=0,
     validators=[validators.MinValueValidator(0),
                 validators.MaxValueValidator(100)]
   )


# ユーザーIDと映画ID、評価値のモデル(IDが文字列)
class RecoData(models.Model):
  user_id = models.CharField(
    verbose_name='user_id',
    blank=True,
    null=True,
    max_length=100,
    default=''
  )

  movie_id = models.IntegerField(
    verbose_name='movie_id',
    blank=True,
    null=True,
    default=0,
    validators=[validators.MinValueValidator(0),
                validators.MaxValueValidator(1000000)]
  )

  rate = models.FloatField(
    verbose_name='rate',
    blank=True,
    null=True,
    default=0,
    validators=[validators.MinValueValidator(0.),
                validators.MaxValueValidator(5.)]
  )

  def __str__(self):
    return str('user_id :') + str(self.user_id) + str(" movie_id :") + str(self.movie_id) +  str(" rate :") + str(self.rate)