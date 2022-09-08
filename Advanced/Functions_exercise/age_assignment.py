def age_assignment(*args, **kwargs):
    result = {}
    for each in args:
        first_letter = each[0]
        age = kwargs[first_letter]
        result[each] = age

    aa = [f'{key} is {value} years old.'for key, value in (sorted(result.items(),
                  key=lambda x: x[0]))]
    return '\n'.join(aa)
print(age_assignment("Peter", "George", G=26, P=19))
