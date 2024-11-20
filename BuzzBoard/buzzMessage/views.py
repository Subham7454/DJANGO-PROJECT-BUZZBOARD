from django.shortcuts import render, get_object_or_404, redirect
from .models import Tweet
from .forms import TweetForm,UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import SearchForm



# Home Page
def index(request):
    return render(request, 'index.html')

# List of Tweets
def tweet_list(request):
    tweets = Tweet.objects.all().order_by('-created_at')  # Fetch tweets ordered by creation date
    return render(request, 'tweet_list.html', {'tweets': tweets, 'user': request.user})

# Create a New Tweet
@login_required
def tweet_create(request):
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)  # Save the form but don't commit to DB yet
            tweet.user = request.user  # Assign the logged-in user
            tweet.save()  # Save the tweet to the database
            return redirect('tweet_list')  # Redirect to the list view
    else:
        form = TweetForm()  # Instantiate a blank form for GET requests
    return render(request, 'tweet_form.html', {'form': form})

# Edit an Existing Tweet
@login_required
def tweet_edit(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)  # Ensure only the owner can edit
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES, instance=tweet)
        if form.is_valid():
            form.save()  # Save the edited tweet
            return redirect('tweet_list')
    else:
        form = TweetForm(instance=tweet)  # Pre-fill the form with tweet data for GET requests
    return render(request, 'tweet_form.html', {'form': form})

# Delete a Tweet
@login_required
def tweet_delete(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id, user=request.user)  # Ensure only the owner can delete
    if request.method == 'POST':
        tweet.delete()  # Delete the tweet
        return redirect('tweet_list')
    return render(request, 'tweet_confirm_delete.html', {'tweet': tweet})  # Confirmation page


#register

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)  
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)  # Automatically logs the user in after registration
            return redirect('tweet_list')  # Redirect to your desired page
    else:
        form = UserRegistrationForm()
    
    return render(request, 'registration/register.html', {'form': form})



def search_view(request):
    form = SearchForm(request.GET)
    results = None
    if form.is_valid():
        query = form.cleaned_data['query']
        results = Tweet.objects.filter(text__icontains=query)  # Use 'text' instead of 'content'
    return render(request, 'search_results.html', {'form': form, 'results': results})