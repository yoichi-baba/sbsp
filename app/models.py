from django.core.validators import FileExtensionValidator
from django.db import models

from users.models import User


class Item(models.Model):
    """
    酒マスタ
    """

    # 名称
    alcohol_name = models.CharField(
        verbose_name='名称',
        max_length=50,
        blank=False,
        null=False,
    )

    alcohol_kbn_name = models.CharField(
        verbose_name='区分名',
        max_length=10,
        blank=True,
        null=True,
    )

    # 内容量
    alcohol_capacity = models.IntegerField(
        verbose_name='内容量',
        blank=True,
        null=True,
    )

    # 度数
    alcoholic_proof = models.IntegerField(
        verbose_name='度数',
        blank=True,
        null=True,
    )

    # 本数
    alcohol_num = models.IntegerField(
        verbose_name='本数',
        blank=True,
        null=True,
    )

    # 商品説明
    alcohol_info = models.TextField(
        verbose_name='商品説明',
        blank=True,
        null=True,
    )

    # 以下、管理項目

    # 作成者(ユーザー)
    created_by = models.ForeignKey(
        User,
        verbose_name='作成者',
        blank=True,
        null=True,
        related_name='CreatedBy',
        on_delete=models.SET_NULL,
        editable=False,
    )

    # 作成時間
    created_at = models.DateTimeField(
        verbose_name='作成時間',
        blank=True,
        null=True,
        editable=False,
    )

    # 更新者(ユーザー)
    updated_by = models.ForeignKey(
        User,
        verbose_name='更新者',
        blank=True,
        null=True,
        related_name='UpdatedBy',
        on_delete=models.SET_NULL,
        editable=False,
    )

    # 更新時間
    updated_at = models.DateTimeField(
        verbose_name='更新時間',
        blank=True,
        null=True,
        editable=False,
    )

    def __str__(self):
        """
        リストボックスや管理画面での表示
        """
        return self.alcohol_name

    class Meta:
        """
        管理画面でのタイトル表示
        """
        verbose_name = '酒マスタ'
        verbose_name_plural = '酒マスタ'
