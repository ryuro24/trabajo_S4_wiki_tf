from django import forms
from .models import Usuario

class RegistroUsuarioForm(forms.ModelForm):
    confirmar_contrasena = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control bg-dark-x border-0 mb-2',
            'placeholder': 'Confirme su contraseña',
            'style': 'background-color: #ffffff;',
            'id': 'id_confirmar_contrasena'
        }),
        label='Confirmar contraseña'
    )

    class Meta:
        model = Usuario
        fields = ['email', 'contrasena']
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-control bg-dark-x border-0',
                'placeholder': 'nombre@ejemplo.com',
                'style': 'background-color: #ffffff;',
                'id': 'id_email'
            }),
            'contrasena': forms.PasswordInput(attrs={
                'class': 'form-control bg-dark-x border-0 mb-2',
                'placeholder': 'Ingrese su contraseña',
                'style': 'background-color: #ffffff;',
                'id': 'id_contrasena'
            }),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("contrasena")
        confirm_password = cleaned_data.get("confirmar_contrasena")
        email = cleaned_data.get("email")

        # Passwords validation
        if password and confirm_password and password != confirm_password:
            self.add_error('confirmar_contrasena', "Las contraseñas no coinciden.")

        # Email uniqueness validation
        if email:
            if Usuario.objects.filter(email=email).exists():
                self.add_error('email', "Este correo electrónico ya está registrado.")

        return cleaned_data


class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control bg-dark-x border-0',
            'placeholder': 'nombre@ejemplo.com',
            'style': 'background-color: #ffffff;',
            'id': 'id_email'
        }),
        label='Correo electrónico'
    )
    contrasena = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control bg-dark-x border-0 mb-2',
            'placeholder': 'Ingrese su contraseña',
            'style': 'background-color: #ffffff;',
            'id': 'id_contrasena'
        }),
        label='Contraseña'
    )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        contrasena = cleaned_data.get('contrasena')

        if email and contrasena:
            try:
                # Try to fetch the user by email (case-insensitive)
                usuario = Usuario.objects.get(email__iexact=email)

                # Direct password comparison without using check_password
                if contrasena != usuario.contrasena:  # Comparing plaintext password
                    raise forms.ValidationError("Correo electrónico o contraseña incorrectos.")

                # If the password is correct and everything is fine, just return
                return cleaned_data

            except Usuario.DoesNotExist:
                raise forms.ValidationError("Correo electrónico o contraseña incorrectos.")
            

class EditarUsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['email', 'contrasena']
        widgets = {
            'contrasena': forms.PasswordInput(),
        }