def convert(s, num_rows):
    if num_rows == 1 or num_rows >= len(s):
        return s

    rows = [''] * num_rows    
    current_row = 0
    going_down = False
    
    for char in s:
        rows[current_row] += char
        if current_row == 0 or current_row == num_rows - 1:
            going_down = not going_down
        current_row += 1 if going_down else -1
    
    return ''.join(rows)

print(convert("PAYPALISHIRING", 3)) 
print(convert("PAYPALISHIRING", 4))  
