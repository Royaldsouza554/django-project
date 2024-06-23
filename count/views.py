from django.shortcuts import render
from django.http import HttpResponse

def count_letters(request, sentence):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0
    vowel_list = []
    consonant_list = []

    for char in sentence:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
                vowel_list.append(char)
            else:
                consonant_count += 1
                consonant_list.append(char)

    context = {
        'sentence': sentence,
        'vowel_count': vowel_count,
        'consonant_count': consonant_count,
        'vowel_list': vowel_list,
        'consonant_list': consonant_list,
    }
    
    return render(request, 'count/count.html', context)
