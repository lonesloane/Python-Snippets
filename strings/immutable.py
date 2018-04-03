title = "Recipe 5: Rewriting, and the Immutable String"

# slicing

colon_position = title.index(':')

discard_text = title[:colon_position]
post_colon_text = title[colon_position+1:]

print('discarded: {}'.format(discard_text))
print('kept: {}'.format(post_colon_text))

pre_colon_text, _, post_colon_text = title.partition(':')
print('discarded: {}'.format(pre_colon_text))
print('kept: {}'.format(post_colon_text))
