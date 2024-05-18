def read(n: int, book: [int], target: int) -> str:
    saved_book = {}
    for i, pages in enumerate(book):
        if (target - pages) in saved_book:
            return "YES"
        saved_book[pages] = i
    
    return "NO"