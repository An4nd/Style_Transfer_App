from django import forms
from crispy_forms.helper import FormHelper


class ImageForm(forms.Form):
    
    content_image=forms.ImageField()
    style_image = forms.ImageField()
    def __init__(self,*args,**kwargs):
        super(ImageForm,self).__init__(*args,**kwargs)
        self.helper=FormHelper()
        self.helper.form_show_labels=False


