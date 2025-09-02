from django import forms
from .models import TempSites


# 定義一個名為 addsitesForm 的表單類，繼承自 forms.ModelForm
class addsitesalertForm(forms.ModelForm):
    name = forms.CharField(label="名稱", required=True)
    type = forms.CharField(label="類型", required=True)
    description = forms.CharField(label="簡述", required=True)
    year = forms.CharField(label="發現年份", required=True)
    latitude = forms.CharField(label="緯度", required=True)
    longitude = forms.CharField(label="經度", required=True)
    note = forms.CharField(label="備註", required=True)
    county = forms.CharField(label="縣市", required=True)
    town = forms.CharField(label="鄉鎮", required=True)
    towncode = forms.CharField(label="鄉鎮代碼", required=False)

    # Meta 類，用於指定要使用的模型和要在表單中包含的字段
    class Meta:

        # 將此表單鏈接到 TempSites 模型
        model = TempSites

        # 指定表單中包含的字段
        fields = [
            "name",
            "type",
            "description",
            "year",
            "latitude",
            "longitude",
            "note",
            "county",
            "town",
            "towncode",
        ]
