def word_transform():
    '''Requests and sorts input strings'''
    original = input('Enter the original word: ').lower()
    transform = input('Enter the word to edit into:  ').lower()
    print()
    original_sorted = sorted(original)
    transform_sorted = sorted(transform)
    return original, transform, original_sorted, transform_sorted

def copy_char(original_sorted, transform_sorted):
    original_leftover = []
    transform_copied = []
    cost = 0

    for char in original_sorted:
        if char in transform_sorted:
            #copies to new list and removes from old
            transform_copied.append(char)
            transform_sorted.remove(char)
            cost += 5
        else:
            #characters that were not copied
            original_leftover.append(char)
            
    return transform_sorted, transform_copied, original_leftover, cost

def del_insert(original, transform, transform_sorted, transform_copied, original_leftover, cost):
    if len(original_leftover) == len(transform_sorted):
    # delete + insert letters costs 40 points for each
        cost += len(original_leftover) * 40
    
        print(f'{original} --> {transform}')
        print(f'Original and new words are both: {len(original)} characters')
        print(f'{len(transform_copied)} characters copied: {transform_copied}')
        print(f'{len(original_leftover)} characters deleted and inserted: {original_leftover} --> {transform_sorted}')
        print()
        print(f'Total Edit Cost: {cost} points')
    
    elif len(original_leftover) > len(transform_sorted):
        #cost for delete + insert
        cost += len(transform_sorted) * 40
    
        #cost for deleting extra characters from original 
        cost += ((len(original_leftover) - (len(transform_sorted)))) * 20
        print(f'{original} --> {transform}')
        print(f'{original}: {len(original)} characters, {transform}: {len(transform)} characters')
        print(f'{len(transform_copied)} characters copied: {transform_copied}')
        print(f'{len(original_leftover)} characters deleted and/or inserted: {original_leftover} --> {transform_sorted}')
        print()
        print(f'Total Edit Cost: {cost} points')

    else:
        #delete + insert
        cost += len(original_leftover) * 40
    
        #cost for inserting extra characters to match transformed word
        cost += ((len(transform_sorted) - (len(original_leftover)))) * 20
    
        print(f'{original} --> {transform}')
        print(f'{original}: {len(original)} characters, {transform}: {len(transform)} characters')
        print(f'{len(transform_copied)} characters copied: {transform_copied}')
        print(f'{len(transform_sorted)} characters deleted and/or inserted: {original_leftover} --> {transform_sorted}')
        print()
        print(f'Total Edit Cost: {cost} points')
        
def run_string_edit():
    #gets input
    original, transform, original_sorted, transform_sorted = word_transform()
    
    #calculates cost for characters that can be copied
    transform_sorted, transform_copied, original_leftover, cost = copy_char(original_sorted, transform_sorted)
    
    #calculates cost for deleted and/or inserted characters and prints out report
    del_insert(original, transform, transform_sorted, transform_copied, original_leftover, cost)