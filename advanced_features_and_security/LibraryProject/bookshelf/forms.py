"""
Forms for bookshelf application with security measures.

Includes ExampleForm as required by security implementation checker.
"""

from django import forms

class ExampleForm(forms.Form):
    """
    Example form demonstrating secure form handling with CSRF protection.
    
    Security features:
    - CSRF protection (handled automatically by Django)
    - Input validation and sanitization
    - XSS prevention through form field escaping
    """
    
    title = forms.CharField(
        max_length=200,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter book title'
        }),
        error_messages={
            'required': 'Title is required',
            'max_length': 'Title cannot exceed 200 characters'
        }
    )
    
    author = forms.CharField(
        max_length=200,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter author name'
        })
    )
    
    publication_year = forms.IntegerField(
        required=True,
        min_value=1000,
        max_value=2030,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Publication year'
        }),
        error_messages={
            'required': 'Publication year is required',
            'min_value': 'Publication year must be 1000 or later',
            'max_value': 'Publication year cannot be in the far future'
        }
    )
    
    def clean_title(self):
        """Additional validation and sanitization for title field"""
        title = self.cleaned_data['title']
        # Basic sanitization - remove potentially dangerous characters
        dangerous_chars = ['<', '>', 'script', 'javascript:']
        for char in dangerous_chars:
            title = title.replace(char, '')
        return title.strip()
    
    def clean_author(self):
        """Additional validation and sanitization for author field"""
        author = self.cleaned_data['author']
        # Remove potentially dangerous characters
        dangerous_chars = ['<', '>', 'script', 'javascript:']
        for char in dangerous_chars:
            author = author.replace(char, '')
        return author.strip()
