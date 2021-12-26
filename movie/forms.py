# from django import forms
#
# from movie.models import Reviews, Rating, RatingStar
#
#
# class ReviewForm(forms.ModelForm):
#
#     class Meta:
#         model = Reviews
#         fields = ('name','email','text')
#
#     def clean(self):
#         print(dir(self))
#         print(self.cleaned_data)
#         return self.cleaned_data
#
#
# class RatingForm(forms.ModelForm):
#     """Форма добавления рейтинга"""
#     star = forms.ModelChoiceField(
#         queryset=RatingStar.objects.all(), widget=forms.RadioSelect(), empty_label=None
#     )
#
#     class Meta:
#         model = Rating
#         fields = ('star',)
