from django import forms

class SnippetForm(forms.Form):
   title = forms.CharField(label='Title', max_length=100)
   language = forms.CharField(label='Language', max_length=100)
   img_url = forms.CharField(label='Image Link', max_length=100)
   description = forms.CharField(label='Description', max_length=100)
 

 #         self.title = title
#         self.language = language
#         self.img_url = img_url
#         self.description = description