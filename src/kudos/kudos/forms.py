from django import forms


class KudoForm(forms.Form):
  from_person = forms.CharField(label='From', max_length=100)
  to_person = forms.CharField(label='To', max_length=100)
  comment = forms.CharField(widget=forms.Textarea)

  def clean(self):
    cleaned_data = super(KudoForm, self).clean()
    from_person = cleaned_data.get('from_person')
    to_person = cleaned_data.get('to_person')
    comment = cleaned_data.get('comment')
    if not from_person and not to_person and not comment:
      raise forms.ValidationError('You have to write something!')
