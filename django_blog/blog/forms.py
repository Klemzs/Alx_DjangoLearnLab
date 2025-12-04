from .models import Comment, Post, Tag
from django import forms

class TagWidget(forms.TextInput):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.attrs.update({
            'class': 'tag-input',
            'data-role': 'tagsinput',
            'placeholder': 'Add tags separated by commas'
        })

# PostForm with tags
class PostForm(forms.ModelForm):
    tags = forms.CharField(
        required=False,
        widget=TagWidget(),  # Use TagWidget
        help_text='Separate tags with commas'
    )
    
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']  # Include tags in fields
        widgets = {  # Add widgets section
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 10}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            tag_names = [tag.name for tag in self.instance.tags.all()]
            self.fields['tags'].initial = ', '.join(tag_names)
    
    def save(self, commit=True):
        post = super().save(commit=False)
        if commit:
            post.save()
            self.save_tags(post)
        return post
    
    def save_tags(self, post):
        post.tags.clear()
        tags_input = self.cleaned_data.get('tags', '')
        if tags_input:
            tag_names = [name.strip() for name in tags_input.split(',') if name.strip()]
            for tag_name in tag_names:
                tag, created = Tag.objects.get_or_create(name=tag_name.lower())
                post.tags.add(tag)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
