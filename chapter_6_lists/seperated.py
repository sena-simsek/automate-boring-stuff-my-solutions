# Automate the Boring Stuff Chapter 6 Practice Project by Sena Simsek
spam = ['apples','bananas','tofu','cats']
def seperated(items):
    if len(items) == 0:
        pass

    before_last = items[:-1]
    last = items[-1]
    results = ', '.join(before_last) +', and ' +last
    print(results)

seperated(spam)
