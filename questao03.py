print("Escreva uma palavra:")
word1 = input()
print("Escreva mais uma palavra:")
word2 = input()
print("\nEssas são suas duas palavras: ", word1, "e", word2)
word_size1 = len(word1)
half_the_word1 = (word_size1 // 2)
word_size2 = len(word2)
half_the_word2 = (word_size2 // 2)
word3 = word1[0] + word2[0] + word1[half_the_word1] + word2[half_the_word2] + word1[-1] + word2[-1]
print("\nEssa é a sua nova palavra: ", word3)