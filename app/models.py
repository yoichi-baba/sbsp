from django.db import models

from users.models import User


class Item(models.Model):
    """
    データ定義クラス
      各フィールドを定義する
    参考：
    ・公式 モデルフィールドリファレンス
    https://docs.djangoproject.com/ja/2.1/ref/models/fields/
    """

    # ファイターID
    fighter_id = models.CharField(
        verbose_name='ファイターID',
        max_length=3,
        blank=False,
        null=False,
    )

    # ファイター名
    fighter_name = models.CharField(
        verbose_name='ファイター名',
        max_length=50,
        blank=True,
        null=True,
    )

    # ファイター名(英語)
    fighter_name_en = models.CharField(
        verbose_name='ファイター名(英語)',
        max_length=50,
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
        return self.fighter_name

    class Meta:
        """
        管理画面でのタイトル表示
        """
        verbose_name = 'ファイター名マスタ'
        verbose_name_plural = 'ファイター名マスタ'
