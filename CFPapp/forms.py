from django.forms import ChoiceField, ModelForm, MultipleChoiceField, Select, TextInput
from django import forms
from CFPapp.models import *







class LoginForm(forms.Form):
    nom = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': '', 'style': 'width:300px;', 'class': 'fr-input'}))
    mail = forms.CharField( widget=forms.TextInput(attrs={'placeholder': '', 'style': 'width:300px;', 'class': 'fr-input'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': '', 'style': 'width:300px;', 'class': 'fr-input'}))


############A1

class POSTFormA1_C1(ModelForm):
    class Meta:
        model = PostA1_C1
        fields =[ "created_by","A1_C1",]
        widgets ={

            'created_by': TextInput(attrs={'readonly': 'readonly'}),
            'A1_C1': Select(attrs={'style': 'width:800px; display:inline-block;',  'class': 'form-control'}),

        }
    def clean(self):
        super(POSTFormA1_C1, self).clean()

        return self.cleaned_data

class POSTFormA1_C2(ModelForm):
    class Meta:
        model = PostA1_C2
        fields =[ "created_by","A1_C2"]
        widgets ={
            'created_by': TextInput(attrs={'readonly': 'readonly'}),
            'A1_C2': Select(attrs={'style': 'width:800px; display:inline-block;',  'class': 'form-control'}),

        }

    def clean(self):
        super(POSTFormA1_C2, self).clean()

        return self.cleaned_data

class POSTFormA1_C3(ModelForm):
    class Meta:
        model = PostA1_C3
        fields =[ "created_by","A1_C3"]
        widgets ={
            'created_by': TextInput(attrs={'readonly': 'readonly'}),
            'A1_C3': Select(attrs={'style': 'width:800px; display:inline-block;',  'class': 'form-control'}),

        }

    def clean(self):
        super(POSTFormA1_C3, self).clean()

        return self.cleaned_data


class POSTFormA2_C1(ModelForm):
    class Meta:
        model = PostA2_C1
        fields =[ "created_by","A2_C1",]
        widgets ={

            'created_by': TextInput(attrs={'readonly': 'readonly'}),
            'A2_C1': Select(attrs={'style': 'width:820px; display:inline-block;',  'class': 'form-control'}),

        }
    def clean(self):
        super(POSTFormA2_C1, self).clean()

class POSTFormA2_C2(ModelForm):
    class Meta:
        model = PostA2_C2
        fields =[ "created_by","A2_C2",]
        widgets ={

            'created_by': TextInput(attrs={'readonly': 'readonly'}),
            'A2_C2': Select(attrs={'style': 'width:840px; display:inline-block;',  'class': 'form-control'}),
        }
    def clean(self):
        super(POSTFormA2_C2, self).clean()

class POSTFormA2_C3(ModelForm):
    class Meta:
        model = PostA2_C3
        fields =[ "created_by","A2_C3",]
        widgets ={
            'created_by': TextInput(attrs={'readonly': 'readonly'}),
            'A2_C3': Select(attrs={'style': 'width:800px; display:inline-block;',  'class': 'form-control'}),
        }
    def clean(self):
        super(POSTFormA2_C3, self).clean()

class POSTFormA3_C1(ModelForm):
    class Meta:
        model = PostA3_C1
        fields =[ "created_by", "A3_C1",]
        widgets ={

            'created_by': TextInput(attrs={'readonly': 'readonly'}),
            'A3_C1': Select(attrs={'style': 'width:744px; display:inline-block;',  'class': 'form-control'}),

        }
    def clean(self):
        super(POSTFormA3_C1, self).clean()

class POSTFormA3_C2(ModelForm):
    class Meta:
        model = PostA3_C2
        fields =[ "created_by", "A3_C2",]
        widgets ={

            'created_by': TextInput(attrs={'readonly': 'readonly'}),
            'A3_C2': Select(attrs={'style': 'width:700px; display:inline-block;',  'class': 'form-control'}),

        }
    def clean(self):
        super(POSTFormA3_C2, self).clean()

class POSTFormA3_C3(ModelForm):
    class Meta:
        model = PostA3_C3
        fields =[ "created_by", "A3_C3",]
        widgets ={

            'created_by': TextInput(attrs={'readonly': 'readonly'}),
            'A3_C3': Select(attrs={'style': 'width:700px; display:inline-block;',  'class': 'form-control'}),

        }
    def clean(self):
        super(POSTFormA3_C3, self).clean()

class POSTFormA4_C1(ModelForm):
    class Meta:
        model = PostA4_C1
        fields =[ "created_by","A4_C1",]
        widgets ={

            'created_by': TextInput(attrs={'readonly': 'readonly'}),
            'A4_C1': Select(attrs={'style': 'width:700px; display:inline-block;',  'class': 'form-control'}),

        }
    def clean(self):
        super(POSTFormA4_C1, self).clean()

class POSTFormA4_C2(ModelForm):
    class Meta:
        model = PostA4_C2
        fields =[ "created_by","A4_C2",]
        widgets ={

            'created_by': TextInput(attrs={'readonly': 'readonly'}),
            'A4_C2': Select(attrs={'style': 'width:700px; display:inline-block;',  'class': 'form-control'}),

        }
    def clean(self):
        super(POSTFormA4_C2, self).clean()

class POSTFormA4_C3(ModelForm):
    class Meta:
        model = PostA4_C3
        fields =[ "created_by", "A4_C3",]
        widgets ={

            'created_by': TextInput(attrs={'readonly': 'readonly'}),
            'A4_C3': Select(attrs={'style': 'width:800px; display:inline-block;',  'class': 'form-control'}),

        }
    def clean(self):
        super(POSTFormA4_C3, self).clean()

class POSTFormA5_C1(ModelForm):
    class Meta:
        model = PostA5_C1
        fields =[ "created_by","A5_C1"]
        widgets ={

            'created_by': TextInput(attrs={'readonly': 'readonly'}),
            'A5_C1': Select(attrs={'style': 'width:800px;',}),

        }
    def clean(self):
        super(POSTFormA5_C1, self).clean()

class POSTFormA5_C2(ModelForm):
    class Meta:
        model = PostA5_C2
        fields =[ "created_by","A5_C2",]
        widgets ={

            'created_by': TextInput(attrs={'readonly': 'readonly'}),
            'A5_C2': Select(attrs={'style': 'width:800px;',}),

        }
    def clean(self):
        super(POSTFormA5_C2, self).clean()

class POSTFormA5_C3(ModelForm):
    class Meta:
        model = PostA5_C3
        fields =[ "created_by","A5_C3"]
        widgets ={

            'created_by': TextInput(attrs={'readonly': 'readonly'}),
            'A5_C3': Select(attrs={'style': 'width:800px;',}),

        }
    def clean(self):
        super(POSTFormA5_C3, self).clean()

class POSTFormA6_C1(ModelForm):
    class Meta:
        model = PostA6_C1
        fields =[ "created_by","A6_C1"]
        widgets ={

            'created_by': TextInput(attrs={'readonly': 'readonly'}),
            'A6_C1': Select(attrs={'style': 'width:800px;',}),

        }
    def clean(self):
        super(POSTFormA6_C1, self).clean()

class POSTFormA6_C2(ModelForm):
    class Meta:
        model = PostA6_C2
        fields =[ "created_by", "A6_C2",]
        widgets ={

            'created_by': TextInput(attrs={'readonly': 'readonly'}),
            'A6_C2': Select(attrs={'style': 'width:800px;',}),

        }
    def clean(self):
        super(POSTFormA6_C2, self).clean()

class POSTFormA6_C3(ModelForm):
    class Meta:
        model = PostA6_C3
        fields =[ "created_by","A6_C3"]
        widgets ={

            'created_by': TextInput(attrs={'readonly': 'readonly'}),
            'A6_C3': Select(attrs={'style': 'width:800px;',}),

        }
    def clean(self):
        super(POSTFormA6_C3, self).clean()

###############################################################

class POSTFormB1_C1(ModelForm):
    class Meta:
        model = PostB1_C1
        fields =[ "created_by","B1_C1",]
        widgets ={

            'created_by': TextInput(attrs={'readonly': 'readonly'}),
            'B1_C1': Select(attrs={'style': 'width:700px; display:inline-block;',  'class': 'form-control'}),

        }
    def clean(self):
        super(POSTFormB1_C1, self).clean()

class POSTFormB1_C2(ModelForm):
    class Meta:
        model = PostB1_C2
        fields =[ "created_by","B1_C2",]
        widgets ={

            'created_by': TextInput(attrs={'readonly': 'readonly'}),
            'B1_C2': Select(attrs={'style': 'width:700px; display:inline-block;',  'class': 'form-control'}),

        }
    def clean(self):
        super(POSTFormB1_C2, self).clean()

class POSTFormB1_C3(ModelForm):
    class Meta:
        model = PostB1_C3
        fields =[ "created_by","B1_C3",]
        widgets ={

            'created_by': TextInput(attrs={'readonly': 'readonly'}),
            'B1_C3': Select(attrs={'style': 'width:700px; display:inline-block;',  'class': 'form-control'}),

        }
    def clean(self):
        super(POSTFormB1_C3, self).clean()


class POSTFormB2_C1(ModelForm):
    class Meta:
        model = PostB2_C1
        fields =[ "created_by","B2_C1",]
        widgets ={

            'created_by': TextInput(attrs={'readonly': 'readonly'}),
            'B2_C1': Select(attrs={'style': 'width:700px; display:inline-block;',  'class': 'form-control'}),

        }
    def clean(self):
        super(POSTFormB2_C1, self).clean()

class POSTFormB2_C2(ModelForm):
    class Meta:
        model = PostB2_C2
        fields =[ "created_by","B2_C2",]
        widgets ={

            'created_by': TextInput(attrs={'readonly': 'readonly'}),
            'B2_C2': Select(attrs={'style': 'width:700px; display:inline-block;',  'class': 'form-control'}),

        }
    def clean(self):
        super(POSTFormB2_C2, self).clean()


class POSTFormB2_C3(ModelForm):
    class Meta:
        model = PostB2_C3
        fields =[ "created_by","B2_C3",]
        widgets ={

            'created_by': TextInput(attrs={'readonly': 'readonly'}),
            'B2_C3': Select(attrs={'style': 'width:700px; display:inline-block;',  'class': 'form-control'}),

        }
    def clean(self):
        super(POSTFormB2_C3, self).clean()

class POSTFormB3_C1(ModelForm):
    class Meta:
        model = PostB3_C1
        fields =[ "created_by","B3_C1",]
        widgets ={

            'created_by': TextInput(attrs={'readonly': 'readonly'}),
            'B3_C1': Select(attrs={'style': 'width:700px; display:inline-block;',  'class': 'form-control'}),

        }
    def clean(self):
        super(POSTFormB3_C1, self).clean()

class POSTFormB3_C2(ModelForm):
    class Meta:
        model = PostB3_C2
        fields =[ "created_by","B3_C2",]
        widgets ={

            'created_by': TextInput(attrs={'readonly': 'readonly'}),
            'B3_C2': Select(attrs={'style': 'width:700px; display:inline-block;',  'class': 'form-control'}),

        }
    def clean(self):
        super(POSTFormB3_C2, self).clean()

class POSTFormB3_C3(ModelForm):
    class Meta:
        model = PostB3_C3
        fields =[ "created_by","B3_C3",]
        widgets ={

            'created_by': TextInput(attrs={'readonly': 'readonly'}),
            'B3_C3': Select(attrs={'style': 'width:700px; display:inline-block;',  'class': 'form-control'}),

        }
    def clean(self):
        super(POSTFormB3_C3, self).clean()

class POSTFormB4_C1(ModelForm):
    class Meta:
        model = PostB4_C1
        fields =[ "created_by","B4_C1",]
        widgets ={

            'created_by': TextInput(attrs={'readonly': 'readonly'}),
            'B4_C1': Select(attrs={'style': 'width:700px; display:inline-block;',  'class': 'form-control'}),

        }
    def clean(self):
        super(POSTFormB4_C1, self).clean()

class POSTFormB4_C2(ModelForm):
    class Meta:
        model = PostB4_C2
        fields =[ "created_by","B4_C2",]
        widgets ={

            'created_by': TextInput(attrs={'readonly': 'readonly'}),
            'B4_C2': Select(attrs={'style': 'width:700px; display:inline-block;',  'class': 'form-control'}),

        }
    def clean(self):
        super(POSTFormB4_C2, self).clean()


class POSTFormB4_C3(ModelForm):
    class Meta:
        model = PostB4_C3
        fields =[ "created_by","B4_C3",]
        widgets ={

            'created_by': TextInput(attrs={'readonly': 'readonly'}),
            'B4_C3': Select(attrs={'style': 'width:700px; display:inline-block;',  'class': 'form-control'}),

        }
    def clean(self):
        super(POSTFormB4_C3, self).clean()


##################################################
class POSTFormC1_C1(ModelForm):
    class Meta:
        model = PostC1_C1
        fields =[ "created_by","C1_C1",]
        widgets ={

            'created_by': TextInput(attrs={'readonly': 'readonly'}),
            'C1_C1': Select(attrs={'style': 'width:700px; display:inline-block;',  'class': 'form-control'}),

        }
    def clean(self):
        super(POSTFormC1_C1, self).clean()

class POSTFormC1_C2(ModelForm):
    class Meta:
        model = PostC1_C2
        fields =[ "created_by","C1_C2",]
        widgets ={

            'created_by': TextInput(attrs={'readonly': 'readonly'}),
            'C1_C2': Select(attrs={'style': 'width:700px; display:inline-block;',  'class': 'form-control'}),

        }
    def clean(self):
        super(POSTFormC1_C2, self).clean()

class POSTFormC1_C3(ModelForm):
    class Meta:
        model = PostC1_C3
        fields =[ "created_by","C1_C3",]
        widgets ={

            'created_by': TextInput(attrs={'readonly': 'readonly'}),
            'C1_C3': Select(attrs={'style': 'width:700px; display:inline-block;',  'class': 'form-control'}),

        }
    def clean(self):
        super(POSTFormC1_C3, self).clean()


class POSTFormC2_C1(ModelForm):
    class Meta:
        model = PostC2_C1
        fields =[ "created_by","C2_C1",]
        widgets ={

            'created_by': TextInput(attrs={'readonly': 'readonly'}),
            'C2_C1': Select(attrs={'style': 'width:700px; display:inline-block;',  'class': 'form-control'}),

        }
    def clean(self):
        super(POSTFormC2_C1, self).clean()

class POSTFormC2_C2(ModelForm):
    class Meta:
        model = PostC2_C2
        fields =[ "created_by","C2_C2",]
        widgets ={

            'created_by': TextInput(attrs={'readonly': 'readonly'}),
            'C2_C2': Select(attrs={'style': 'width:700px; display:inline-block;',  'class': 'form-control'}),

        }
    def clean(self):
        super(POSTFormC2_C2, self).clean()


class POSTFormC2_C3(ModelForm):
    class Meta:
        model = PostC2_C3
        fields =[ "created_by","C2_C3",]
        widgets ={

            'created_by': TextInput(attrs={'readonly': 'readonly'}),
            'C2_C3': Select(attrs={'style': 'width:700px; display:inline-block;',  'class': 'form-control'}),

        }
    def clean(self):
        super(POSTFormC2_C3, self).clean()

class POSTFormC3_C1(ModelForm):
    class Meta:
        model = PostC3_C1
        fields =[ "created_by","C3_C1",]
        widgets ={

            'created_by': TextInput(attrs={'readonly': 'readonly'}),
            'C3_C1': Select(attrs={'style': 'width:700px; display:inline-block;',  'class': 'form-control'}),

        }
    def clean(self):
        super(POSTFormC3_C1, self).clean()

class POSTFormC3_C2(ModelForm):
    class Meta:
        model = PostC3_C2
        fields =[ "created_by","C3_C2",]
        widgets ={

            'created_by': TextInput(attrs={'readonly': 'readonly'}),
            'C3_C2': Select(attrs={'style': 'width:700px; display:inline-block;',  'class': 'form-control'}),

        }
    def clean(self):
        super(POSTFormC3_C2, self).clean()

class POSTFormC3_C3(ModelForm):
    class Meta:
        model = PostC3_C3
        fields =[ "created_by","C3_C3",]
        widgets ={

            'created_by': TextInput(attrs={'readonly': 'readonly'}),
            'C3_C3': Select(attrs={'style': 'width:700px; display:inline-block;',  'class': 'form-control'}),

        }
    def clean(self):
        super(POSTFormC3_C3, self).clean()

class POSTFormC4_C1(ModelForm):
    class Meta:
        model = PostC4_C1
        fields =[ "created_by","C4_C1",]
        widgets ={

            'created_by': TextInput(attrs={'readonly': 'readonly'}),
            'C4_C1': Select(attrs={'style': 'width:790px; display:inline-block;',  'class': 'form-control'}),

        }
    def clean(self):
        super(POSTFormC4_C1, self).clean()

class POSTFormC4_C2(ModelForm):
    class Meta:
        model = PostC4_C2
        fields =[ "created_by","C4_C2",]
        widgets ={

            'created_by': TextInput(attrs={'readonly': 'readonly'}),
            'C4_C2': Select(attrs={'style': 'width:790px; display:inline-block;',  'class': 'form-control'}),

        }
    def clean(self):
        super(POSTFormC4_C2, self).clean()


class POSTFormC4_C3(ModelForm):
    class Meta:
        model = PostC4_C3
        fields =[ "created_by","C4_C3",]
        widgets ={

            'created_by': TextInput(attrs={'readonly': 'readonly'}),
            'C4_C3': Select(attrs={'style': 'width:800px; display:inline-block;',  'class': 'form-control'}),

        }
    def clean(self):
        super(POSTFormC4_C3, self).clean()



###############################################################

class CFPForm(ModelForm):
    class Meta:
        model = CFP_infos

        fields =[ "created_by","fonction","anciennete_annee", "anciennete_mois"]
        widgets = {
            'created_by': TextInput(attrs={'readonly': 'readonly'}),
            'fonction': Select(attrs={'initial': 'Choisir votre fonction actuelle','style': 'width:400px;', 'class': 'fr-input'}),
            'anciennete_annee': TextInput(attrs={'placeholder': '', 'style': 'width:400px;', 'class': 'fr-input'}),
            'anciennete_mois': TextInput(attrs={'placeholder': '', 'style': 'width:400px;', 'class': 'fr-input'}),


        }

    def clean(self):
        super(CFPForm, self).clean()

        return self.cleaned_data